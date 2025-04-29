from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
import streamlit as st

@st.cache_resource(show_spinner="Loading Qwen model...")
def load_qwen_model(model_path):
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype="auto",
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    return model, tokenizer

@st.cache_resource(show_spinner="Creating Qwen pipeline...")
def create_pipeline(_model, _tokenizer):
    return pipeline(
        task="text-generation",
        model=_model,
        tokenizer=_tokenizer,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        max_new_tokens=1024,
        device_map="auto"
    )