def main():
	test_cases=int(input())
	i=0
	f=""
	found=[]
	while(i<test_cases):
		tweets=int(input())
		j=0
		tweet=[]
		check=[]
		count=[]
		finder=[]
		checktweets=[]
		for q in range(0,tweets):
			tweet.extend("0")
			check.extend("0")
			count.extend("1")
			checktweets.extend("0")
		while(j<tweets):
			tweet[j]=input()
			check[j]=tweet[j].split(" ")
			checktweets[j]=check[j][0]
			k=j
			if(k>0):
				while(k>=0):
					if(str(checktweets[j])==str(checktweets[k])):
						if(k != j):
							count[j]=int(count[j])+1
					k=k-1
			elif(k==0):
				count[0]=0
			j=j+1
		maxCount=count[0]
		j=tweets-1
		a=tweets-1
		while(a>=0):
			if((count[a] == '1')or(count[a]=="1")):
				count[a]=1
			a=a-1	
		while(j>=0):
			if(count[j]>maxCount):
				maxCount=count[j]
			j=j-1
		k=tweets-1
		while(k>=0):
			if(maxCount==count[k]):
				maxTweet=tweet[k].split(" ")
				finder.append(maxTweet[0])
			k=k-1
		finder.sort()
		for tw in finder:
			f=f+tw+" "+str(maxCount)+"."
		i=i+1
	printable=f.split(".")	
	for tw in printable:
		print(tw)
main()			
