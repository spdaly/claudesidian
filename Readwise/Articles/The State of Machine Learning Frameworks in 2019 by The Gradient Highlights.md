# The State of Machine Learning Frameworks in 2019

![rw-book-cover](https://thegradient.pub/content/images/2019/10/pasted-image-0-1.png)
<br>
>[!note]- Readwise Information
>Title:: The State of Machine Learning Frameworks in 2019
>Author:: [[The Gradient]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2019-10-10]]
>Last-Highlighted-Date:: [[2024-11-22]]
>Readwise-Link:: https://readwise.io/bookreview/46112069
>Readwise-Source:: #Readwise/source/reader
>Source URL:: https://thegradient.pub/state-of-ml-frameworks-2019-pytorch-dominates-research-tensorflow-dominates-industry/?utm_source=substack&utm_medium=email
--- 

## Linked Notes
```dataview
LIST
FROM [[The State of Machine Learning Frameworks in 2019 by The Gradient Highlights]]
```

---

## Highlights
- Why do researchers love PyTorch?
  • **Simplicity.** It’s similar to numpy, very pythonic, and integrates easily with the rest of the Python ecosystem. For example, you can simply throw in a pdb breakpoint anywhere into your PyTorch model and it’ll work. In TensorFlow, debugging the model requires an active session and ends up being much trickier.
  • **Great API.** Most researchers prefer PyTorch’s API to TensorFlow’s API. This is partially because PyTorch is better designed and partially because TensorFlow has handicapped itself by switching APIs so many times (e.g. ‘layers’ -> ‘slim’ -> ‘estimators’ -> ‘tf.keras’).
  • **Performance.** Despite the fact that PyTorch’s dynamic graphs give strictly less opportunity for optimization, there have been many anecdotal reports that PyTorch is as [fast](https://www.reddit.com/r/MachineLearning/comments/cvcbu6/d_why_is_pytorch_as_fast_as_and_sometimes_faster/) if not [faster](https://arxiv.org/abs/1608.07249) than TensorFlow. It's not clear if this is really true, but at the very least, TensorFlow hasn't gained a decisive advantage in this area. [View Highlight](https://readwise.io/open/815279266) ^rw815279266
