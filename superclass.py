class T:
	def t(self):
		print "super class"
class TT(T):
	def tt(self):
		print "sub class"
if __name__=='__main__':
	obj = TT()
	obj.t()


