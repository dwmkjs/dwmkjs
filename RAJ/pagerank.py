			# A B C D	
input_graph=[[0,1,1,0], #A
			 [0,0,0,1], #B
			 [1,1,0,1], #C
			 [0,0,1,0]] #D

def page_rank(graph):
	page_rank=[]
	return_value=[]
	for i in range(len(graph)):
		page_rank.append((1/float(len(graph))))
	for i in range(0,2):
		pre_page_rank=page_rank[:]
		for j in range(len(graph)):
			pagerankj=0.0
			for k in range(len(graph)):
				if graph[k][j]==1:
					count=0
					for l in range(len(graph[k])):
						if graph[k][l]==1:
							count=count+1
					pagerankj=pagerankj+pre_page_rank[k]/float(count)
			page_rank[j]=pagerankj
	for i in range(len(page_rank)):
		return_value.append([page_rank[i],i])
	return_value.sort(key=lambda x: x[0])
	final_page_rank=[]
	for i in range(len(return_value)):
		final_page_rank.append([return_value[i][1],i])
	return final_page_rank

print(page_rank(input_graph))