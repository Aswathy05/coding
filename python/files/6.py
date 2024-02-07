def display_words(file_name):
    with open(file_name,"r") as f:
        words=f.read().split()
        for i in words:
            if(len(i)<4):
                print(i)
display_words("ebook.txt")                
