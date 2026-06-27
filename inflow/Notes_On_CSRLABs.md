Please note that an additional field called signerName should also be added when creating CSR. For client authentication to the API server we will use the built-in signer kubernetes.io/kube-apiserver-client.

  

For client authentication to the API server we will use the built-in signer kubernetes.io/kube-apiserver-client.

  

What does line mean isn't the cert already signed by the CA ???

No, at this stage, the certificate is **not** signed yet! That is exactly why this field is required.

This is a very common point of confusion when learning the Kubernetes Certificates API. The confusion usually comes from mixing up a CSR with a final Certificate.

Here is exactly what that line means and how the Kubernetes internal Certificate Authority (CA) handles it.

### 1. A CSR is just an "Application"

A **CSR (Certificate Signing Request)** is not a valid certificate. It is literally just a cryptographic application form. When you generate a CSR using OpenSSL, you are essentially creating a document that says: _"My name is Jane, here is my public key, please turn this into a real certificate."_

Because it is just an application, it is useless until a recognized Certificate Authority (CA) actually stamps (signs) it.

### 2. Kubernetes is the CA

In a normal web environment, you would take your CSR and send it to a company like DigiCert or Let's Encrypt to sign it.

In Kubernetes, **the cluster itself acts as the CA**. You submit your CSR to Kubernetes by creating a `CertificateSigningRequest` YAML object.

### 3. Why `signerName` is Required (The Departments)

When you hand your CSR to Kubernetes, the cluster's internal CA says, _"Okay, I can sign this for you. But what do you intend to use this certificate for?"_

The Kubernetes CA has different internal "departments" (signers) that issue certificates for completely different purposes. If you don't specify the `signerName`, Kubernetes will reject the YAML because it doesn't know which department to route your application to.

Here are the main signers you will encounter:

- **`kubernetes.io/kube-apiserver-client`:** You use this when a human user (like an admin or a developer) needs to authenticate to the API using `kubectl`. It ensures the final certificate is stamped with the correct cryptographic extensions for "Client Authentication."
    
- **`kubernetes.io/kubelet-serving`:** You use this if a worker node needs a certificate so the API server can securely connect to the node's `kubelet` to fetch logs or execute commands.
    
- **`kubernetes.io/kube-apiserver-client-kubelet`:** You use this when the `kubelet` itself needs to log in to the API server to report its status.
    

### The Full CKA Workflow

To see where the actual signing happens, look at the full lifecycle of creating a user in Kubernetes:

1. **The Request:** You create a `.csr` file locally using `openssl req...`
    
2. **The Submission:** You wrap that `.csr` in a Kubernetes YAML file, explicitly setting `signerName: kubernetes.io/kube-apiserver-client`.
    
3. **The Creation:** You run `kubectl apply -f my-csr.yaml`. The API server stores your application, but it is **still in a `Pending` state.** It is not signed yet!
    
4. **The Approval:** A human administrator reviews the application and runs `kubectl certificate approve my-csr`.
    
5. **The Signature:** _This_ is the exact moment the CA signs the certificate. The `kube-controller-manager` looks at the `signerName`, realizes it needs to build a client-auth certificate, signs the CSR using the cluster's `/etc/kubernetes/pki/ca.key`, and attaches the final, usable certificate to the object.
    
6. **The Retrieval:** You extract the final signed certificate by running a command like `kubectl get csr my-csr -o jsonpath='{.status.certificate}'`.
    

Create a CertificateSigningRequest and submit it to a Kubernetes Cluster via kubectl. Below is a snippet of shell that you can use to generate the CertificateSigningRequest.

cat <<EOF | kubectl apply -f -

apiVersion: certificates.k8s.io/v1

kind: CertificateSigningRequest

metadata:

name: myuser # example

spec:

# This is an encoded CSR. Change this to the base64-encoded contents of myuser.csr

