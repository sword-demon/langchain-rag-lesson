# -*- coding: utf-8 -*-
"""
@File    : common.py
@Author  : wxvirus
@Time    : 2026/4/25 17:10
@Desc    :
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="glm-5.1",
    temperature=0.6,
    base_url=os.environ.get("GLM_API_BASE"),
    api_key=os.environ.get("GLM_API_KEY"),
)

response = llm.invoke("你是谁")
print(response)
