1. A Pod is a smallest unit in Kubernets that runs one or more containers. Deployment can create mutltiple replicas and restart failed Pods. Deployment can manage Pods automatically.
I would use a Deployment instead of a bare Pod for better scalability as I did to scale web app from 1 to 3.

2. ConfigMap is used for the MongoDB URL in order to make the application easier to manage because if the database URL changes, it can be updated without editing the Deployment file.

3. The original pod was not removed. When I changed replicas from 1 to 3, Kubernetes kept the original pod running and created additional pods. 

4. if MongoDB pod crached, the web application may fail to access the database temporarily. 
Kubernets automatically tries to restart MongoDB pod beacuse it's managed by Deployment.

5. One thing hat confused me was when I re-ran the Kubernetes YAML commands and it kept showing "unchanged". I thought something was off because i wanted to take screenshots of the creation process but Kubernetes was telling me that the resources already existed. I solved this by checking the running resources using "kubectl get all" and taking the required screenshot.