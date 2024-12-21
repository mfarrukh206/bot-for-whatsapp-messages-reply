auto_reply_messages = {
    "hello": "Hi there! ",
    "hi": "Hello! ",
    "how are you": "I'm doing well, thank you!  Tum kaisay ho?",
    "kaise ho": "Main theek hoon, tum kaise ho? ",
    "how are you doing": "I'm good, thanks! How about you?",
    "ok": "Ok, thank you! ",
    "bye": "Bye! See you soon! ",
    "by": "Bye! See you soon! ",
    "goodbye": "Goodbye! Take care! ",
    "whats up": "Nothing much, just hanging out!  Tumhara kya haal hai?",
    "what's up": "Not much, what about you? ",
    "thank you": "You're welcome!  Khush raho!",
    "thanks": "No problem! Glad I could help! ",
    "shukriya": "Shukriya!  Tumhara din acha guzray!",
    "good morning": "Good morning!  Subha Bakhair! Umeed hai tumhara din acha guzray ga.",
    "good night": "Good night!  Khuda Hafiz! Sweet dreams! ",
    "good evening": "Good evening!  Sham bakhair! Hope you're doing well.",
    "good afternoon": "Good afternoon!  Din kaisa guzar raha hai?",
    "yes": "Great! ",
    "haan": "Haan bilkul! ",
    "no": "I see. Let me know if you need anything else. ",
    "nahi": "Nahi yeh galat baat hai. ",
    "help": "How can I assist you? ",
    "madad": "Tumhari madad kaisay karoon? ",
    "who are you": "I am an automated assistant here to help you! ",
    "tum kaun ho": "Main aik chatbot hoon jo tumhari madad kare ga! ",
    "what can you do": "I can assist with common questions and tasks! ",
    "contact support": "You can contact support at [support email/number]. ",
    "order status": "Your order is currently being processed. ",
    "shipping update": "Your order has shipped!  Tracking number: [tracking_number].",
    "where is my order": "Your order is on its way! ",
    "payment": "For payment issues, contact support at [support details]. ",
    "refund": "We will process your refund soon! ",
    "salamat rahay": "Allah tumhain salamat rakhay! ",
    "default": "Sorry, I didn't understand that."
}

# ///////////////////////////////////////////////////////////////////////////////////////////////
# import openai

# # Set your OpenAI API key
# openai.api_key = 'sk-ZT03OqieXfDE1DQQfF_-iYEOsKIxMK2YMNVVDpJik4T3BlbkFJiAeog2LqLnokP8-2segw-XUh6WWHOUFPf0W3jix9UA'

# # Initialize GPT response function for both English and Urdu
# def get_gpt_reply(user_message):
#     # Check if the user message contains Urdu script or common Urdu words to detect the language
#     urdu_words = ["kaise", "kya", "ap", "hai", "mein", "sab"]
    
#     if any(word in user_message.lower() for word in urdu_words):
#         language = "urdu"
#     else:
#         language = "english"
    
#     # Add language context in the prompt to tell GPT to reply accordingly
#     if language == "urdu":
#         prompt = f"The following message is in Urdu, reply to it in Urdu:\n\nUser: {user_message}"
#     else:
#         prompt = f"The following message is in English, reply to it in English:\n\nUser: {user_message}"

#     try:
#         # Send the message to GPT
#         response = openai.Completion.create(
#             model="gpt-3.5-turbo",  # You can use other models like gpt-4 if needed
#             prompt=prompt,
#             max_tokens=150,
#             temperature=0.7  # Adjust for randomness
#         )

#         # Extract the reply
#         return response.choices[0].text.strip()
    
#     except Exception as e:
#         print(f"Error getting GPT reply: {e}")
#         return "Sorry, I couldn't process your request."
    

# user_input = input("enter your message:  ")
# response = get_gpt_reply(user_input)


# print(response)