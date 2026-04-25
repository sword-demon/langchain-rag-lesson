# -*- coding: utf-8 -*-
"""
@File    : qwen.py
@Author  : wxvirus
@Time    : 2026/4/25 16:59
@Desc    : 
"""
import os

from langchain_community.chat_models.tongyi import ChatTongyi
from dotenv import load_dotenv

load_dotenv()

llm = ChatTongyi(
    model="qwen-max",
    api_key=os.environ.get("TONGYI_API_KEY")
)

response = llm.invoke("你是谁?")
print(response)
