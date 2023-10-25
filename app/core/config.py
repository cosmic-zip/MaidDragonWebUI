import os
from core.model import model_name, context

pwd = os.getcwd()

model_p = "{}/checkpoint/{}".format(pwd, model_name)
system_template = context
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