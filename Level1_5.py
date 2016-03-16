class Main:
    def get_string(self):
        self.string = input("Please enter a value or a string: ")
        print(self.string)

    def upcase_string(self):
        new_string = self.string.upper()
        print(new_string)

new_string = Main()
new_string.get_string()
new_string.upcase_string()


