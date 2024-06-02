#Here lets use our class(student datatype) to create an object,
#-here "object is an instance of class(datatype)" 

from studentclass import student


student1 = student("prabhas", "commerce",False ,"st.jhons", 3.4 )
student2 = student("prashantneel", "commerce",False ,"little flower", 4.4 )

print(student1.is_on_probation)
print(student2.gpa)

print(student1.honor_roll())