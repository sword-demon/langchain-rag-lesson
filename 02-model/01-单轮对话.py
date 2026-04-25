# -*- coding: utf-8 -*-
"""
@File    : 01-单轮对话.py
@Author  : wxvirus
@Time    : 2026/4/25 21:56
@Desc    :
"""

import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="glm-5.1",
    temperature=0.6,
    api_key=os.environ.get("GLM_API_KEY"),
    base_url=os.environ.get("GLM_API_BASE"),
)

response = llm.invoke("三国志的作者是谁?")
print(response.content)
