# Alpaca Data format.

The format to pass data for finetuning is called the ‘Alpaca format’. In large language model research circles as it was the format used to finetune the original LlaMA model from Meta to result in the Alpaca model, one of the first widely distributed instruction-following large language models (although not licensed for commercial use).

The following code snippet loads the dataset from the Hugging Face hub into memory, transforms the necessary fields into a consistently formatted string representing the prompt, and inserts the response( i.e. the description), immediately afterwards. 

```
import pandas as pd
from datasets import load_dataset
from datasets import Dataset

#Load the dataset from the HuggingFace Hub
rd_ds = load_dataset("xiyuez/red-dot-design-award-product-description")

#Convert to pandas dataframe for convenient processing
rd_df = pd.DataFrame(rd_ds['train'])

#Combine the two attributes into an instruction string
rd_df['instruction'] = 'Create a detailed description for the following product: '+ rd_df['product']+', belonging to category: '+ rd_df['category']

rd_df = rd_df[['instruction', 'description']]

#Get a 5000 sample subset for fine-tuning purposes
rd_df_sample = rd_df.sample(n=5000, random_state=42)

#Define template and format data into the template for supervised fine-tuning
template = """Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:

{}

### Response:\n"""

rd_df_sample['prompt'] = rd_df_sample["instruction"].apply(lambda x: template.format(x))
rd_df_sample.rename(columns={'description': 'response'}, inplace=True)
rd_df_sample['response'] = rd_df_sample['response'] + "\n### End"
rd_df_sample = rd_df_sample[['prompt', 'response']]

rd_df['text'] = rd_df["prompt"] + rd_df["response"]
rd_df.drop(columns=['prompt', 'response'], inplace=True)
```

The of data for supervised fine-tuning

Below is an instruction that describes a task. Write a response that appropriately completes the request.

```
### Instruction:

Create a detailed description for the following product: Beseye Pro, belonging to category: Cloud-Based Home Security Camera

### Response:

Beseye Pro combines intelligent home monitoring with decorative art. The camera, whose form is reminiscent of a water drop, is secured in the mounting with a neodymium magnet and can be rotated by 360 degrees. This allows it to be easily positioned in the desired direction. The camera also houses modern technologies, such as infrared LEDs, cloud-based intelligent video analyses and SSL encryption.

### End
```


Three steps for creating data that resembles alpaca format for finetuning.

1. Created automated script for generating data for general simple prompts.

2. Create handcrafted sophisticated prompts, for tricky questions and do more literature review on automation of this procedure.

3. Try to generate multiple prompts for same answer.