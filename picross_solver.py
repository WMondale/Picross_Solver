#picross_solver
#Makes a 2D array of inputted dimensions, takes a list of positive integers for
#each row and column of the array, and marks the array with blocks or blanks as #are logically confirmed to be certain

#get dimensions for the picross array
r=0
c=0
while r<1 or r%1!=0:
	try:
		r=float(input("Please input row length:\n"))
	except ValueError:
		pass
r=int(r)
while c<1 or c%1!=0:
	try:
		c=float(input("Please input column height:\n"))
	except ValueError:
		pass
c=int(c)

#construct 2D array of puzzle
nonogram=[["-" for x in range(r)] for x in range(c)]

#construct list of numbers for all rows and columns
rows=[[] for n in range(c)]
columns=[[]for n in range(r)]

#get defining numbers for each row and column
print("Row Input\n")
for n in range(c):
	print("Row "+str(n+1)+"; press 0 to advance to next row:\n")
	i=0
	while i>0 or len(rows[n])==0:
		if sum(rows[n])+len(rows[n])-1>r:
			rows[n]=[]
			print("Invalid long list.  Resetting")
			print(rows[n])
		try:
			i=int(input())
			if i>=0:
				rows[n].append(i)
				print(rows[n])
		except:
			pass
rows=[[rows[x][y] for y in range(len(rows[x])-1)] for x in range(len(rows))]

for n in range(r):
	print("Column "+str(n+1)+"; press 0 to advance to next column:\n")
	i=0
	while i>0 or len(columns[n])==0:
		if sum(columns[n])+len(columns[n])-1>r:
			columns[n]=[]
			print("Invalid long list.  Resetting")
			print(columns[n])
		try:
			i=int(input())
			if i>=0:
				columns[n].append(i)
				print(columns[n])
		except:
			pass
columns=[[columns[x][y] for y in range(len(columns[x])-1)] for x in range(len(columns))]

#run through each row and column, compare each solution to the one before
#for each row
for n in rows:
	solset=[]
	comp=[]
	#for each number in the row
	for m in n:
		comp.append(["O" for x in range(m)])
	#for each group of blocks
	for a in comp:
		solset[0]=solset[0]+a
		if len(solset[0])<r:
			solset[0].append(0)
