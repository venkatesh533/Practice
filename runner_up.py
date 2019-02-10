if __name__ == '__main__':
    n = int(input())
    if n in range(2,11):
        arr = list(map(int, input().split()))
        for i in arr:
            if i in list(range(-100,101)):
                arr = set(arr)
                arr = sorted(list(arr))
            else:
                print('Enter number between -100 to 100')
    else:
        print('Please enter between 2 to 10')
    print(arr[::-1][1])