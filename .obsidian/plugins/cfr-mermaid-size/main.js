'use strict';

/* CFR Mermaid Size — arrastar para redimensionar diagramas Mermaid, com o
   tamanho gravado dentro do próprio bloco.

   O Obsidian injeta o módulo "obsidian" em tempo de execução; em Node ele não
   existe. O try/catch é o que permite testar as funções puras fora do app. */
let obsidian = null;
try {
  obsidian = require('obsidian');
} catch (_) {
  obsidian = null;
}

const MIN_PCT = 10; // abaixo disso o diagrama fica ilegível
const MAX_PCT = 100; // acima disso a PÁGINA passa a rolar de lado (medido)

/* Uma chave por conceito, cada uma opcional e independente. Juntar as duas na
   mesma linha obrigaria a inventar um tamanho para quem só quer alinhar. */
const MARCA = /^\s*%%\s*cfr-size\s*:\s*(\d+(?:\.\d+)?)\s*%%\s*$/;
/* `cfr-size` não casa com `cfr-size-mobile`: depois do nome a regex exige
   `\s*:`, e o hífen não passa. As duas chaves não se confundem. */
const MARCA_MOBILE = /^\s*%%\s*cfr-size-mobile\s*:\s*(\d+(?:\.\d+)?)\s*%%\s*$/;
const MARCA_ALINHAMENTO = /^\s*%%\s*cfr-align\s*:\s*([\wçãéíó]+)\s*%%\s*$/i;

const ALINHAMENTO_PADRAO = 'center';

/* Leitura tolerante, escrita canônica: aceita a palavra em português caso ela
   seja digitada à mão, mas o que o plugin grava é sempre a forma em inglês,
   para casar com `cfr-size`. */
const ALINHAMENTOS = {
  left: 'left',
  esquerda: 'left',
  center: 'center',
  centro: 'center',
  right: 'right',
  direita: 'right'
};

/* Lê as marcas do bloco. `tamanho` é null quando não há marca, quando o valor
   não é número ou quando está fora da faixa — em todos esses casos o diagrama
   renderiza no tamanho natural, que é o comportamento sem plugin. Alinhamento
   desconhecido cai no padrão em vez de virar erro. */
function lerMarcas(linhas) {
  let tamanho = null;
  let tamanhoMobile = null;
  let alinhamento = ALINHAMENTO_PADRAO;

  const percentualValido = (bruto) => {
    const valor = Number(bruto);
    if (!Number.isFinite(valor)) return null;
    if (valor < MIN_PCT || valor > MAX_PCT) return null;
    return valor;
  };

  for (const linha of linhas) {
    const noCelular = MARCA_MOBILE.exec(linha);
    if (noCelular) {
      if (tamanhoMobile === null) tamanhoMobile = percentualValido(noCelular[1]);
      continue;
    }

    const comum = MARCA.exec(linha);
    if (comum) {
      if (tamanho === null) tamanho = percentualValido(comum[1]);
      continue;
    }

    const alinhado = MARCA_ALINHAMENTO.exec(linha);
    if (alinhado) {
      alinhamento = ALINHAMENTOS[alinhado[1].toLowerCase()] || ALINHAMENTO_PADRAO;
    }
  }

  return { tamanho, tamanhoMobile, alinhamento };
}

/* Qual valor vale AQUI. Fica separado da leitura de propósito: `lerMarcas` diz
   o que está escrito, esta função diz o que se aplica — assim a regra é
   testável em Node, sem simular dispositivo.

   Estados INDEPENDENTES, sem herança: cada aparelho enxerga só a sua chave, e
   a ausência dela é o tamanho natural. A primeira versão fazia o celular
   herdar o `cfr-size` enquanto não tivesse chave própria — o efeito era que
   mexer no desktop mexia no celular, que é justamente o que se queria evitar.
   O preço, consciente: um diagrama dimensionado no PC nasce no tamanho
   natural no celular até ser ajustado lá. */
