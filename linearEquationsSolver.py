def linearEquationsSolver(testcases):
	for cases in range(testcases):
		variables=input('No. of variables:')
		lst=[]
		for i in range(variables):
			lst.append([])
			for j in range(variables+1):
				element=input('>>>')
				lst[i].append(element)
		
		i=0
		while i<variables:
			maximum=max(lst[p][i] for p in range(variables))
			if maximum!=lst[i][i]:
				#swap(max wala row and ith row)
				j=i+1
				while j<variables:
					if lst[j][i]==maximum:
						for k in range(variables+1):
							temp=lst[i][k]
							lst[i][k]=lst[j][k]
							lst[j][k]=temp
						break
					j+=1
			i+=1

		# solving the equations
		i=0
		while i<variables-1:
			j=variables-1
			while j>0:
				k=0
				factor=(float(lst[j][i]))/lst[j-1][i]
				while k<=variables:
					lst[j][k]=lst[j][k]-(lst[j-1][k]*factor)
					k+=1
				j-=1
			i+=1
		#print lst
		for i in range(variables):
			nonzero=0
			for j in range(variables):
				if lst[i][j]!=0:
					nonzero=1
					break
			if nonzero==0:
				print 'Inconsistent'
				return
			
		# making the first coefficient term =1
		i=0
		while i<variables:
			factor=lst[i][i]
			k=0
			while k<=variables:
				lst[i][k]=float(lst[i][k])/factor
				k+=1
			i+=1
		#print lst

		# for finding the final result
		result=[]
		i=variables-1
		while i>=0:
			k=variables-1
			while k>i:
				lst[i][variables]-=lst[i][k]*lst[i+1][variables]
				k-=1
			result.append(lst[i][variables])
			i-=1

		# showing the results
		print 'Results'
		for i in range(len(result)):
			print result[len(result)-i-1]

if __name__=='__main__':
	linearEquationsSolver(input('No of testcases:'))



