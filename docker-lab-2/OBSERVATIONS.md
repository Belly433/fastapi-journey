1.  docker run starts a container directly on the local machine using Docker. It is a standalone process managed only by Docker.
In other hand, kubectl run creates a pod inside a Kubernetes cluster. The container is no longer managed directly by the user, but by Kubernetes.

Both using the same image, the main difference is that Kubernetes introduces an orchestration layer: the pod is managed by the cluster instead of running locally.

2. In kubectl describe pod, the Scheduler event is responsible for assigning the pod to a node.

This corresponds to the kube-scheduler component in the Kubernetes control plane. Its role is to decide where the pod should run based on available resources and constraints.

3. components observed:

- kube-apiserver: This is the main entry point of Kubernetes. All commands like kubectl communicate with the cluster through it.
- etcd: This is the key-value database that stores the entire cluster state (nodes, configurations).

4. With the Alpine image, any changes made inside the pod (for example creating files) were lost after exiting or restarting the pod.

This is because pods are ephemeral — they do not persist changes unless storage is explicitly configured.

In Docker Lab 1, changes inside a container could persist if the container was not removed. In Kubernetes, the pod lifecycle is managed differently, and containers are expected to be disposable.

5. After deleting the pod, Kubernetes did not restart it because it was created manually using kubectl run, without any controller managing it.

Kubernetes only ensures self-healing when a higher-level object like a Deployment or ReplicaSet is used. These controllers continuously monitor the desired state and recreate pods if they are deleted. Since the pod was standalone, once deleted, it was permanently removed.
