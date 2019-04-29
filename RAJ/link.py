
class Node :
	def __init__(self,pname,data,next_node=[]) :
		self.pname=pname
		self.data=data	
		self.next_node=next_node
	
	def printf(self):
		print (self.pname)
		print (self.data)
		for i in range(len(self.next_node)):
			print (self.next_node[i])
	

node1=Node('asd','qwert',None)
node2=Node('yuo','zcb',None)
list=[node1,node2]
newnode=Node('abc','xyz',list)

print(newnode.next_node[1].pname)	

