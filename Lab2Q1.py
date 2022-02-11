#(String) Write a program that reads in an email address, e.g. joe@suss.edu.sg 
#Display the name and the organisation on separate lines. Example: 
 #Input email address: joe@suss.edu.sg  
 #Name is joe 
 #Organisation is suss.edu.sg  
 #Assume input is valid.



def lab2():
    email = input("Enter email: ")
    name, org = email.split("@")
    print("Name is", name.strip())
    print("Organisation is: ", org.strip())

lab2()