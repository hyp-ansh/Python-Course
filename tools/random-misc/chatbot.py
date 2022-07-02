import randomstuff, random

rs_client = randomstuff.Client(api_key="n62LRZBO6T46", version="4")

tired_response = [
    "I am little tired, Please give me some rest",
    "Who are you to ask me questions Continuously",
    "Leave me alone for some times",
    "Time to Sleep, I will get back to you soon",
    "I have a job to do, Come back later",
    "I need to rest, leave me alone for some times",
    "I am not feeling well, Please Come back later",
]

yes_no = input("Do you want to turn on chatbot [y/n] -> ").lower()
if "y" in yes_no: is_chatbot = True
else: is_chatbot = False

def chatbot():
    while is_chatbot:
        try:
            user_input = input("Say : ")
            response = rs_client.get_ai_response(
                message=user_input,
                server="primary",
                master="Osho",
                bot="FRIDAY",
                language="en",)
            if ("stop" and ("chat bot" or "chatbot")) in user_input:
                print("Stopping Chatbot...")
                break
            else:
                reply = response.message
                print(reply)
        except Exception as e:
            print(random.choice(tired_response))


if is_chatbot: chatbot()
else: print("Chatbot is off")
