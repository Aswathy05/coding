def avg(*args):
    count=0
    for i in args:
        count+=i
    return float("{:.2f}".format(count/len(args)))

