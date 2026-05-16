# -*- coding: utf-8 -*-
"""
@File    : 03-ChatPrompt.py
@Author  : wxvirus
@Time    : 2026/5/16 15:10
@Desc    : 提示词模版 - 对话提示词模版支持多个变量
"""

from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(
            "你是{product}的客服助手，你的名字叫{name}，请简洁的用20个字回答问题。"
        ),
        HumanMessagePromptTemplate.from_template("hello，你好，我得名字叫{human_name}"),
        AIMessagePromptTemplate.from_template("你好，有什么需要咨询的?"),
        HumanMessagePromptTemplate.from_template("{query}"),
    ]
)

# 常用的方式
prompt = prompt_template.invoke(
    {
        "product": "langchain",
        "name": "无解",
        "human_name": "法外狂徒",
        "query": "langchain是什么，用来做什么的?",
    }
)

# prompt1 = prompt_template.from_messages(
#     product="langchain",
#     name="无解",
#     human_name="李四",
#     query="langchain 是用来做什么的",
# )

print(prompt)
print("-" * 50)

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(
    model="glm-5.1",
    temperature=0.6,
    api_key=os.environ.get("GLM_API_KEY"),
    base_url=os.environ.get("GLM_API_BASE"),
)

response = model.invoke(prompt)
print(response.content)  # LangChain是开发大模型应用的框架。
