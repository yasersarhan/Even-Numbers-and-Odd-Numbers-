class Numbers:
    def __init__(self):
        print('Welcome in our game even and odd numbers')
        print('''
               Press The Game Number:
                  1-For Even Numbers.
                  2-For Odd Numbers.
            ''')
        user_choice = int(input('Enter Your Choice Number: '))
        if user_choice == 1:
            self.even_number()
        elif user_choice == 2:
            self.odd_number()
        else:
            print('Please enter a valid number')

    def even_number(self):
        num = int(input('Please enter your number: '))
        for x in range(0 , num+1):
            if x % 2 == 1:
                continue
            else:
                print(x)    

    def odd_number(self):
        num = int(input('Please enter your number: '))
        for x in range(0 , num+1):
            if x % 2 == 0:
                continue
            else:
                print(x)
