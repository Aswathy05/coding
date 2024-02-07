def find_all(file_name):
    with open(file_name,"r") as f:
        words = f.read().split()
        lst=[]
        for i in words:
            if i not in lst:
                lst.append(i)
        dict={}
        for i in lst:
            count=0
            for j in words:
                if(i==j):
                    count+=1
            dict[i]=count     
        print(dict)           

find_all("frequency.txt")        
