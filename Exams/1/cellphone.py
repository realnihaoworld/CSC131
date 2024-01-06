class CellPhone:

    default_ring_tone = 'chime1.mp3'
    default_mode = 'light'
    
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.ring_tone = CellPhone.default_ring_tone
        self.mode = CellPhone.default_mode
        
    @property
    def phone_number(self):
        return self._phone_number
        
    @phone_number.setter
    def phone_number(self, new_number):  # noqa: F811
        if len(new_number) == 10:
            self._phone_number = new_number
        else:
            raise Exception('The number needs to be 10 digits.')
            
    def call(self, other_phone):
        other_phone.ring()
        
    def ring(self):
        print(f'{self.phone_number} is ringing')
        
    def __str__(self):
        return self.phone_number

c1 = CellPhone('1234567890')
c2 = CellPhone('0987654321')
c1.call(c2)
print(c2)
