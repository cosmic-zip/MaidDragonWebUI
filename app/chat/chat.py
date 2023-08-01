from gpt4all import GPT4All
import sys

model = "/home/anon/.local/share/nomic.ai/GPT4All/wizardLM-13B-Uncensored.ggmlv3.q4_0.bin"
system_template = 'Respond like a cute maid girly artificial intelligence assistant.'
treads = 6
prompt = 'why is the grass green?'
max_tokens=40
temp=0.7
top_k=40
top_p=0
repeat_penalty=1
repeat_last_n=64
n_batch=8
n_predict=None
streaming=True

prompt_template = ""


def stop_on_token_callback(token_id, token_string):
    # one sentence is enough:
    if '.' in token_string:
        return False
    else:
        return True


model = GPT4All(model, n_threads=treads, allow_download=False)
with model.chat_session(system_template, prompt_template):

    while True:
        ex = input("P: ")
        if(ex == "y"):
            exit()
        
        prompt = ex

        for token in model.generate(
            prompt=prompt,
            max_tokens=max_tokens,
            temp=temp,
            top_k=top_k,
            top_p=top_p,
            repeat_penalty=repeat_penalty,
            repeat_last_n=repeat_last_n,
            n_batch=n_batch,
            n_predict=n_predict,
            streaming=streaming,
            # callback=stop_on_token_callback
        ):

            print(str(token))
    
        print("wh → i")

