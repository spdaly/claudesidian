# The Docker Handbook – Learn Docker for Beginners

![rw-book-cover](https://www.freecodecamp.org/news/content/images/2021/02/docker-1280x612-2021.png)
<br>
>[!note]- Readwise Information
>Title:: The Docker Handbook – Learn Docker for Beginners
>Author:: [[freeCodeCamp.org]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2021-02-01]]
>Last-Highlighted-Date:: [[2023-02-06]]
>Readwise-Link:: https://readwise.io/bookreview/24120742
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[Containers]] [[Docker]] 
>Source URL:: https://www.freecodecamp.org/news/the-docker-handbook/
--- 

## Linked Notes
```dataview
LIST
FROM [[The Docker Handbook – Learn Docker for Beginners by freeCodeCamp.org Highlights]]
```

---

## Highlights
- Containerization involves encapsulating or packaging up software code and all its dependencies so that it can run uniformly and consistently on any infrastructure. [View Highlight](https://readwise.io/open/471515660) ^rw471515660
- Even if you get through the entire development phase, what if the person responsible for managing the servers follows the wrong deployment procedure?
  All these issues can be solved if only you could somehow:
  • Develop and run the application inside an isolated environment (known as a container) that matches your final deployment environment.
  • Put your application inside a single file (known as an image) along with all its dependencies and necessary deployment configurations.
  • And share that image through a central server (known as a registry) that is accessible by anyone with proper authorization. [View Highlight](https://readwise.io/open/471515785) ^rw471515785
- That is the idea behind containerization: putting your applications inside a self-contained package, making it portable and reproducible across various environments. [View Highlight](https://readwise.io/open/471515800) ^rw471515800
- [Docker](https://www.docker.com/) is such an implementation. It's an open-source containerization platform that allows you to containerize your applications, share them using public or private registries, and also to [orchestrate](https://docs.docker.com/get-started/orchestration/) them. [View Highlight](https://readwise.io/open/471515884) ^rw471515884
- A container is an abstraction at the application layer that packages code and dependencies together. Instead of virtualizing the entire physical machine, containers virtualize the host operating system only. [View Highlight](https://readwise.io/open/471516456) ^rw471516456
- Just like virtual machines, containers are completely isolated environments from the host system as well as from each other. They are also a lot lighter than the traditional virtual machine, so a large number of containers can be run simultaneously without affecting the performance of the host system.‌ [View Highlight](https://readwise.io/open/471516464) ^rw471516464
- Containers and virtual machines are actually different ways of virtualizing your physical hardware. The main difference between these two is the method of virtualization. [View Highlight](https://readwise.io/open/471519756) ^rw471519756
- Each virtual machine comes with its own guest operating system which is just as heavy as the host operating system. [View Highlight](https://readwise.io/open/471519760) ^rw471519760
- Unlike a virtual machine, a container does the job of virtualization in a smarter way. Instead of having a complete guest operating system inside a container, it just utilizes the host operating system via the container runtime while maintaining isolation – just like a traditional virtual machine. [View Highlight](https://readwise.io/open/471519774) ^rw471519774
- Images are multi-layered self-contained files that act as the template for creating containers. They are like a frozen, read-only copy of a container. Images can be exchanged through registries. [View Highlight](https://readwise.io/open/471519909) ^rw471519909
- [Open Container Initiative (OCI)](https://opencontainers.org/) defined a standard specification for container images [View Highlight](https://readwise.io/open/471519949) ^rw471519949
- Containers are just images in running state. [View Highlight](https://readwise.io/open/471520077) ^rw471520077
- An image registry is a centralized place where you can upload your images and can also download images created by others. [View Highlight](https://readwise.io/open/471520089) ^rw471520089
- • **Docker Daemon:** The daemon (`dockerd`) is a process that keeps running in the background and waits for commands from the client. The daemon is capable of managing various Docker objects.
  • **Docker Client:** The client  (`docker`) is a command-line interface program mostly responsible for transporting commands issued by users.
  • **REST API:** The REST API acts as a bridge between the daemon and the client. Any command issued using the client passes through the API to finally reach the daemon. [View Highlight](https://readwise.io/open/471520124) ^rw471520124
- ![docker-run-hello-world](https://www.freecodecamp.org/news/content/images/2021/01/docker-run-hello-world.svg) [View Highlight](https://readwise.io/open/471520158) ^rw471520158
- But the good thing about Alpine is that it's built around `musl` `libc` and `busybox` and is lightweight. Where the latest [ubuntu](https://hub.docker.com/_/ubuntu) image weighs at around 28MB, [alpine](https://hub.docker.com/_/alpine) is 2.8MB. [View Highlight](https://readwise.io/open/471520958) ^rw471520958
- Using bind mounts, you can easily mount one of your local file system directories inside a container. Instead of making a copy of the local file system, the bind mount can reference the local file system directly from inside the container. [View Highlight](https://readwise.io/open/471521142) ^rw471521142
- A network in Docker is another logical object like a container and image. Just like the other two, there is a plethora of commands under the `docker network` group for manipulating networks. [View Highlight](https://readwise.io/open/471521981) ^rw471521981
- By default, Docker has five networking drivers. They are as follows:
  • `bridge` - The default networking driver in Docker. This can be used when multiple containers are running in standard mode and need to communicate with each other.
  • `host` - Removes the network isolation completely. Any container running under a `host` network is basically attached to the network of the host system.
  • `none` - This driver disables networking for containers altogether. I haven't found any use-case for this yet.
  • `overlay` - This is used for connecting multiple Docker daemons across computers and is out of the scope of this book.
  • `macvlan` - Allows assignment of MAC addresses to containers, making them function like physical devices in a network. [View Highlight](https://readwise.io/open/471522046) ^rw471522046
- Instead of writing so many commands, there is an easier way to manage multi-container projects, a tool called [Docker Compose](https://docs.docker.com/compose/). [View Highlight](https://readwise.io/open/471531722) ^rw471531722
- Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. [View Highlight](https://readwise.io/open/471531730) ^rw471531730
