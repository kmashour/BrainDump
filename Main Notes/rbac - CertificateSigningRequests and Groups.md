---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[rbac]]"
sub_type: core-concept
source_type: documentation
tags:
  - kubernetes/rbac
  - kubernetes/security
  - status/completed
---

# rbac - CertificateSigningRequests and Groups

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Main Notes/rbac]] > **CertificateSigningRequests and Groups**

---

## 🎯 CSR as a Cryptographic Application

A **Certificate Signing Request (CSR)** is not a valid certificate. It is a cryptographic application form that binds a public key to an identity (Common Name `CN` and Organizations `O`).
* **The CA Signature:** In a Kubernetes cluster, the cluster itself acts as the Certificate Authority (CA). When a CSR is submitted, it remains in a `Pending` state. The controller manager (`kube-controller-manager`) signs the certificate using the cluster root key (`/etc/kubernetes/pki/ca.key`) only after the CSR resource is explicitly approved (`kubectl certificate approve`).
* **Metadata Injection:** When a CSR is submitted via `kubectl apply`, the API server automatically intercepts the request and injects the user's active `username` and `groups` into the CSR object metadata. This records exactly who requested the certificate for audit purposes.

---

## ⚙️ The Role of `signerName`

Kubernetes directs CSRs to specific signing pipelines (departments) using the `signerName` field:
1. **`kubernetes.io/kube-apiserver-client`:** Issues client certificates for human users or external controllers to authenticate against the API server. Stamped with Extended Key Usage (EKU) for client auth.
2. **`kubernetes.io/kubelet-serving`:** Issues serving certificates for node Kubelets to secure connection endpoints (e.g. when the API server contacts a Kubelet to fetch logs or execute commands).
3. **`kubernetes.io/kube-apiserver-client-kubelet`:** Issues client certificates for Kubelets to authenticate themselves when communicating back to the API server.

---

## 🔒 Extended Key Usages (EKU) & TLS Validation

The `usages` list in the CSR spec translates directly to **x509 Extended Key Usage (EKU)** metadata fields burned into the signed certificate:
* **`client auth` (Client Authentication):** Encodes the **TLS Web Client Authentication** Object Identifier (OID) in the cert. The API server drops TLS handshakes if a client attempts to connect using a cert missing this OID.
* **`server auth` (Server Authentication):** Encodes the **TLS Web Server Authentication** OID. Used by servers to prove identity.
* **Validation Check Constraint:** The API server enforces strict validation checks. For example, if `signerName` is set to `kubernetes.io/kube-apiserver-client`, the `usages` list **must** contain `client auth` (and not `server auth` exclusively). If a mismatch is detected, the API validation engine rejects the manifest at submission time.

---

## 👥 How Groups Map to RBAC

Kubernetes does **not** store or manage users or groups inside its database (`etcd`). There are no `kubectl get users` or `kubectl create group` commands.

```
[ Certificate / Token ]
   Organization (O=developers)  -----\
                                     v
                              [ API Server ] ---> Matches string name ---> [ RoleBinding ] ---> Grants access
                                     ^
[ RoleBinding Subject ]              |
   Group: developers  ---------------/
```

1. **Organization Field Encoding:** When generating a CSR, the group names are added as Organization (`O=`) fields in the Subject line (e.g., `/CN=agent-smith/O=system:masters/O=developers`).
2. **Identity Extraction:** Upon connection, the API server's authenticator decrypts the client certificate, reads the `O=` fields, and registers the client's session under those group names.
3. **RBAC Subject Binding:** The authorization engine checks the `subjects` section of all active `RoleBindings` and `ClusterRoleBindings`. If it finds a subject of `kind: Group` whose name matches the group name extracted from the cert, it applies the permissions of the referenced `Role` or `ClusterRole`.

### Key Built-in Groups
* **`system:masters`:** A hardcoded administrative bypass group. Users in this group bypass all RBAC checks completely—the API server automatically permits any request they make, making it a critical security boundary.
* **`system:authenticated`:** A baseline group automatically applied to any session that completes a valid authentication handshake.

---

*Read more in the main security module: [0-7_security_and_network_policies.md](../Reference%20Notes/0-7_security_and_network_policies.md#L368-L428)*
