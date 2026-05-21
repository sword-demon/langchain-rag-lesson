# -*- coding: utf-8 -*-
"""
@File    : 04-MessageHolder.py
@Author  : wxvirus
@Time    : 2026/5/16 15:23
@Desc    : 消息占位符
"""

"""
效果:

System: 你是一个,乐于助人的助手，在回答用户的问题时，需要带上用户的名字
Human: 我是张三
AI: 你好，有什么需要咨询的?
Human: 三国志作者是谁?
张三，您好！《三国志》的作者是西晋时期的史学家陈寿。
"""

import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

prompt_template = ChatPromptTemplate(
    [
        ("system", "你是一个,乐于助人的助手，在回答用户的问题时，需要带上用户的名字"),
        ("user", "我是{name}"),
        MessagesPlaceholder("msgs"),
    ]
)

s = prompt_template.invoke(
    {
        "msgs": [
            AIMessage(content="你好，有什么需要咨询的?"),
            HumanMessage(content="三国志作者是谁?"),
        ],
        "name": "张三",
    }
)

print(s.to_string())

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="glm-5.1",
    temperature=0.6,
    api_key=os.environ.get("GLM_API_KEY"),
    base_url=os.environ.get("GLM_API_BASE"),
)

response = model.invoke(s)
print(response.content)