function tamanhoParaDispositivo(marcas, ehMobile) {
  if (!marcas) return null;
  return ehMobile ? marcas.tamanhoMobile : marcas.tamanho;
}

/* Grava (ou atualiza) a marca dentro do bloco delimitado por [inicio, fim].
   Recebe o texto INTEIRO do arquivo e devolve o texto novo — é chamada de
   dentro do vault.process(), que garante leitura e escrita atômicas. */
function gravarMarcas(texto, inicio, fim, alteracoes) {
  const linhas = texto.split(/\r?\n/);
  if (!Number.isInteger(inicio) || !Number.isInteger(fim)) return texto;
  if (inicio < 0 || fim >= linhas.length || inicio >= fim) return texto;

  const quebra = texto.includes('\r\n') ? '\r\n' : '\n';
  let fimAtual = fim;
  let mudou = false;

  /* Insere, atualiza ou remove UMA chave, sem tocar na outra: é isso que faz
     alinhar não apagar o tamanho, e vice-versa. Procura só ENTRE as cercas —
     nunca sobrescreve a cerca nem a marca de outro bloco da mesma nota. */
  const aplicarChave = (regex, novaLinha) => {
    for (let i = inicio + 1; i < fimAtual; i++) {
      if (!regex.test(linhas[i])) continue;
      if (novaLinha === null) {
        linhas.splice(i, 1);
        fimAtual -= 1;
      } else {
        if (linhas[i] === novaLinha) return; // já está assim: não suja o arquivo
        linhas[i] = novaLinha;
      }
      mudou = true;
      return;
    }
    if (novaLinha === null) return; // nada a remover
    linhas.splice(inicio + 1, 0, novaLinha);
    fimAtual += 1;
    mudou = true;
  };

  /* null = apagar a linha (é o "voltar a herdar" do celular);
     undefined = não mexer nesta chave. */
  const gravarPercentual = (valorPedido, regex, nome) => {
    if (valorPedido === undefined) return;
    if (valorPedido === null) {
      aplicarChave(regex, null);
      return;
    }
    const numero = Number(valorPedido);
    if (!Number.isFinite(numero)) return;
    const pct = Math.round(Math.min(MAX_PCT, Math.max(MIN_PCT, numero)));
    aplicarChave(regex, `%% ${nome}: ${pct} %%`);
  };

  if (alteracoes) {
    gravarPercentual(alteracoes.tamanho, MARCA, 'cfr-size');
    gravarPercentual(alteracoes.tamanhoMobile, MARCA_MOBILE, 'cfr-size-mobile');
  }

  if (alteracoes && alteracoes.alinhamento !== undefined) {
    const valor = ALINHAMENTOS[String(alteracoes.alinhamento).toLowerCase()];
    if (valor) {
      /* Centro é o padrão: em vez de gravar "center", apaga a linha. Nota
         limpa, e nada muda para quem nunca alinhou. */
      aplicarChave(
        MARCA_ALINHAMENTO,
        valor === ALINHAMENTO_PADRAO ? null : `%% cfr-align: ${valor} %%`
      );
    }
  }

  return mudou ? linhas.join(quebra) : texto;
}

/* ------------------------------------------------------------------
   Camada DOM
   ------------------------------------------------------------------ */

/* A largura vai no CONTAINER, não no <svg>: é o container que a alça
   redimensiona, e o svg acompanha por CSS (width:100%). Validado em mock —
   arrastar o container de 400px para 640px escala o SVG junto, sem barra de
   rolagem. Pôr a largura no svg quebraria o resize. */
function aplicarMarcas(container, marcas) {
  const { tamanho, alinhamento } = marcas;

  if (tamanho == null) {
    container.style.removeProperty('width');
    container.classList.remove('cfr-mms-ativo');
  } else {
    container.style.width = `${tamanho}%`;
    container.classList.add('cfr-mms-ativo');
  }

  /* Centro é o padrão e não ganha classe — a ausência já é a informação. */
  container.classList.remove('cfr-mms-esq', 'cfr-mms-dir');
  if (alinhamento === 'left') container.classList.add('cfr-mms-esq');
  if (alinhamento === 'right') container.classList.add('cfr-mms-dir');
}

