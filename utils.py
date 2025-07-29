import os

import httpx

from schema import Conversation, Message


def call_llm(conversation: Conversation):
    """
    Calls the LLM provider using httpx
    """
    # get Credentials
    api_key = "sk-hVV5pRvA8T7ZYN6pO9_ZkA"
    url = "https://llm.intellexio.com/v1/chat/completions"

    # set HTTP Headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # set HTTP Body
    body = {
        "model": "gemini/gemini-2.0-flash",
        "messages": conversation["messages"]
    }

    # send POST request
    with httpx.Client() as client:
        response = client.post(
            url = url,
            json = body,
            headers = headers,
            timeout = 600
        )
    
    response.raise_for_status()

    return response


def update_conversation(conversation: Conversation, message: Message):
    """
    Updates the conversation history with new message
    """
    # validation
    assert message["role"] in {"user", "system", "assistant"}, f"found invalid role: {message['role']}"
    assert isinstance(message["content"], str), f"message is not a string"

    # add message to conversation
    conversation["messages"].append(message)

    return conversation


def postprocess(response: httpx.Response):
    """
    Extracts the LLM response from the raw response
    from the LLM Provider.
    """
    response = response.json()
    message = Message(
        role = "assistant",
        content = response["choices"][0]["message"]["content"]
    )
    return message