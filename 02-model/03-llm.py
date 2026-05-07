# -*- coding: utf-8 -*-
"""
@File    : 03-llm.py
@Author  : wxvirus
@Time    : 2026/5/7 23:25
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

prompt = "请用一句话解释量子力学。"

response = llm.invoke(prompt)
print(response)
