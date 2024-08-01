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
-  Python 3.12.4
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

### Setting up LM studio 

### Settign up Google key 