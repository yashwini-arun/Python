while True:
    msg = input("How are you feeling today? (type 'exit' to quit): ")

    if msg.lower() == "exit":
        print("Bot: Take care! See you soon.")
        break
    elif "happy" in msg.lower():
        print("Bot: That's great to hear! ")
    elif "sad" in msg.lower():
        print("Bot: I'm sorry to hear that. Things will get better. ")
    elif "angry" in msg.lower():
        print("Bot: Take a deep breath. You're stronger than you think. ")
    else:
        print("Bot: Thanks for sharing. I'm here for you. ")
