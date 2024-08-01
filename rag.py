import autogen
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from autogen import Agent 

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

assistant = RetrieveAssistantAgent(
    name="assistant",
    system_message='''
    If you need any clarification, ask the user proxy. write a python script to perform log sanitisation. 
    Replace the private information, IP address with unique value and provide a mapping table as a seperate text file and the sanitised log file as seperate text files. 
    Take note that the log file has more than one format of IP address, you should account for all the possible formats of IP address. Take note that Ipv6 Ip addresses has more than one representation as well. Account for all the representation. 
    After sucessfully executing the code, the checker should step in to check if any IP address is missing''',
    # code_execution_config={"last_n_messages": 2, "work_dir": "coding", "use_docker":False},
    # human_input_mode="ALWAYS",
    llm_config=llm_config,
)

ragproxyagent = RetrieveUserProxyAgent(
    name="ragproxyagent",
    retrieve_config={
        "task": "qa",
        "docs_path": "https://en.wikipedia.org/wiki/IPv6_address",
        # "docs_path": "https://www.juniper.net/documentation/us/en/software/junos/interfaces-security-devices/topics/topic-map/security-interface-ipv4-ipv6-protocol.html",
        # "docs_path": "https://en.wikipedia.org/wiki/IP_address",
        # "docs_path": "./docs.txt",
        # "docs_path": "https://simple.wikipedia.org/wiki/IP_address",
        
        "get_or_create": True,
    },
    human_input_mode="ALWAYS",
    code_execution_config={"last_n_messages": 2, "work_dir": "coding", "use_docker":False},
    system_message="Your role is to find out the different type of IP address so that the assistant can accurately sanitise the IP address from the log file. The log file name is pfirewall.log. Tell the assistant what are the types of IP address it should look out for. After executing codes successfully, checker should be the next speaker."
)

checker = autogen.AssistantAgent("checker", 
                           llm_config=llm_config, 
                           system_message="your job here is to to look through the sanitized log file to check if there is any IP address that is not being cleaned up. do not terminate unless the user intervents.",
                        #    code_execution_config={"last_n_messages": 2, "work_dir": "coding", "use_docker":False},
                           )

def custom_speaker_selection_func(last_speaker: Agent, groupchat: autogen.GroupChat):
    if last_speaker is checker:
        return ragproxyagent
    else:
        return 'auto'

groupchat = autogen.GroupChat(
    agents=[ragproxyagent, checker, assistant],
    messages=[],
    allow_repeat_speaker=False,
    speaker_selection_method=custom_speaker_selection_func

)

manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)



assistant.reset()
ragproxyagent.initiate_chat(
    manager, 
    # assistant,
    message=ragproxyagent.message_generator, problem="I want to perform log sanitisation, the private information is IP address. Replace all Ip addresses with a unique placeholder value and provide a mapping table to map the santised IP address to the unique value as a seperate file.")





# checker, check sanitized_pfirewall.log to see if we miss any IP address out. Write a python code to do so.


# checker, check sanitized_pfirewall.log to see if there is still any IP address in sanitized_pfirewall.log. Write a python code to do so. IF there is IP address, please help to resanitize, create a new sanitzied log file and a new mapping table.If no IP address found then print no IP address found. 


# checker, check sanitized_pfirewall.log to see if we miss any IP address out. Write a python code to do so. remmeber to create the python code and execute it. do not stop the conversation abruptly without my permission. in the python code, you do not need to check against any mapping table text file (e.g., ip_mapping.txt). you just need to check whether there is any ip addresses that have been missed out in the sanitized_pfirewall.log file. if there is any ip address, please resanitize the file and update the mapping table file (ip_mapping.txt) accordingly. for this checker task, you need to execute the python code.