bp=int(input("Enter the basic pay:"))
da=88/100*bp
hra=8/100*bp
cca=1000
insurance=2000
pf=10/100*bp
gp=bp+da+hra+cca
deductions=insurance+pf
netsal=gp-deductions
print(netsal)