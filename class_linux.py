#!/usr/bin/python3


class Linux:
    """Create a class Networking, under which to place all the trng packages"""

    def __init__(self):
        """Constructor Method: Declare and Initialize attributes"""
        #  self.subject = subject
        #  self.dictionary = dictionary

    def flash_cards(self, subject, dictionary):
        """METHOD: Spin through k,v pairs to quiz user on subject"""
        print("==== LET'S TRAIN ====")
        print(f"This session's training topic: {subject.upper()}")
        print("(x) at any time to Exit")

        wrong_answers = {}
        i = 0
        answer = ""
        while i < len(dictionary):
            if answer == 'x':
                break
            for key in dictionary:
                i += 1
                print(f"\n{key}")
                answer = input('> ').lower()
                value = dictionary[key]
                if answer == 'x':
                    break
                elif answer == value.lower():
                    print("<< CORRECT >>")
                else:
                    print("Not quite")
                    print(value)
                    wrong_answers[key] = value
        print("Redo wrong answers (Y | n)")
        response = input('> ').lower()
        if response == 'y':
            for key in wrong_answers:
                print(f"\n{key}")
                answer = input('> ').lower()
                value = dictionary[key]
                if answer == 'x':
                    break
                elif answer == value.lower():
                    print("<< CORRECT >>")
                else:
                    print("Not quite")
                    print(value)
                    wrong_answers[key] = value
        else:
            print(f"\n{subject.upper()} missed:\n")
            for key, value in wrong_answers.items():
                print(f"{key} : {value}")

