def assignemnt_analyser(filename):
    with open(filename,"r") as f:
        lines = f.readlines()
        print("Number of lines:",len(lines))
        f.seek(0)
        words1 = f.read().split()
        words,char=0,0
        for i in words1:
            words+=1
            for j in i:
                char+=1
        print("Number of words:",words)
        print("Number of charcters:",char)       
assignemnt_analyser("assignment.txt")




