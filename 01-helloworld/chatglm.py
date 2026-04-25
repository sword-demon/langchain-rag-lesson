# -*- coding: utf-8 -*-
"""
@File    : openai.py
@Author  : wxvirus
@Time    : 2026/4/25 16:40
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
    base_url=os.environ.get("GLM_API_BASE")
)

response = llm.invoke("hello world")

print(response)
