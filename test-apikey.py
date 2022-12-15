import os
import openai
import wandb


openai.api_key = "eBG00lPrVLPgiv/NVehnHYe49c9cHqDY+DNZJRAte3Rk2QaI2BxjCuYmmwRTtUwD"
run = wandb.init(project='GPT-3 in Python')
prediction_table = wandb.Table(columns=["prompt", "completion"])

run = wandb.init(project='GPT-3 in Python')
prediction_table = wandb.Table(columns=["prompt", "completion"])
gpt_prompt = "Correct this to standard English:\n\nShe no went to the market."


response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=gpt_prompt,
  temperature=0.5,
  max_tokens=256,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)


print(response['choices'][0]['text'])


prediction_table.add_data(gpt_prompt,response['choices'][0]['text'])
