def prrep():
  m={}
  sub={}
  n=int(input("Enter the number of products :"))
  for i in range(1,n+1):
    m[i]=i-1
  for i in range(1,n+1):
     sub["prname",i]=str(input("Enter the name :"))
     sub["prprize",i]=str(input("Enter the prize :"))
     sub["prcat",i]=str(input("Enter the category name of product: "))
     sub["catcode",i]=str(input("Enter the category code :"))
     sub["prdesc",i]=str(input("Enter the description :"))
     year=str(input("Enter the year of expiry :"))
     month=str(input("Enter the expiry month in numbers :"))
     date=str(input("Enter the day of expiry :"))
     sub["exdate",i]=[date+":"+month+":"+year]
     m[i]=sub
  print(m)
prrep()

def cusinfo():
 cusmain={}
 sub={}
 m=int(input("Enter the number of customers :"))
 for i in range(1,m+1):
  sub["cusname",i]=str(input("Enter the name :"))
  sub["cusphone",i]=str(input("Enter the phone number :"))
  sub["cusaddress",i]=str(input("Enter the address of customer: "))
  sub["cusmailid",i]=str(input("Enter the mail id :"))
  cusmain[i]=sub
 print(cusmain)
cusinfo()