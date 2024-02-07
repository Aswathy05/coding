mat=[]
for i in range(9):
    row=input().split()
    mat.append(row)
for i in range(9):
    if(len(set(mat[i]))!=9):
        print("No")
        break
else:    
    tmat=[list(x) for x in zip(*mat)]
    for i in range(9):
        if(len(set(tmat[i]))!=9):
            print("No")
            break      
    else:    
        sudo=[]  
        for i in range(9):
            box=[]
            for j in range(3):
                box.append(mat[i][j])  
            sudo.append(box)  
        for i in range(9):
            box=[]
            for j in range(3,6):
                box.append(mat[i][j])
            sudo.append(box)    
        for i in range(9):
            box=[]
            for j in range(6,9):
                box.append(mat[i][j])
            sudo.append(box)           
        box1=[sudo[0]+sudo[1]+sudo[2]]
        box2=[sudo[3]+sudo[4]+sudo[5]]
        box3=[sudo[6]+sudo[7]+sudo[8]]
        box4=[sudo[9]+sudo[10]+sudo[11]]
        box5=[sudo[12]+sudo[13]+sudo[14]]
        box6=[sudo[15]+sudo[16]+sudo[17]]
        box7=[sudo[18]+sudo[19]+sudo[20]]
        box8=[sudo[21]+sudo[22]+sudo[23]]
        box9=[sudo[24]+sudo[25]+sudo[26]]
        if((len(set((box1[0])))!=9) or (len(set((box2[0])))!=9) or (len(set((box3[0])))!=9) or (len(set((box4[0])))!=9) or (len(set((box5[0])))!=9) or (len(set((box6[0])))!=9) or (len(set((box7[0])))!=9) or (len(set((box8[0])))!=9) or (len(set((box9[0])))!=9)):
            print("No") 
        else:
            print("Yes")    

        """ sudo[0][1]=mat[i][j]
        sudo[0][2]=mat[i][j]
        sudo[1][0]=mat[i][j]
        sudo[1][1]=mat[i][j]
        sudo[1][2]=mat[i][j]
        sudo[2][0]=mat[i][j]
        sudo[2][1]=mat[i][j]
        sudo[2][2]=mat[i][j] """




