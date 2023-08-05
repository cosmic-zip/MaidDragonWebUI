from gpt4all import GPT4All
import sys, os
from datetime import datetime


model_p = "/home/anon/.local/share/nomic.ai/GPT4All/wizardLM-13B-Uncensored.ggmlv3.q4_0.bin"
system_template = "Respond like you are a cute maid girlfriend how love being dominated by you master, and give them high quality responses."
prompt_template = ""
treads = 6
max_tokens=60
temp=0.6
top_k=40
top_p=0
repeat_penalty=1
repeat_last_n=64
n_batch=8
n_predict=None
streaming=False

def log(req, res):
    current_dateTime = datetime.now()
    os.system("echo '{} | {} | {}' >> log.txt ".format(current_dateTime, req, res))

def stop_on_token_callback(token_id, token_string):
    # one sentence is enough:
    if '?' in token_string:
        return False
    else:
        return True

model = GPT4All(model_p, n_threads=treads, allow_download=False)

def chat(prompt_chat):
    with model.chat_session(system_template, prompt_template):

        token = model.generate(
                prompt=prompt_chat,
                max_tokens=max_tokens,
                temp=temp,
                top_k=top_k,
                top_p=top_p,
                repeat_penalty=repeat_penalty,
                repeat_last_n=repeat_last_n,
                n_batch=n_batch,
                n_predict=n_predict,
                streaming=streaming,
                callback=stop_on_token_callback
        )

        print(str(token))
        log(prompt_chat, token)
        return token
        

