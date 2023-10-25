# Maid Dragon GPT4ALL UI

MaidDragon is an exciting development in the world of artificial 
intelligence, serving as a frontend for GPT-4AL, an advanced AI 
language model. This combination of technology brings together 
the cutting-edge capabilities of GPT-4AL with a user-friendly 
interface.

**Install**


```bash
git clone https://github.com/th3Maid/MaidDragonWebUI.git
```

**Model Placement**: Place your model files inside the /app/checkpoint directory. This is the designated location for your model within the application.

**File Editing**: Go to the /app/core/model.py, Within this file, find the specific file where you need to insert your model's name.

To use the llama model:

    Ex: model_name = "llama-2-7b-chat.ggmlv3.q4_0.bin"

Please ensure that you use the exact same model name both inside the /app/checkpoint directory and when configuring your model. 

**Running**

```bash
chmod +x server.sh
```