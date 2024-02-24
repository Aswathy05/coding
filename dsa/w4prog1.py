def orangecap(d):
    d_values=d.values()
    sum_dict={}
    for i in d_values:
        for j in i:
            if j not in sum_dict:
                sum_dict[j]=i[j]
            else:
                sum_dict[j]+=i[j]   
    maxi=(max(sum_dict.values())) 
    for i in sum_dict:
        if(sum_dict[i]==maxi):
            return(i,maxi)      
print(orangecap({'test1':{'Pant':84, 'Kohli':120}, 'test2':{'Pant':59, 'Gill':42}}))