request: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQ1ZqQ0NBVDRDQVFBd0VURVBNQTBHQTFVRUF3d0dZVzVuWld4aE1JSUJJakFOQmdrcWhraUc5dzBCQVFFRgpBQU9DQVE4QU1JSUJDZ0tDQVFFQTByczhJTHRHdTYxakx2dHhWTTJSVlRWMDNHWlJTWWw0dWluVWo4RElaWjBOCnR2MUZtRVFSd3VoaUZsOFEzcWl0Qm0wMUFSMkNJVXBGd2ZzSjZ4MXF3ckJzVkhZbGlBNVhwRVpZM3ExcGswSDQKM3Z3aGJlK1o2MVNrVHF5SVBYUUwrTWM5T1Nsbm0xb0R2N0NtSkZNMUlMRVI3QTVGZnZKOEdFRjJ6dHBoaUlFMwpub1dtdHNZb3JuT2wzc2lHQ2ZGZzR4Zmd4eW8ybmlneFNVekl1bXNnVm9PM2ttT0x1RVF6cXpkakJ3TFJXbWlECklmMXBMWnoyalVnald4UkhCM1gyWnVVV1d1T09PZnpXM01LaE8ybHEvZi9DdS8wYk83c0x0MCt3U2ZMSU91TFcKcW90blZtRmxMMytqTy82WDNDKzBERHk5aUtwbXJjVDBnWGZLemE1dHJRSURBUUFCb0FBd0RRWUpLb1pJaHZjTgpBUUVMQlFBRGdnRUJBR05WdmVIOGR4ZzNvK21VeVRkbmFjVmQ1N24zSkExdnZEU1JWREkyQTZ1eXN3ZFp1L1BVCkkwZXpZWFV0RVNnSk1IRmQycVVNMjNuNVJsSXJ3R0xuUXFISUh5VStWWHhsdnZsRnpNOVpEWllSTmU3QlJvYXgKQVlEdUI5STZXT3FYbkFvczFqRmxNUG5NbFpqdU5kSGxpT1BjTU1oNndLaTZzZFhpVStHYTJ2RUVLY01jSVUyRgpvU2djUWdMYTk0aEpacGk3ZnNMdm1OQUxoT045UHdNMGM1dVJVejV4T0dGMUtCbWRSeEgvbUNOS2JKYjFRQm1HCkkwYitEUEdaTktXTU0xMzhIQXdoV0tkNjVoVHdYOWl4V3ZHMkh4TG1WQzg0L1BHT0tWQW9FNkpsYWFHdTlQVmkKdjlOSjVaZlZrcXdCd0hKbzZXdk9xVlA3SVFjZmg3d0drWm89Ci0tLS0tRU5EIENFUlRJRklDQVRFIFJFUVVFU1QtLS0tLQo=

signerName: kubernetes.io/kube-apiserver-client

expirationSeconds: 86400 # one day

usages:

- client auth

EOF

Some points to note:

usages has to be client auth

expirationSeconds could be made longer (i.e. 864000 for ten days) or shorter (i.e. 3600 for one hour). You cannot request a duration shorter than 10 minutes.

request is the base64 encoded value of the CSR file content.

  

usages:

- client auth

  

What does client auth do ?

At a fundamental cryptographic level, `client auth` translates directly to an **x509 Extended Key Usage (EKU)** extension. It dictates the legal, permitted actions the certificate holder is allowed to perform.

When you sit for the CKA and CKS in December, the difference between simply having a valid certificate and having a certificate with the correct _usages_ is a common troubleshooting trap.

Here is the exact breakdown of what this field does and why Kubernetes strictly enforces it.

### The "Visa" Analogy

Think of a Certificate Authority (CA) signature as a government issuing a passport. It proves your identity is real.

However, just because you have a valid passport doesn't mean you can get a job in a foreign country; you need a specific work visa for that. The `usages` field is the visa.

- **`client auth` (Client Authentication):** This tells the API server: _"The person holding this certificate is legally allowed to use it to log in and act as a client making requests."_ This is the exact usage required for a human user or a CI/CD pipeline trying to run `kubectl` commands.
    
- **`server auth` (Server Authentication):** This tells the client: _"The machine holding this certificate is legally allowed to host a service and act as a server."_ This is what the `kube-apiserver` uses on its own `apiserver.crt` to prove to you that it is the real control plane.
    

### The Cryptographic Reality

When you put `- client auth` in your CSR YAML and the Kubernetes CA approves it, the CA physically burns the **TLS Web Client Authentication** Object Identifier (OID) into the final certificate's metadata.

If you try to authenticate to the `kube-apiserver` using a certificate that was signed by the correct CA, but is missing that specific `client auth` extension, the API server will instantly drop your connection. It will say: _"I recognize the signature, but this certificate is not authorized for logging in."_

### The Match Requirement

This field is also a strict validation check against the `signerName` we discussed in your previous question.

