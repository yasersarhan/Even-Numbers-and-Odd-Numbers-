class DivisionGame:
    def __init__(self):
        print('Welcome in our division game')
        num = int(input('Please enter your number: '))
        for x in range(1, 11):
            if num % x == 0:
                print(str(num)+' can division on '+str(x))
            else:
                print(str(num)+' can not division on '+str(x))

g = DivisionGame()
