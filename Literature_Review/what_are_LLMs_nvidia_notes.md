# What are LLMs ? (Nvidia blog)
[Link here](https://www.nvidia.com/en-us/glossary/data-science/large-language-models/) 
It is class of deep learning architectures called transformer networks.

Why transformer architecture is suited for LLMs.
1. positional encodings: Positional encoding embeds the order of which the input occurs within a given sequence. Essentially, instead of feeding words within a sentence sequentially into the neural network, thanks to positional encoding, the words can be fed in non-sequentially.
2. self attention: Self-attention assigns a weight to each part of the input data while processing it. This weight signifies the importance of that input in context to the rest of the input.


Main use-cases:
1. Generation (story writing).
2. Summarization.
3. Translation.
4. Classification.
5. Chatbot.

How do they work?
LLM are usually trained through unsupervised learning. With unsupervised learning, models can find previously unknown patterns  in data using unsupervised learning. Removes the need for data labelling.

Foundation models : the modes that serves multiple use-cases, does require task specific training to solve a particular task.

The ability for the foundation model to generate text for a wide variety of purposes without much instruction or training is called zero-shot learning.

To make the model behave in certain way, to customize to achieve higher accuracy, there are several ways. Few of them:
1. prompt tuning.
2. fine tuning.
3. adapters.

Open source Models:
1. Lamma2
2. Claude2
3. Vicuna
4. Mistral AI (recently).
