class bikeshop:
	def __init__(self,stock):
		self.stock=stock
	def displayBike(self):
		print("Total bikes",self.stock)
	def rentforbike(self,q):
		if q<=0:
			print("Enter the positive value or greater then zero")
		elif q>self.stock :
			print("enter the value (less then stock)")
		else: 
			print("\nTotal price" ,q*100)
			print("\nTotal Bikes",self.stock-q)
while True:
	obj=bikeshop(100)
	uc=int(input("1 Display stocks\n2 Rent a Bike\n3 Exit\n "))
	if uc==1:
		obj.displayBike()
	elif uc==2:
		n=int(input("Enter the Quantity: "))
		obj.rentforbike(n)
	else:
		break
