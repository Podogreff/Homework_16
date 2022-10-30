class CustomException(Exception):
    def __init__(self, msg):
        if msg:
            self.msg = msg
            with open("logs.txt", "w") as file:
                file.write(self.msg)


def age_check(age, name):
    if age < 18:
        raise CustomException(f"Person {name}: {age}, entrance to the club is __denied__\n")
    else:
        print(f"Person {name}: {age}, access __allowed__")


age_check(12, "Ruslan")
age_check(13, "Vlad")

