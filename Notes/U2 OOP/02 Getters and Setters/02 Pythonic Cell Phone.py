

class CellPhone:
    
    default_ring_tone = "chime1.mp3"
    default_mode = "light"
    
    def __init__(self, phone_number: int):
        self._phone_number = phone_number
        self.ring_tone = CellPhone.default_ring_tone
        self.mode = CellPhone.default_mode
    
    # getter
    @property
    def phone_number(self):
        print("This one is the getter")
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, new_phone_number):
        print("Hi this is the setter")
        if len(new_phone_number) == 10:
            self._phone_number = new_phone_number
        
    def call(self, other_phone):
        other_phone.ring()
    
    def ring(self):
        print(f"{self.phone_number} is ringing")
    
    def __str__(self):
        return self.phone_number

phone1 = CellPhone("1234567890")
print(phone1)
phone1.phone_number = '12'
# print(phone1)
# phone1.set_phone_number("9876543210")
# print(phone1)