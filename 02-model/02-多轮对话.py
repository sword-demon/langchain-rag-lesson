# -*- coding: utf-8 -*-
"""
@File    : 02-多轮对话.py
@Author  : wxvirus
@Time    : 2026/4/25 21:57
@Desc    :
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="glm-5.1",
    temperature=0.6,
    api_key=os.environ.get("GLM_API_KEY"),
    base_url=os.environ.get("GLM_API_BASE"),
)

messages = [
    SystemMessage(
        content="你是知识渊博的专家，知道很多著名的书籍相关的知识，请简洁的用20个字回答问题"
    ),
    HumanMessage(content="我的身份是学员，名字叫小王"),
    AIMessage(content="欢迎，有什么需要咨询的？"),
    HumanMessage(content="三国志介绍的是什么故事？"),
    AIMessage(content="《三国志》介绍三国时期魏蜀吴三国的历史与人物。"),
    HumanMessage(content="红楼梦呢?"),
]

response = llm.invoke(messages)
print(response.content)
