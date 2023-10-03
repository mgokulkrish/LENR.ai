# What is a Transformer Model? (Nvidia Blog)

For the actual blog post - [click here](https://blogs.nvidia.com/blog/2022/03/25/what-is-a-transformer-model).

## Definition

The Transformer Model is the building block for all things LLM (Large Language Model). Transformers are revolutionizing advancements in AI/ML. Since Transformers are creating a paradigm shift in AI they are also being referred to as **'Foundational Models'**.

Transformers are a type of neural network that learns context and meaning by tracking relationships in sequential data like words in a sentence.

Transformers are translating text and speech in near real-time, opening meetings and classrooms to diverse and hearing-impaired attendees.
They’re helping researchers understand the chains of genes in DNA and amino acids in proteins in ways that can speed drug design.

## Details

Transformers are replacing RNN and CNN - the most popular neural networks 5 years ago.

In RNN and CNN, users had to train neural networks with large, labeled datasets. Labeling such datasets was expensive and time consuming to generate.
Since transformers find patterns between elements mathematically, there is no need for labels. Pattern generation also takes place in parallel which allows the models to ingest large quantities of data.

Transformers use positional encoders to tag data elements coming in and out of the network. The models consists of Attention Units that follow these tags creating an algebraic map of how each element relates of each other. These pattern matching strategies allow AI to visualize the same patterns seen by Humans.

## Salient Features and Conclusion

1. RNN and CNN generate a series of hidden states - H(t) which is a function of previous hidden states - H(t-1). This prevents parallel computing.
2. RNN and CNN also require labelled data sets (Supervised learning).

Transformer Models solves both these problem statements - [paper](https://arxiv.org/pdf/1706.03762.pdf)
