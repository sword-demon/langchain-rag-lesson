# -*- coding: utf-8 -*-
"""
@File    : 04-chat.py
@Author  : wxvirus
@Time    : 2026/5/7 23:29
@Desc    :
"""

import os

from dotenv import load_dotenv
# 聊天模型
from langchain_openai import ChatOpenAI

load_dotenv()
from langchain.messages import SystemMessage, HumanMessage

llm = ChatOpenAI(
    model="glm-5.1",
    temperature=0.6,
    api_key=os.environ.get("GLM_API_KEY"),
    base_url=os.environ.get("GLM_API_BASE"),
)

messages = [
    # 系统提示词
    SystemMessage(
        content="你是一个知识渊博的助手，擅长回答各种问题。请简洁的回答，字数控制在 20个字内"
    ),
    HumanMessage(content="请用一句话解释量子力学"),
]

response = llm.invoke(messages)
print(type(response))  # 类型是一个 AIMessage
# print(response)
