# But What Is a Neural Network? | Chapter 1, Deep Learning

![rw-book-cover](https://i.ytimg.com/vi/aircAruvnKk/maxresdefault.jpg)
<br>
>[!note]- Readwise Information
>Title:: But What Is a Neural Network? | Chapter 1, Deep Learning
>Author:: [[3Blue1Brown]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2017-10-05]]
>Last-Highlighted-Date:: [[2024-06-18]]
>Readwise-Link:: https://readwise.io/bookreview/41597240
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[artificial intelligence]] [[neural network]] 
>Source URL:: https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi
--- 

## Linked Notes
```dataview
LIST
FROM [[But What Is a Neural Network? | Chapter 1, Deep Learning by 3Blue1Brown Highlights]]
```

---

## Highlights
- activation is a high number. So all of these 784 neurons make up the first layer of our network. Now jumping over to the last layer, this has 10 neurons, each representing one of the digits. The activation in these neurons, again some number that's between 0 and 1, represents how much the system thinks that a given image corresponds with a given digit. [View Highlight](https://readwise.io/open/735384413) ^rw735384413 
- See also: [[👻 ai highlighted]] 
- and let me show you what I mean by that. It means if you feed in an image, lighting up all 784 neurons of the input layer according to the brightness of each pixel in the image, that pattern of activations causes some very specific pattern in the next layer which causes some pattern in the one after it, which finally gives some pattern in the output layer. And the brightest neuron of that output layer is the network's choice, so to speak, for what digit this image represents. [View Highlight](https://readwise.io/open/735384414) ^rw735384414 
- See also: [[👻 ai highlighted]] 
- A 4 basically breaks down into three specific lines, and things like that. Now in a perfect world, we might hope that each neuron in the second to last layer corresponds with one of these subcomponents, that anytime you feed in an image with, say, a loop up top, like a 9 or an 8, there's some specific neuron whose activation is going to be close to 1. And I don't mean this specific loop of pixels, the hope would be that any generally loopy pattern towards the top sets off this neuron. [View Highlight](https://readwise.io/open/735384415) ^rw735384415 
- See also: [[👻 ai highlighted]] 
- don't you think? So let me show you a more notationally compact way that these connections are represented. This is how you'd see it if you choose to read up more about neural networks. 214 00:13:41,380 --> 00:13:40,520 Organize all of the activations from one layer into a column as a vector. Then organize all of the weights as a matrix, where each row of that matrix corresponds to the connections between one layer and a particular neuron in the next layer. What that means is that taking the weighted sum of the activations in [View Highlight](https://readwise.io/open/735384416) ^rw735384416 
- See also: [[👻 ai highlighted]] 
