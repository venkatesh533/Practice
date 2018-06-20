
def num_repeat(li):
    d = {}
    if type(li) == list:
        for i in list(li):
            d[i] = li.count(i)
        val = sorted(d.items(), key=lambda x: x[1])
        print(val)
    else:
        print('Please enter list of elements only')
