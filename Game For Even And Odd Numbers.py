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
