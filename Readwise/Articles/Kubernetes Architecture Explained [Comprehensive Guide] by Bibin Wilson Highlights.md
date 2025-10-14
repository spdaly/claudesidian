# Kubernetes Architecture Explained [Comprehensive Guide]

![rw-book-cover](https://devopscube.com/wp-content/uploads/2022/12/kubernetes-architecture.png)
<br>
>[!note]- Readwise Information
>Title:: Kubernetes Architecture Explained [Comprehensive Guide]
>Author:: [[Bibin Wilson]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2023-01-20]]
>Last-Highlighted-Date:: [[2023-02-08]]
>Readwise-Link:: https://readwise.io/bookreview/24180641
>Readwise-Source:: #Readwise/source/reader
>Source URL:: https://devopscube.com/kubernetes-architecture-explained/
--- 

## Linked Notes
```dataview
LIST
FROM [[Kubernetes Architecture Explained [Comprehensive Guide] by Bibin Wilson Highlights]]
```

---

## Highlights
- The first and foremost thing you should understand about Kubernetes is, it is a **distributed system**. Meaning, it has multiple components spread across different servers over a network. These servers could be Virtual machines or bare metal servers. We call it a Kubernetes cluster. [View Highlight](https://readwise.io/open/472764676) ^rw472764676
- A Kubernetes cluster consists of control plane nodes and worker nodes [View Highlight](https://readwise.io/open/472764671) ^rw472764671
- The **kube-api server** is the central hub of the Kubernetes cluster that exposes the Kubernetes API. [View Highlight](https://readwise.io/open/472764701) ^rw472764701
- [etcd](https://github.com/etcd-io/etcd) is an open-source strongly consistent, distributed key-value store. So what does it mean [View Highlight](https://readwise.io/open/472764839) ^rw472764839
- To put it simply, when you use kubectl to get kubernetes object details, you are getting it from etcd. Also, when you deploy an object like a pod, an entry gets created in etcd [View Highlight](https://readwise.io/open/472765177) ^rw472765177
- etcd it is the only **Statefulset** component in the control plane [View Highlight](https://readwise.io/open/472765537) ^rw472765537
- The kube-scheduler is responsible for **scheduling pods on worker nodes**. [View Highlight](https://readwise.io/open/472766284) ^rw472766284
- [Controllers](https://kubernetes.io/docs/concepts/architecture/controller/) are programs that run infinite control loops. Meaning it runs continuously and watches the actual and desired state of objects. If there is a difference in the actual and desired state, it ensures that the kubernetes resource/object is in the desired state. [View Highlight](https://readwise.io/open/472768668) ^rw472768668
- In Kubernetes, controllers are control loops that watch the state of your cluster, then make or request changes where needed. Each controller tries to move the current cluster state closer to the desired state. [View Highlight](https://readwise.io/open/472768683) ^rw472768683
- Let’s say you want to create a deployment, you specify the desired state in the manifest YAML file (declarative approach). [View Highlight](https://readwise.io/open/472769936) ^rw472769936
- **Kube controller manager** is a component that manages all the Kubernetes controllers. [View Highlight](https://readwise.io/open/472770073) ^rw472770073
- When kubernetes is deployed in cloud environments, the cloud controller manager acts as a bridge between Cloud Platform APIs and the Kubernetes cluster. [View Highlight](https://readwise.io/open/472770130) ^rw472770130
- Kubelet is an agent component that runs on every node in the cluster. t does not run as a container instead runs as a daemon, managed by systemd [View Highlight](https://readwise.io/open/472770568) ^rw472770568
- Service in Kubernetes is a way to expose a set of pods internally or to external traffic. When you create the service object, it gets a virtual IP assigned to it. It is called clusterIP. It is only accessible within the Kubernetes cluster. [View Highlight](https://readwise.io/open/472794563) ^rw472794563
- You cannot ping the ClusterIP because it is only used for service discovery, unlike pod IPs which are pingable [View Highlight](https://readwise.io/open/472794715) ^rw472794715
- When you expose pods using a Service (ClusterIP), Kube-proxy creates network rules to send traffic to the backend pods (endpoints) grouped under the Service object. Meaning, all the load balancing, and service discovery are handled by the Kube proxy. [View Highlight](https://readwise.io/open/472794795) ^rw472794795
- Kubernetes supports multiple [container runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/) (CRI-O, Docker Engine, containerd, etc) that are compliant with **[Container Runtime Interface (CRI)](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-node/container-runtime-interface.md)**. This means, all these container runtimes implement the CRI interface and expose gRPC [CRI APIs](https://kubernetes.io/docs/concepts/architecture/cri/) (runtime and image service endpoints). [View Highlight](https://readwise.io/open/472795133) ^rw472795133
- First, you need to understand **[Container Networking Interface (CNI)](https://www.cni.dev/)**
  It is a plugin-based architecture with vendor-neutral [specifications](https://github.com/containernetworking/cni/blob/spec-v1.0.0/SPEC.md) and libraries for creating network interfaces for Containers. [View Highlight](https://readwise.io/open/472795958) ^rw472795958
- With CNI container networking can be standardized across container orchestration tools like Kubernetes, Mesos, CloudFoundry, Podman, Docker, etc. [View Highlight](https://readwise.io/open/472795534) ^rw472795534
