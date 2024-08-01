import os
from autogen import AssistantAgent, UserProxyAgent, ConversableAgent, GroupChat, GroupChatManager
import google.generativeai as genai
# from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
# from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

llm_config = {"model": "gemini-1.5-flash", "api_key":"AIzaSyAHNdDCfn5_lAqtw0QUdnmbhMFc6izHRJk", "api_type": "google"}

# llm_config = {
#     "config_list": [
#         {
#              "model": "TheBloke/Mistral-7B-Instruct-v0.2-GGUF/mistral-7b-instruct-v0.2.Q4_K_S.gguf","base_url": "http://localhost:1234/v1", "api_key":"lm-studio"
#         }

#     ], 
#     "cache_seed": None,  # Disable caching.
# }
   
# llm_config = {
#     "config_list": [
#         {
#              "model": "RichardErkhov/microsoft_-_phi-1_5-gguf/phi-1_5.Q2_K.gguf","base_url": "http://localhost:1234/v1", "api_key":"lm-studio"
#         }

#     ], 
#     "cache_seed": None,  # Disable caching.
# }

# llm_config = {
#     "config_list": [
#         {
#              "model": "Deci/DeciLM-7B-instruct-GGUF/decilm-7b-uniform-gqa-q8_0.gguf","base_url": "http://localhost:1234/v1", "api_key":"lm-studio"
#         }

#     ], 
#     "cache_seed": None,  # Disable caching.
# }

# llm_config = {
#     "config_list": [
#         {
#              "model": "bartowski/Starling-LM-7B-beta-GGUF/Starling-LM-7B-beta-IQ4_XS.gguf","base_url": "http://localhost:1234/v1", "api_key":"lm-studio"
#         }

#     ], 
#     "cache_seed": None,  # Disable caching.
# }

assistant = AssistantAgent("assistant", 
                           llm_config=llm_config, 
                           system_message='''
                            If you need any clarification, ask the user proxy. write a python script to perform log sanitisation. 
    Replace the private information, IP address with unique value and provide a mapping table as a seperate text file and the sanitised log file as seperate text files. The name of the file to be sanitized is called pfirewall.log '''
                           )


user_proxy = UserProxyAgent("user_proxy", code_execution_config={"last_n_messages": 2, "work_dir": "coding", "use_docker":False}, human_input_mode="ALWAYS", 
                            system_message="ask the user proxy for the name of the file to be sanitised, keep your response short and succient."
                           )

# Start the chat
user_proxy.initiate_chat(
    assistant,
    message="I want to perform log sanitisation on the file pfirewall.log, the private information is IP address. Replace all Ip addresses with a unique placeholder value and provide a mapping table to map the santised IP address to the unique value as a seperate file."
    #message="Create a firewall configuration blocking outgoing ping on another computer with IP address 192.168.1.1"
)