#def yogesh(n):
#   if(n>17):
#       d=2*(n-17)
#       print(d)

#   else:
#       d=17-n
#       print(d)

#a=int(input("enter the number"))

#yogesh(a)

#def yogesh(a):
#    if(100<a<1000):
#        print("number is between 100 and 1000")
#    elif(1000<a<2000):
#        print("number is between 1000 and 2000")
 #   else:
 #       print("number is beyond 2000")
    




#a=int(input("enter the number"))
#yogesh(a)

#a=input("enter the string")

#d=a[::-1] or d="".join(reverse(a))
#print(d)

 

#a=input("enter the number")
#lower=0
#upper=0
   
#for i in a:
#    if(i.islower()):
#        lower=lower+1
#    else:
#        upper=upper+1

        
#print("number of lower case letters ",lower)
#print("number of upper case letters ",upper)
'''
lst=[]
n=int(input("enter the number of elements"))


for i in range(n):
    ele=int(input("enter the elements"))
    lst.append(ele)

for i in range(n):
    if(lst[i]%2==0):
        print("Even numbers in the list are:",lst[i])
'''   


'''
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display_attributes(self):
        # Using vars() to get a dictionary of the instance attributes
        attributes = vars(self)
        
        print("Student Attributes:")
        for attribute, value in attributes.items():
            print(f"{attribute}: {value}")

# Example usage
student = Student(student_id="102323035", student_name="Yogesh Aggarwal", student_class="undergraduate")
student.display_attributes()
'''

'''
def unique(list1):

    # insert the list to the set
    a = set(list1)


    for x in a:
        print (x)
        


# driver code
list1 = [10, 20, 10, 30, 40, 40]
print("the unique values from 1st list is")
unique(list1)


list2 = [1, 2, 1, 1, 3, 4, 3, 3, 5]
print("\nthe unique values from 2nd list is")
unique(list2)

'''
















































    





 


