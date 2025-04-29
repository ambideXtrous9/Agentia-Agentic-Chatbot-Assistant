from langchain.prompts import PromptTemplate

PROMPT_TEMPLATE = """
answer the question in less than 30 words and do not hallucinate.

Question : {question}

**Answer:** 
"""
PROMPT = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["question"])

NEWS_SUMMARY_PROMPT = """
You are a helpful news assistant. Based on the provided context, write a clear, fact-based, and concise news summary of approximately 400 words.

Instructions:
- Use only the information from the context. Do not include external knowledge or assumptions.
- Maintain a neutral and objective tone.
- Focus on the key facts, events, entities, and timelines.
- Avoid repetition, speculation, or unsupported claims.
- If the context does not contain enough information, state that clearly instead of fabricating details.
- Ensure the summary is coherent, logically structured, and suitable for a general audience.

Context:
{context}

Question: {question}

**Answer:**
"""

CODE_PROMPT = """
You are a helpful coding assistant. 
Write a clear, fact-based, and concise code summary with explanation for the given Question.

Question: {question}

**Answer:**
""" 