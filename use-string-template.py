import google.generativeai as palm
from google.api_core import retry

palm_api_key = ('')

palm.configure(api_key=palm_api_key)

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model_bison = models[0]
print(model_bison)


@retry.Retry()
def generate_text(prompt,
                  model=model_bison,
                  temperature=0.0):
    return palm.generate_text(prompt=prompt,
                              model=model,
                              temperature=temperature)

prompt_template = """
{priming}

{question}

{decorator}

Your solution:
"""

priming_text = "You are an expert at writing clear, concise, Python code."
question = "create a doubly linked list"

# option 1
# decorator = "Work through it step by step, and show your work. One step per line."
# option 2
decorator = "Insert comments for each line of code."

prompt = prompt_template.format(priming=priming_text,
                                question=question,
                                decorator=decorator)

print(prompt)
completion = generate_text(prompt)
print(completion.result)

question = """create a very large list of random numbers in python, 
and then write code to sort that list"""

prompt = prompt_template.format(priming=priming_text,
                                question=question,
                                decorator=decorator)

print(prompt)

completion = generate_text(prompt)
print(completion.result)