/* Lê o alinhamento do DOM em vez de guardar em variável: mesma regra do
   getSectionInfo — o estado é consultado na hora do clique, não decorado da
   renderização. */
function alinhamentoAtual(container) {
  if (container.classList.contains('cfr-mms-esq')) return 'left';
  if (container.classList.contains('cfr-mms-dir')) return 'right';
  return ALINHAMENTO_PADRAO;
}

/* O Mermaid renderiza de forma assíncrona: quando o post-processor roda, o
   .mermaid pode ainda não existir. Mesma forma canônica do aguardaIndice() dos
   painéis: observa, resolve UMA vez, e desiste em 3s para não vazar observer. */
/* O nome da classe do bloco renderizado é a única peça que não dá para testar
   fora do Obsidian. Em vez de apostar numa, procura em ordem de preferência e
   cai no pai do <svg> como último recurso — assim uma mudança de classe do app
   não mata o plugin inteiro. */
function acharContainer(el) {
  const porClasse = el.querySelector('.mermaid, .block-language-mermaid');
  if (porClasse) return porClasse;
  /* Fallback só para SVG que o PRÓPRIO Mermaid gerou: ele numera o id
     ("mermaid-1723...") e escreve o aria-roledescription do tipo de diagrama.
     A versão anterior aceitava qualquer <svg> e pescava ícone de callout —
     medido no vault: 2 diagramas, 6 alças instaladas. */
  const svg = el.querySelector('svg[id^="mermaid"], svg[aria-roledescription]');
  if (svg && svg.parentElement) return svg.parentElement;
  return null;
}

function esperarMermaid(el, aoAchar) {
  let feito = false;
  let observador = null;
  let desistencia = null;

  const tentar = () => {
    if (feito) return false;
    const container = acharContainer(el);
    if (!container) return false;
    feito = true;
    if (observador) observador.disconnect();
    if (desistencia) clearTimeout(desistencia);
    aoAchar(container);
    return true;
  };

  if (tentar()) return;

  observador = new MutationObserver(tentar);
  desistencia = setTimeout(() => {
    feito = true;
    observador.disconnect();
  }, 3000);
  observador.observe(el, { childList: true, subtree: true });
}

/* Pointer Events cobrem mouse, caneta e toque com um código só — por isso não
   há um caminho separado para o celular. Durante o arrasto, só o DOM muda; a
   nota é tocada uma única vez, ao soltar. */
function instalarAlca(container, aoSoltar) {
  if (container.querySelector(':scope > .cfr-mms-alca')) return; // já instalada

  const alca = container.ownerDocument.createElement('div');
  alca.className = 'cfr-mms-alca';
  alca.setAttribute('aria-label', textos().alca);
  container.appendChild(alca);

  let inicioX = 0;
  let larguraInicial = 0;
  let larguraPai = 0;
  let pctAtual = null;

  alca.addEventListener('pointerdown', (ev) => {
    ev.preventDefault();
    ev.stopPropagation();
    const pai = container.parentElement;
    if (!pai) return;
    larguraPai = pai.clientWidth;
    if (!larguraPai) return;
    inicioX = ev.clientX;
    larguraInicial = container.getBoundingClientRect().width;
    alca.setPointerCapture(ev.pointerId);
    alca.classList.add('cfr-mms-arrastando');
  });

  alca.addEventListener('pointermove', (ev) => {
    if (!alca.hasPointerCapture(ev.pointerId)) return;
    const largura = larguraInicial + (ev.clientX - inicioX);
    const pct = Math.min(MAX_PCT, Math.max(MIN_PCT, (largura / larguraPai) * 100));
    pctAtual = Math.round(pct);
    container.style.width = `${pctAtual}%`;
    container.classList.add('cfr-mms-ativo');
  });

  const encerrar = (ev) => {
    if (!alca.hasPointerCapture(ev.pointerId)) return;
    alca.releasePointerCapture(ev.pointerId);
    alca.classList.remove('cfr-mms-arrastando');
    if (pctAtual == null) return;
    const valor = pctAtual;
    pctAtual = null;
    aoSoltar(valor);
  };

  alca.addEventListener('pointerup', encerrar);
  alca.addEventListener('pointercancel', encerrar);
}

