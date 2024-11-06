# 💻 LABCAMP - Build your first AI Agent

Welcome! 🚀

In this labcamp, you will learn the basic concepts of AI agents and how to build your first AI agent using OpenAI API and assistants playground.
This repository contains the source code for the three labs that we will be working on during the labcamp. Each lab is located in a separate folder (i.e., `task1`, `task2`, and `task3`) including a `README.md` file with the instructions and the resources required for each lab.

## Pre-requisites
Before we start, make sure you have the following prerequisites installed on your machine:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Python](https://www.python.org/downloads/)
- [OpenAI account](https://openai.com/index/openai-api/) with an API key (given during the labcamp)
- [Git - command line client](https://git-scm.com/downloads)

**N.B.**: The API key should be stored in a file named `.env` in the root directory of the project. See the `.env.example` file for an example of how to store the API key.

### Setup the environment:
1. Create a new python virtual environment in the project directory.

For Linux/Mac users:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
For Windows users:
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Install the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extensions for VSCode

4. Open the this folder in VSCode and run the first cell of the notebook `task_3/openai_assistant.ipynb` to test the setup. Remember to activate the virtual environment in the notebook (`.venv`)


If you need help or have any questions, feel free to reach out to us. We are here to help you! 🤗

Good luck and have fun! 🎉


## 🔗 Some useful links

- [More on LLM agents](https://www.promptingguide.ai/it/research/llm-agents)
- [More on agents reasoning](https://www.promptingguide.ai/it/techniques/react)
- [More on OpenAI assistants APIs](https://platform.openai.com/docs/assistants/overview)
- [Production-ready agents framework](https://www.langchain.com/langgraph)
