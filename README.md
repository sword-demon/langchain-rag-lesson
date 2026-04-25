# langchain-rag-lesson

一个面向本地练习的 LangChain 入门仓库，当前包含最小可运行的多模型聊天示例，覆盖：

- `Tongyi / qwen-max`
- `GLM / glm-5.1`

## 仓库结构

```text
langchain-rag-lesson/
├── 01-helloworld/
│   ├── chatglm.py
│   ├── common.py
│   └── qwen.py
├── main.py
├── pyproject.toml
└── .env.example
```

## 环境准备

1. 安装 `uv`
2. 在仓库根目录执行依赖安装

```bash
uv sync
```

3. 复制环境变量模板并填写真实密钥

```bash
cp ".env.example" ".env"
```

## 环境变量

| 变量名 | 用途 | 对应脚本 |
| --- | --- | --- |
| `GLM_API_KEY` | 智谱 GLM API Key | `01-helloworld/chatglm.py`、`01-helloworld/common.py` |
| `GLM_API_BASE` | 智谱 OpenAI 兼容接口地址 | `01-helloworld/chatglm.py`、`01-helloworld/common.py` |
| `TONGYI_API_KEY` | 阿里通义 API Key | `01-helloworld/qwen.py` |

## 运行方式

```bash
uv run python "01-helloworld/qwen.py"
uv run python "01-helloworld/chatglm.py"
uv run python "01-helloworld/common.py"
```

## 当前状态

当前仓库还是 lesson/playground 形态，重点在于：

- 验证 LangChain 对不同模型提供商的最小接入方式
- 为后续 RAG 示例保留统一的依赖入口

尚未包含：

- 向量库接入
- 文档切分与 embedding 流程
- 检索链与问答链编排
- 系统化测试
