## baseclass
class Employee():
 
    def __init__ (self, first, last, id, status):
        self.first = first 
        self.last = last 
        self.id = id 
        self.status = status
        self.fullname = '{} ' '{}' .format(self.first, self.last)
    def emp_retirement_app(emp_id):
        for emp in employee_list:
            if emp.id == emp_id:
                
                 return'''
                                        ID '{}', Your application has been sent to your email {}.{}@rakimail.com
                                        Check your email and follow the retirment procedures.
                                        
                                        


                                        ''' .format(emp.id, emp.first, emp.last)
                 
            
        return ''' 
                                                            Invalid ID!




        '''
    
    def get_ID_details(self):
               return f"First: {self.first}, Last: {self.last}, Status: {self.status}"
    
    
## subclass
class Developer (Employee):

    def fire (fire_ID):
       for emp in employee_list:
           if fire_ID == emp.id:
            fire_list.append (fire_ID)
            return "Application to fire " " {} " "({})" " is pending. " .format(emp.id, emp.fullname)
       return print ("""
                                                Invalid ID 
                    
                      
                      
                      """)
    
    
    def employee_status (emp_status):
       for emp in employee_list:
           if emp_status == emp.status:
               print (''' 
                                                {} {} 
''' .format(emp.fullname, emp.id))
        

    
    def dev_retirement_app(dev_id):
        for dev in developer_list:
            if dev.id == dev_id:
                
                 return'''
                                        ID '{}', Your application has been sent to your email {}.{}@rakimail.com
                                        Check your email and follow the retirment procedures.
                                        
                                        


                                        ''' .format(dev.id, dev.first, dev.last)
        return ''' 
                                                            Invalid ID!




        '''
    
                 
            

#subclass of subclass
class Manager (Developer):

    def fire_result (): 
       print (fire_list)
       manager_select = input ("Select ID number: ")
       if manager_select in fire_list:
          verdict = input("Would you like to fire? ('accept'/'decline'): ")
          if verdict == 'accept':
            fire_list.remove(manager_select)
            return "{} " "Has been fired!" .format(manager_select)
          elif verdict == 'decline':
             fire_list.remove(manager_select)
             return "{} " "Has been kept!" .format(manager_select)
       else:
          print ("ID not in fire list.")
          return
    def developer_status (dev_status):
       return "Developer is currently: " '{}' .format(dev_status.status)
    
    def man_retirement_app(man_id):
        for man in manager_list:
            if man.id == man_id:
                
                 return'''
                                        ID '{}', Your application has been sent to your email {}.{}@rakimail.com
                                        Check your email and follow the retirment procedures.
                                        
                                        


                                        ''' .format(man.id, man.first, man.last)
        return ''' 
                                                            Invalid ID!




        '''
    def developer_status (dev_status):
       for dev in developer_list:
           if dev_status == dev.status:
               print (''' 
                                                {} {} 
''' .format(dev.fullname, dev.id))
               
    def fire_result(): 
        pass



## current Employees
    
employee1 = Employee("John", "Doe", "001", "Active")
employee2 = Employee("Jane", "Doe", "002", "Inactive")
employee3 = Employee("Jim", "Beam", "003", "Active")
employee4 = Employee("Jill", "Valentine", "004", "Active")
employee5 = Employee("Jack", "Sparrow", "005", "Inactive")
employee6 = Employee("June", "Summer", "006", "Active")
employee7 = Employee("Jared", "Smith", "007", "Inactive")
employee8 = Employee("Jessica", "Jones", "008", "Active")
employee9 = Employee("Jeremy", "Clarkson", "009", "Inactive")
employee10 = Employee("Julia", "Roberts", "010", "Active")

## current Developers

developer1 = Employee ("Malak", "Mek", "123", "Active")
developer2 = Employee ("Mazen", "Nerd", "1324","Active" )
developer3 = Employee ("Raki", "Thefella", "000", "Active")
developer4 = Employee ("Jason", "Shanaon", "246", "Active")
developer5 = Employee ("Roba", "Tron", "808", "Inactive")
developer_fire = Employee ("Sam", "Bad", "454", "Inactive")

## current Managers

managers1 = Employee("Azima", "Salama", "111", "Active")
manager2 = Employee ("Adham", "Khalid", "222", "Active")
manager3 = Employee ("Yahia", "Shalaby", "555", "Inactive")


## Lists

fire_list = [developer_fire]

employee_list = [employee1, employee2, employee3, employee4, employee5,
                employee6, employee7, employee8, employee9, employee10, developer_fire]

developer_list = [developer1, developer2, developer3, developer4, developer5]

manager_list = [managers1, manager2, manager3]


 


## start of program


print ('''
                                     WELCOME TO ___ CORPORATION DATABASE''')

user_role = input ('''
                                        Role
                                    -1- Employee
                                    -2- Developer
                                    -3- Manager
 > ''')

#Employee Interface

if user_role == "1":
   while True:
    emp_pass = input(''' 
                                    Enter Employee password given through email when hired: 
> ''')
    while True:
     if emp_pass == "Emp556":
       print ("Welcome Employee")
       print ('''      
                                     Commands Page 
                                     -1- ID Number Search 
                                     -2- Retirment Application
                                     -3- Sign out 
             ''')
       emp_command = input("Enter Task: ")
     if emp_command == "1":
            while True:
                emp_id_search = input ('''
                                        Enter Employee ID: 
                                        (Enter '0' for Commands Page)
                                        > ''')
                found = False
                if emp_id_search == "0":
                 break
                for employee in employee_list:
                    if employee.id == emp_id_search:
                        print (employee.get_ID_details())
                        found = True
                        break
                if not found:
                    print("ID not found in current employee list")
     if emp_command == "2":
            while True:
             user_id = input ("""
                                 Input your ID:
                                 (Enter 0 For Back) 
                                 > """)
             if user_id == "0":
              break
            retirment_output = Employee.emp_retirement_app(user_id)
            print (retirment_output)
            break
     if emp_command == "3":
           print (''' 
                                    You have signed out, goodbye!
''')
           exit()
           
     else:
       print("password incorrect!")
       break
     

