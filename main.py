from Commands.text_to_speech import Voice, VoiceError
from Commands.command_initiator import Command


def main():
    print("Talk")
    while True:
        audio = Voice.listen()
        try:
            command = Voice.recognize_cloud(audio)
            text = Command.selector(command)
        except VoiceError:
            text = "I'm sorry, I didn't catch that."

        print(text)
        if text is not None:
            Voice.say(text)


if __name__ == '__main__':
    main()
