from config.prompts import NEWS_SUMMARY_PROMPT

def news_search(question, search_tool, qwen_pipe):
    new_results = search_tool.run(question)
    new_text = "\n\n".join([f"title : {item['title']}\n\ncontext : {item['snippet']}" for item in new_results])
    
    full_prompt = NEWS_SUMMARY_PROMPT.format(context=new_text, question=question)
    answer = qwen_pipe(full_prompt)
    return answer[0]["generated_text"]