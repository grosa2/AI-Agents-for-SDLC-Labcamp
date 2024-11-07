# Task 3 - Git Assistant

## What:
Setup an agent able to interact with local git repositories to extract bug-fixing commits from a provided input git repository.

## How:
- Setup an agent using OpenAI Assistants playground with tool calling enabled
- Define a function schema to execute commands using the git client, specifically:
    - A function to execute commands via git client
    - *Optional:* a Function to list files and folders in the agent working directory, to clone the repository if not present
- Implement the functions and integrate them with the provided agent template (`openai_assistant.ipynb`)
- **Extract all the bug fix commits from the provided git repository that closed a GitHub issue for the repository [`docker/genai-stack`](https://github.com/docker/genai-stack)** (hint: use git log!). An example is a commit message like "Fix typo in PDF bot (#90)".
The agent should return the commit hash, the issue number, and the commit message.
- *Optional:* Extract the fix commits with a message referencing the bug-inducing commit hash for the repository [`DarkCaster/Perpetual`](https://github.com/DarkCaster/Perpetual). 
An example is a commit message like "Fix bug introduced in commit 12a45b7."

**Hint:** To implement the git client function, you can use the `subprocess` module in Python to execute shell commands. For example, `subprocess.run("git " + <command arguments>...` executes the git command with the provided arguments. In this way you provide the agent with the git tool where it passess the arguments that will be added to the git command.

The notebook `openai_assistant_git_fast_start.ipynb` contains a fast start template to implement the git client agent.

There are other repositories where you test the git agent:
- [qbeslab/atlantic-signatures](https://github.com/qbeslab/atlantic-signatures)
- [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j)
- [i-am-bee/bee-agent-framework](https://github.com/i-am-bee/bee-agent-framework)


## Example session:
```
Question: Give the hash of the last commit for the github repository at https://github.com/grosa1/pyszz.git
 
(print this thougth)
First I need to look if the repository exists in my working directory, otherwise I have to clone it. Second, I have to extract the commit log using the git action.
 
(now request a function call) 
list_repositories(workdir)
 
(you receive the function output)
Oct 20 01:05 grosa1_pyszz
 
(you print this thougth)
I have the repository in ./workdir/grosa1_pyszz. Now I will extract the commit log.
 
(now request a function call) 
run_git_command: --git-dir=./workdir/grosa1_pyszz/.git log -1 --pretty=format:"%H"
 
(you receive the function output)
579e555005986be6a7249000510c07d3981485a3
 
(You then output)
The requested commit hash is 579e555005986be6a7249000510c07d3981485a3.
```
