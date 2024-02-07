with open("code.txt","r") as f:
    f_read=f.readlines()
    with open("recordcode.txt","w") as g:
        for i in f_read:
            if not (i.startswith("#")):
                g.write(i)






