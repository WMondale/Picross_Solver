#picross_solver
#in the nonogram list, "-" represents undetermined spaces, " " represents confirmed blank spaces, and "O" represents confirmed blocks.  This means that, when comparing "isolation" solutions to the present row, it is acceptable for a mismatch to contain a "-"; it's the " "-"O" or vice-versa pairs that invalidate the solution
#also, solutions do not contain "-"'s, so check through the row/column proper to screen out "O"-" " mismatch solutions

from copy import deepcopy

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
	sol=[]
	groups=group(num,l)
	blanks=l-sum(num)-len(num)+1
	s=[[" "]*blanks]+groups
	sol.append(s)
	for n in range(len(groups)):
		for m in range(blanks):
			s=deepcopy(sol[-1])
			del s[n][-1]
			s[n+1].append(" ")
			sol.append(s)
	for x in range(len(sol)):
		sol[x]=combine(sol[x])
	return sol

#filters the solution set of solutions that are shown to be wrong
def fil(sol,o):
	n=0
	while n<len(sol):
		for m in range(len(o)):
			if o[m]!="-" and o[m]!=sol[n][m]:
				del sol[n]
				n=n-1
		n=n+1
	return sol

#goes through a list of possible solutions to create a single list to be applied
def absol(sol):
	ret=sol[0]
	for n in sol[1:]:
		for m in range(len(n)):
			if ret[m]!=n[m]:
				ret[m]="-"
	return ret

x=solset([2],5)#debug
y=(fil(x,["-","O","-","-","-"]))#debug
print(absol(y))#debug

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
