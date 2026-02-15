import autogen

assistant = autogen.AssistantAgent("assistant")
user_proxy = autogen.UserProxyAgent("user")

user_proxy.initiate_chat(
    assistant,
    message="Write a Python function to compute factorial."
)
