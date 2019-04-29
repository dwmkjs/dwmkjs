
support=3
confidence=5
# list_elements =[] list_search_from=[]
def search(list_elements,list_search_from):
	temp=0
	for i in range(len(list_elements)):
		if list_elements[i] in list_search_from:
			temp=temp+1
	if temp==len(list_elements):
		return 1
	else:
		return 0

def uniquedata(data_list):
	unique_data_items=[]
	for i in range(len(data_list)):
		for j in range(len(data_list[i])):
			if data_list[i][j] not in unique_data_items:
				unique_data_items.append(data_list[i][j])

	return unique_data_items
def combinations(C,K):
 	newC=[]
 	for i in range(len(C)):
 		for j in range(i+1,len(C)):
 			no_common_elements=0
 			for k in range(len(C[i])):
 				if search(C[i][k],C[j])==1:
 					no_common_elements=no_common_elements+1
 			if no_common_elements==K-1 :
 				validate=1
 				for m in range(len(newC)):
 					if search(uniquedata([C[i],C[j]]),newC[m])==1:
 						validate=0
 				if validate==1:
 					newC.append(uniquedata([C[i],C[j]]))
 	#print newC
 	return newC
def getSupport(Ci,transctions):
	count=0
	for j in range(len(transctions)):
		if search(Ci,transctions[j])==1:
			count=count+1;
	return count;

# combinations([["a","b","d"],["a","c","d"],["b","c","a"],["c","d","a"]],3)
def frequency(C,transctions,K):
	L=[]
	while True:
		Lpre=L
		L=[]	
		for i in range(len(C)):
			if getSupport(C[i],transctions)>=support:
				L.append([getSupport(C[i],transctions),C[i]])	
		K=+1
		l=[]
		for j in range(len(L)):
			l.append(L[j][1]) 
		C=combinations(l,K)
		if L==[]:
			return Lpre


print(frequency(["a","b","c"],[["a","b"],["a","b","c"],["a","b"],["a"],["a","c"],["b","c"],["b"]],1))