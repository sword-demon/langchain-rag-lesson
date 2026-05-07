# -*- coding: utf-8 -*-
"""
@File    : 01-StringPrompt.py
@Author  : wxvirus
@Time    : 2026/5/7 23:36
@Desc    : 提示词模版
"""

import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="glm-5.1",
    temperature=0.6,
    api_key=os.environ.get("GLM_API_KEY"),
    base_url=os.environ.get("GLM_API_BASE"),
)

prompt_template = PromptTemplate.from_template("给我们讲一个关于{topic}的笑话")

prompt = prompt_template.invoke({"topic": "猫"})

response = llm.invoke(prompt)

print(response.content)
