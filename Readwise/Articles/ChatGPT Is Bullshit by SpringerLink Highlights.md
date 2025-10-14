# ChatGPT Is Bullshit

![rw-book-cover](https://media.springernature.com/full/springer-static/cover-hires/journal/10676)
<br>
>[!note]- Readwise Information
>Title:: ChatGPT Is Bullshit
>Author:: [[SpringerLink]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2024-06-08]]
>Last-Highlighted-Date:: [[2024-06-21]]
>Readwise-Link:: https://readwise.io/bookreview/41678079
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[artificial intelligence]] [[ethics]] [[Ethics]] [[generative ai]] 
>Source URL:: https://link.springer.com/article/10.1007/s10676-024-09775-5
--- 

## Linked Notes
```dataview
LIST
FROM [[ChatGPT Is Bullshit by SpringerLink Highlights]]
```

---

## Highlights
- In this paper, we argue against the view that when ChatGPT and the like produce false claims they are lying or even hallucinating, and in favour of the position that the activity they are engaged in is bullshitting, in the Frankfurtian sense (Frankfurt, [2002](https://link.springer.com/article/10.1007/s10676-024-09775-5`#`ref-CR11), [2005](https://link.springer.com/article/10.1007/s10676-024-09775-5`#`ref-CR12)). Because these programs cannot themselves be concerned with truth, and because they are designed to produce text that *looks* truth-apt without any actual concern for truth, it seems appropriate to call their outputs bullshit. [View Highlight](https://readwise.io/open/736488921) ^rw736488921
- We think that this is worth paying attention to. Descriptions of new technology, including metaphorical ones, guide policymakers’ and the public’s understanding of new technology; they also inform applications of the new technology. They tell us what the technology is for and what it can be expected to do. Currently, false statements by ChatGPT and other large language models are described as “hallucinations”, which give policymakers and the public the idea that these systems are misrepresenting the world, and describing what they “see”. We argue that this is an inapt metaphor which will misinform the public, policymakers, and other interested parties. [View Highlight](https://readwise.io/open/736489360) ^rw736489360 
- See also: [[👻 ai highlighted]] [[favorite]] 
- However, large language models, and other AI models like ChatGPT, are doing considerably less than what human brains do, and it is not clear whether they do what they do in the same way we do [View Highlight](https://readwise.io/open/736489584) ^rw736489584
- The most obvious difference between an LLM and a human mind involves the *goals* of the system. [View Highlight](https://readwise.io/open/736489625) ^rw736489625
- They do so by estimating the likelihood that a particular word will appear next, given the text that has come before. [View Highlight](https://readwise.io/open/736489647) ^rw736489647
- Note: Great simple definition of what an LLM is doing behind the scenes.
- The machine does this by constructing a massive statistical model, one which is based on large amounts of text, mostly taken from the internet. This is done with relatively little input from human researchers or the designers of the system; rather, the model is designed by constructing a large number of nodes, which act as probability functions for a word to appear in a text given its context and the text that has come before it. Rather than putting in these probability functions by hand, researchers feed the system large amounts of text and train it by having it make next-word predictions about this training data. They then give it positive or negative feedback depending on whether it predicts correctly. Given enough text, the machine can construct a statistical model giving the likelihood of the next word in a block of text all by itself.
  This model associates with each word a vector which locates it in a high-dimensional abstract space, near other words that occur in similar contexts and far from those which don’t. When producing text, it looks at the previous string of words and constructs a different vector, locating the word’s surroundings – its context – near those that occur in the context of similar words. We can think of these heuristically as representing the meaning of the word and the content of its context. But because these spaces are constructed using machine learning by repeated statistical analysis of large amounts of text, we can’t know what sorts of similarity are represented by the dimensions of this high-dimensional vector space. Hence we do not know how similar they are to what we think of as meaning or context. The model then takes these two vectors and produces a set of likelihoods for the next word; it selects and places one of the more likely ones—though not always the most likely. Allowing the model to choose randomly amongst the more likely words produces more creative and human-like text; the parameter which controls this is called the ‘temperature’ of the model and increasing the model’s temperature makes it both seem more creative and more likely to produce falsehoods. The system then repeats the process until it has a recognizable, complete-looking response to whatever prompt it has been given. [View Highlight](https://readwise.io/open/736489848) ^rw736489848
- Note: Elevator pitch on how LLMs work.
- The accuracy problem for LLMs and other generative Ais is often referred to as the problem of “AI hallucination”: the chatbot seems to be hallucinating sources and facts that don’t exist. These inaccuracies are referred to as “hallucinations” in both technical (OpenAI, [2023](https://link.springer.com/article/10.1007/s10676-024-09775-5`#`ref-CR23)) and popular contexts (Weise & Metz, [2023](https://link.springer.com/article/10.1007/s10676-024-09775-5`#`ref-CR28)). [View Highlight](https://readwise.io/open/736490205) ^rw736490205 
- See also: [[generative ai]] 
- Note: Definition of hallucinations with references.
- One attempted solution is to hook the chatbot up to some sort of database, search engine, or computational program that can answer the questions that the LLM gets wrong (Zhu et al., [2023](https://link.springer.com/article/10.1007/s10676-024-09775-5`#`ref-CR31)). [View Highlight](https://readwise.io/open/736490342) ^rw736490342 
- See also: [[retrieval augmented generation]] 
- The problem here isn’t that large language models hallucinate, lie, or misrepresent the world in some way. It’s that they are not designed to represent the world at all; instead, they are designed to convey convincing lines of text. [View Highlight](https://readwise.io/open/736491169) ^rw736491169
- “Nothing in the design of language models (whose training task is to predict words given context) is actually designed to handle arithmetic, temporal reasoning, etc. To the extent that they sometimes get the right answer to such questions is only because they happened to synthesize relevant strings out of what was in their training data. No reasoning is involved […] Similarly, language models are prone to making stuff up […] because they are not designed to express some underlying set of information in natural language; they are only manipulating the form of language” (Shah & Bender, [2022](https://link.springer.com/article/10.1007/s10676-024-09775-5`#`ref-CR26)). [View Highlight](https://readwise.io/open/736491226) ^rw736491226
- Note: LLMs getting it right is only a matter of probability given the data used to train the model. It's not reasoning.
- The suggestion that the speaker must intend to deceive is a common stipulation in literature on lies. According to the “traditional account” of lying: [View Highlight](https://readwise.io/open/736491637) ^rw736491637
- Frankfurt understands bullshit to be characterized not by an intent to deceive but instead by a reckless disregard for the truth. [View Highlight](https://readwise.io/open/736491679) ^rw736491679
- Note: What is bullshit?
- For an utterance to be classed as bullshit, it must not be accompanied by the explicit intentions that one has when lying, i.e., to cause a false belief in the hearer. Of course, it must also not be accompanied by the intentions characterised by an honest utterance. So far this story is entirely negative. Must any positive intentions be manifested in the utterer? [View Highlight](https://readwise.io/open/736491837) ^rw736491837
- We are not confident that chatbots can be correctly described as having any intentions at all, and we’ll go into this in more depth in the next Sect. (3.2). But we are quite certain that ChatGPT does not intend to convey truths, and so is a soft bullshitter. We can produce an easy argument by cases for this. Either ChatGPT has intentions or it doesn’t. If ChatGPT has no intentions at all, it trivially doesn’t intend to convey truths. So, it is indifferent to the truth value of its utterances and so is a soft bullshitter. [View Highlight](https://readwise.io/open/736489361) ^rw736489361 
- See also: [[👻 ai highlighted]] 
- Bullshit (general)
  Any utterance produced where a speaker has indifference towards the truth of the utterance.
  Hard bullshit
  Bullshit produced with the intention to mislead the audience about the utterer’s agenda.
  Soft bullshit
  Bullshit produced without the intention to mislead the hearer regarding the utterer’s agenda. [View Highlight](https://readwise.io/open/736492048) ^rw736492048
- Note: Types of bullshit
- ChatGPT functions not to convey truth or falsehood but rather to convince the reader of – to use Colbert’s apt coinage – the *truthiness* of its statement, and ChatGPT is designed in such a way as to make attempts at bullshit efficacious (in a way that pens, dictionaries, etc., are not). So, it seems that at minimum, ChatGPT is a soft bullshitter: if we take it not to have intentions, there isn’t any attempt to mislead about the attitude towards truth, but it *is* nonetheless engaged in the business of outputting utterances that look as if they’re truth-apt. We conclude that ChatGPT is a *soft bullshitter.* [View Highlight](https://readwise.io/open/736489362) ^rw736489362 
- See also: [[👻 ai highlighted]] 
- The basic architecture of these models reveals this: they are designed to come up with a *likely continuation of a string of text* [View Highlight](https://readwise.io/open/736492154) ^rw736492154
- This is why we favour characterising ChatGPT as a bullshit machine. This terminology avoids the implications that perceiving or remembering is going on in the workings of the LLM. We can also describe it as bullshitting whenever it produces outputs. Like the human bullshitter, some of the outputs will likely be true, while others not. And as with the human bullshitter, we should be wary of relying upon any of these outputs. [View Highlight](https://readwise.io/open/736489364) ^rw736489364 
- See also: [[👻 ai highlighted]] 
- Edwards also notes that attributing resulting problems to “hallucinations” of the models may allow creators to “blame the AI model for faulty outputs instead of taking responsibility for the outputs themselves” [View Highlight](https://readwise.io/open/736492543) ^rw736492543 
- See also: [[generative ai]] [[👻 ai highlighted]] 
- In human psychology, a “confabulation” occurs when someone’s memory has a gap and the brain convincingly fills in the rest without intending to deceive others. ChatGPT does not work like the human brain, but the term “confabulation” arguably serves as a better metaphor because there’s a creative gap-filling principle at work […]. [View Highlight](https://readwise.io/open/736492629) ^rw736492629
