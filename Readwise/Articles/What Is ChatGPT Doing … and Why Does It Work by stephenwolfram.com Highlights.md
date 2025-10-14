# What Is ChatGPT Doing … and Why Does It Work?

![rw-book-cover](https://content.wolfram.com/uploads/sites/43/2023/02/hero3-chat-exposition.png)
<br>
>[!note]- Readwise Information
>Title:: What Is ChatGPT Doing … and Why Does It Work?
>Author:: [[stephenwolfram.com]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2023-02-14]]
>Last-Highlighted-Date:: [[2023-11-16]]
>Readwise-Link:: https://readwise.io/bookreview/28365085
>Readwise-Source:: #Readwise/source/reader
>Source URL:: https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/
--- 

## Linked Notes
```dataview
LIST
FROM [[What Is ChatGPT Doing … and Why Does It Work? by stephenwolfram.com Highlights]]
```

---

## Highlights
- The first thing to explain is that what ChatGPT is always fundamentally trying to do is to produce a “reasonable continuation” of whatever text it’s got so far, where by “reasonable” we mean “what one might expect someone to write after seeing what people have written on billions of webpages, etc. [View Highlight](https://readwise.io/open/538819365) ^rw538819365
- it doesn’t look at literal text; it looks for things that in a certain sense “match in meaning”. But the end result is that it produces a ranked list of words that might follow, together with “probabilities [View Highlight](https://readwise.io/open/538819385) ^rw538819385
- just asking over and over again “given the text so far, what should the next word be?” [View Highlight](https://readwise.io/open/538819465) ^rw538819465
- there’s a particular so-called “temperature” parameter that determines how often lower-ranked words will be used, and for essay generation, it turns out that a “temperature” of 0.8 seems best. (It’s worth emphasizing that there’s no “theory” being used here; it’s just a matter of what’s been found to work in [View Highlight](https://readwise.io/open/538819535) ^rw538819535
- Note: Adding a randomness factor to the inference to make the resulting content more realistic and less “flat.”
- There are about 40,000 [reasonably commonly used words in English](https://reference.wolfram.com/language/ref/WordList.html) [View Highlight](https://readwise.io/open/538820175) ^rw538820175
- In a [crawl of the web](https://commoncrawl.org/) there might be a few hundred billion words; in books that have been digitized there might be another hundred billion words. But with 40,000 common words, even the number of possible 2-grams is already 1.6 billion—and the number of possible 3-grams is 60 trillion. So there’s no way we can estimate the probabilities even for all of these from text that’s out there. And by the time we get to “essay fragments” of 20 words, the number of possibilities is larger than the number of particles in the universe, so in a sense they could never all be written down [View Highlight](https://readwise.io/open/538834373) ^rw538834373
- ChatGPT is precisely a so-called “large language model” (LLM) that’s been built to do a good job of estimating those probabilities [View Highlight](https://readwise.io/open/538834388) ^rw538834388
- then a certain set of “knobs you can turn” (i.e. parameters you can set) to fit your data. And in the case of ChatGPT, lots of such “knobs” are used—actually, 175 billion of them [View Highlight](https://readwise.io/open/538834910) ^rw538834910
- The most popular—and successful—current approach uses [neural nets](https://reference.wolfram.com/language/guide/NeuralNetworks.html). Invented—in a form remarkably close to their use today—[in the 1940s](https://www.wolframscience.com/nks/notes-10-12--history-of-ideas-about-thinking/), neural nets can be thought of as simple idealizations of how [brains seem to work](https://www.wolframscience.com/nks/notes-10-12--the-brain/) [View Highlight](https://readwise.io/open/538836313) ^rw538836313
- how does a neural net like this “recognize things”? The key is the [notion of attractors](https://www.wolframscience.com/nks/chap-6--starting-from-randomness`#`sect-6-7--the-notion-of-attractors). [View Highlight](https://readwise.io/open/627450487) ^rw627450487
- For each task we want the neural net to perform (or, equivalently, for each overall function we want it to evaluate) we’ll have different choices of weights. (And—as we’ll discuss later—these weights are normally determined by “training” the neural net using machine learning from examples of the outputs we want [View Highlight](https://readwise.io/open/538836429) ^rw538836429
- makes neural nets so useful (presumably also in brains) is that not only can they in principle do all sorts of tasks, but they can be incrementally “trained from examples” to do those tasks. [View Highlight](https://readwise.io/open/538836781) ^rw538836781
- we just show lots of examples of what’s a cat and what’s a dog, and then have the network “machine learn” from these how to distinguish them [View Highlight](https://readwise.io/open/538836878) ^rw538836878
- rather it’s that the neural net somehow manages to distinguish images on the basis of what we consider to be some kind of “general catness [View Highlight](https://readwise.io/open/538836955) ^rw538836955
- Essentially what we’re always trying to do is to find weights that make the neural net successfully reproduce the examples we’ve given. And then we’re relying on the neural net to “interpolate” (or “generalize”) “between” these examples in a “reasonable” way [View Highlight](https://readwise.io/open/538837191) ^rw538837191
- At each stage in this “training” the weights in the network are progressively adjusted—and we see that eventually we get a network that successfully reproduces the function we want. So how do we adjust the weights? The basic idea is at each stage to see “how far away we are” from getting the function we want—and then to update the weights in such a way as to get closer [View Highlight](https://readwise.io/open/538839906) ^rw538839906
- To find out “how far away we are” we compute what’s usually called a “loss function” (or sometimes “cost function [View Highlight](https://readwise.io/open/538839918) ^rw538839918
