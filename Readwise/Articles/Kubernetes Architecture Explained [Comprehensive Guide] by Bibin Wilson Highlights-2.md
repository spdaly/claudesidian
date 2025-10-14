# Kubernetes Architecture Explained [Comprehensive Guide]

![rw-book-cover](https://devopscube.com/wp-content/uploads/2022/12/kubernetes-architecture.png)
<br>
>[!note]- Readwise Information
>Title:: Kubernetes Architecture Explained [Comprehensive Guide]
>Author:: [[Bibin Wilson]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2023-01-20]]
>Last-Highlighted-Date:: [[2023-08-07]]
>Readwise-Link:: https://readwise.io/bookreview/24180639
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
- The first and foremost thing you should understand about Kubernetes is, it is a **distributed system**. Meaning, it has multiple components spread across different servers over a network. These servers could be Virtual machines or bare metal servers. We call it a Kubernetes cluster. [View Highlight](https://readwise.io/open/576239725) ^rw576239725
- A Kubernetes cluster consists of control plane nodes and worker nodes [View Highlight](https://readwise.io/open/576239724) ^rw576239724
- The **kube-api server** is the central hub of the Kubernetes cluster that exposes the Kubernetes API. [View Highlight](https://readwise.io/open/576239726) ^rw576239726
- [etcd](https://github.com/etcd-io/etcd) is an open-source strongly consistent, distributed key-value store. So what does it mean [View Highlight](https://readwise.io/open/576239727) ^rw576239727
- To put it simply, when you use kubectl to get kubernetes object details, you are getting it from etcd. Also, when you deploy an object like a pod, an entry gets created in etcd [View Highlight](https://readwise.io/open/576239728) ^rw576239728
- etcd it is the only **Statefulset** component in the control plane [View Highlight](https://readwise.io/open/576239729) ^rw576239729
- The kube-scheduler is responsible for **scheduling pods on worker nodes**. [View Highlight](https://readwise.io/open/576239731) ^rw576239731
- [Controllers](https://kubernetes.io/docs/concepts/architecture/controller/) are programs that run infinite control loops. Meaning it runs continuously and watches the actual and desired state of objects. If there is a difference in the actual and desired state, it ensures that the kubernetes resource/object is in the desired state. [View Highlight](https://readwise.io/open/576239732) ^rw576239732
- In Kubernetes, controllers are control loops that watch the state of your cluster, then make or request changes where needed. Each controller tries to move the current cluster state closer to the desired state. [View Highlight](https://readwise.io/open/576239733) ^rw576239733
- Let’s say you want to create a deployment, you specify the desired state in the manifest YAML file (declarative approach). [View Highlight](https://readwise.io/open/576239735) ^rw576239735
- **Kube controller manager** is a component that manages all the Kubernetes controllers. [View Highlight](https://readwise.io/open/576239737) ^rw576239737
- When kubernetes is deployed in cloud environments, the cloud controller manager acts as a bridge between Cloud Platform APIs and the Kubernetes cluster. [View Highlight](https://readwise.io/open/576239739) ^rw576239739
- Kubelet is an agent component that runs on every node in the cluster. t does not run as a container instead runs as a daemon, managed by systemd [View Highlight](https://readwise.io/open/576239740) ^rw576239740
- Service in Kubernetes is a way to expose a set of pods internally or to external traffic. When you create the service object, it gets a virtual IP assigned to it. It is called clusterIP. It is only accessible within the Kubernetes cluster. [View Highlight](https://readwise.io/open/576239741) ^rw576239741
- You cannot ping the ClusterIP because it is only used for service discovery, unlike pod IPs which are pingable [View Highlight](https://readwise.io/open/576239742) ^rw576239742
- When you expose pods using a Service (ClusterIP), Kube-proxy creates network rules to send traffic to the backend pods (endpoints) grouped under the Service object. Meaning, all the load balancing, and service discovery are handled by the Kube proxy. [View Highlight](https://readwise.io/open/576239743) ^rw576239743
- Kubernetes supports multiple [container runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/) (CRI-O, Docker Engine, containerd, etc) that are compliant with **[Container Runtime Interface (CRI)](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-node/container-runtime-interface.md)**. This means, all these container runtimes implement the CRI interface and expose gRPC [CRI APIs](https://kubernetes.io/docs/concepts/architecture/cri/) (runtime and image service endpoints). [View Highlight](https://readwise.io/open/576239744) ^rw576239744
- First, you need to understand **[Container Networking Interface (CNI)](https://www.cni.dev/)**
  It is a plugin-based architecture with vendor-neutral [specifications](https://github.com/containernetworking/cni/blob/spec-v1.0.0/SPEC.md) and libraries for creating network interfaces for Containers. [View Highlight](https://readwise.io/open/576239747) ^rw576239747
- With CNI container networking can be standardized across container orchestration tools like Kubernetes, Mesos, CloudFoundry, Podman, Docker, etc. [View Highlight](https://readwise.io/open/576239746) ^rw576239746
