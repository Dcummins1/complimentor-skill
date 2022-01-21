from mycroft import MycroftSkill, intent_file_handler
import requests

class Complimentor(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('complimentor.intent')
    def handle_complimentor(self, message):
        response = requests.get("https://complimentr.com/api")
        compliment = response.json()["compliment"]
        self.speak_dialog(compliment)


def create_skill():
    return Complimentor()

