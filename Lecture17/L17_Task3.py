class SmartDevice:
    def __init__(self, brand):
        self.brand = brand
        self.__is_on = False  

    @property
    def is_on(self):
        return self.__is_on

    def turn_on(self):
        self.__is_on = True
        print(f"{self.brand} მოწყობილობა ჩაირთო.")

    def turn_off(self):
        self.__is_on = False
        print(f"{self.brand} მოწყობილობა გამოირთო.")

class SmartLight(SmartDevice):
    def __init__(self, brand, brightness = 50):
        super().__init__(brand)
        self.brightness = brightness

    def turn_on(self):
        super().turn_on()
        print( f"ბრენდი: {self.brand}, სიკაშკაშე: {self.brightness}%")


sl1 = SmartLight("Smart",80)
print(f"ბრენდი: {sl1.brand}")
print("="*40)

sl1.turn_on()
print("="*40)

sl1.turn_off()


