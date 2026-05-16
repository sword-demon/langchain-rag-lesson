# -*- coding: utf-8 -*-
"""
@File    : 02-ChatPrompt.py
@Author  : wxvirus
@Time    : 2026/5/16 15:04
@Desc    : 提示词模版 - 会话模版
"""

from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate(
    [("system", "你是一个乐于助人的助手"), ("user", "给我们讲一个有关于{topic}的笑话")]
)

# PromptValue
prompt = prompt_template.invoke({"topic": "猫"})
print(prompt)
