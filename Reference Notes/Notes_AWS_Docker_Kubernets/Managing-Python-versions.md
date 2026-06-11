---
tags:
  - python
Type: Reference Note
source:
page:
links:
Folgezettel:
---
## virtual environments in python
creating a virtual environment 
```bash
python -m venv venvName
or
python3.11 -m venv venvName
```

Activate a virtual environment 

```bash
source venvName/bin/activate
```

``` Powershell
.\\venvName\\Scripts\\activate.bat
```

- When we run Python using the `python` command, the `sys.path` values are modified so that any imports are looked for inside the virtual environment's third-party library folder. So anything we've installed in the virtual environment will be available, but things we've installed in other virtual environments won't be available.


```bash
pip install -r requirements.txt
```

requirements.txt
- "\==" means "install exactly this version".
- "\>=" means "install the latest version, which must be above the following".

```
requests==1.0.0
flask>=1.1.2
gunicorn==20.0.4
pymongo[srv]==3.11
```

To install the latest minor/patch version of a library, we can do this:
```
flask>=1.1.2,<2.0
```

we usually normally update if there is a minor and patch version update but we tend to be very careful when it comes to Major version updates 

## Managing Python versions

As a note, for Windows I've often use the [`pyenv-win` project](https://github.com/pyenv-win/pyenv-win?ref=blog.teclado.com), which has worked well for me.

To install `pyenv` on MacOS, I've just gone for Homebrew:

First, see if the version of Python you want is available (you may have to update `pyenv` to see recent versions, which I do with `brew update && brew upgrade pyenv`):

```bash
pyenv install --list
```

```bash
pyenv install 3.10.7
```


```bash
pyenv version
```

```bash
pyenv versions
```

If no local is selected it will automatically select a global version
The local version is specific to a particular directory and its subdirectories...
```bash
pyenv local 3.10.7
```

global for my system 
```bash
pyenv global 3.10.7
```


## TLDR
```bash
pyenv exec python -m venv .venv
```

the python version will depend if its defined locally or globally 