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

#removes an element from the end of a designated sublist and appends it to the end of the next sublist
def mover(sol,e):
	h=sol[e][-1]
	del sol[e][-1]
	sol[e+1].append(h)
	return sol

#generates a set of solutions for a number list and length
def solset(num,l,o):
	if len(num)==0:
		return [[" " for n in range(l)]]
	sol=[]
	groups=group(num,l)
	blanks=l-sum(num)-len(num)+1
	s=[[" "]*blanks]+groups
	sol.append(s)
	ret=[]
	if fil(deepcopy(combine(sol[0])),o):
		ret.append(deepcopy(combine(sol[0])))
	cop=[]
	for n in range(blanks):
		s=deepcopy(sol)
		sol=[]
		for m in s:
			if len(m[0])==0:
				break
			for p in range(0,len(m)-1):
				m=mover(m,p)
				sol.append(deepcopy(m))
		cop=deepcopy(sol)
		for x in range(len(cop)):
			cop[x]=combine(cop[x])
			if fil(cop[x],o):
				ret.append(cop[x])
	return ret
			


#filters the solution set of solutions that are known to be wrong
def fil(n,o):
	ret=True
	for m in range(len(o)):
		if o[m]!="-" and o[m]!=n[m]:
			ret=False
			break
	return ret
			

#goes through a list of possible solutions to create a single list to be applied
def absol(sol):
	ret=sol[0]
	for n in sol[1:]:
		for m in range(len(n)):
			if ret[m]!=n[m]:
				ret[m]="-"
	return ret

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

#run until no changes to rows or columns have been made
change=True
while change:
	for n in range(len(rows)):
		change=False
		m=solset(rows[n],r,nonogram[n])
		m=absol(m)
		print("Loading.")
		if m!=nonogram[n]:
			print("Loading..")
			nonogram[n]=m
			print("Loading...")
			change=True

	for n in range(len(columns)):
		m=solset(columns[n],c,[nonogram[x][n] for x in range(c)])
		m=absol(m)
		print("Loading.")
		if m!=[nonogram[x][n] for x in range(c)]:
			print("Loading..")
			col(nonogram,m,n)
			print("Loading...")
			change=True

#print what has been solved
print("The Solution:")
for n in nonogram:
	print(n)
