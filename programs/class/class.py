#test work with class

class cl:
    a=123
    def data(self, value):
        self.dataa = value
    def display(self):
        print(self.data)

x=cl()
y=cl()


#print("x.data  ",x.data)
#x.data = 321
#print("x.data  ",x.data)

print("befor dell cl.a  ",cl.a)
delattr(cl,"a")
print("after dell cl.a  ",cl.a)
