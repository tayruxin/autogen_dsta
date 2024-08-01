# Log Sanitization with autogen and rag

## Features

There are 3 different infrastrucutures in the codebase.

1. `rag.py`:

- Description:
  This module features four different AI agents that communicate with each other using Retrieval-Augmented Generation (RAG). Additionally, it includes a checker agent that verifies the sanitized log file after processing.
- Components:
  - Multiple AI agents using RAG for communication and task execution.
  - Checker agent for post-sanitization verification.

2. `log_sanitization.py`:

- Description:
  This module involves two AI agents: an assistant agent that generates the sanitization code and a user proxy agent that gathers human input.
- Components:
  - Assistant agent for code generation
  - User proxy agent for collecting and incorporating human input

3. `custommodelclient.py`:

- Description:
  Similar to log_sanitization.py, this module also features an assistant and a user proxy agent. However, it is designed to load a local LLM (Large Language Model) onto your machine.
- Components:
  - Assistant agent for code generation.
  - User proxy agent for human input.
  - Local LLM model loaded onto the machine.

## Environment

- Python 3.12.4
- IDE: VSCode
- LM studio: To host the local model

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tayruxin/autogen_dsta.git
   ```
2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Setting up LM studio

1. Download LM studio on your machine from [here](https://github.com/tayruxin/autogen_dsta.git)
2. Download the local model that you wish to try from LM studio
3. Update the model name according to the model that you downloaded from LM studio

```
z llm_config = {
#     "config_list": [
#         {
#              "model": "TheBloke/Mistral-7B-Instruct-v0.2-GGUF/mistral-7b-instruct-v0.2.Q4_K_S.gguf","base_url": "http://localhost:1234/v1", "api_key":"lm-studio"
#         }

#     ],
#     "cache_seed": None,  # Disable caching.
# }
```

### 2. Using Google/OpenAI key

1. Obtain your API key
2. Insert the API key into the API key field

```
llm_config = {"model": "gemini-1.5-flash", "api_key":"YOUR_API_KEY", "google"}
```
