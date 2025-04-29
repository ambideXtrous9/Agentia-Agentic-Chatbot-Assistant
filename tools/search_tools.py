from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
import streamlit as st

@st.cache_resource(show_spinner="Setting up search tool...")
def setup_search_tool():
    wrapper = DuckDuckGoSearchAPIWrapper(max_results=10)
    return DuckDuckGoSearchResults(api_wrapper=wrapper, source="news", output_format="list")