/* ------------------------------------------------------------------
   O plugin
   ------------------------------------------------------------------ */

/* Em Node não há obsidian.Plugin; a classe base vazia é o que permite carregar
   este arquivo nos testes sem executar o app. */
/* O plugin é publicado, então a interface sai em inglês — menos para quem usa
   o Obsidian em português. Duas línguas resolvidas por tabela; nada de
   framework de i18n para seis frases. */
const TEXTOS = {
  en: {
    left: 'Align left',
    center: 'Align center',
    right: 'Align right',
    limparDesktop: 'Clear desktop size',
    limparMobile: 'Clear mobile size',
    alca: 'Resize diagram'
  },
  pt: {
    left: 'Alinhar à esquerda',
    center: 'Centralizar',
    right: 'Alinhar à direita',
    limparDesktop: 'Limpar o tamanho no desktop',
    limparMobile: 'Limpar o tamanho no celular',
    alca: 'Redimensionar diagrama'
  }
};

/* Puro para ser testável: recebe o código de idioma, devolve a tabela a usar. */
function escolherIdioma(bruto) {
  return String(bruto || '').toLowerCase().startsWith('pt') ? 'pt' : 'en';
}

/* O Obsidian guarda o idioma da interface em localStorage['language']. */
function textos() {
  let bruto = '';
  try {
    bruto =
      (typeof window !== 'undefined' && window.localStorage.getItem('language')) ||
      (typeof navigator !== 'undefined' && navigator.language) ||
      '';
  } catch (_) {
    bruto = '';
  }
  return TEXTOS[escolherIdioma(bruto)];
}

/* Menu nativo do Obsidian no clique direito — nenhum controle novo ocupando o
   diagrama. `stopPropagation` impede que o menu do editor apareça por cima. */
function instalarMenu(container, acoes) {
  if (container.dataset.cfrMmsMenu) return; // já instalado
  container.dataset.cfrMmsMenu = '1';

  container.addEventListener('contextmenu', (ev) => {
    if (!obsidian || !obsidian.Menu) return;
    ev.preventDefault();
    ev.stopPropagation();

    const atual = alinhamentoAtual(container);
    const menu = new obsidian.Menu();
    const t = textos();

    for (const [valor, titulo, icone] of [
      ['left', t.left, 'align-left'],
      ['center', t.center, 'align-center'],
      ['right', t.right, 'align-right']
    ]) {
      menu.addItem((item) =>
        item
          .setTitle(titulo)
          .setIcon(icone)
          .setChecked(atual === valor)
          .onClick(() => acoes.aoAlinhar(valor))
      );
    }

    /* Limpar é por aparelho, como o próprio tamanho: no celular apaga a chave
       do celular, no desktop apaga a do desktop. Sem este item, desfazer
       exigiria editar `%%` à mão — no celular, onde editar texto é pior. */
    if (acoes.temTamanho && acoes.temTamanho()) {
      menu.addSeparator();
      menu.addItem((item) =>
        item
          .setTitle(acoes.rotuloLimpar)
          .setIcon('rotate-ccw')
          .onClick(() => acoes.aoLimpar())
      );
    }

    menu.showAtMouseEvent(ev);
  });
}

/* Relê as marcas do arquivo NA HORA do clique, em vez de usar as linhas
   capturadas na renderização — mesma regra do getSectionInfo: estado se
   consulta, não se decora. */
function lerMarcasAtuais(ctx, el) {
  const info = ctx.getSectionInfo(el);
  if (!info) return { tamanho: null, tamanhoMobile: null, alinhamento: ALINHAMENTO_PADRAO };
  return lerMarcas(info.text.split(/\r?\n/).slice(info.lineStart, info.lineEnd + 1));
}

