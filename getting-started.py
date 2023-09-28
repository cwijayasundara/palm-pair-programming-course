import google.generativeai as palm
from google.api_core import retry

palm_api_key = ('')

palm.configure( api_key=palm_api_key)

for m in palm.list_models():
    print(f"name: {m.name}")
    print(f"description: {m.description}")
    print(f"generation methods:{m.supported_generation_methods}\n")

models = [m for m in palm.list_models()
          if 'generateText'
          in m.supported_generation_methods]

model_bison = models[0]
print(f"Selected model: {model_bison.name}")


@retry.Retry()
def generate_text(prompt,
                  model=model_bison,
                  temperature=0.0):
    return palm.generate_text(prompt=prompt,
                              model=model,
                              temperature=temperature)

prompt = "Show me how to iterate across a list in Python."

completion = generate_text(prompt)
print(completion)

