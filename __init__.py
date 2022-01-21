from mycroft import MycroftSkill, intent_file_handler


class Complimentor(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('complimentor.intent')
    def handle_complimentor(self, message):
        self.speak_dialog('complimentor')


def create_skill():
    return Complimentor()