Kubernetes is designed to prevent administrators from making stupid mistakes. If you set `signerName: kubernetes.io/kube-apiserver-client`, the internal API logic looks at your YAML and says: _"Okay, you want a client certificate. I will now check your `usages` list. If I do not see `client auth` listed there, I will reject this entire YAML manifest before it even gets submitted."_

  request: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQ1ZqQ0NBVDRDQVFBd0VURVBNQTBHQTFVRUF3d0dZVzVuWld4aE1JSUJJakFOQmdrcWhraUc5dzBCQVFFRgpBQU9DQVE4QU1JSUJDZ0tDQVFFQTByczhJTHRHdTYxakx2dHhWTTJSVlRWMDNHWlJTWWw0dWluVWo4RElaWjBOCnR2MUZtRVFSd3VoaUZsOFEzcWl0Qm0wMUFSMkNJVXBGd2ZzSjZ4MXF3ckJzVkhZbGlBNVhwRVpZM3ExcGswSDQKM3Z3aGJlK1o2MVNrVHF5SVBYUUwrTWM5T1Nsbm0xb0R2N0NtSkZNMUlMRVI3QTVGZnZKOEdFRjJ6dHBoaUlFMwpub1dtdHNZb3JuT2wzc2lHQ2ZGZzR4Zmd4eW8ybmlneFNVekl1bXNnVm9PM2ttT0x1RVF6cXpkakJ3TFJXbWlECklmMXBMWnoyalVnald4UkhCM1gyWnVVV1d1T09PZnpXM01LaE8ybHEvZi9DdS8wYk83c0x0MCt3U2ZMSU91TFcKcW90blZtRmxMMytqTy82WDNDKzBERHk5aUtwbXJjVDBnWGZLemE1dHJRSURBUUFCb0FBd0RRWUpLb1pJaHZjTgpBUUVMQlFBRGdnRUJBR05WdmVIOGR4ZzNvK21VeVRkbmFjVmQ1N24zSkExdnZEU1JWREkyQTZ1eXN3ZFp1L1BVCkkwZXpZWFV0RVNnSk1IRmQycVVNMjNuNVJsSXJ3R0xuUXFISUh5VStWWHhsdnZsRnpNOVpEWllSTmU3QlJvYXgKQVlEdUI5STZXT3FYbkFvczFqRmxNUG5NbFpqdU5kSGxpT1BjTU1oNndLaTZzZFhpVStHYTJ2RUVLY01jSVUyRgpvU2djUWdMYTk0aEpacGk3ZnNMdm1OQUxoT045UHdNMGM1dVJVejV4T0dGMUtCbWRSeEgvbUNOS2JKYjFRQm1HCkkwYitEUEdaTktXTU0xMzhIQXdoV0tkNjVoVHdYOWl4V3ZHMkh4TG1WQzg0L1BHT0tWQW9FNkpsYWFHdTlQVmkKdjlOSjVaZlZrcXdCd0hKbzZXdk9xVlA3SVFjZmg3d0drWm89Ci0tLS0tRU5EIENFUlRJRklDQVRFIFJFUVVFU1QtLS0tLQo=

  

How to delete this fast in VIM instead of using dd

Mashing `dd` fifteen times is a rite of passage, but there are much faster, "Vim-ninja" ways to nuke a giant block of text like that base64 string.

Here are the top three fastest methods, ranked from most precise to most visual.

### 1. The Pro Way: Delete Until a Word (`d/`)

Because you know the next line in your YAML is `signerName:`, you can tell Vim to delete everything from your cursor up to that specific word.

1. Put your cursor on the first letter of the base64 string (`L`).
    
2. Type exactly this: `d/signerName`
    
3. Press **Enter**.
    

**Result:** Vim instantly deletes the entire string and stops perfectly right before `signerName`.

### 2. The Visual Way: Line Visual Mode (`V`)

If you want to actually see exactly what you are deleting before you commit to it, use Visual Mode.

1. Put your cursor on the first line of the string.
    
2. Press **`Shift` + `v`** (This enters Visual Line mode; the whole line will highlight).
    
3. Use the down arrow (or **`j`**) to highlight the rest of the block.
    
4. Press **`d`**.
    

### 3. The Math Way: Multiplier (`[Number]dd`)

If you have line numbers turned on and can see exactly how many lines the block takes up, you can delete them all in one keystroke.

1. Let's say the base64 string spans 14 lines.
    
2. Put your cursor on the first line.
    
3. Type **`14dd`**.
    

**Result:** Vim deletes the next 14 lines instantly.

**Bonus Tip for YAML:** If you ever need to delete an entire curly brace `{}` or bracket `[]` block, put your cursor anywhere inside the brackets and type **`di[`** (delete inside brackets) or **`di{`** (delete inside braces). Vim will instantly hollow out the entire block for you!

the first approach Proway is not working

Ah, I know exactly what happened!

Because that massive base64 string is actually just **one single, very long line** of text (even if it wraps visually on your screen to look like a block), the `d/` command acted a bit too aggressively.

When you typed `d/signerName`, Vim deleted the text, but it also swallowed the invisible line break at the exact end of that long line. This likely yanked `signerName:` up onto the exact same line as `request:` , completely breaking your YAML formatting.

When dealing with a massive string that lives on a single line, here are the actual fastest, one-keystroke "Vim-ninja" commands:

### 1. The Ultimate Ninja Move: `C` (Change to end of line)