const Base = obsidian && obsidian.Plugin ? obsidian.Plugin : class {};

class CfrMermaidSize extends Base {
  onload() {
    this.registerMarkdownPostProcessor((el, ctx) => this.processar(el, ctx));
  }

  processar(el, ctx) {
    esperarMermaid(el, (container) => {
      /* Sem posição no arquivo (Live Preview, embed), o plugin não tem como
         gravar. Então não instala a alça: melhor não oferecer o controle do
         que gravar no lugar errado. */
      const info = ctx.getSectionInfo(el);
      if (!info) return;

      const linhas = info.text.split(/\r?\n/).slice(info.lineStart, info.lineEnd + 1);
      const ehMobile = this.ehMobile();
      const marcas = lerMarcas(linhas);

      aplicarMarcas(container, {
        tamanho: tamanhoParaDispositivo(marcas, ehMobile),
        alinhamento: marcas.alinhamento
      });

      /* A chave gravada depende de ONDE você arrastou: no celular nasce a
         chave própria dele, e o tamanho do desktop fica intocado. */
      instalarAlca(container, (pct) =>
        this.gravar(ctx, el, ehMobile ? { tamanhoMobile: pct } : { tamanho: pct })
      );

      /* O tamanho aplicado vem do DOM, não das linhas da renderização: se você
         já arrastou, o valor de lá está velho e o menu desfaria o seu
         redimensionamento. Aplica na hora e grava depois — a resposta ao
         clique é o feedback, sem indicador de "salvando". */
      const tamanhoNaTela = () =>
        container.style.width ? parseFloat(container.style.width) : null;

      instalarMenu(container, {
        aoAlinhar: (alinhamento) => {
          aplicarMarcas(container, { tamanho: tamanhoNaTela(), alinhamento });
          this.gravar(ctx, el, { alinhamento });
        },
        /* Só aparece quando ESTE aparelho tem tamanho gravado — relendo o
           arquivo no clique, não usando o que foi lido na renderização. */
        temTamanho: () => tamanhoParaDispositivo(lerMarcasAtuais(ctx, el), ehMobile) != null,
        rotuloLimpar: ehMobile ? textos().limparMobile : textos().limparDesktop,
        aoLimpar: () => {
          aplicarMarcas(container, {
            tamanho: null,
            alinhamento: alinhamentoAtual(container)
          });
          this.gravar(ctx, el, ehMobile ? { tamanhoMobile: null } : { tamanho: null });
        }
      });
    });
  }

  ehMobile() {
    if (obsidian && obsidian.Platform && typeof obsidian.Platform.isMobile === 'boolean') {
      return obsidian.Platform.isMobile;
    }
    return !!(this.app && this.app.isMobile);
  }

  async gravar(ctx, el, alteracoes) {
    /* getSectionInfo é relido AQUI, no clique — nunca guardado da
       renderização. Número de linha envelhece se o arquivo mudar no meio
       (sync, outra edição) e a escrita acertaria a linha errada. */
    const info = ctx.getSectionInfo(el);
    if (!info) return;

    const arquivo = this.app.vault.getAbstractFileByPath(ctx.sourcePath);
    if (!obsidian || !(arquivo instanceof obsidian.TFile)) return;

    await this.app.vault.process(arquivo, (dados) =>
      gravarMarcas(dados, info.lineStart, info.lineEnd, alteracoes)
    );
  }
}

module.exports = {
  __esModule: true,
  default: CfrMermaidSize,
  /* exportadas por nome para os testes em Node */
  lerMarcas,
  gravarMarcas,
  tamanhoParaDispositivo,
  escolherIdioma,
  aplicarMarcas,
  esperarMermaid,
  instalarAlca,
  instalarMenu,
  MIN_PCT,
  MAX_PCT,
  MARCA,
  MARCA_ALINHAMENTO
};

/* nosourcemap */