def numbers(args,*vartuple):
    x = args
    y = list(vartuple)
    y.append(x)

    for num in y:
        if num % 2 == 0:
            print('This is an even number')
        else:
            print('This is an odd number')
    
numbers(23,34,87)
