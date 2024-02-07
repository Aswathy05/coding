#print prime numbers bw 1-100
for n in range(2,100):
	i=2
	count=0
	while(i*i<=n):
		if(n%i==0):
			count+=1
			break
		i+=1
	if(count==0):
		print(n)
		