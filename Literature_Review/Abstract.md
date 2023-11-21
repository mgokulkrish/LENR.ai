## Problem Statement
Analysis and Feasibility of Large Language Models to serve as a conversational agent and as a Recommendation system in a specialized domain (Low Energy Nuclear Reactions).

## Literature Review:
- Llama2 Research Paper (LLM): [paper](https://ai.meta.com/research/publications/llama-2-open-foundation-and-fine-tuned-chat-models/)
- LoRA Research Paper (LLM Fine Tuning): [paper](https://arxiv.org/abs/2106.09685)
- A Survey on LLM for Recommendation (LLM as Rec Sys): [paper](https://arxiv.org/abs/2305.19860)
- Low Energy Nuclear Reaction Source Book (LENR study): [link](https://pubs.acs.org/doi/pdf/10.1021/bk-2008-0998.ch001)
- What is LENR Research? FAQ (New Energy Times): [link](https://newenergytimes.com/v2/reports/LENR-FAQ.shtml)
- QLoRA (LLM Fine Tuning for Quantized LLMs): [paper](https://arxiv.org/abs/2305.14314)
- Measuring MMLU (Benchmark for testing LLMs): [paper](https://arxiv.org/abs/2009.03300)
- TruthfulQA Benchmark: [paper](https://arxiv.org/abs/2109.07958)
- Research Paper collection for LLM as RecSys: [link](https://github.com/nancheng58/Awesome-LLM4RS-Papers)
- LDA and Topic Modelling: [paper](https://arxiv.org/abs/1711.04305)
- StableLLM (LLM for stability.ai): [link](https://github.com/Stability-AI/StableLM)
- Llama inference code: [link](https://github.com/facebookresearch/llama)
- Karpathy’s Llama2.c: [link](https://github.com/karpathy/llama2.c)
- Transformer Network -Attention Model: [paper](https://arxiv.org/abs/1706.03762) 
- Document-level Machine Translation with LLMs: [paper](https://arxiv.org/abs/2304.02210)  
- Reinforcement Self-Training For Language Modelling: [paper](https://arxiv.org/abs/2308.08998)
- Findings on Multilingual Machine Translation with Large Language Models: [paper](https://arxiv.org/abs/2304.04675) 
- Exploring Human-like Translation strategies using LLMs: [paper](https://arxiv.org/abs/2305.04118) 

### 1. Data Preparation for fine_tuning.
- Efficient Fine-Tuning with LoRA: A Guide to Optimal Parameter Selection for Large Language Models [article](https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms)
- Details on Alpaca fine_tuning [article](https://github.com/tatsu-lab/stanford_alpaca)
- How to train your own ChatGPT Alpaca style, part one [article](https://fastml.com/how-to-train-your-own-chatgpt-alpaca-style-part-one/)


## Execution Plan:
1. Topic Modelling, Research Survey to increase the domain size.
2. Dataset Expansion.
3. Data Preparation.
4. LLM Fine Tuning.
    1. LLama2 7B model.
    2. LLM from Mistral AI 7B model.
    3. StableLLM 3B model.

5. Developing Benchmarks to evaluate the accuracy/performance of LENR.
6. Do General Benchmarking (MMLU, TruthfulQA).
7. Observation and result on LLM as RecSys and usefulness as chatbot.