Since you are likely deleting the old base64 string so you can paste a new one, this is the absolute best command in Vim.

1. Put your cursor on the `L` at the very beginning of the base64 string.
    
2. Press **`Shift` + `c`** (Capital C).
    

**Result:** Vim instantly deletes the giant string all the way to the end of the line, AND automatically drops you into `INSERT` mode so you can immediately hit paste. Two birds, one stone.

### 2. The Quick Delete: `D` (Delete to end of line)

If you just want to delete the string and stay in normal mode without inserting anything yet.

1. Put your cursor on the `L`.
    
2. Press **`Shift` + `d`** (Capital D).
    

**Result:** It instantly chops off the rest of the line, leaving `request:` perfectly intact, without touching the `signerName:` line below it.

### 3. Delete the "Word": `daw` (Delete a word)

Vim considers that entire unbroken base64 string to be one single "word."

1. Put your cursor anywhere inside the base64 string (it doesn't even have to be at the beginning).
    
2. Type **`daw`** (stands for "delete a word").
    

**Result:** Vim instantly hollows out the string, leaving your cursor right next to `request:` .

diw vs dIw

This is one of the most powerful distinctions in Vim. The difference between a lowercase `w` and an uppercase `W` determines exactly how Vim defines what a "word" actually is.

In short: **Lowercase `w` stops at punctuation. Uppercase `W` only stops at spaces.**

Here is the exact breakdown of how they behave, which is especially critical when editing Kubernetes YAML, IP addresses, or URLs.

### 1. `diw` (Delete Inside word - lowercase)

A lowercase `w` ("word") consists of letters, digits, and underscores. The absolute second Vim sees a dot, a slash, a dash, or a colon, it considers that the end of the word.

**The Scenario:** You have an IP address in your YAML file. Your cursor is on the `168`. `server: https://192.168.1.50:6443`

- **You type:** `diw`
    
- **What Vim sees:** It looks left and right, hits the dots, and says, _"Ah, `168` is the whole word."_
    
- **The Result:** `server: https://192..1.50:6443` (It only deleted the 168).
    

### 2. `diW` (Delete Inside WORD - uppercase)

An uppercase `W` ("WORD") consists of **any non-blank characters**. It completely ignores punctuation. The only thing that stops a `W` is a literal physical space (or a line break).

**The Scenario:** Same exact IP address, cursor still on the `168`. `server: https://192.168.1.50:6443`

- **You type:** `diW`
    
- **What Vim sees:** It looks left and right, ignores the dots and colons, keeps going until it hits the space after `server:` , and says, _"This entire URL string is one giant word."_
    
- **The Result:** `server:` (It deleted the entire URL and IP block perfectly).
    

### The DevOps Cheat Sheet

When you are rushing through a cluster configuration file:

- **Use `diw`** when you want to change a specific segment of a string (e.g., changing `v1` to `v2` in `apps/v1`, or changing `blue` to `green` in `app-config.blue.yaml`).
    
- **Use `diW`** when you want to nuke an entire URL, IP address, file path (`/etc/kubernetes/pki/ca.crt`), or complex YAML value in a single keystroke.
    

so when I was using /d singerName do I just write or should I use : /d signerName ?

Ah, this is a perfect question and highlights one of the most common syntax mix-ups when learning Vim!

To answer directly: **You do not use a colon (`:`), and the `d` must come _before_ the slash.**

You should literally just type this exactly as it appears while in Normal mode, and then press Enter: **`d/signerName`**

Here is exactly why the syntax is structured that way and why adding a colon breaks it.

### The "Grammar" of Vim

Vim commands are built like sentences in English. They almost always follow this formula: **Operator + Motion**.

1. **The Operator (The Verb):** What do you want to do?
    
    - In this case, you want to delete, so your verb is **`d`**.
        
2. **The Motion (The Noun/Destination):** Where do you want to do it?
    
    - You want to do it from where your cursor is right now, all the way up to the word "signerName".
        
    - The command to search forward in Vim is **`/`**.
        
    - So your destination is **`/signerName`**.
        

When you combine them, you say: _"Delete (`d`) up to the search result for signerName (`/signerName`)."_ ### Why you shouldn't use a colon (`:`) In Vim, pressing `:` drops you into a completely different mode called **Command-line mode** (this is what you use for saving with `:w` or quitting with `:q`).

If you type `:` first, Vim expects a global file command, not a quick text-editing command.

### Why `/d` doesn't work

If you type `/d signerName`, you are telling Vim's search function to literally look for the text string _"d signerName"_ in your document. Since that text doesn't exist, Vim will just beep at you or say "Pattern not found."

**Summary:** Make sure you are in Normal mode (hit `Esc` a few times if you aren't sure), type `d`, then type `/signerName`, and hit **Enter**!

okay can I open vim and split the screen to just navigate files and use cat or use the terminal ?

Yes, absolutely! You can turn Vim into a full mini-workspace. Vim actually has a built-in file explorer and a built-in terminal emulator.

This is an incredibly powerful workflow, especially for the CKA exam where you can't install fancy plugins and have to rely on raw Vim.

Here is exactly how you set up that split-screen workspace.

### 1. The File Explorer (`Netrw`)

Vim has a built-in file manager called Netrw. You don't need to leave Vim or use `cat` to look at files.

- **Open a vertical split file explorer:** Type `:Vex` (Vertical Explorer) and press Enter.
    
- **Open a horizontal split file explorer:** Type `:Sex` (Split Explorer) and press Enter.
    

**How to use it:**

- Use `j` and `k` to move up and down the file list.
    
- Press `Enter` on a file to open it in that split.
    
- Press `-` (minus) to go up one directory.
    

### 2. The Built-in Terminal

If you actually want a real bash terminal running inside a Vim split so you can run `kubectl`, `cat`, or `grep` while looking at your YAML file, you can do that too!

- **Open a terminal in a horizontal split:** Type `:term` and press Enter.
    
- **Open a terminal in a vertical split:** Type `:vert term` and press Enter.
    

**The Golden Rule of the Vim Terminal:** When you are in the terminal split, typing acts like a normal bash terminal. **To get back to Vim Normal mode so you can switch windows, you must press:** **`Ctrl + \` followed immediately by `Ctrl + n`** _(Think of it as "Control Backslash, Control Normal")._

### 3. How to Navigate Between Your Splits

Once you have your YAML file on the left and your Terminal or Explorer on the right, you need to jump between them.

Vim uses **`Ctrl + w`** (Window) followed by a directional key:

- **`Ctrl + w` then `h`**: Move to the left split.
    
- **`Ctrl + w` then `l`**: Move to the right split.
    
- **`Ctrl + w` then `j`**: Move to the bottom split.
    
- **`Ctrl + w` then `k`**: Move to the top split.
    

### The Ultimate CKA Workflow

1. Open Vim: `vim my-pod.yaml`
    
2. Open a terminal next to it: `:vert term`
    
3. In the terminal, run `kubectl apply -f my-pod.yaml`. If it fails, leave the error on the screen!
    
4. Press `Ctrl + \` then `Ctrl + n` to escape terminal mode.
    
5. Press `Ctrl + w` then `h` to jump back to your YAML file.
    
6. Fix the typo, type `:w` to save, jump back to the terminal, and run apply again!
    

the ctrl+w and ctrl+\ and ctrl+n is not working in browser environemnt ?

Ah, you have just discovered the ultimate nemesis of the web-based certification exam!

This is not a Vim problem; this is a **Browser problem**.

When you take the CKA exam (or practice on platforms like Killer.sh), you are running a terminal inside a web browser (Chrome, Firefox, etc.). The browser has its own hardcoded shortcuts that take priority over the web page:

- **`Ctrl + w`** tells the browser to **Close the Current Tab**.
    
- **`Ctrl + n`** tells the browser to **Open a New Window**.
    

The browser "steals" these keystrokes before they ever reach Vim. If you try to switch splits, you accidentally close your exam!

Here are the two ways to defeat this, ranging from a quick Vim hack to the ultimate CKA exam strategy.

### Strategy 1: The Vim Remap (The Quick Fix)

If you are determined to use Vim's built-in splits and terminal, you have to tell Vim to use different keys that the browser doesn't care about.

Before you start working, open `~/.vimrc` (`vim ~/.vimrc`) and paste these two lines:

Vim Script

```
" Change terminal escape to Ctrl + x
tnoremap <C-x> <C-\><C-n>

" Change window switching from Ctrl+w to Ctrl+q
nnoremap <C-q> <C-w>
```

Save and exit. Now, to escape the terminal you just press **`Ctrl + x`**, and to switch windows you press **`Ctrl + q` then `h/j/k/l`**.

### Strategy 2: TMUX (The Official CKA "Pro" Strategy)

Relying on Vim's internal terminal during a high-pressure web exam is risky. Almost all CKA candidates abandon Vim splits and use **`tmux`** (Terminal Multiplexer) instead. `tmux` is pre-installed on every exam node, and its command key is **`Ctrl + b`**, which browsers safely ignore!

Instead of splitting Vim, you split your actual terminal screen _before_ you open Vim.

**How to do it instantly:**

1. At your normal bash prompt, type `tmux` and press Enter. (Your screen will refresh with a green bar at the bottom).
    
2. **To split the screen vertically:** Press **`Ctrl + b`**, release both keys, and then press **`%`** (Shift + 5).
    
3. **To jump between left and right:** Press **`Ctrl + b`**, release, and press the **Left or Right Arrow Key**.
    

**The Ultimate Workflow:** Now you have two pure bash terminals side-by-side.

- On the left pane, you run `vim pod.yaml`.
    
- You press `Ctrl + b` -> `Right Arrow`.
    
- On the right pane, you run `kubectl apply -f pod.yaml`.
    
- You don't have to deal with weird terminal escape modes, and you never have to touch `Ctrl + w` again!
    

okay can you set me with Tmux , as I understand I can use tmax to manage windows yet inside each one I need to know VIM as I already know it >

You have the exact right mental model. Think of `tmux` as your window manager and Vim as your text editor. `tmux` carves up your screen into safe, browser-proof boxes, and you run standard Vim inside any box you choose.

Mastering this specific workflow is one of the best ways to reclaim lost time and stay organized during those December certification exams.

Here is your focused, zero-fluff `tmux` setup designed specifically for the CKA/CKS environment.

### 1. The Golden Rule: The "Prefix" Key

Every single command in `tmux` requires a two-step handshake. You must always press the **Prefix Key** first to tell `tmux` you are about to give it an order, otherwise you are just typing into the terminal.

- **The Prefix is:** `Ctrl + b`
    
- **How to use it:** Press `Ctrl` and `b` at the same time, **let go of both keys**, and then press your command key.
    

### 2. The Core Exam Commands

You do not need to be a `tmux` power user. You only need these five commands to survive the exam.

- **Start `tmux`:** Type `tmux` in your normal terminal and press Enter. (You will see a green status bar appear at the bottom).
    
- **Split Vertically (Side-by-Side):** `Ctrl + b` then `%` _(Shift + 5)_
    
- **Split Horizontally (Top/Bottom):** `Ctrl + b` then `"` _(Shift + ')_
    
- **Jump Between Panes:** `Ctrl + b` then the **Arrow Keys** (Up, Down, Left, Right).
    
- **Zoom a Pane (Full Screen):** `Ctrl + b` then `z`. _(This temporarily hides all other panes so you can focus on a giant YAML file. Press `Ctrl + b` then `z` again to shrink it back to normal)._
    
- **Close a Pane:** Just type `exit` in the terminal or press `Ctrl + d`.
    

### 3. The CKA "Secret Weapon" (Mouse Mode)

By default, scrolling with your mouse wheel or clicking on panes doesn't work in `tmux`. You can change this instantly, which makes navigating between Vim and `kubectl` incredibly fast.

As soon as you enter the exam and start `tmux`, type this exact command into the terminal to enable mouse support:

Bash

```
tmux set -g mouse on
```

**What this gives you:**

- You can now physically click on the left or right pane to instantly jump your cursor there (no need for `Ctrl + b` + Arrows).
    
- You can click and drag the dividing line between panes to resize them!
    
- You can scroll up with your mouse wheel to read long `kubectl describe` outputs.
    

### 4. Your Standard Exam Workflow

Here is how you will actually put this together when tackling a question:

1. **Start the environment:** Type `tmux`, press Enter. Type `tmux set -g mouse on`, press Enter.
    
2. **Create your workspace:** Press `Ctrl + b` then `%` to create a left and right pane.
    
3. **The Left Pane (The Editor):** Run `vim deployment.yaml`. This pane is strictly for editing.
    
4. **The Right Pane (The Executioner):** Click into the right pane. Run `kubectl apply -f deployment.yaml`.
    
5. **The Feedback Loop:** If `kubectl` throws an error, look at the line number, click back to your left pane, fix the YAML, save (`:w`), click the right pane, and hit the Up Arrow to run `apply` again.
    

You now have a persistent, browser-safe, dual-monitor setup running inside a single terminal tab!

in the split terminal when I highligt the terminal output with the mouse I cant copy it ?

You just hit the biggest side-effect of turning mouse mode on!

When you enable `mouse on` in `tmux`, it intercepts your mouse clicks. When you highlight text, you are no longer highlighting it for your computer's normal clipboard; you are highlighting it inside `tmux`'s internal memory. That is why standard copy/paste suddenly stops working.

Since you are preparing for the web-based exam environment, here is exactly how you bypass this and get your copy/paste working again.

### Method 1: The "Shift" Key Override (The Fastest Way)

You do not need to turn mouse mode off. You just need to tell your browser to temporarily ignore `tmux`. You do this using the **Shift** key.

1. **Hold down the `Shift` key** on your keyboard.
    
2. While holding `Shift`, **click and drag** your mouse over the text you want to copy (like a pod name or a piece of YAML).
    
3. Because you are holding `Shift`, your browser takes over, and you can now use your normal system copy command (usually **Right-Click -> Copy**, or `Ctrl + Shift + C` / `Cmd + C`).
    
4. To paste it into your Vim pane, go into `INSERT` mode and use your normal paste command (Right-Click -> Paste, or `Shift + Insert`, or `Ctrl + Shift + V`).
    

_Note: On some operating systems, holding `Alt` or `Option` does this instead of `Shift`, but `Shift` is the standard for Linux terminal emulators._

### Method 2: The Native `tmux` Buffer (Copying between panes)

If you just want to copy a line from your `kubectl` output on the right pane, and paste it directly into Vim on the left pane without using your system clipboard, you can use `tmux`'s internal memory!

1. Do **not** hold Shift. Just use your mouse to highlight the text in the terminal.
    
2. **Let go of the mouse button.** The moment you let go, the yellow highlight will disappear. That means `tmux` just secretly copied it into its internal buffer!
    
3. Click over to your Vim pane and make sure you are in `INSERT` mode.
    
4. Press **`Ctrl + b`**, let go, and then press **`]`** (the right square bracket).
    

`tmux` will instantly dump whatever you highlighted right where your cursor is!

apiVersion: certificates.k8s.io/v1

kind: CertificateSigningRequest

metadata:

  creationTimestamp: "2026-06-27T12:28:21Z"

  name: agent-smith

  resourceVersion: "2187"

  uid: 94805837-e36c-48ac-8e50-74d694eb96b2

spec:

  extra:

    authentication.kubernetes.io/credential-id:

    - X509SHA256=e3d94edf9a20962e5f2c5e69333dd911a0109e1d6ec83277461527c29b0ca19d

  groups:

  - system:masters

  - system:authenticated

  request: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQ1dEQ0NBVUFDQVFBd0V6RVJNQThHQTFVRUF3d0libVYzTFhWelpYSXdnZ0VpTUEwR0NTcUdTSWIzRFFFQgpBUVVBQTRJQkR3QXdnZ0VLQW9JQkFRRE8wV0pXK0RYc0FKU0lyanBObzV2UklCcGxuemcrNnhjOStVVndrS2kwCkxmQzI3dCsxZUVuT041TXVxOTlOZXZtTUVPbnJEVU8vdGh5VnFQMncyWE5JRFJYall5RjQwRmJtRCs1eld5Q0sKeTNCaWhoQjkzTUo3T3FsM1VUdlo4VEVMcXlhRGtuUmwvanYvU3hnWGtvazBBQlVUcFdNeDRCcFNpS2IwVSt0RQpJRjVueEF0dE1Wa0RQUTdOYmVaUkc0M2IrUVdsVkdSL3o2RFdPZkpuYmZlek90YUF5ZEdMVFpGQy93VHB6NTJrCkVjQ1hBd3FDaGpCTGt6MkJIUFI0Sjg5RDZYYjhrMzlwdTZqcHluZ1Y2dVAwdEliT3pwcU52MFkwcWRFWnB3bXcKajJxRUwraFpFV2trRno4MGxOTnR5VDVMeE1xRU5EQ25JZ3dDNEdaaVJHYnJBZ01CQUFHZ0FEQU5CZ2txaGtpRwo5dzBCQVFzRkFBT0NBUUVBUzlpUzZDMXV4VHVmNUJCWVNVN1FGUUhVemFsTnhBZFlzYU9SUlFOd0had0hxR2k0CmhPSzRhMnp5TnlpNDRPT2lqeWFENnRVVzhEU3hrcjhCTEs4S2czc3JSRXRKcWw1ckxaeTlMUlZyc0pnaEQ0Z1kKUDlOTCthRFJTeFJPVlNxQmFCMm5XZVlwTTVjSjVURjUzbGVzTlNOTUxRMisrUk1uakRRSjdqdVBFaWM4L2RoawpXcjJFVU02VWF3enlrcmRISW13VHYybWxNWTBSK0ROdFYxWWllKzBIOS9ZRWx0K0ZTR2poNUw1WVV2STFEcWl5CjRsM0UveTNxTDcxV2ZBY3VIM09zVnBVVW5RSVNNZFFzMHFXQ3NiRTU2Q0M1RGhQR1pJcFVibktVcEF3a2ErOEUKdndRMDdqRytocGtueG11RkFlWHhnVXdvZEFMYUo3anUvVERJY3c9PQotLS0tLUVORCBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0K

  signerName: kubernetes.io/kube-apiserver-client

  usages:

  - digital signature

  - key encipherment

  - server auth

  username: agent-x

status: {}

  

  

What are these groups ?

These groups represent the Kubernetes authorization groups for the person who **submitted** this CSR to the API server.

When you run `kubectl apply -f my-csr.yaml`, the Kubernetes API server intercepts the request and automatically injects your `username` and `groups` into the YAML before saving it. This is a security feature so that the administrator approving the certificate knows exactly who requested it.

Here is exactly what those two specific groups mean in Kubernetes:

### 1. `system:masters` (The "God Mode" Group)

This is the single most powerful and dangerous group in Kubernetes. It is heavily tested on both the CKA and CKS exams.

- **What it does:** It completely bypasses all Role-Based Access Control (RBAC).
    
- **The Rule:** If a user belongs to `system:masters`, the API server doesn't even bother checking if a `Role` or `ClusterRole` exists for them. It instantly grants them permission to do absolutely anything in the cluster.
    
- **Exam Tip:** You should never assign regular human users or service accounts to this group. It is strictly meant for the cluster administrator (which is why the `admin.conf` file generated by `kubeadm` has this group baked into its certificate).
    

### 2. `system:authenticated` (The Default Group)

This is a built-in baseline group.

- **What it does:** It simply means the API server recognized the user's credentials (like a valid token, OIDC login, or valid certificate).
    
- **The Rule:** Any time a user successfully logs in, the API server automatically slaps the `system:authenticated` group onto their session. It doesn't grant any special permissions by itself, but it distinguishes them from `system:unauthenticated` (anonymous users).
    

### 🚨 The CKA/CKS Exam Trap in this YAML 🚨

Because you are studying for the exams, you need to look very closely at the `usages` list in the YAML you provided:

YAML

```
  usages:
  - digital signature
  - key encipherment
  - server auth    <--- WARNING!
```

Based on our previous conversation, you know that `kubernetes.io/kube-apiserver-client` is a signer strictly used for **client authentication** (users logging into the cluster).

However, whoever created this YAML requested `server auth` (which is used for a server proving its identity to a client).

If you try to submit this exact YAML to a modern Kubernetes cluster, the API server will instantly reject it with an error. The API server strictly enforces that the `usages` requested perfectly match the `signerName`. If you want a client certificate, you _must_ request `client auth`!

okay but is the groups created part of the RBAC sections ?? in the course I don't understand what it is ?

This is one of the most frustrating roadblocks when studying for the CKA, because the official documentation and courses often skip over a massive "secret" about how Kubernetes handles identities.

Here is the secret that will make the entire RBAC system click for you: **Users and Groups do not exist inside Kubernetes.** You cannot run `kubectl get users` or `kubectl create group`. There is no database table inside `etcd` that stores user accounts or group memberships. Kubernetes completely outsources identity management.

Here is exactly how Groups work and how they connect to the RBAC section.

### 1. Where does the Group actually live?

Since Kubernetes doesn't store groups, the group only exists **inside the certificate itself** (or inside an OIDC token if you are using a corporate login like Azure AD or Keycloak).

When we looked at that CSR earlier, you saw:

YAML

```
groups:
- system:masters
```

When the Kubernetes CA signs that certificate, it physically burns that group name into the cryptographic metadata of the certificate (specifically into the `Organization` or `O=` field of the x509 cert).

### 2. The API Server (The Bouncer)

When you type a `kubectl` command, you hand your certificate to the API server. The API server acts like a bouncer at a club. It reads the certificate and says: _"Okay, the cryptography is valid. I see your name is 'agent-x', and I see your certificate says you belong to a group called 'developers'."_

At this exact moment, the API server doesn't know what "developers" means. It just trusts the certificate.

### 3. RBAC (The Rulebook)

This is where the RBAC section of your course comes in. RBAC does not _create_ the group; RBAC simply **maps permissions to the group name that the API server read from the certificate.**

You create a `Role` (the permissions). Then, you create a `RoleBinding` (the bridge).

Here is what the `RoleBinding` looks like:

YAML

```
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods-binding
  namespace: default
subjects:
- kind: Group         # <--- Here is the connection!
  name: developers    # The API server looks for this exact string in your cert
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

### The Full Flow Summary

1. **The Administrator (You):** Uses OpenSSL to create a certificate with the word `developers` baked into it. You give this certificate to a junior engineer.
    
2. **The Junior Engineer:** Runs `kubectl get pods`.
    
3. **Authentication:** The API Server reads the cert and says, _"You have the `developers` badge."_
    
4. **Authorization (RBAC):** The API Server checks the RBAC `RoleBindings`. It finds one that says, _"Anyone wearing the `developers` badge is allowed to read pods."_
    
5. **The Result:** The command succeeds!
    

So, the Group is just a string of text passed from the certificate to the RBAC engine. The RBAC engine just checks if that string matches any rules you wrote in your YAML!