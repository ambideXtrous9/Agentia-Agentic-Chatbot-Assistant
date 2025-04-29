#!/bin/bash
mkdir -p qwen_agent/{config,models,tools,nodes}
touch qwen_agent/config/prompts.py \
      qwen_agent/models/__init__.py \
      qwen_agent/models/qwen_model.py \
      qwen_agent/tools/__init__.py \
      qwen_agent/tools/search_tools.py \
      qwen_agent/tools/memory.py \
      qwen_agent/nodes/__init__.py \
      qwen_agent/nodes/classifier.py \
      qwen_agent/nodes/greeting.py \
      qwen_agent/nodes/coder.py \
      qwen_agent/nodes/search.py \
      qwen_agent/nodes/news_search.py \
      qwen_agent/workflow.py \
      qwen_agent/app.py
