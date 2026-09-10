# 📂 Section: Supply Chain Security
## 📖 Image Security
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/Image-Security/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/Image-Security/page)

# Image Security

> Best practices for securing container images, including naming conventions, secure repositories, and Kubernetes pod configurations.

In this lesson, we will explore the best practices for securing container images. We will discuss image naming conventions, configuring secure image repositories, and setting up Kubernetes pods to pull images from these secured repositories. Throughout this article, you'll find examples of pod definitions and commands that illustrate these concepts in detail.

## Understanding Image Names

Consider the following simple pod definition file:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
    - name: nginx
      image: nginx
```

In this definition, an Nginx container is deployed using the image named "nginx". But what exactly does "nginx" represent, and from where is it pulled?

This image name follows Docker's image naming convention. Here, "nginx" is shorthand for "library/nginx". The absence of a user or account name implies that Docker uses its default "library" account, which hosts official images maintained by a dedicated team according to best practices.

:::note
If you create your own repository, replace "library" with your username or company name. For example:
:::

Instead of:

```yaml theme={null}
image: library/nginx
```

you might use:

```yaml theme={null}
image: your-company/nginx
```

## Image Registries

When an image location is not explicitly specified, Kubernetes assumes that the image is pulled from Docker Hub (with the DNS name docker.io). Registries serve as image stores—every time you create or update an image, you push it to a registry. These images are later pulled from the registry for application deployment.

There are numerous popular registries available. For instance, Google's container registry (gcr.io) hosts many Kubernetes-related images, including those used for cluster end-to-end tests. While these images are publicly accessible, internal applications often require a private registry to maintain security.

For example, consider these image names:

```yaml theme={null}
image: docker.io/library/nginx
image: gcr.io/kubernetes-e2e-test-images/dnsutils
```

For in-house applications that should not be publicly available, it is advisable to use an internal private registry. Most cloud service providers—such as AWS, Azure, and Google Cloud Platform (GCP)—offer private registries by default. Regardless of whether it is Docker Hub, Google's registry, or your internal registry, you can secure your repositories with private access and credentials.

## Accessing Private Registries

To run a container using a private image, first authenticate with the private registry using the `docker login` command:

```bash theme={null}
docker login private-registry.io
```

After entering your Docker ID and credentials, you can start your container with a private image:

```bash theme={null}
docker run private-registry.io/apps/internal-app
```

To configure Kubernetes to pull the image from your private registry, update your pod definition to include the full image path:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
    - name: nginx
      image: private-registry.io/apps/internal-app
```

However, since the Docker runtime on the worker nodes pulls these images, Kubernetes needs the appropriate credentials to access the private registry.

### Creating a Kubernetes Secret for Docker Registry

To securely store your registry credentials, create a secret of type Docker registry. Follow these steps:

1. Authenticate against your private registry:

   ```bash theme={null}
   docker login private-registry.io
   docker run private-registry.io/apps/internal-app
   ```

2. Create a Kubernetes secret that stores these credentials:

   ```bash theme={null}
   kubectl create secret docker-registry regcred \
     --docker-server=private-registry.io \
     --docker-username=registry-user \
     --docker-password=registry-password \
     --docker-email=registry-user@org.com
   ```

3. Update your pod definition to include the secret under the `imagePullSecrets` section:

   ```yaml theme={null}
   apiVersion: v1
   kind: Pod
   metadata:
     name: nginx-pod
   spec:
     containers:
       - name: nginx
         image: private-registry.io/apps/internal-app
     imagePullSecrets:
       - name: regcred
   ```

When the pod is created, Kubernetes uses the credentials stored in the secret to authenticate with your private registry and successfully pull the image.

:::note
This guide detailed how to secure container images by understanding image naming conventions, utilizing image registries, and setting up Kubernetes to pull from private registries using secrets.
:::

This concludes our discussion on securing images. For additional practice and further examples on implementing secure images in your Kubernetes clusters, please visit our [practice exercises](/docs/practice-exercises).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/e4511664-185f-4204-9aa2-b4250cbadf84/lesson/1dc8b9e2-2f8c-4c62-b718-cbaadf05a542" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/e4511664-185f-4204-9aa2-b4250cbadf84/lesson/371155ba-3296-4fa9-8909-0bb98679c6ec" />
</CardGroup>

---


# 📂 Section: Supply Chain Security
## 📖 Introduction to KubeLinter
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/Introduction-to-KubeLinter/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/Introduction-to-KubeLinter/page)

# Introduction to KubeLinter

> This article explores KubeLinter, a tool that identifies configuration issues in Kubernetes deployments and ensures adherence to best practices.

In this lesson, we explore KubeLinter—an essential tool that enhances your Kubernetes deployments by identifying configuration issues and ensuring adherence to best practices. KubeLinter scrutinizes your manifest files, highlighting potential risks and offering guidance to improve security, efficiency, and reliability.

Below is a sample Kubernetes deployment manifest used to deploy an application named "myapp" with the image `my-app-image:latest`. Note that this example contains several common misconfigurations:

1. It deploys only a single replica, which eliminates redundancy.
2. It uses the "latest" tag for the image, which is discouraged in production environments.
3. It lacks recommended configurations such as resource requests, resource limits, security contexts, and liveness/readiness probes.

```yaml theme={null}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app-container
        image: my-app-image:latest
        ports:
        - containerPort: 8080
```

KubeLinter helps you address these issues through automated checks and tailored recommendations. Its capabilities include:

* Suggesting the addition of liveness and readiness probes when missing.
* Flagging deployments that use only a single replica.
* Recommending the inclusion of necessary security contexts.
* Enforcing rules that disallow the use of the "latest" tag for container images.
* Validating resource definitions by ensuring proper requests and limits.

All of these checks are configurable, empowering you to enforce custom policies that align with your organization's security and operational standards. After analyzing your Kubernetes manifest files based on these policies, KubeLinter generates a comprehensive report with actionable recommendations.

