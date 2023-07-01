from game.menus.login import login

WIDTH = 90


def line(str):
    print(str * int(WIDTH/len(str)))


def center(text):
    print(text.center(WIDTH))


def main_menu():
    print("1. Create User")


def header(text):
    line('=')
    center(text)
    line('=')

class Msg:
    def __init__(self, text, decorator=""):
        self.text = text
        self.decorator = decorator
    def center(self):
        space = int((WIDTH - len(self.text) - (len(self.decorator)*2))/4)*' '
        print(f'{space}{self.decorator}{space}{self.text}{space}{self.decorator}{space}')

def main():
    header("Stygian Abyss")
    main_menu()
    opt = input()
    if opt == '1':
        user = login()
        print(user)

if __name__ == '__main__':
    main()