
# [1] The aim of the app: Create an application for starting fund-raise projects in
# Egypt.

import re
from datetime import datetime

# def check_password(passwd ,confrm_passwd):
#     if(passwd == confrm_passwd):


# ###############################Registration Function#####################################
def register_fun(fname, lname, password, confirmPassword, email, phone):
    writter = open("users.txt", "a")
    while(True):
        if((confirmPassword == password) and (re.match(r"^[a-zA-Z][a-zA-z0-9\.]+\@[a-z-A-z]+\.[a-zA-Z]{3}", email)) and (re.match(r"^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{5}$", phone))):
            writter.write(fname+"|")
            writter.write(lname+"|")
            writter.write(password+"|")
            writter.write(confirmPassword+"|")
            writter.write(email+"|")
            writter.write(phone+"\n")
            print("\n Congratulations\n")
            writter.close()
            break
        else:
            print('Not Valid Passowrld or email or phone')
            break
# Login Function

# ###############################login Function#####################################
def login_fun(email, passwd):
    with open("users.txt", "r") as reader:
        lines = reader.readlines()
        for line in lines:
            password = line.split('|')[2]
            Email = line.split("|")[4]
            fname = line.split("|")[0]
            if(passwd == password and email == Email):
                while True:
                    user_choise = int(input('''
                    ****** Select Option *******
                    1- Create Project 
                    2- Delete Project 
                    3- Show Projects
                    4- exit
                    '''))
                    if(user_choise == 1):
                        print("******** Create ***********")
                        P_title = input("Enter Project Title : ")
                        P_details = input("Enter Project details:")
                        P_total_target = input("Enter Total Target:")
                        my_string = str(input('Enter start date(yyyy/mm/dd): '))
                        P_strat_date = datetime.strptime(my_string, "%Y/%m/%d")
                        my_string2 = str(input('Enter end date(yyyy/mm/dd): '))
                        P_end_date = datetime.strptime(my_string2, "%Y/%m/%d")
                        print(P_strat_date)
                        print(P_end_date)
                        create_Project(fname,P_title , P_details , P_total_target , P_strat_date , P_end_date)

                    elif(user_choise == 2):
                        print("******** Delete ***********")
                        delete_project(fname)
                    elif(user_choise == 3):
                        print("******** Show all projects ***********")
                        show_project(fname)
                    elif(user_choise == 4):
                        break
                    else:
                        print("Invalied Option : ")

                break
        print(" Not A member...You Need to Register first!")
        print(passwd)
        print(email)
        print(fname)
        return fname

# ############################### Create Project Function##############################
# Full Done
def create_Project(username ,title , details , totalTarget , startDate , endDate):
     writter = open("projects.txt", "a")
     while(True):
        if((startDate < datetime.now()) and (endDate > startDate)):
            writter.write(username+"|")
            writter.write(title+"-")
            writter.write(details+"-")
            writter.write(totalTarget+"-")
            writter.write(str(startDate)+"-")
            writter.write(str(endDate)+"\n")
            print("\n Congratulations\n")
            print("Donnnne")            
            writter.close()
            break
        else:
            print('Error Date !')
            break
# ############################### Create Project Function##############################
# Done except user message if he don't have project
def show_project(username):
     with open("projects.txt", "r") as reader:
        lines = reader.readlines()
      
        for line in lines:
            # print(line.split("|")[0] , username)
            if(line.split("|")[0] == username):
              print(line+"\n")
              break
        # print("You Don't have any Project Yet")

# ############################### Delete Project Function############################## 
# full done 
def delete_project(username):
   with open("projects.txt", "r") as f:       
    # read data line by line  
    data = f.readlines() 

   # open file in write mode 
    with open("projects.txt", "w") as f:       
         for line in data :           
        # condition for data to be deleted 
          if (line.split("|")[0] != username):  
            f.write(line) 
            print("deleted!")


while True:
    user_choise = int(input('''
    ******* Main Menu *******
     ----- Select Option -----
    1- Enter 1 to register
    2- Enter 2 to login
    3- Enter 3 to exit
    '''))
    if(user_choise == 1):
        print("******** Register ***********")
        firstName = input("Enter Your First Name : ")
        lastName = input("Enter Your Last Name : ")
        password = input("Enter Your password : ")
        confirm_password = input("Confirm password : ")
        email = input("Enter Your Email : ")
        phone = input("Enter Your Phone : ")
        register_fun(firstName, lastName, password,
                     confirm_password, email, phone)
        print('-'*50)
    elif(user_choise == 2):
        print("******** Login ***********")
        email = input("Enter Your Email : ")
        passwd = input('Enter Your Password : ')
        x = login_fun(email, passwd)
        print(x)
    elif(user_choise == 3):
        break
    else:
        print("Invalied Option : ")
