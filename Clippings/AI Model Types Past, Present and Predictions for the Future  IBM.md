---
title: "AI Model Types: Past, Present and Predictions for the Future | IBM"
source: "https://www.ibm.com/think/insights/ai-model-types-past-present-future-predictions"
author:
  - "[[Rina Caballar]]"
  - "[[Cole Stryker]]"
published:
created: 2025-10-14
description: "AI models have come a long way. What began as rule-based, programmed engines or expert systems have evolved into trained models capable of autonomous decision-making or predictions. Let’s look at how AI models have changed and how they’re shaping up for the future."
tags:
  - "clippings"
---
My IBM Subscribe

## Authors

Staff Writer

IBM Think

Staff Editor, AI Models

IBM Think

have come a long way. What began as rule-based, programmed engines or expert systems have evolved into trained models capable of autonomous decision-making or predictions. AI applications, in turn, have moved beyond [game-playing programs](https://www.ibm.com/history/early-games) to (genAI) tools capable of complex .

Let’s look at how AI models have changed and how they’re shaping up for the future.

Industry newsletter

### The latest AI trends, brought to you by experts

Get curated insights on the most important—and intriguing—AI news. Subscribe to our weekly Think newsletter. See the [IBM Privacy Statement](https://www.ibm.com/privacy).

Your subscription will be delivered in English. You will find an unsubscribe link in every newsletter. You can manage your subscriptions or unsubscribe [here](https://www.ibm.com/account/reg/signup?formid=news-urx-51525). Refer to our [IBM Privacy Statement](https://www.ibm.com/us-en/privacy) for more information.  

## Classic AI model types are here to stay

Traditional AI models have been around for decades. Two of these fundamental paradigms include and models. While models predict discrete categories, regression models predict continuous values. Both fall under , a (ML) technique that relies on for .

Conventional ML model types owe their staying power to years of research. They have been honed over time, and their maturity and proven approaches align with sectors like finance and healthcare, where deterministic results are often favored over the probabilistic outputs of more complex models. For example, classifiers help with , distinguishing fraudulent from legitimate transactions. Meanwhile, aid in tasks like image classification, and , identifying the exact location and boundaries of tumors in medical images and specifying whether they’re benign or malignant.

Other industries also continue to adopt classical machine learning models. Marketing teams can apply classifiers for on social media, manufacturing companies can use models for supply chain and scientists can implement support vector regression (an extension of ) for climate modeling.

## The AI model types topping current charts

Within the last decade or so, AI advancements have mostly focused on , a subset of ML that simulates the human brain’s intricate decision-making through deep, multilayered . This has ushered in a genAI era, with trained using strategies to make sense of unlabeled without the need for human intervention.

Generative model types started with variational , which propelled further breakthroughs in anomaly detection and . Then came and for image and video generation.

But the true game-changer was the . This neural network architecture excels at handling sequential , making it an ideal fit for . Transformers evolved from and now power the behind popular virtual assistants and such as OpenAI’s (backed by ), AI tools like Midjourney for image generation, AI-powered coding assistants like GitHub Copilot and even the recent surge of .

Innovation has been swift, with transformers shifting from supporting mainly NLP tasks to , such as vision transformers for . [Abraham Daniels](https://research.ibm.com/people/abraham-daniels), a Senior Technical Product Manager for IBM’s [Granite](https://www.ibm.com/granite) suite of , refers to these efforts as a “consolidation of model capabilities” that can improve the . “From a user standpoint, it’s about getting the right model for the job.”

Models continue to evolve. , for example, are to break down complex problems, applying techniques that incentivize these LLMs to generate smaller, intermediate “ steps” before arriving at a conclusion. Meanwhile, [world models](https://www.ibm.com/think/news/cosmos-ai-world-models) learn computational representations of the real world, including causal relationships, physical dynamics and spatial characteristics. These learning algorithms can help [physical AI](https://www.ibm.com/think/news/physical-ai-age-p-1-engineering-brain) systems like robots and self-driving cars better perceive and navigate their environments in real time.

For Daniels, the approach is the current mainstay. MoE divides a deep learning model into “experts”—subnetworks that specialize in processing particular input data—then selectively activates certain experts for a specific task. “MoE models are still the de facto model types that demonstrate the highest performance while still maintaining a level of efficiency on training and ,” he says.

However, , specifically that can effectively tackle long sequences, are gaining ground and might soon dethrone MoE. At [IBM Research](https://research.ibm.com/), for instance, Daniels and his team are working on a hybrid model combining the best of Mamba and MoE. “We take a lot of the efficiencies from a Mixture of Experts-style model and the capabilities of a state space model.”

### Redefining beauty through AI innovation

Malcolm Gladwell dives into the exciting collaboration between L'Oréal and IBM, exploring how a custom AI foundation model could revolutionize cosmetic product development and drive more innovation and sustainability.

## Where the next generation of AI models are headed

The rapid pace of development in means that different types of AI models keep cropping up, making it difficult to predict what to expect in the coming years. But [David Cox](https://research.ibm.com/people/david-cox), VP for AI models at IBM Research, has noticed an encouraging trend of outshining their larger counterparts, with compute- and energy-intensive models compressed “by a factor of almost 10 every six to nine months,” he observes.

Such shrinkage makes SLMs faster and more efficient to run on compact hardware. “It’s going to be much more widespread because we can pack more into smaller packages,” Cox adds.

Daniels echoes the sentiment, noting that “from an enterprise standpoint, you want to be able to utilize these models for your own domain or data. And tuning these models is a lot simpler and more cost-effective. You can experiment a lot more quickly with these small models.”

Another direction Daniels sees AI models taking involves modularity, with companies “able to use a model but call on a specific feature or capability as part of their use case without having to load a new model.” This dynamic switching skill is made possible by an AI technology known as an activated .

According to Cox, an [activated LoRA](https://research.ibm.com/blog/inference-friendly-aloras-lora) allows a model to change its weights during inferencing. “We can lean its weights toward different tasks at runtime. It can become the best system when it needs to be, or it can become the best function-calling agent when it needs to be. And it doesn’t matter what its other skills are because it can lean that way,” he says. “There’s going to be a lot of flexibility. The model will orchestrate its own inference, and that’s going to be really exciting.”

Smaller, more dynamic model types could signify the AI industry hitting what Daniels calls a “scaling wall” in terms of model computing power. “We’ve got to change the thinking about what comes next,” he says.

This next step might just be an approach known as [generative computing](https://research.ibm.com/blog/generative-computing-mellea). The idea is to treat models as computing functions, much like the programs that make up any other software. Instead of and calls, [generative computing](https://www.ibm.com/think/news/how-generative-computing-reinvent-software) employs a runtime environment equipped with programming abstractions, such as structured requirements, safety guardrails and validation checks.

“We’re focusing on how to have a more programmatic or defined experience with the model so we can get more deterministic about what comes in and what comes out,” says Daniels. “And in terms of what comes out of the model, we can organize it so we have reproducible and accurate results that align with the actual task at hand.”

One way to think about it, Cox notes, is to treat a model’s memory as a new data type and the model itself as a sort of processor for that data. “It’s like a new representation, a new format, and then it just becomes natural to do things like loading programs to change the behavior of the system.”

Cox adds that generative computing has “a ton of potential for making these models more predictable and more trustworthy—all by using them in a different way and integrating them as software in a different way. We’re hoping that’s going to be a trend that picks up. We’re seeing pieces of it across the ecosystem, but bringing it all together focuses the effort in a different way.”

No matter what’s in store for the [future of AI](https://www.ibm.com/think/insights/artificial-intelligence-future) models, Daniels envisions that the success of any existing or emerging model hinges on the answers to these three questions: Is strong? Is it cost-effective to use? Does the model fit the business case?

“If you could answer those three questions and you’ve got a good model, then you’ve got a case to move forward,” says Daniels.

[How to choose the right foundation model](https://www.ibm.com/account/reg/signup?formid=urx-52620)

[Learn how to choose the right approach in preparing datasets and employing foundation models.](https://www.ibm.com/account/reg/signup?formid=urx-52620)

[IBM named a Strong Performer in the "Forrester Wave: AI Foundation Models for Language, Q2 2024"](https://www.ibm.com/account/reg/signup?formid=urx-52889)

[Businesses recognize that they cannot scale generative AI with foundation models that they cannot trust. Download the excerpt to learn why IBM, with flagship “Granite models”, is named a Strong Performer.](https://www.ibm.com/account/reg/signup?formid=urx-52889)

[The CEO's guide to model optimization](https://www.ibm.com/thought-leadership/institute-business-value/report/ceo-generative-ai/ceo-ai-model-optimization)

[Learn how to continually push teams to improve model performance and outpace the competition by using the latest AI techniques and infrastructure.](https://www.ibm.com/thought-leadership/institute-business-value/report/ceo-generative-ai/ceo-ai-model-optimization)

[IBM is named a Leader in Data Science & Machine Learning](https://www.ibm.com/account/reg/signup?formid=urx-53728)

[Learn why IBM has been recognized as a Leader in the 2025 Gartner® Magic Quadrant™ for Data Science and Machine Learning Platforms.](https://www.ibm.com/account/reg/signup?formid=urx-53728)

[watsonx Developer Hub](https://www.ibm.com/watsonx/developer/get-started/models)

[Support your next project with some of our most commonly used capabilities. Get started and learn more about the supported models that IBM provides.](https://www.ibm.com/watsonx/developer/get-started/models)

Related solutions

## Related solutions

IBM Granite

Achieve over 90% cost savings with Granite's smaller and open models, designed for developer efficiency. These enterprise-ready models deliver exceptional performance against safety benchmarks and across a wide range of enterprise tasks from cybersecurity to RAG.

[Explore Granite](https://www.ibm.com/granite) Artificial intelligence solutions

Put AI to work in your business with IBM's industry-leading AI expertise and portfolio of solutions at your side.

[Explore AI solutions](https://www.ibm.com/artificial-intelligence) AI consulting and services

Reinvent critical workflows and operations by adding AI to maximize experiences, real-time decision-making and business value.

[Explore AI services](https://www.ibm.com/consulting/artificial-intelligence)

Take the next step

Explore the IBM library of foundation models in the IBM watsonx portfolio to scale generative AI for your business with confidence.

[Discover watsonx.ai](https://www.ibm.com/products/watsonx-ai/foundation-models) [Explore IBM Granite AI models](https://www.ibm.com/granite)

The chat window has been closed