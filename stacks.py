Employee = []
s = 'y'
while (s == 'y'):
    print("1.) PUSH"
        "2.) POP"
        "3.) DISPLAY")
    choice = int(input("Enter the choice: "))
    if (choice == 1):
        e_name = input("ENTER THE NAME OF EMPLOEE: ")
        e_id = int(input("ENTER THE ID OF EMPLOYEE: "))
        emp = (e_name,e_id)
        Employee.append(emp)
    elif(choice == 2):
        if (Employee == []):
            print("EMPTY STACK!!!")
        else:
            e_name,e_id = Employee.pop()
            print("THE DELTED ELEMENT IS",e_name,e_id)
    elif(choice== 3):
        i = len(Employee)
        while i>0:
            print(Employee[i-1])
            i= i-1
    else:
        print("INVALID CHOICE!!!")
    s = input("DO YOUWANT TO CONTINUE(y/n): ")