#picross_solver
#in the nonogram list, "-" represents undetermined spaces, " " represents confirmed blank spaces, and "O" represents confirmed blocks.  This means that, when comparing "isolation" solutions to the present row, it is acceptable for a mismatch to contain a "-"; it's the " "-"O" or vice-versa pairs that invalidate the solution
#also, solutions do not contain "-"'s, so check through the row/column proper to screen out "O"-" " mismatch solutions

#data type validation method
def validate(typ,msg):
	var=input(msg)
	try:
		var=typ(var)
	except ValueError:
		print("Invalid data type")
		while type(var) is not typ:
			try:
				var=typ(input(msg))
			except ValueError:
				print("Invalid data type.")
	return var

#number list metalist method
def rnc(l,m,msg):
	lst=[]
	for n in range(l):
		i=1
		lst.append([])
		print(msg+str(n+1))
		while i!=0:
			i=validate(int,"")
			if i>0:
				lst[n].append(i)
				print(lst[n])
				if (sum(lst[n])+len(lst[n])-1)>m:
					lst[n]=[]
					print("Overboard, resetting.\n")
					print(lst[n])
	return lst

#builds list of block groups, the basis of solutions
def group(num,l):
	blocks=[]
	blocks.append(["O" for x in range(num[0])])
	for n in num[1:]:
		blocks.append([" "]+["O" for x in range(n)])
	return blocks


#method for assigning a column
def col(main,lst,c):
	for n in range(len(main)):
		main[n][c]=lst[n]
	return main

#combine sublists in a list into a single list
def combine(lst):
	ret=[]
	for n in lst:
		ret=ret+n
	return ret

#generates a set of solutions for a number list and length
def solset(num,l):
	if len(num)==0:
		return [[" " for n in range(l)]]
	groups=group(num,l)
	sol=[]
	blanks=l-sum(num)-len(num)+1
	for n in range(len(groups)):
		print(groups)#debug
		print(len(groups))#debug
		for m in range(blanks):
			s=groups#for reasons beyond me, "groups" seems to change with s
			print(s)#debug
			print(groups)#debug
			s[n]=[" " for x in range(blanks-m)]+s[n]+[" " for x in range(m)]
			s=combine(s)
			sol.append(s)
	return sol

print(solset([1,2],5))#debug

#get dimensions
r=0
while r<1:
	r=validate(int,"Input row length:\n")

c=0
while c<1:
	c=validate(int,"Input column height:\n")

#make the array proper
nonogram=[["-" for n in range(r)] for m in range(c)]

#get a list of number lists for each row and column
print("Input number lists for rows; 0 ends and advances to next list.\n")
rows=rnc(c,r,"Row ")
print("Input number lists for columns; 0 ends and advances to next list.\n")
columns=rnc(r,c,"Column ")
