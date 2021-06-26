class BIT:
	def __init__(self,n):
		self.sums=[0]*(n+1)
	def update(self,i,v): #v is delta
		while i < len(self.sums):
			self.sums[i]+=v
			i+=(i&-i)
	def query(self,i):
		res = 0
		while i > 0:
			res += self.sums[i]
			i -=(i&-i)
		return res
	
		
