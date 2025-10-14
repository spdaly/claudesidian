# Mixture of Experts: How an Ensemble of AI Models Decide As One

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_174804/1695407369-0923-ensemble-models-explained.jpg)
<br>
>[!note]- Readwise Information
>Title:: Mixture of Experts: How an Ensemble of AI Models Decide As One
>Author:: [[Deepgram]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2023-09-22]]
>Last-Highlighted-Date:: [[2024-06-18]]
>Readwise-Link:: https://readwise.io/bookreview/41596930
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[Architecture]] [[artificial intelligence]] [[Mixture of Experts]] [[Technology]] 
>Source URL:: https://deepgram.com/learn/mixture-of-experts-ml-model-guide?utm_source=www.aiminds.com&utm_medium=newsletter&utm_campaign=marc-andreessen-s-ai-manifesto-sora-s-biggest-competitor-and-andrew-ng-on-ai-governance
--- 

## Linked Notes
```dataview
LIST
FROM [[Mixture of Experts: How an Ensemble of AI Models Decide As One by Deepgram Highlights]]
```

---

## Highlights
- Mixture of Experts [View Highlight](https://readwise.io/open/735381113) ^rw735381113
- Artificial neural networks have emerged as the cornerstone of [deep learning](https://deepgram.com/ai-glossary/deep-learning), offering a remarkable way of drawing valuable insights from a plethora of data. However, the efficacy of these neural networks hinges heavily on their parameter count. [Mixture-of-Experts (MoE)](https://deepgram.com/ai-glossary/mixture-of-experts) presents an efficient approach to dramatically increasing a model’s capabilities without introducing a proportional amount of computational overhead. [View Highlight](https://readwise.io/open/735382213) ^rw735382213 
- See also: [[👻 ai highlighted]] 
- Originally [proposed](https://www.cs.toronto.edu/~hinton/absps/jjnh91.pdf) in 1991 by Robert A. Jacobs et al., MoE adopts a conditional computation paradigm by only selecting parts of an ensemble, referred to as experts, and activating them depending on the data at hand. [View Highlight](https://readwise.io/open/735382034) ^rw735382034
- Notably, each expert model is initialized and trained in the same manner, and the gating network is typically configured to dispatch data equally to each expert. Unlike traditional MoE methods, all experts are trained jointly with the MoE layer on the same dataset. It is fascinating how each expert can become “specialized” in their own task, and experts in MoE do not collapse into a single model. [View Highlight](https://readwise.io/open/735382214) ^rw735382214 
- See also: [[👻 ai highlighted]] 
