from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional
from nodes.classifier import classify_input
from nodes.greeting import handle_greeting
from nodes.coder import generate_code
from nodes.search import general_search
from nodes.news_search import news_search
import streamlit as st

class GraphState(TypedDict):
    question: Optional[str] = None
    classification: Optional[str] = None
    response: Optional[str] = None

@st.cache_resource(show_spinner="Creating workflow...")
def create_workflow(_qwen_pipe, _qwen_tokenizer, _search_tool):
    # Node functions
    def classify_input_node(state):
        return {"classification": classify_input(state.get('question', ''))}
    
    def handle_greeting_node(state):
        return {"response": handle_greeting()}
    
    def coder_node(state):
        answer = generate_code(state.get('question', ''), _qwen_pipe)
        return {"response": answer}
    
    def handle_search_node(state):
        answer = general_search(state.get('question', ''), _qwen_pipe)
        return {"response": answer}
    
    def duckduckgo_memory_node(state):
        answer = news_search(state.get('question', ''), _search_tool, _qwen_pipe)
        return {"response": answer}
    
    def decide_next_node(state):
        c = state.get('classification')
        if c == "greeting": return "handle_greeting"
        elif c == "code": return "qwen_coder"
        elif c == "duck_search": return "duckduckgo_memory_node"
        else: return "handle_search"
    
    # Build graph
    workflow = StateGraph(GraphState)
    workflow.add_node("classify_input", classify_input_node)
    workflow.add_node("handle_greeting", handle_greeting_node)
    workflow.add_node("handle_search", handle_search_node)
    workflow.add_node("qwen_coder", coder_node)
    workflow.add_node("duckduckgo_memory_node", duckduckgo_memory_node)
    
    workflow.add_conditional_edges("classify_input", decide_next_node, {
        "handle_greeting": "handle_greeting",
        "handle_search": "handle_search",
        "qwen_coder": "qwen_coder",
        "duckduckgo_memory_node": "duckduckgo_memory_node",
    })
    
    workflow.set_entry_point("classify_input")
    workflow.add_edge("handle_greeting", END)
    workflow.add_edge("handle_search", END)
    workflow.add_edge("qwen_coder", END)
    workflow.add_edge("duckduckgo_memory_node", END)
    
    return workflow.compile()