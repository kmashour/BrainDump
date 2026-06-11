![[configmaps+and+secrets.html]]



We said over and over is that declarative programming is better and having files with the configurations steps can be helpful 

but in config maps and secrets are things that imperative way of programming is much more convenient than  the declarative way  

```
kubectl get configmap app-config -o yaml
```

in the end of the day after using imperative we will want to save the configuration in some sort of file to keep track of the changes this command will return the component data to a yml format so i can copy it a file and include it in the version control, its saved by the kubernetes cluster to we just ask the api-server to retrieve that data and save to a file 

in this the imperative approach saved me time and created a manifest for me 


  --from-literal=LOG_LEVEL="INFO"\ --> level of verbosity in the logs 

```
name: DATABASE_URL  
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: DATABASE_URL --> 
```
 name: DATABASE_URL --> the name of the env variable that will be updated inside the app 
 
 key: DATABASE_URL --> the name of the key inside the config map that we will use its value to assign the env variable name it can be any name but we choose the same name so it is easier debugged   

in the example we used two types of of config maps passing the environment variables and volume mounts and its valid no problem 

![[Pasted image 20250426133325.png]]

as we can see the mount path was /etc/config , the volume mount did the following created a file which is the key and inside it is the value 

The better approach is organization dependent, sometimes when injecting such files in a container some organization may use encryption tool within the container as part of the application running and the decryption process will a insider job as part of the running application within the container   

------------------------------

In secrets the imperative way may even save more time because it will do the encoding part, values must be base64 