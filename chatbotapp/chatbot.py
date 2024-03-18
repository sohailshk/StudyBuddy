# chatbot.py
import json

class WebsiteChatbot:
    def __init__(self):
        self.responses = {
            "join-room": "http://127.0.0.1:8000/",
            "create-room": "http://127.0.0.1:8000/create-room/",
            "update-user": "http://127.0.0.1:8000/update-user/",
        }
    
    def respond(self, question):
        if "create room" in question.lower() or "create room" in question.lower():
            return json.dumps({"response": "To create a room, please visit: " + self.responses["create-room"]})
        elif "join room" in question.lower() or "join room" in question.lower():
            return json.dumps({"response": "To join a room, please visit: " + self.responses["join-room"]})
        elif "update user" in question.lower() or "update user" in question.lower():
            return json.dumps({"response": "To edit your profile, please visit: " + self.responses["update-user"]})
        else:
            return json.dumps({"response": "I'm sorry, I'm not sure how to answer that question. Could you please ask something else?"})
