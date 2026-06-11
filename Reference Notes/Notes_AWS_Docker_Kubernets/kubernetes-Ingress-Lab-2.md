![[ingress+-+lab02+-+resources.html]]


### ANY ANNOTATION USED IN THIS LAB IS NGINX SPECIFIC 



In lab environments and environments that are not exposed to the internet we can do something called self signed certificates 

Usually we use a CA like lets encrypt to get a cert with our website name (url domain name) to have a http request

```ubuntu
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=example.com/0=example.com"
```
-nodes --> don't encrypt the keys 
-keyout [tls.key] --> key name
-out --> certificate name 
canonical name --> CN=example.com
organization name --> 0=example.com

```
ls -ltr
```

secret is a component to add confidential items like tls cert and tls key , api keys , password . we need to let ingress object know the secret name.. 

secret like any kubernetes object can be created in an imperative way and a declarative way 
we will use imperative way because its simpler and faster 

creating a secret object
![[Pasted image 20250423235759.png]]

tls -> indicates that we are creating a secret of type tls so it waits for a cert and a key 


----------

