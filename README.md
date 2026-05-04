# LLM Agent Toolkit

Reusable infrastructure for building LLM-based coding agents. Extracted from [Midas Agent](https://github.com/zysilm/midas-agent) to share common components across different agent architectures.

## What's included

| Module | Description |
|---|---|
| `llm/` | LLM abstraction layer — request/response types, provider ABC, LiteLLM implementation (100+ providers) |
| `runtime/` | IO backend abstraction — unified file I/O and bash execution for local and Docker modes |
| `docker/` | Docker container lifecycle management for SWE-bench evaluation environments |
| `context/` | Context window management — output truncation (middle-elision) and conversation compaction |
| `stdlib/` | Agent building blocks — Action ABC, ActionRegistry, ReAct agent loop, Plan-Execute agent, standard tool actions (bash, str_replace_editor, task_done) |
| `evaluation/` | Patch scoring — ExecutionScorer ABC and SWE-bench scorer (delegates to official `run_instance`) |
| `types` | Shared types — `Issue`, `BudgetExhaustedError`, `ActionEvent` |

## Installation

```bash
# From git
pip install git+https://github.com/zysilm/llm-agent-toolkit.git

# With SWE-bench evaluation support
pip install "llm-agent-toolkit[swebench] @ git+https://github.com/zysilm/llm-agent-toolkit.git"
```

Or add to your `pyproject.toml`:

```toml
[tool.poetry.dependencies]
llm-agent-toolkit = {git = "https://github.com/zysilm/llm-agent-toolkit.git"}
```

## Quick start

### LLM provider

```python
from llm_agent_toolkit.llm.litellm_provider import LiteLLMProvider
from llm_agent_toolkit.llm.types import LLMRequest

provider = LiteLLMProvider(model="openai/gpt-4o", api_key="sk-...")
response = provider.complete(LLMRequest(
    messages=[{"role": "user", "content": "Hello"}],
    model="default",
))
```

### ReAct agent

```python
from llm_agent_toolkit.stdlib.react_agent import ReactAgent
from llm_agent_toolkit.stdlib.actions.bash import BashAction
from llm_agent_toolkit.stdlib.actions.str_replace_editor import StrReplaceEditorAction

agent = ReactAgent(
    system_prompt="You are a coding assistant.",
    actions=[BashAction(), StrReplaceEditorAction()],
    call_llm=provider.complete,
)
result = agent.run(context="Fix the bug in main.py")
```

### Docker execution

```python
from llm_agent_toolkit.docker.container_manager import ContainerManager
from llm_agent_toolkit.runtime.io_backend import DockerIO

cm = ContainerManager()
cid = cm.start(image="python:3.11-slim")
io = DockerIO(container_id=cid)

output = io.run_bash("python --version")
cm.stop()
```

## Design philosophy

This toolkit provides **infrastructure, not strategy**. It gives you the building blocks (LLM calls, tool execution, Docker containers, context management) but does not prescribe how to decompose tasks, learn from failures, or manage budgets. Those decisions belong to the agent implementation built on top of this toolkit.
