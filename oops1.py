class employee:
    #special method/magic method
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 5000
        self.designation = "SDE"
        print("attributes/data have been initiated")


    def travel(self,des):
        print("This travel function was called manually")
        print(f"Employee is travelling to {des}")

#create an obj/instance of the class
sam = employee()

# print(sam.salary)
# print(sam.id)
#sam.travel("Meerut")
print(type(sam))