#Developer Interface

elif user_role == "2":
    while True:
        dev_pass = input(''' 
                                    Enter Developer password given through email when were hired: 
''')
        if dev_pass == "Dev334":
           while True:
            print ('''                                     Commands Page 
                                        -1- DeveloperID Search 
                                        -2- Retirment Application
                                        -3- Employee status check  
                                        -4- Fire Application
                                        -5- Sign out 
    ''' )
            dev_command = input("Enter Task: ")
            if dev_command == "1":
                while True:
                    dev_id_search = input ('''
                                        Enter Developer ID: 
                                        (Enter '0' for Commands Page)
                                        > ''')
                    found = False
                    if dev_id_search == "0":
                        break
                    for developer in developer_list:
                        if developer.id == dev_id_search:
                            print (developer.get_ID_details())
                            found = True
                            break
                    if not found:
                        print("ID not found in current employee list")
            elif dev_command == "2":
                    while True:
                        dev_retire_com = input ("Enter Your ID Number: ")
                        dev_retire_output = Developer.dev_retirement_app(dev_retire_com)
                        print (dev_retire_output)
                        break
            elif dev_command == "3":
                    dev_status_search = None
                    while dev_status_search != "0":
                        dev_status_search = input('''
                            -1- Active
                            -2- Inactive
                            -0- Back 
                        ''')
                        if dev_status_search == "1":
                            print(Developer.employee_status("Active"))
                        elif dev_status_search == "2":
                            print(Developer.employee_status("Inactive"))
            elif dev_command == "4":
                while True:
                    dev_fire_command = input (""" 
                                                Enter ID of Employee to fire:
                                                (Enter 0 for Back)
""")
                    fire_app_output = Developer.fire(dev_fire_command)
                    print (fire_app_output)
                    if dev_fire_command == "0":
                        break
            elif dev_command == "5":
                exit()
                
        else:
            print("password incorrect!")


##Manger Interface

if user_role == "3":
    while True:
        man_pass = input(''' 
                                    Enter Developer password given through email when were hired: 
''')
        if man_pass == "Man123":
           while True:
            print ('''                                     Commands Page 
                                        -1- ManagerID Search 
                                        -2- Retirment Application
                                        -3- Employee status check  
                                        -4- Developer status Check
                                        -5- Pending Fire Applications
                                        -6- Sign out 
    ''' )
            man_command = input("Enter Task: ")

            if man_command == "1":
                while True:
                    man_id_search = input ('''
                                        Enter Developer ID: 
                                        (Enter '0' for Commands Page)
                                        > ''')
                    found = False
                    if man_id_search == "0":
                        break
                    for manager in manager_list:
                        if manager.id == man_id_search:
                            print (manager.get_ID_details())
                            found = True
                            break
                    if not found:
                        print("ID not found in current employee list")
                    
            elif man_command == "2":
             while True:
                man_retire_com = input ("Enter Your ID Number: ")
                man_retire_output = Manager.man_retirement_app(man_retire_com) #solution
                if man_retire_output == ''' 
                                                            Invalid ID!




        ''':
                    print (man_retire_output)
                
                else: 
                    print (man_retire_output)
                    break
                    
            elif man_command == "3":
                while True:
                    emp_status_search = None
                    while emp_status_search != "0":
                        emp_status_search = input('''
                            -1- Active
                            -2- Inactive
                            -0- Back 
                        ''')
                        if emp_status_search == "1":
                            print(Developer.employee_status("Active"))
                        elif emp_status_search == "2":
                            print(Developer.employee_status("Inactive"))
                    if emp_status_search == "0":
                        break
            elif man_command == "4":
                while True:
                    dev_status_search = None
                    while dev_status_search != "0":
                        dev_status_search = input('''
                            -1- Active
                            -2- Inactive
                            -0- Back 
                        ''')
                        if dev_status_search == "1":
                            print(Manager.developer_status ("Active"))
                        elif dev_status_search == "2":
                            print(Manager.developer_status("Inactive"))
                    if dev_status_search == "0":
                        break
            elif man_command == "5":
                while True:
                    if not fire_list:
                        print("There are no pending fire applications.")
                        break

                    print("Employees pending fire applications:")
                    for emp in fire_list:
                        print(f"ID: {emp.id}, Name: {emp.first} {emp.last}")
                    
                    user_fire_input = input(''' 
                                            Input the ID of the employee to be fired:
                                            (Enter 0 for Back) 
                                            > ''')
                    selected_emp = next((emp for emp in fire_list if emp.id == user_fire_input), None)
                    if selected_emp:
                            # Implement the logic for firing the employee
                            # For example, removing the employee from fire_list and employee_list
                            fire_list.remove(selected_emp)
                            employee_list = [emp for emp in employee_list if emp.id != selected_emp.id]
                            print(f"Employee {selected_emp.id} - {selected_emp.first} {selected_emp.last} has been fired.")
                    else:
                            print("ID not found in fire list.")

            elif man_command == "6":
                exit ()
        else:
            "Password incorrect"