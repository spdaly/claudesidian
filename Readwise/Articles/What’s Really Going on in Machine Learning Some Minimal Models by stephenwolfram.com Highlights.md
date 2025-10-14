# What’s Really Going on in Machine Learning? Some Minimal Models

![rw-book-cover](https://content.wolfram.com/sites/43/2024/08/sw-ml-social-share-v2.png)
<br>
>[!note]- Readwise Information
>Title:: What’s Really Going on in Machine Learning? Some Minimal Models
>Author:: [[stephenwolfram.com]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2024-08-22]]
>Last-Highlighted-Date:: [[2024-09-05]]
>Readwise-Link:: https://readwise.io/bookreview/43804781
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[machine learning]] [[neural network]] 
>Source URL:: https://writings.stephenwolfram.com/2024/08/whats-really-going-on-in-machine-learning-some-minimal-models/
--- 

## Linked Notes
```dataview
LIST
FROM [[What’s Really Going on in Machine Learning? Some Minimal Models by stephenwolfram.com Highlights]]
```

---

## Highlights
- It’s surprising how little is known about the foundations of machine learning. Yes, from an engineering point of view, an immense amount has been figured out about how to build neural nets that do all kinds of impressive and [sometimes almost magical things](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/). But at a fundamental level we still don’t really know why neural nets “work”—and we don’t have any kind of “scientific big picture” of what’s going on inside them. [View Highlight](https://readwise.io/open/781285237) ^rw781285237 
- See also: [[👻 ai highlighted]] 
- And the simplicity of their construction makes it much easier to “see inside them”—and to get more of a sense of what essential phenomena actually underlie machine learning. One might have imagined that even though the training of a machine learning system might be circuitous, somehow in the end the system would do what it does through some kind of identifiable and “explainable” mechanism. But we’ll see that in fact that’s typically not at all what happens. [View Highlight](https://readwise.io/open/781285238) ^rw781285238 
- See also: [[👻 ai highlighted]] 
- Instead it looks much more as if the training manages to home in on some quite wild computation that “just happens to achieve the right results”. Machine learning, it seems, isn’t building structured mechanisms; rather, it’s basically just sampling from the typical complexity one sees in the computational universe, picking out pieces whose behavior turns out to overlap what’s needed. And in a sense, therefore, the possibility of machine learning is ultimately yet another consequence of the phenomenon of [computational irreducibility](https://www.wolframscience.com/nks/chap-12--the-principle-of-computational-equivalence`#`sect-12-6--computational-irreducibility). [View Highlight](https://readwise.io/open/781285240) ^rw781285240 
- See also: [[👻 ai highlighted]] 
- But the presence of computational irreducibility also has another important implication: that even though we can expect to find limited pockets of computational reducibility, we can’t expect a “general narrative explanation” of what a machine learning system does. In other words, there won’t be a traditional (say, mathematical) “general science” of machine learning (or, for that matter, probably also neuroscience). [View Highlight](https://readwise.io/open/781285258) ^rw781285258
- And while in biology there’s a general sense that “things arise through evolution”, quite how this works has always been rather mysterious. But (rather to my surprise) I recently [found a very simple model](https://writings.stephenwolfram.com/2024/05/why-does-biological-evolution-work-a-minimal-model-for-biological-evolution-and-other-adaptive-processes/) that seems to do well at capturing at least some of the most essential features of biological evolution. And while the model isn’t the same as what we’ll explore here for machine learning, it has some definite similarities. And in the end we’ll find that the core phenomena of machine learning and of biological evolution appear to be remarkably aligned—and both fundamentally connected to the phenomenon of computational irreducibility. [View Highlight](https://readwise.io/open/781285241) ^rw781285241 
- See also: [[👻 ai highlighted]] 
- The typical methodology of neural net training involves progressively tweaking real-valued parameters, usually using methods based on calculus, and on finding derivatives. [View Highlight](https://readwise.io/open/781285749) ^rw781285749
- The fact that this could possibly work relies on the crucial—and at first unexpected—fact that in the computational universe even very simple programs can ubiquitously produce all sorts of complex behavior. And the point then is that this behavior has enough richness and diversity that it’s possible to find instances of it that align with machine learning objectives one’s defined. In some sense what machine learning is doing is to “mine” the computational universe for programs that do what one wants. [View Highlight](https://readwise.io/open/781285242) ^rw781285242 
- See also: [[👻 ai highlighted]] 
- In some sense computational irreducibility “levels the playing field” for different processes of adaptive evolution, and lets even simple ones be successful. Something similar seems to happen for the whole framework we’re using. Any of a wide class of systems seem capable of successful machine learning, even if they don’t have the detailed structure of traditional neural nets. We can see this as a typical reflection of the [Principle of Computational Equivalence](https://www.wolframscience.com/nks/chap-12--the-principle-of-computational-equivalence/): that even though systems may differ in their details, they are ultimately all equivalent in the computations they can do. [View Highlight](https://readwise.io/open/781285243) ^rw781285243 
- See also: [[👻 ai highlighted]] 
- So what does this mean for the “science of machine learning”? One might have hoped that one would be able to “look inside” machine learning systems and get detailed narrative explanations for what’s going on; that in effect one would be able to “explain the mechanism” for everything. But what we’ve seen here suggests that in general nothing like this will work. All one will be able to say is that somewhere out there in the computational universe there’s some (typically computationally irreducible) process that “happens” to be aligned with what we want. [View Highlight](https://readwise.io/open/781285244) ^rw781285244 
- See also: [[👻 ai highlighted]] 
- So what about machine learning? What pockets of computational reducibility show up there, from which we might build “human-level scientific laws”? Much as with the emergence of “simple continuum behavior” from computationally irreducible processes happening at the level of molecules in a gas or ultimate discrete elements of space, we can expect that at least certain computationally reducible features will be more obvious when one’s dealing with larger numbers of components. And indeed in sufficiently large machine learning systems, it’s routine to see smooth curves and apparent regularity when one’s looking at the kind of aggregated behavior that’s probed by things like training curves. [View Highlight](https://readwise.io/open/781285246) ^rw781285246 
- See also: [[👻 ai highlighted]] 
- It has to be said, however, that by laying bare more of the essence of machine learning here, it becomes easier to at least define the issues of merging typical “formal computation” with machine learning. Traditionally there’s been a tradeoff between the computational power of a system and its trainability. And indeed in terms of what we’ve seen here this seems to reflect the sense that “larger chunks of computational irreducibility” are more difficult to fit into something one’s incrementally building up by a process of adaptive evolution. [View Highlight](https://readwise.io/open/781285247) ^rw781285247 
- See also: [[👻 ai highlighted]] 
