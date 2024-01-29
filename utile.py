def maxnum(numbers):
    flist=numbers[0]
    for number in numbers:
        if flist<number:
            flist=number
    print(f'The largest number is {flist}')


