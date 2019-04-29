import math

listcat=['age','competition','type','profit']
list1=[['old', 'yes' ,'software',0],['old', 'no' ,'software',0],['old', 'no' ,'hardware',0],['mid', 'yes' ,'software',0],['mid', 'yes' ,'hardware',1],['mid', 'no' ,'hardware',1],['mid', 'no' ,'software',1],['new', 'yes' ,'software',1],['new', 'no' ,'hardware',1],['new', 'no' ,'software',1]]


def getSubArgs(listdata):
	temp=[]
	check=0
	for i in range(len(listdata)):
		if i==0:
			temp.append(listdata[i][0])
		for j in range(len(temp)):
			if temp[j]==listdata[i][0] :
				check=1
			else:
				check=0
		if check==0:
			temp.append(listdata[i][0])
	return temp
print(getSubArgs(list1))
print(math.log(100,2))



