class Phone():
    def __init__(self, phone_number):
        self.phone_number = phone_number
    def __str__(self):
        return str(self.phone_number)
    def call(self, other_number):
        print(f'Ring ring ring, calling {other_number} from {self.phone_number}')
    def text(self, other_number, msg):
        print(f'beet boop sending text from {self.phone_number} to {other_number}')
        print(msg)
gabes_phone = Phone(6666661234)

# print(gabes_phone)

gabes_phone.call(5105483936)

# gabes_phone.text(1234567890, "u up?")

class IPhone(Phone):
    def __init__(self, phone_number, generation, color):
        super().__init__(phone_number)
        self.generation = generation
        self.color = color

    def __str__(self):
        return f'gen {self.generation}  {self.color} Iphone {self.phone_number}'
    def set_fingerprint(self, my_fingerprint):
        self.fingerprint = my_fingerprint
    def unlock(self, fingerprint=None):
        if(not self.fingerprint):
            print("fingerprint unlock not setup")
        elif (fingerprint == self.fingerprint):
            print('phone unlocked, fingerprint matches')
        else:
            print("phone locked, fingerprint does not match")
westons_iphone = IPhone(4443332211, 14, 'Rose Gold')

print(westons_iphone)
# westons_iphone.call(gabes_phone.phone_number)
# westons_iphone.text(gabes_phone.phone_number, f'Hey nerd, I have a {westons_iphone.color} IPhone!')
westons_iphone.set_fingerprint("Weston's thumb")
westons_iphone.unlock("Weston's thumb")

class Android(Phone):
    def __init__(self, phone_number, keyboard="Default"):
        super().__init__(phone_number)
        self.keyboard = keyboard
    def __str__(self):
        return f'This Android uses the {self.keyboard} keyboard'
Phone.BBQ = 5105483936
gabes_android = Android(6666661234, 'UK')
print(gabes_android.BBQ)
