from vllm import LLM, SamplingParams
from constant import PROMPT_INPUT_FOR_TASK_CLS
import torch
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "1,2"

num_gpus = 2
model_name_or_dir = "GAIR/ReAlign-Task-Classifier" # or the local directory to store the downloaded model
llm = LLM(model=model_name_or_dir, tensor_parallel_size=num_gpus)

def get_category(query):
    input = PROMPT_INPUT_FOR_TASK_CLS.format(input=query)
    sampling_params = SamplingParams(temperature=0.0, top_p=1.0, max_tokens=50)
    outputs = llm.generate(input, sampling_params)
    task = outputs[0].outputs[0].text
    return task


# should be `advice_giving`.
# If the classified result is not in task list, set it as `default`.

