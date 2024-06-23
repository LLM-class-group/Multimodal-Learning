# Multimodal-Learning

In this work, we explores the relationship between the performance of the multimodal model LLaVA on the
Science QA dataset and the quality of alignment data, and provides some conjectures on how fine-tuning
affects model performance.

### Usage



#### Data 

- All our training data are in `ScienceQA/data/scienceqa/`

#### Fine-Tuning

- Run `LLaVA/scripts/finetune_sqa.sh`.

#### Evaluation 

- Run `LLaVA/scripts/sqa_eval_batch.sh` to generate responses parallelly.

- Run `LLaVA/scripts/sqa_eval_gather.sh` to evalue the responses and gather evaluation results.


### Project Structure

- `LLaVA/`: The LLaVA directory
  - `eval_results/` contain detailed evaluation results
    - `full/` contains the results after finetuning the model with all 12726 questions.
    - `mini/` contains the results after finetuning the model with 1000 randomly selected questions.
- `ReAlign/`: The Reformatted Alignment directory
- `ScienceQA/`: The ScienceQA dataset directory
  - `data/scienceqa/` contains all our training datasets
    - `llava_train_QCM-LEA.json` is the full-origin dataset in our paper
    - `llava_train_short.json` is the full-short dataset in our paper
    - `llava_train_realigned_v4.json` is the full-realign-preliminary dataset in our paper
    - `llava_minitrain_QCM-LEA.json` is the mini-origin dataset in our paper
    - `llava_minitrain_short.json` is the mini-short dataset in our paper
    - `llava_minitrain_realigned_2` is the mini-realign dataset in our paper


### Evaluation Results



| Dataset        | Accuracy | Question Count | 
| ------------- | ------------- | ------------------ | 
| full-origin       | 0.9115        | 12726    |
| full-short        | 0.9057        | 12726    |
| full-realign-preliminary      | 0.8783       | 12726   |
| mini-origin       | 0.7475        | 1000    |
| mini-short        | 0.6991       | 1000    |
| mini-realign      | 0.7548        | 1000    |

### Acknowledgement

* We extend our sincere thanks to Ethan Chern and Pengfei Liu for valuable discussions on our work. 
* We are deeply appreciative of the computing resources provided by GAIR.