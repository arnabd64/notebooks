import utils
from schema import Conversation, Message


def cli():
    username = "arnab"
    print("\n", "+-"*10, "Chatbot", "-+"*10, "\n")
    print("Enter System Prompt")
    system = input("[system] >> ")

    # create a conversation
    conversation = Conversation(
        messages = [
            Message(role="system", content=system)
        ]
    )

    # input a user message
    print("\n","+-"*10, "Chat Session", "-+"*10, "\n")
    while True:
        user_message = input(f"[{username}] >> ")
        if user_message.lower() == "exit":
            return
        
        user_message = {"role": "user", "content": user_message}

        # add user message to conversation
        conversation = utils.update_conversation(conversation, user_message)

        # generate response
        api_response = utils.call_llm(conversation)
        llm_response = utils.postprocess(api_response)

        # add ai message to conversation
        conversation = utils.update_conversation(conversation, llm_response)

        print(f"\n[ai] >> {llm_response['content']}")



if __name__ == "__main__":
    cli()