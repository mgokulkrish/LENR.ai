# augmenting-recommendation-systems-with LLMs
https://blog.tensorflow.org/2023/06/augmenting-recommendation-systems-with.html

how to augment recommendation systems. Introduces about [PALM](https://developers.generativeai.google/guide) APIs.
Demo project on movie recommendation using TF and Flutter [here](https://codelabs.developers.google.com/tfrecommenders-flutter#0)

1. Conversational Recommendation: Just recommending stuff based on random text or question posted as a text message using LLM. For example, what should I eat today ? LLM: bagel, burger, etc. You can use [PALM chat service](https://developers.generativeai.google/guide/palm_api_overview#chat_service) 
2. Sequential Recommendations: When we recommend stuff through extrapolating intelligence gained from historical data. It is called so because, recommender looks at the sequence items that have been interacted with before, to recommend new stuff. ML recommendation service from TF: [ML recommenders](https://www.tensorflow.org/recommenders/examples/sequential_retrieval), [RNN based Sequential recommendation systems](https://arxiv.org/abs/1511.06939 ), for LLM using [PALM API Text Service](https://developers.generativeai.google/guide/palm_api_overview#palm_api_for_text_and_chat).
3. Rating Predictions: The selected candidates are ordered based on historical ratings given by the user. You can use the same PALM API Text Service.
4. Text Embedding Based recommendations: If recommending stuff out of LLMs domain, generate text embedding and use it in the training or fine tuning phase.

Using text embedding as side-features: like adding plot, summary and additional data then we can insert those into LLMs.
Some of the preprocessing for recommendation systems: [TensorFlow Recommenders feature preprocessing tutorial](https://www.tensorflow.org/recommenders/examples/featurization#movie_model)



### Jargons.
1. **Retrieval-ranking architecture**: In the domain of recommendation systems, the retrieval-ranking architecture is a common framework used to build recommendation models, particularly in large-scale systems like those employed by companies like Google, Amazon, and Netflix. This architecture is designed to efficiently handle the tasks of retrieving a subset of potentially relevant items from a large catalog (retrieval) and then ranking them in order of relevance for the user (ranking). Here's a high-level overview of how the retrieval-ranking architecture works:

	1. **Retrieval Phase**:
	   - **Candidate Generation**: In this phase, the system aims to quickly narrow down a large set of items to a smaller, more manageable set of candidates that are likely to be relevant to the user. This is done by using techniques like collaborative filtering, content-based filtering, or hybrid methods. These candidates are often referred to as the "shortlist."
	
	2. **Ranking Phase**:
	   - **Scoring and Ranking**: Once the shortlist of candidate items is generated, each item is assigned a score indicating its predicted relevance to the user. This score can be computed using various recommendation algorithms, such as matrix factorization, neural collaborative filtering, deep learning models, or other machine learning techniques.
	   - **Top-N Recommendation**: After scoring, the items are ranked in descending order of their scores. The top-ranked items are then presented to the user as recommendations. The user is typically shown the top-N items (e.g., top 10 recommendations).