<Frame>
  ![The image explains Kubelinter's workflow: configurable checks, analysis and linting, and report and suggestions, with document icons and a checkmark symbol.](https://kodekloud.com/kk-media/image/upload/v1752871694/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Introduction-to-KubeLinter/frame_100.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  • Prevents misconfigurations\
  • Enhances security through customizable rules\
  • Improves the reliability of your Kubernetes deployments\
  • Automates reviews, helping to achieve cost efficiency and compliance
</Callout>

<Frame>
  ![The image lists benefits of using Kubelinter: preventing misconfigurations, improving security, enhancing reliability, and enabling automated reviews.](https://kodekloud.com/kk-media/image/upload/v1752871695/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Introduction-to-KubeLinter/frame_120.jpg)
</Frame>

## Installation and Basic Usage

Start by downloading and installing KubeLinter from the official repository with the following commands:

```bash theme={null}
curl -Lo kube-linter.tar.gz \
  https://github.com/stackrox/kube-linter/releases/download/0.2.3/kube-linter-linux-amd64.tar.gz
tar -xzf kube-linter.tar.gz
sudo mv kube-linter /usr/local/bin/
```

After installation, navigate to the directory containing your Kubernetes configuration files, and run KubeLinter to analyze them:

```bash theme={null}
cd path/to/k8s-configs
kube-linter lint .
```

KubeLinter then audits your configurations and flags any detected issues with detailed report outputs.

## Integration with CI/CD Pipelines

Embedding KubeLinter within your CI/CD pipeline ensures that Kubernetes manifests meet security and best practices before deployment. Whether you use Jenkins, GitHub Actions, or any similar platform, integrating KubeLinter helps catch mistakes early on.

Here’s how the typical process works:

1. Check out the code from your repository.
2. Run KubeLinter to lint your Kubernetes configurations.
3. Build Docker images and proceed with subsequent CI/CD tasks if linting passes.
4. Publish test results and issue notifications if problems are detected.

<Frame>
  ![The image illustrates a CI/CD integration workflow: checkout code, lint Kubernetes manifests, build Docker image, push Docker image, and deploy to Kubernetes.](https://kodekloud.com/kk-media/image/upload/v1752871696/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Introduction-to-KubeLinter/frame_200.jpg)
</Frame>

### Jenkins Integration

The following Jenkins pipeline example demonstrates how to incorporate KubeLinter into your CI/CD process:

```groovy theme={null}
stages {
    stage('Checkout') {
        steps {
            checkout scm
        }
    }
    stage('Install KubeLinter') {
        steps {
            sh 'curl -sSfL https://raw.githubusercontent.com/stackrox/kubelinter/main/scripts/install.sh | sh -'
        }
    }
    stage('Lint Kubernetes Manifests') {
        steps {
            sh 'kube-linter lint .'
        }
    }
}
```

### GitHub Actions Integration

Below is an example GitHub Actions configuration for running KubeLinter:

```yaml theme={null}
name: Lint Kubernetes Manifests
on: [push]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run KubeLinter
        run: kube-linter lint .
```

Integrating KubeLinter into your CI/CD workflow guarantees that your Kubernetes configurations undergo thorough validation before deployment, reducing misconfigurations and enhancing your clusters' overall security and stability.

For further details and advanced configuration options, refer to the [KubeLinter documentation](https://github.com/stackrox/kube-linter).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/e4511664-185f-4204-9aa2-b4250cbadf84/lesson/c6882453-00b7-4859-afcc-2cadf7b124ee" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/e4511664-185f-4204-9aa2-b4250cbadf84/lesson/68624590-bdf1-4590-b314-5521bb72bc9c" />
</CardGroup>

---


# 📂 Section: Supply Chain Security
## 📖 Minimize Base Image Footprint
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/Minimize-Base-Image-Footprint/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/Minimize-Base-Image-Footprint/page)

# Minimize base image footprint

> This article provides guidance on minimizing the base image footprint in Docker images for improved efficiency, security, and faster deployments.

Welcome to this comprehensive lesson on minimizing the base image footprint in Docker images. In this guide, you will learn how to structure and optimize your Docker images for efficiency, security, and faster deployments.

## Understanding Base Images

Understanding how images are built is crucial for optimizing them. Consider the following Dockerfile used to build a custom web application image:

```dockerfile theme={null}
# Dockerfile – My Custom Webapp
FROM httpd
COPY index.html htdocs/index.html
```

The initial line of this Dockerfile specifies the parent image from which the custom image is constructed—in this example, the HTTPD image. But have you ever wondered how the HTTPD image itself is constructed? Let’s examine its Dockerfile:

```dockerfile theme={null}
# Dockerfile - httpd
FROM debian:buster-slim
ENV HTTPD_PREFIX /usr/local/apache2
ENV PATH $HTTPD_PREFIX/bin:$PATH
WORKDIR $HTTPD_PREFIX
# <content trimmed>
```

Here, the HTTPD image is built upon the Debian base image. The Debian image is defined as follows:

```dockerfile theme={null}
# Dockerfile - debian:buster-slim
FROM scratch
ADD rootfs.tar.xz /
CMD ["bash"]
```

When an image is constructed from scratch (i.e., without a parent image), it is referred to as a base image. Although terms like "parent image" and "base image" are sometimes used interchangeably, for the purpose of this lesson, any image that serves as the foundation for another image is considered a base image.

## Best Practices for Building Images

When creating Docker images, follow these best practices to ensure efficiency, security, and ease of management:

1. **Separate Applications:**\
   Do not combine multiple applications (e.g., a web server, a database) within a single image. Instead, build separate, modular images for each component. This approach allows each component to manage its own libraries and dependencies and enables independent scaling.

<Frame>
  ![The image shows three icons: a blue globe, a green box, and a pink database, under the title "Modular."](https://kodekloud.com/kk-media/image/upload/v1752871697/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Minimize-base-image-footprint/frame_150.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  For modularity, ensure that each container performs a single task. This not only simplifies management but also enhances security through isolation.
</Callout>

2. **Avoid Data Persistence Inside Containers:**\
   Containers are ephemeral by design. Avoid storing data or state within a container; always make use of external volumes or caching services (e.g., Redis) to persist data securely.

3. **Select Base Images Wisely:**\
   Choose your base image based on your application's specific needs. If your web application requires an HTTPD server, opt for a trusted HTTPD image from Docker Hub. Look for images that come with authenticity markers, such as the official or verified publisher tags, and ensure they are regularly updated.

   Below is a sample snippet for selecting a base image:

   ```dockerfile theme={null}
   FROM <base-image>
   COPY index.html htdocs/index.html
   ```

4. **Minimize Image Size:**\
   Smaller images download faster and launch more quickly. Use minimal versions of operating systems, install only the necessary libraries, and remove temporary files along with unnecessary tools like curl or wget that could be exploited by attackers. Additionally, if package managers (e.g., yum or apt) are not needed in production, consider removing them.

5. **Differentiate Development and Production Images:**\
   Development images may include debugging tools and extra packages that should not be present in production. Maintain separate images for development and production to optimize performance and security.

## Minimizing Vulnerabilities

Reducing the number of packages and keeping your image footprint small can significantly decrease security vulnerabilities. For example, consider using Google's distroless images, which include only the application and runtime dependencies without additional software like package managers, shells, or network tools.

To illustrate the impact on security, compare the vulnerability scan results of a standard HTTP image with an HTTP Alpine image using the Trivy tool:

```bash theme={null}
trivy image httpd
httpd (debian 10.8)
====================
Total: 124 (UNKNOWN: 0, LOW: 88, MEDIUM: 9, HIGH: 25, CRITICAL: 2)

trivy image httpd:alpine
httpd:alpine (alpine 3.12.4)
==============================
Total: 0 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 0)
```

This comparison clearly demonstrates that smaller images with fewer packages have a reduced attack surface, leading to fewer vulnerabilities.

<Callout icon="triangle-alert" color="#FF6B6B">
  Always verify the security updates and patches of any base image you choose to prevent introducing vulnerabilities into your Docker images.
</Callout>

## Conclusion

By following these best practices—selecting suitable base images, reducing installed packages, and maintaining a modular approach—you can build Docker images that are both efficient and secure. Implement what you've learned in this lesson and experiment with hands-on exercises to refine these techniques.

For further reading, consider exploring [Docker’s Official Documentation](https://docs.docker.com/) and [Best Practices for Docker Images](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/e4511664-185f-4204-9aa2-b4250cbadf84/lesson/5ef152ec-a459-4560-a6ff-20f56f4e9fc8" />
</CardGroup>

---


# 📂 Section: Supply Chain Security
## 📖 Overview of Supply Chain Security
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/Overview-of-Supply-Chain-Security/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/Overview-of-Supply-Chain-Security/page)

# Overview of Supply Chain Security

> This article delves into the importance of supply chain security and its role in ensuring the integrity of both physical and digital products.

This article delves into the importance of supply chain security and its role in ensuring the integrity of both physical and digital products.

Imagine a factory assembly line where each product goes through multiple stages before reaching the customer. In a secure supply chain, every stage—from receiving raw materials to the final shipment—is rigorously monitored for quality and safety.

## Stages of a Secure Supply Chain

1. **Receiving and Inspection**\
   The process begins with the receipt of raw materials and components from various suppliers. Each component undergoes thorough quality inspections to confirm its compliance with defined standards. Once verified, the components advance to the next stage.

2. **Assembly and Intermediate Quality Checks**\
   During the assembly phase, components are combined to form the final product. Additional quality and security checks are conducted to ensure that every stage of the build adheres to strict standards.

3. **Rigorous Quality Assurance Testing**\
   In the third phase, comprehensive quality assurance (QA) testing identifies any defects. Detected issues are either corrected immediately or the affected products are reworked.

<Frame>
  ![The image illustrates supply chain security, highlighting a four-phase process with a focus on quality control in Phase 3, ensuring product safety before finalization.](https://kodekloud.com/kk-media/image/upload/v1752871698/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Overview-of-Supply-Chain-Security/frame_60.jpg)
</Frame>

4. **Packaging and Secure Release**\
   Once the product passes all previous stages, it moves to the final phase: packaging and release. Packaged products are shipped securely, ensuring they reach customers without being tampered with. This process serves as a strong analogy for a secure supply chain in software development.

<Callout icon="lightbulb" color="#1CB2FE">
  Just as raw materials are inspected in a factory, developers work in secure environments where source code is written and tested. Securing the supply chain in software involves multiple stages, from development to deployment.
</Callout>

## Securing the Software Development Life Cycle

In a secure software development process, the source code is initially crafted and tested by developers in a trusted environment. Following this, the code enters the build phase—where it is compiled and prepared for deployment. It is crucial to ensure the integrity of the build process by isolating environments, keeping dependencies up-to-date, and scanning for vulnerabilities using tools like [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/) and [Snyk](https://snyk.io/).

Before deployment, container images are scanned thoroughly to detect any vulnerabilities. Tools such as [Clair](https://github.com/quay/clair) and [Trivy](https://github.com/aquasecurity/trivy) are commonly used for this process. This stage is analogous to the careful logistics required to deliver a finished product safely to the end user.

<Frame>
  ![The image illustrates "Supply Chain Security" with stages: Source, Build, Test, and Deploy, each marked with a green check, alongside relevant icons.](https://kodekloud.com/kk-media/image/upload/v1752871699/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Overview-of-Supply-Chain-Security/frame_150.jpg)
</Frame>

## Enhancing Deployment Security

Deployment is the final and critical stage in ensuring software integrity. It involves implementing robust security measures to safeguard production environments from unauthorized access or modifications. Techniques such as [Pod Security Policies](https://kubernetes.io/docs/concepts/policy/pod-security-policy/), network policies, and role-based access controls (RBAC) help secure Kubernetes resources during deployment.

<Frame>
  ![The image outlines "Supply Chain Security" focusing on "Implement Deployment Security" through Pod Security Policies, Network Policies, and Role-Based Access Control (RBAC).](https://kodekloud.com/kk-media/image/upload/v1752871700/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Overview-of-Supply-Chain-Security/frame_200.jpg)
</Frame>

## The Benefits of Robust Supply Chain Security

Implementing a secure supply chain process offers numerous advantages:

* **Early Vulnerability Detection:** Issues are identified during early stages, allowing for swift remediation.
* **Optimized Resource Management:** Continuous inspections prevent security incidents from disrupting production.
* **Improved Compliance:** Adhering to stringent security standards helps organizations meet industry regulations.
* **Efficient Incident Response:** Streamlined processes minimize damage in the event of a breach.
* **Enhanced Overall Security Posture:** A secure supply chain reinforces the integrity of every stage—from development to deployment.

<Frame>
  ![The image outlines supply chain security benefits, including early vulnerability detection, better resource management, improved compliance, efficient incident response, and enhanced security posture across sourcing, building, testing, and deploying stages.](https://kodekloud.com/kk-media/image/upload/v1752871701/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Overview-of-Supply-Chain-Security/frame_240.jpg)
</Frame>

<Callout icon="triangle-alert" color="#FF6B6B">
  Neglecting any stage of the supply chain security process can expose your systems to risks and potential breaches. Always ensure that security measures are enforced at every phase to protect both your digital and physical products.
</Callout>

By comprehensively securing your supply chain, you reinforce the safety of the products and services delivered to your customers, ensuring trust and reliability throughout your operational processes.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/e4511664-185f-4204-9aa2-b4250cbadf84/lesson/7daa7498-717c-4f3c-a1d1-1ca07ddb70b1" />
</CardGroup>

---


# 📂 Section: Supply Chain Security
## 📖 Risks of Inadequate Supply Chain Management
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/Risks-of-Inadequate-Supply-Chain-Management/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/Risks-of-Inadequate-Supply-Chain-Management/page)

# Risks of Inadequate Supply Chain Management

> This article outlines risks associated with inadequate supply chain management in software environments, highlighting vulnerabilities, operational issues, and potential financial and reputational damage.

This article outlines several potential risks associated with inadequate supply chain management in software environments. Poor supply chain practices can expose organizations to vulnerabilities, operational issues, and significant financial and reputational damage. Explore the scenarios below to understand how each risk can manifest and jeopardize your digital ecosystem.

***

## Unpatched Vulnerabilities Leading to Major Data Breaches

Neglecting known vulnerabilities in software components can create an opening for attackers. For instance, if a company overlooks a critical vulnerability, it might lead to exploitation that exposes millions of records. Such an incident can trigger extensive financial losses, regulatory fines, and irreversible damage to customer trust.

<Frame>
  ![The image highlights a high-risk, fixable vulnerability in "Component 4" of an app, potentially causing financial losses, regulatory fines, and customer trust issues.](https://kodekloud.com/kk-media/image/upload/v1752871703/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Risks-of-Inadequate-Supply-Chain-Management/frame_20.jpg)
</Frame>

***

## Risks from Untrusted Third-Party Components

Integrating unverified software components from third-party vendors may introduce hidden malware. Attackers could use these components as a backdoor to infiltrate the network, compromising overall security. This vulnerability not only disrupts operations but also results in expensive incident response and remediation efforts.

<Frame>
  ![The image illustrates unverified content in an app, highlighting components from an untrusted third-party vendor, leading to severe operational disruptions and costly remediation efforts.](https://kodekloud.com/kk-media/image/upload/v1752871704/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Risks-of-Inadequate-Supply-Chain-Management/frame_50.jpg)
</Frame>

***

## Exposure Through Inadequate Credential Security

Storing sensitive credentials without proper encryption leaves them vulnerable. When unencrypted credentials are compromised, attackers gain easy access to critical customer data, potentially leading to severe data breaches and a loss of customer confidence.

<Frame>
  ![The image illustrates configuration errors in deployment, showing unprotected secrets in an app, vulnerable to an attacker.](https://kodekloud.com/kk-media/image/upload/v1752871705/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Risks-of-Inadequate-Supply-Chain-Management/frame_70.jpg)
</Frame>

<Callout icon="triangle-alert" color="#FF6B6B">
  Ensuring that credentials are always encrypted and stored securely is essential to prevent unauthorized access.
</Callout>

***

## Vulnerabilities from Overly Permissive Configuration Settings

Improperly configured access controls can provide attackers with an easy gateway to critical systems. Overly permissive settings, such as lax network policies or missing role-based access controls (RBAC) in Kubernetes clusters, enable attackers to infiltrate vulnerable pods and exploit network weaknesses.

<Frame>
  ![The image illustrates configuration errors in deployment, highlighting how lack of network policies or RBAC in a Kubernetes cluster can facilitate unauthorized access by hackers.](https://kodekloud.com/kk-media/image/upload/v1752871707/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Risks-of-Inadequate-Supply-Chain-Management/frame_100.jpg)
</Frame>

***

## Container Security Misconfigurations and Host Compromise

Improper container security configurations pose a serious risk. If containers are not set up correctly, attackers may break out of the container environment and tamper with the underlying host system. This breach can lead to data theft, manipulation of system operations, and complete host control.

<Frame>
  ![The image illustrates a runtime security threat where attackers escape a compromised container in a Kubernetes cluster, potentially gaining control over the host system.](https://kodekloud.com/kk-media/image/upload/v1752871708/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Risks-of-Inadequate-Supply-Chain-Management/frame_120.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Regular security assessments, proper container isolation, and adherence to best practices in container configuration are crucial to safeguard the host environment.
</Callout>

***

## Summary of Supply Chain Vulnerabilities

The cumulative risks of inadequate supply chain management can pave the way for cyber attacks, operational disruptions, financial losses, regulatory or legal actions, and a competitive disadvantage in the marketplace. It is vital to continuously monitor and update security practices to mitigate these risks effectively.

<Frame>
  ![The image lists common threats and vulnerabilities: cyber attacks, operational disruptions, financial losses, regulatory and legal consequences, and competitive disadvantage.](https://kodekloud.com/kk-media/image/upload/v1752871709/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Risks-of-Inadequate-Supply-Chain-Management/frame_130.jpg)
</Frame>

By understanding and addressing these risks, organizations can build a robust defense mechanism that protects their software supply chain and secures their operational integrity.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/e4511664-185f-4204-9aa2-b4250cbadf84/lesson/547e5337-fe01-4a8a-9c2b-17c39a10f5d7" />
</CardGroup>

---


# 📂 Section: Supply Chain Security
## 📖 SBOM Format
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/SBOM-Format/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/SBOM-Format/page)

# SBOM Format

> This article explores SPDX and CycloneDX SBOM formats, highlighting their focuses on licensing compliance and security aspects respectively.

This article explores two widely adopted Software Bill of Materials (SBOM) formats: SPDX and CycloneDX. Both formats have distinct focuses—SPDX emphasizes licensing and legal compliance, while CycloneDX concentrates on security aspects such as identifying vulnerabilities and managing supply chain risks.

***

## SPDX Format

SPDX is a comprehensive SBOM format that organizes information into several key sections to ensure thorough documentation of software packages.

### Overview

The SPDX format is structured into the following sections:

1. **Document Information:** Contains metadata about the SPDX document, including creator details, creation date, and version.
2. **Relationships:** Defines how various components of the SBOM interrelate (e.g., file-to-package or dependency relationships).
3. **Package Information:** Provides specific software package details such as name, version, supplier, and verification information (e.g., checksums).
4. **Snippets:** Captures smaller sections of code or components, including excerpts from open-source libraries.
5. **File Information:** Tracks individual files within the package.
6. **Additional Metadata:** Offers extra details like notes, licensing information, and review records to ensure the SBOM’s accuracy.

<Frame>
  ![The image outlines the ISBOM SPDX format, listing categories like Document, Package, File, License, Relationships, Snippets, Annotations, and Review Information.](https://kodekloud.com/kk-media/image/upload/v1752871710/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-SBOM-Format/frame_70.jpg)
</Frame>

### Example: SPDX Document for NGINX Package

Below is an example JSON snippet representing an SPDX document for the NGINX package. This document follows the SPDX 2.3 specification and was generated by ANKOR using the SIFT tool.

```json theme={null}
{
  "spdxVersion": "SPDX-2.3",
  "dataLicense": "CC0-1.0",
  "SPDXID": "SPDXRef-DOCUMENT",
  "name": "nginx",
  "documentNamespace": "https://anchore.com/syft/image/nginx-2a35db70-da10-45cd-b82d-00921857780f",
  "creationInfo": {
    "licenseListVersion": "3.25",
    "creators": [
      "Organization: Anchore, Inc",
      "Tool: syft-1.13.0"
    ]
  },
  "created": "2024-09-24T18:17:42Z"
}
```

This document is licensed under CC0 1.0 and provides essential metadata about the NGINX package.

### Example: SPDX Document for the Grep Package

The following JSON snippet details the SPDX document for the grep package (version 3.8-5). It includes supplier information, licensing details, and security references relevant for vulnerability tracking.

```json theme={null}
{
  "package": {
    "name": "grep",
    "SPDXID": "SPDXRef-Package-deb-grep-a86139312d2f5a59d",
    "versionInfo": "3.8-5",
    "supplier": "Person: Anibal Monsalve Salazar (anibal@debian.org)",
    "originator": "Person: Anibal Monsalve Salazar (anibal@debian.org)",
    "downloadLocation": "NOASSERTION",
    "filesAnalyzed": true,
    "packageVerificationCode": {
      "packageVerificationCodeValue": "6da86e7e3a9f53bf5faee3942e2c8e2551ca7d8d"
    },
    "sourceInfo": "acquired package info from DPKG DB: /usr/share/doc/grep/copyright, /var/lib/dpkg/info/grep.md5sums, /var/lib/dpkg/status",
    "licenseConcluded": "NOASSERTION",
    "licenseDeclared": "GPL-3.0-only AND GPL-3.0-or-later",
    "copyrightText": "NOASSERTION",
    "externalRefs": [
      {
        "referenceCategory": "SECURITY",
        "referenceType": "cpe23Type",
        "referenceLocator": "cpe:2.3:a:grep:grep:3.8-5:*****:*:*:*:*:*:*"
      },
      {
        "referenceCategory": "PACKAGE-MANAGER",
        "referenceType": "url",
        "referenceLocator": "pkg:deb/debian/grep@3.8-5?arch=amd64&distro=debian-12"
      }
    ]
  }
}
```

### Example: SPDX File Information for a Pod Namespace Service File

This JSON snippet demonstrates file information for a pod namespace service file, including details such as file types and checksum data.

```json theme={null}
{
  "file": {
    "fileName": "/usr/lib/systemd/system/pam_namespace.service",
    "SPDXID": "SPDXRef-File---systemd-system-pam-namespace.service-87d70ca1b93138b1",
    "fileTypes": [
      "TEXT"
    ],
    "checksums": [
      {
        "algorithm": "SHA1",
        "checksumValue": "9b870dae75ff7a0c34eeb85e4c9c42a8cfdc10f8"
      },
      {
        "algorithm": "SHA256",
        "checksumValue": "e4dcd011776e596cbb73dcffde737aa043b5308fobf797a23d4229de54d716"
      }
    ],
    "licenseConcluded": "NOASSERTION",
    "licenseInfoInFiles": [
      "NOASSERTION"
    ],
    "copyrightText": "",
    "comment": "layerID: sha256:82e2ab394fabf575000041a8f0801b04e91c7027b7c174fe95332c7ebb6501cb"
  }
}
```

<Callout icon="lightbulb" color="#1CB2FE">
  This snippet records detailed metadata about the file, including file type and checksum information. License details are marked as "NOASSERTION" when no definitive information is provided.
</Callout>

***

## CycloneDX Format

CycloneDX is designed as a lightweight SBOM format that places special emphasis on security and compliance. It is particularly useful for identifying vulnerabilities and managing component dependencies.

### Overview

Key sections in the CycloneDX format include:

* **BOM Metadata:** Contains general information about the SBOM such as version, timestamp, and creator details.
* **Components List:** Enumerates the individual parts or modules within the software.
* **Vulnerabilities:** Lists known security vulnerabilities associated with the components.
* **Software Services:** Details any services associated with the software.
* **Annotations:** Provides additional notes or contextual information.
* **Dependencies and Extensions:** Offers further insights into component dependencies and extended metadata.

### Example: CycloneDX BOM in JSON

The following JSON snippet illustrates a CycloneDX BOM, showcasing schema information, metadata, and component details.

```json theme={null}
{
  "$schema": "http://cyclonedx.org/schema/bom-1.6.schema.json",
  "bomFormat": "CycloneDX",
  "specVersion": "1.4",
  "serialNumber": "urn:uuid:e7f6caab-6589-430d-bb7f-0076d23e9efb",
  "version": 1,
  "metadata": {
    "timestamp": "2024-09-24T18:46:28Z",
    "tools": {
      "components": [
        {
          "type": "application",
          "author": "anchore",
          "name": "syft",
          "version": "1.13.0"
        }
      ]
    }
  },
  "component": {
    "bom-ref": "eb2d7db1213e6155",
    "type": "container",
    "name": "nginx",
    "version": "sha256:edf555d07d2ddeb6b616d9024442feac12a91310c9a156fa6f60cd602881a"
  },
  "properties": [
    {
      "name": "syft:image:labels:maintainer",
      "value": "NGINX Docker Maintainers <docker-maint@nginx.com>"
    }
  ],
  "components": [
    {
      "bom-ref": "pkg:deb/debian/adduser@3.134?arch=all&distro=debian-12&package-id=8a498975e59f569c2",
      "type": "library",
      "publisher": "Debian Adduser Developers <adduser@packages.debian.org>"
    }
  ]
}
```

<Callout icon="lightbulb" color="#1CB2FE">
  This CycloneDX BOM snippet highlights the use of the format for documenting containerized applications, and includes metadata about tools utilized during the SBOM generation.
</Callout>

***

## Comparison Between SPDX and CycloneDX

Both SPDX and CycloneDX are powerful SBOM formats, each with their own set of strengths. The table below summarizes their key differences:

| Feature             | SPDX                                                                                          | CycloneDX                                                                                       |
| ------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Format & Complexity | Extensive metadata with focus on licensing and compliance. Available in JSON and RDF formats. | Lightweight format focusing on security and vulnerabilities. Available in JSON and XML formats. |
| Security Focus      | Detailed license data and compliance metrics.                                                 | Emphasizes vulnerability tracking and dependency management.                                    |
| Ease of Use         | More complex due to extensive metadata coverage.                                              | Simpler and more focused on security and compliance.                                            |

<Callout icon="triangle-alert" color="#FF6B6B">
  When choosing an SBOM format, consider your focus—comprehensive legal and licensing details with SPDX versus streamlined security insights with CycloneDX.
</Callout>

<Frame>
  ![The image compares SPDX and CycloneDX, highlighting differences in purpose, format types, complexity, metadata support, license information, dependency tracking, and ease of use.](https://kodekloud.com/kk-media/image/upload/v1752871711/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-SBOM-Format/frame_290.jpg)
</Frame>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/e4511664-185f-4204-9aa2-b4250cbadf84/lesson/17cd35eb-5adc-4732-8814-4037bfe61761" />
</CardGroup>

---


# 📂 Section: Supply Chain Security
## 📖 SBOM Workflow
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/SBOM-Workflow/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/SBOM-Workflow/page)

# SBOM Workflow

> This article provides a comprehensive guide to generating and managing a Software Bill of Materials (SBOM) for secure software supply chain practices.

In this article, we provide a clear and comprehensive guide to generating and managing a Software Bill of Materials (SBOM). This guide covers the entire process—from SBOM generation and secure storage to vulnerability scanning, detailed analysis, remediation, and continuous monitoring. Integrating these practices helps you maintain a secure, compliant software supply chain throughout the development lifecycle.

## Overview of the SBOM Process

The SBOM process is comprised of the following key steps:

1. Generate the SBOM.
2. Securely store the SBOM.
3. Scan the SBOM for vulnerabilities.
4. Analyze the scan results.
5. Remediate the identified issues.
6. Continuously monitor the SBOM.

Two key formats dominate in the SBOM space: SPDX and CycloneDX.

<Frame>
  ![The image illustrates an "SBOM Workflow" with steps: Generate SBOM, Store SBOM, Scan SBOM, Analyze Results, Remediate Issues, and Monitor.](https://kodekloud.com/kk-media/image/upload/v1752871712/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-SBOM-Workflow/frame_30.jpg)
</Frame>

Choose the format that best meets your needs:

* Use SPDX for open-source projects and enterprises that require licensing compliance, trace software origins, audit security, and manage vulnerabilities.
* Opt for CycloneDX to enhance vulnerability management across the software lifecycle and to ensure software integrity.

<Frame>
  ![The image presents a choice between two SBOM standards: SPDX and CycloneDX.](https://kodekloud.com/kk-media/image/upload/v1752871713/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-SBOM-Workflow/frame_50.jpg)
</Frame>

## Generating an SBOM

Syft is a widely used tool for generating SBOMs. To get started, download Syft from the official site. It supports scanning both Docker images and local source code directories. Use the commands below as examples:

```bash theme={null}
# Install Syft on Linux/macOS
curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh

# Generate an SPDX SBOM for a Docker image
syft <image-name>:<tag> -o spdx-json

# Generate an SPDX SBOM for a source code directory
syft /path/to/source/code -o spdx-json
```

Once the SBOM is generated, store it in a secure repository. Popular options include JFrog, Sonatype Nexus, and GitHub Packages.

## Scanning the SBOM

After storing the SBOM securely, the next step is vulnerability scanning. Grype is an excellent tool for this purpose. Follow these steps:

```bash theme={null}
# Install Grype
curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh

# Scan the generated SBOM for vulnerabilities
grype sbom:nginx-sbom.cyclonedx.json
```

The output will list any vulnerabilities found in your SBOM. An example output might look like:

```bash theme={null}
~/code/grype main
➜  grype clshapp/qa-page | head
Vulnerability DB                                     Info update available
Pulling image                                       [5.8 MB / 56 MB]
11 Layers |
```

<Callout icon="lightbulb" color="#1CB2FE">
  Review the output carefully to understand the nature of any vulnerabilities detected.
</Callout>

## Analyzing Vulnerabilities

A detailed analysis of the scan results is essential for effective remediation. Below is an example JSON snippet that details a specific vulnerability:

```json theme={null}
{
  "vulnerability": {
    "id": "CVE-2020-11724",
    "severity": "Medium",
    "links": [
      "http://security-tracker.debian.org/tracker/CVE-2020-11724"
    ]
  },
  "cvss-v2": {
    "base-score": 5,
    "vector": "AV:N/AC:L/Au:N/C:N/I:P/A:N"
  },
  "matched-by": {
    "matcher": "dpkg-matcher",
    "search-key": "distro[debian 9] constraint[< 1.10.3-1+deb9u5 (deb)]"
  },
  "artifact": {
    "name": "libnginx-mod-http-xslt-filter",
    "version": "1.10.3-1+deb9u3",
    "type": "deb",
    "found-by": "dpkg-catalog"
  },
  "locations": [
    {
      "path": "/var/lib/dpkg/status",
      "layer-index": 1
    }
  ],
  "metadata": {
    "package": "libnginx-mod-http-xslt-filter",
    "source": "nginx",
    "version": "1.10.3-1+deb9u3"
  }
}
```

In this example, a medium-severity vulnerability (CVE-2020-11724) is found in the package libnginx-mod-http-xslt-filter (version 1.10.3-1+deb9u3). The vulnerability was flagged using the dpkg-matcher on Debian 9 systems, and additional details can be found through the provided link.

## Remediating Vulnerabilities

After analyzing the vulnerabilities, the next step is remediation. This may involve updating the affected package to a secure version or replacing it with an alternative solution.

<Frame>
  ![The image outlines the SBOM process: generate, store, scan, analyze, remediate issues, and monitor, highlighting a problematic component in an app.](https://kodekloud.com/kk-media/image/upload/v1752871714/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-SBOM-Workflow/frame_190.jpg)
</Frame>

<Callout icon="triangle-alert" color="#FF6B6B">
  Ensure that remediation actions are tested in a controlled environment before deploying into production.
</Callout>

## Continuous Monitoring and Alerts

The final step in the SBOM workflow is to establish continuous monitoring and automated alerts within your CI/CD pipelines. This ensures that dependencies are regularly updated and that any new vulnerabilities or compliance issues are quickly addressed.

<Frame>
  ![The image outlines a continuous monitoring process for ISBOM, including generating, storing, scanning, analyzing, remediating, and monitoring, with automated scanning and regular updates.](https://kodekloud.com/kk-media/image/upload/v1752871716/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-SBOM-Workflow/frame_210.jpg)
</Frame>

By automating these processes, you maintain a proactive stance on software security and compliance throughout your software lifecycle.

## Additional Resources

For more detailed information, consider exploring the following resources:

* [SBOM Best Practices](https://example.com/sbom-best-practices)
* [Syft Documentation](https://github.com/anchore/syft)
* [Grype Documentation](https://github.com/anchore/grype)

Establishing a robust SBOM workflow is essential for creating a secure and reliable software development environment. Embrace these practices to enhance the security and integrity of your software supply chain.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/e4511664-185f-4204-9aa2-b4250cbadf84/lesson/3a467f49-70a7-4b61-bd44-f3cb004c32b8" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/e4511664-185f-4204-9aa2-b4250cbadf84/lesson/f0cf8a6a-06b3-4181-a705-9aa352c29969" />
</CardGroup>

---


# 📂 Section: Supply Chain Security
## 📖 Scan images for known vulnerabilities Trivy
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/Scan-images-for-known-vulnerabilities-Trivy/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/Scan-images-for-known-vulnerabilities-Trivy/page)

# Scan images for known vulnerabilities Trivy

> This guide covers scanning container images for vulnerabilities using Trivy, focusing on CVEs and best practices for maintaining security.

Welcome to this comprehensive guide on securing your container images by scanning them for known security vulnerabilities. In this article, we'll explore the fundamentals behind CVEs (Common Vulnerabilities and Exposures) and demonstrate how to use Trivy—a powerful vulnerability scanner—to secure your container images. This guide is designed to improve the flow of information while ensuring all images, diagrams, and code blocks remain intact.

## Understanding CVEs

CVE stands for Common Vulnerabilities and Exposures. Since no code is perfect, vulnerabilities may exist in software that attackers can exploit. When security researchers discover these vulnerabilities, they report them to a centralized CVE database which helps:

• Simplify bug reporting and avoid duplicate entries.\
• Assign a unique identifier to each vulnerability.\
• Provide detailed information for developers and system administrators to prioritize and remediate issues.

<Frame>
  ![The image shows a webpage listing Common Vulnerabilities and Exposures (CVE) search results, detailing specific security issues with descriptions and identifiers.](https://kodekloud.com/kk-media/image/upload/v1752871717/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Scan-images-for-known-vulnerabilities-Trivy/frame_50.jpg)
</Frame>

CVEs are generally classified as:

1. Vulnerabilities that allow bypassing security controls (for instance, accessing sensitive information intended for authorized users only).
2. Vulnerabilities that degrade system performance, cause service interruptions, or otherwise destabilize the system.

Each CVE is rated using a severity scale—from none to critical—based on a numerical value (typically 0 to 10). A score of 9.5 or a "critical" rating signifies a severe vulnerability that requires immediate remediation, whereas lower scores indicate lesser risks.

<Frame>
  ![The image shows a color-coded CVE severity score scale from 0 to 10, with CVSS v2.0 and v3.0 rating comparisons.](https://kodekloud.com/kk-media/image/upload/v1752871718/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Scan-images-for-known-vulnerabilities-Trivy/frame_130.jpg)
</Frame>

For example, a vulnerability in the NGINX controller installer was discovered where it downloads Kubernetes packages using an insecure HTTP URL instead of HTTPS on Debian and Ubuntu systems. This issue is rated a high severity with a score of 7.3.

<Frame>
  ![The image shows details of CVE-2020-5911, highlighting a high severity score of 7.3 for a vulnerability in NGINX Controller on Debian/Ubuntu systems.](https://kodekloud.com/kk-media/image/upload/v1752871720/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Scan-images-for-known-vulnerabilities-Trivy/frame_190.jpg)
</Frame>

In systems containing numerous packages and containerized services, tracking the vulnerability status of each component can be challenging. Vulnerability scanners come into play by analyzing container images and verifying if certain packages (like a specific version of NGINX, e.g., 1.14.2) have known vulnerabilities.

<Frame>
  ![The image shows a "CVE Scanner" with a smartphone icon and a list of CVE identifiers and descriptions related to software vulnerabilities.](https://kodekloud.com/kk-media/image/upload/v1752871722/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Scan-images-for-known-vulnerabilities-Trivy/frame_240.jpg)
</Frame>

Once vulnerabilities are identified, you can:

* Upgrade to a fixed version.
* Apply additional security measures.
* Remove unnecessary vulnerable packages.

The overall security principle is clear: the fewer packages in your container image, the smaller your attack surface.

## Scanning with Trivy

Trivy by Aqua Security is a straightforward yet powerful vulnerability scanner for container images and other artifacts. It integrates seamlessly with CI/CD pipelines, making it an essential tool for modern DevOps practices. For more details, visit the [Trivy documentation](https://aquasecurity.github.io/trivy/).

### Installing Trivy on Debian-based Systems

Follow these steps to install Trivy:

```bash theme={null}
$ sudo apt-get install wget apt-transport-https gnupg lsb-release
$ wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
$ echo "deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/trivy.list
$ sudo apt-get update
$ sudo apt-get install trivy
```

<Callout icon="lightbulb" color="#1CB2FE">
  Ensure your system meets all prerequisites before installation.
</Callout>

After installing, initiate a scan by specifying the container image name exactly as used in a Docker run command. For instance, to scan the image `nginx:1.18.0`, use the following command:

```bash theme={null}
$ trivy image nginx:1.18.0
```

The scan output might look like this:

```bash theme={null}
2021-03-21T02:54:18.240Z     INFO    Detecting Debian vulnerabilities...
2021-03-21T02:54:18.295Z     INFO    Trivy skips scanning programming language libraries because no supported file was detected

nginx:1.18.0 (debian 10.8)
Total: 155 (UNKNOWN: 0, LOW: 110, MEDIUM: 9, HIGH: 33, CRITICAL: 3)

+------------------+---------------------+----------+-----------------+-----------------------------------------+
|      LIBRARY     |    VULNERABILITY ID | SEVERITY | INSTALLED VERSION|                  TITLE                 |
+------------------+---------------------+----------+-----------------+-----------------------------------------+
| apt              | CVE-2011-3374       | LOW      | 1.8.2.2         | It was found that apt-key in apt, all versions, do not correctly..  |
| bash             | CVE-2019-18276      |          | 5.0-4           | bash: when effective UID is not equal to its real UID the...       |
|                  | TEMP-0841856-B188AF |          |                 | -->security-tracker.debian.org/tracker/TEMP-0841856-B188AF        |
| coreutils      | CVE-2016-2781       |          | 8.30-3          | Non-privileged session can escape to the parent session in chroot  |
|                  | CVE-2017-18018      |          |                 | Race condition vulnerability in chown and chgrp                  |
| curl             | CVE-2020-8169       | HIGH     | 7.64.0-4+deb10u1 | libcurl: Partial password disclosure                             |
+------------------+---------------------+----------+-----------------+-----------------------------------------+
```

Trivy offers additional options to filter and customize your scan results. For example, you can limit the output to only critical or high-severity vulnerabilities, or ignore issues that lack a fix:

```bash theme={null}
$ trivy image --severity CRITICAL nginx:1.18.0
$ trivy image --severity CRITICAL,HIGH nginx:1.18.0
$ trivy image --ignore-unfixed nginx:1.18.0
```

If you have stored a Docker image as a tar archive, you can scan it using the `--input` option:

```bash theme={null}
$ docker save nginx:1.18.0 > nginx.tar
$ trivy image --input nginx.tar
```

<Callout icon="lightbulb" color="#1CB2FE">
  Comparing images from different distributions can be eye-opening. For instance, while an `nginx:1.18.0` image on Debian might report many vulnerabilities, a leaner image like `nginx:1.18.0-alpine` might show none.
</Callout>

## Best Practices for Image Scanning

Regular scanning of your container images is essential for long-term security. Even if a scan shows no vulnerabilities today, new issues can emerge later. Consider the following best practices:

• Periodically rescan images to maintain security over time.\
• Integrate scanning into your deployment workflow using Kubernetes Admission Controllers to inspect images before pod deployment (be mindful of potential delays).\
• Maintain an internal registry with pre-scanned, trusted images to reduce recurring scan overhead.\
• Incorporate vulnerability scanning into your CI/CD pipeline to automatically detect issues in every new build.

<Frame>
  ![The image lists best practices for image scanning, including continuous rescanning, using Kubernetes Admission Controllers, maintaining a pre-scanned repository, and integrating scanning into CI/CD pipelines.](https://kodekloud.com/kk-media/image/upload/v1752871723/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Scan-images-for-known-vulnerabilities-Trivy/frame_450.jpg)
</Frame>

## In Summary

Scanning container images for vulnerabilities is a critical step in ensuring a secure deployment environment. With tools like Trivy, you can efficiently detect and remediate vulnerabilities, thereby reducing your overall attack surface and enhancing your container security posture.

Practice these techniques and integrate regular scans into your workflow to safeguard your systems. For additional information on image scanning and container security, refer to relevant documentation and security guidelines.

Happy scanning!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/e4511664-185f-4204-9aa2-b4250cbadf84/lesson/23e7cda2-6540-4704-9e6b-5754cefc2a55" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/e4511664-185f-4204-9aa2-b4250cbadf84/lesson/43e9d2a7-8f3a-447d-ba9e-586ab14d165b" />
</CardGroup>

---


# 📂 Section: Supply Chain Security
## 📖 Section Introduction
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/Section-Introduction/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/Section-Introduction/page)

# Section Introduction

> This article explores supply chain security, emphasizing container image security and methods for analyzing workloads and scanning for vulnerabilities.

In this article, we dive into the fundamentals of supply chain security with a focus on container image security. Our discussion highlights the significance of reducing the footprint of container images to minimize the attack surface and strengthen overall image security. We then detail various methods for analyzing workloads with industry-standard tools and illustrate how to scan images for known vulnerabilities using popular scanning utilities.

<Callout icon="lightbulb" color="#1CB2FE">
  Throughout this article, you will find several practical labs and hands-on exercises designed to reinforce these concepts and provide real-world application experience.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/e4511664-185f-4204-9aa2-b4250cbadf84/lesson/427111cc-6fb9-4c6f-a533-e7075dc7bb94" />
</CardGroup>

---


# 📂 Section: Supply Chain Security
## 📖 What is SBOM and Why Its Important
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/What-is-SBOM-and-Why-Its-Important/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/What-is-SBOM-and-Why-Its-Important/page)

# What is SBOM and Why Its Important

> This article explores the concept of a Software Bill of Materials (SBOM) and outlines its benefits for software security and compliance.

In this article, we explore the concept of a Software Bill of Materials (SBOM) and outline its benefits.

An SBOM is a comprehensive list of all components that comprise a software application. Much like a recipe details the ingredients, instructions, and allergen information for a meal, an SBOM provides transparency about a software system’s composition—including open-source libraries and third-party dependencies. It offers crucial details such as licenses, versions, and patch statuses.

<Callout icon="lightbulb" color="#1CB2FE">
  An SBOM not only reveals what is inside the software but also helps manage security risks and ensures integrity. In the event of a security incident, teams can rapidly pinpoint affected components and evaluate vulnerabilities, enabling swift corrective actions such as applying patches or replacing compromised elements.
</Callout>

Furthermore, SBOMs simplify dependency management by mapping out components and their interdependencies. This systematic documentation ensures all software parts remain current, thereby reducing risks associated with outdated or insecure dependencies. By cataloging components alongside their vulnerabilities, an SBOM significantly enhances overall software security. Many industries require adherence to regulatory standards regarding software composition, and an SBOM supports compliance by documenting licensing information meticulously.

<Frame>
  ![The image illustrates a Software Bill of Materials (SBOM) concept, highlighting components like software composition, supplier details, security vulnerabilities, licenses, versions, and patch status.](https://kodekloud.com/kk-media/image/upload/v1752871724/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-What-is-SBOM-and-Why-Its-Important/frame_50.jpg)
</Frame>

Key benefits of an SBOM include:

* Improved transparency in software composition
* Quicker incident response during security events
* Efficient management of software dependencies
* Enhanced security through detailed vulnerability tracking
* Easier compliance with regulatory standards

These benefits are particularly advantageous when using open-source components, ensuring that every element adheres to necessary regulatory guidelines.

<Frame>
  ![The image lists benefits of ISBOM: transparency, incident response, dependency management, security, and compliance, each represented by an icon.](https://kodekloud.com/kk-media/image/upload/v1752871725/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-What-is-SBOM-and-Why-Its-Important/frame_110.jpg)
</Frame>

## SBOM Example

Consider the following excerpt as an example of an SBOM. It showcases key components typically included, such as the component name, version, supplier details, licensing, dependencies, and associated vulnerability information:

```json theme={null}
{
  "package": {
    "name": "grep",
    "SPDXID": "SPDXRef-Package-deb-grep-a8613391d2f5a59d",
    "versionInfo": "3.8-5",
    "supplier": "Person: Anibal Monsalve Salazar (anibal@debian.org)",
    "originator": "Person: Anibal Monsalve Salazar (anibal@debian.org)",
    "downloadLocation": "NOASSERTION",
    "filesAnalyzed": true,
    "packageVerificationCode": {
      "packageVerificationCodeValue": "6dab867e2a9f53bf5faee39422e2c82e551ca7d8d"
    },
    "sourceInfo": "acquired package info from DPKG DB: /usr/share/doc/grep/copyright, /var/lib/dpkg/info/grep.list",
    "licenseConcluded": "NOASSERTION",
    "licenseDeclared": "GPL-3.0-only AND GPL-3.0-or-later",
    "copyrightText": "NOASSERTION",
    "externalRefs": [
      {
        "referenceCategory": "SECURITY",
        "referenceType": "cpe22Type",
        "referenceLocator": "cpe:2.3:a:grep:grep:3.8-5:*:*:*:*:*:*:*"
      },
      {
        "referenceCategory": "PACKAGE-MANAGER",
        "referenceType": "url",
        "referenceLocator": "pkg:deb/debian/grep@3.8-5?arch=amd64&distro=debian-12"
      }
    ]
  }
}
```

This example highlights essential SBOM details including metadata about the package, supplier and originator information, licensing, and security references. By providing this comprehensive overview, an SBOM becomes a crucial tool in managing software security and mitigating supply chain risks.

For further details on software security best practices and SBOM implementations, consider exploring additional industry resources and documentation.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/e4511664-185f-4204-9aa2-b4250cbadf84/lesson/5afb3b00-07ba-48fd-a7f1-52e350c7a6b6" />
</CardGroup>

---


# 📂 Section: Supply Chain Security
## 📖 Whitelist Allowed Registries Image Policy Webhook
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/Whitelist-Allowed-Registries-Image-Policy-Webhook/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Supply-Chain-Security/Whitelist-Allowed-Registries-Image-Policy-Webhook/page)

# Whitelist Allowed Registries Image Policy Webhook

> Learn how to whitelist allowed registries in Kubernetes to prevent unauthorized container images from being deployed and enhance cluster security.

In this lesson, learn how to whitelist allowed registries in a Kubernetes cluster to prevent unauthorized container images from being deployed. By default, any user with cluster access can deploy pods with images from any registry—even untrusted sources. This can compromise your cluster's security. The following sections explain how to enforce governance rules to restrict container images to approved registries only.

## Understanding the Risk

Consider the following pod definition file. In the image field, a user can reference an image from any registry:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: sample-pod
spec:
  containers:
    - name: sample-app
      image: some-registry.io/a-very-vulnerable-image
```

Deploying an image with known vulnerabilities may expose other applications on the cluster to risk. An attacker could leverage these vulnerabilities to gain access to the underlying operating system. For enhanced security, it is vital to restrict container images to trusted registries.

## Using Admission Controllers to Restrict Registries

One effective method is to use Kubernetes admission controllers. When a pod creation request is made, it is processed through several stages: authentication, authorization, and admission control. By deploying a validating admission webhook server, you can inspect each incoming request and verify that the container image originates from an approved registry. If not, the webhook will reject the request with a clear error message.

For example, consider the following Python code snippet that demonstrates an admission webhook allowing only images from "internal-registry.io":

```python theme={null}
@app.route("/validate", methods=["POST"])
def validate():
    image_name = request.json["request"]["object"]["spec"]["containers"][0]["image"]
    status = True
    message = ""
    if "internal-registry.io" not in image_name:
        message = "You can only use images from the internal-registry.io"
        status = False
    return jsonify(
        {
            "response": {
                "allowed": status,
                "uid": request.json["request"]["uid"],
                "status": {"message": message},
            }
        }
    )
```

<Callout icon="lightbulb" color="#1CB2FE">
  Ensure that your validating webhook server is highly available. This prevents disruptions in pod creation if the webhook becomes unreachable.
</Callout>

## Implementing Policies with OPA and Rego

An alternative approach is to deploy Open Policy Agent (OPA) with a validating webhook. By leveraging OPA's Rego language, you can write custom policies that allow container images only from trusted registries. The example below denies any image that does not begin with "internal-registry.io/":

```rego theme={null}
package kubernetes.admission

deny[msg] {
    input.request.kind.kind == "Pod"
    image := input.request.object.spec.containers[_].image
    not startswith(image, "internal-registry.io/")
    msg := sprintf("Image '%s' is not from a trusted registry", [image])
}
```

## Using the Built-In ImagePolicyWebhook Admission Controller

The Kubernetes API server includes a built-in admission controller called ImagePolicyWebhook. This controller works with an external webhook server to enforce image policy rules using an admission configuration file.

The diagram below illustrates the Kubernetes admission control process. It covers the steps from executing `kubectl` commands through authentication, authorization, and admission controller validations, culminating in pod creation:

<Frame>
  ![The image illustrates the Kubernetes admission control process, showing steps from kubectl through authentication, authorization, admission controllers, to creating a pod.](https://kodekloud.com/kk-media/image/upload/v1752871727/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Whitelist-Allowed-Registries-Image-Policy-Webhook/frame_150.jpg)
</Frame>

### Admission Configuration File

An admission configuration file provides the necessary details for connecting to the webhook server. It includes a reference to a KubeConfig file for authentication credentials along with parameters such as TTLs, retry backoff intervals, and default behaviors. For example:

```yaml theme={null}
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
- name: ImagePolicyWebhook
  configuration:
    imagePolicy:
      kubeConfigFile: <path-to-kubeconfig-file>
      allowTTL: 50
      denyTTL: 50
      retryBackoff: 500
      defaultAllow: true
```

<Callout icon="lightbulb" color="#1CB2FE">
  If the admission webhook server is unreachable, setting `defaultAllow: true` permits pod creation unless the webhook explicitly denies it. Adjust this setting based on your security requirements.
</Callout>

A typical KubeConfig file referenced above might look like this:

```yaml theme={null}
<path-to-kubeconfig-file>
clusters:
- name: name-of-remote-imagepolicy-service
  cluster:
    certificate-authority: /path/to/ca.pem
    server: https://images.example.com/policy
users:
- name: name-of-api-server
  user:
    client-certificate: /path/to/cert.pem
    client-key: /path/to/key.pem
```

### Enabling the ImagePolicyWebhook in the kube-apiserver

After preparing the admission configuration file, you need to enable the ImagePolicyWebhook admission controller in the kube-apiserver. This is achieved by adding it to the enabled admission plugins flag and specifying the path to the configuration file through the admission control config file flag.

For example, if the kube-apiserver runs as a service, you can configure it with the following flags:

```bash theme={null}
ExecStart=/usr/local/bin/kube-apiserver \
  --advertise-address=${INTERNAL_IP} \
  --allow-privileged=true \
  --apiserver-count=3 \
  --authorization-mode=Node,RBAC \
  --bind-address=0.0.0.0 \
  --enable-swagger-ui=true \
  --etcd-servers=https://127.0.0.1:2379 \
  --event-ttl=1h \
  --runtime-config=api/all \
  --service-cluster-ip-range=10.32.0.0/24 \
  --service-node-port-range=30000-32767 \
  --v=2 \
  --enable-admission-plugins=ImagePolicyWebhook \
  --admission-control-config-file=/etc/kubernetes/admission-config.yaml
```

If the kube-apiserver is deployed as a static pod (for example, in a kubeadm-based setup), include similar flags in the pod manifest:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  name: kube-apiserver
  namespace: kube-system
spec:
  containers:
  - command:
    - kube-apiserver
    - --authorization-mode=Node,RBAC
    - --advertise-address=172.17.0.107
    - --allow-privileged=true
    - --enable-bootstrap-token-auth=true
    - --enable-admission-plugins=ImagePolicyWebhook
  image: k8s.gcr.io/kube-apiserver-amd64:v1.13.3
  name: kube-apiserver
```

With these configurations, the ImagePolicyWebhook admission controller ensures that only container images from approved registries are used when creating pods. This significantly strengthens the overall security posture of your Kubernetes cluster.

## Related Resources

For more detailed information on Kubernetes security practices, refer to the following resources:

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
* [Open Policy Agent (OPA) Documentation](https://www.openpolicyagent.org/docs/latest/)

That concludes this lesson. Proceed to the hands-on labs to practice these configurations and further solidify your understanding of securing Kubernetes clusters.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/e4511664-185f-4204-9aa2-b4250cbadf84/lesson/6125bec1-413f-46be-8c24-2d0fca37dd57" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/e4511664-185f-4204-9aa2-b4250cbadf84/lesson/4046f239-4ef2-431c-affc-9f27032a3b28" />
</CardGroup>

---


