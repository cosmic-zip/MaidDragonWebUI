import os

pwd = os.getcwd()

model_p = "{}/checkpoint/wizardLM-13B-Uncensored.ggmlv3.q4_0.bin".format(pwd)
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