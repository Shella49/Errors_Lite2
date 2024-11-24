class NegativeNumberError(Exception):
    def __init__(self, number, message= "Отрицательное число:"):
        self.number =number
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f'{self.message} {self.number}'

def check_positive_numbers(number):
    
    if number < 0:
            raise NegativeNumberError(number) 
             
    return True

if check_positive_numbers(17):
     print("Число положительное ")
if check_positive_numbers(-44):
     print("Число положительное")