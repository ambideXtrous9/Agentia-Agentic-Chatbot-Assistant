from config.prompts import CODE_PROMPT

def generate_code(question, qwen_pipe):

    code_prompt = CODE_PROMPT.format(question=question)
    outputs = qwen_pipe(code_prompt)
    return outputs[0]["generated_text"]