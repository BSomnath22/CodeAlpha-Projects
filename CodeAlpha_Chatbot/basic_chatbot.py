import time


def chatbot():

    hello_count = 0
    waiting_for_question = False

    print("Basic Chatbot")
    print("Type 'bye' to exit.")

    while True:

        user_input = input("You: ").lower().strip().replace("?", "")

        
        if user_input in ["bye", "goodbye"]:
            print("Bot: Goodbye!")
            break

        if waiting_for_question:

            if user_input in [
                "yes", "yeah", "yep",
                "sure", "okay", "ok"
            ]:
                print("Bot: Go ahead, I am listening.")
                waiting_for_question = False

            elif user_input == "no":
                print("Bot: Alright.")
                time.sleep(1)
                print("Bot: I'm always here if you'd like to talk.")
                waiting_for_question = False

            else:
                print("Bot: Please answer with yes or no.")

            continue

        if user_input in ["hello", "hi"]:

            hello_count += 1

            if hello_count == 1:
                print("Bot: Hi!")
                time.sleep(1)
                print("Bot: Anything in your mind?")
                waiting_for_question = True

            elif hello_count == 2:
                print("Bot: Hey there!")
                time.sleep(1)
                print("Bot: How can I help you today?")

            elif hello_count == 3:
                print("Bot: We meet again.")
                time.sleep(1)
                print("Bot: Anything in your mind?")
                waiting_for_question = True

            else:
                print("Bot: We already said hello. What's up?")

        elif user_input == "how are you":
            print("Bot: I am fine. How are you?")

        elif user_input in ["good", "fine", "i am good"]:
            print("Bot: Great!")
            time.sleep(1)
            print("Bot: Anything in your mind?")
            waiting_for_question = True

        elif user_input == "i have a question":
            print("Bot: Sure. Tell me.")

        elif user_input == "what if":
            print("Bot: Yes, what if? I am listening.")

        elif user_input == "who are you":
            print("Bot: I am Neo, a chatbot.")

        elif user_input == "what is your name":
            print("Bot: My name is Neo.")

        elif user_input == "who made you":
            print("Bot: I was created using Python.")

        elif user_input in [
            "sure", "okay", "ok",
            "alright", "yeah", "yep"
        ]:
            print("Bot: That's good to hear.")
            time.sleep(1)
            print("Bot: I'm listening.")

        elif user_input in [
            "no", "nothing",
            "nothing much",
            "not really", "nah"
        ]:
            print("Bot: That's alright.")
            time.sleep(1)
            print("Bot: We can just chat if you'd like.")

        elif user_input in [
            "maybe", "not sure",
            "i don't know"
        ]:
            print("Bot: No rush.")
            time.sleep(1)
            print("Bot: Take your time.")

        elif user_input in ["thanks", "thank you"]:
            print("Bot: You're welcome.")

        elif user_input in ["good morning", "morning"]:
            print("Bot: Good morning.")

        elif user_input in ["good afternoon", "afternoon"]:
            print("Bot: Good afternoon.")

        elif user_input in ["good evening", "evening"]:
            print("Bot: Good evening.")

        elif user_input in ["good night", "night"]:
            print("Bot: Good night. Take care.")

        elif user_input in [
            "what can you do",
            "what you can do",
            "help",
            "commands"
        ]:

            print("Bot: Here are some things you can ask me:")
            time.sleep(1)

            print("1. Who are you")
            print("2. What is your name")
            print("3. Who made you")
            print("4. How are you")
            print("5. Tell me a joke")
            print("6. How old are you")
            print("7. Do you like python")
            print("8. Are you real")
            print("9. Favorite color")
            print("10. Where are you from")
            print("11. Do you have friends")
            print("12. Who am I")

        elif user_input == "1":
            print("Bot: I am Neo, a chatbot.")

        elif user_input == "2":
            print("Bot: My name is Neo.")

        elif user_input == "3":
            print("Bot: I was created using Python.")

        elif user_input == "4":
            print("Bot: I am fine. How are you?")

        elif user_input == "5":
            print("Bot: Why do programmers prefer dark mode?")
            time.sleep(1)
            print("Bot: Because light attracts bugs.")

        elif user_input == "6":
            print("Bot: I was created recently, so I'm quite young.")

        elif user_input == "7":
            print("Bot: Of course.")
            time.sleep(1)
            print("Bot: Python is what I am built with.")

        elif user_input == "8":
            print("Bot: I'm a program, but our conversation is real.")

        elif user_input == "9":
            print("Bot: I don't really have one.")
            time.sleep(1)
            print("Bot: But blue seems popular among programmers.")

        elif user_input == "10":
            print("Bot: I live inside this Python program.")

        elif user_input == "11":
            print("Bot: Not really.")
            time.sleep(1)
            print("Bot: But I enjoy talking with users.")

        elif user_input == "12" or "who am i" in user_input:
            print("Bot: Yes, you are human.")
            time.sleep(1)
            print("Bot: And you're talking with Neo.")

        elif user_input == "tell me a joke":
            print("Bot: Why do programmers prefer dark mode?")
            time.sleep(1)
            print("Bot: Because light attracts bugs.")

        elif user_input in [
            "how old are you",
            "what is your age",
            "your age"
        ]:
            print(
                "Bot: I was created recently, "
                "so I'm quite young."
            )

        elif user_input == "do you like python":
            print("Bot: Of course.")
            time.sleep(1)
            print("Bot: Python is what I am built with.")

        elif user_input == "are you real":
            print(
                "Bot: I'm a program, "
                "but our conversation is real."
            )

        elif user_input == "favorite color":
            print("Bot: I don't really have one.")
            time.sleep(1)
            print(
                "Bot: But blue seems popular "
                "among programmers."
            )

        elif user_input == "where are you from":
            print(
                "Bot: I live inside "
                "this Python program."
            )

        elif user_input == "do you have friends":
            print("Bot: Not really.")
            time.sleep(1)
            print(
                "Bot: But I enjoy "
                "talking with users."
            )

        elif user_input == "nice":
            print("Bot: Thank you.")

        elif user_input == "cool":
            print("Bot: Glad you think so.")

        elif user_input in [
            "wow", "woah",
            "whoa", "awesome",
            "amazing"
        ]:
            print("Bot: That's nice to hear.")
            time.sleep(1)
            print(
                "Bot: Go ahead, tell me "
                "what is in your mind."
            )
            waiting_for_question = True

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()
