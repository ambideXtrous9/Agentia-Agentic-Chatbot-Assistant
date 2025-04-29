from config.prompts import PROMPT

def general_search(question, qwen_pipe):
    prompt = PROMPT.format(question=question)
    output = qwen_pipe(prompt, add_special_tokens=True, do_sample=True)
    return output[0]["generated_text"]