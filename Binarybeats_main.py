'''This is the main program of our project 
Here we take the inputs from the users and execute accordingly

execution flow
                                                                        
importing functions ---> welcome ---> Taking input after giving options untill user logout
            _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _         
            |           |           |           |           |           |           |
        search      create new     view all     delete      edit      about us    logout
                                    contacts                             |
                                                                    Discription and individual contribution

'''

try:                                                        #Handle error that modules are not in same folder
    import Binarybeats_Functions as fcn
    import Binarybeats_deletefunction as dele
    import Binarybeats_editfunction as edit 
except ModuleNotFoundError :
    print('Some files missing !!! Please keep all files in same folder')


print('''                                            
             \ \      / /   __   | |   ___    ___   _ __ ___      ___ 
              \ \ /\ / /  / _ \  | |  / __/  / _ \  | '_ ` _ \   / _ \ 
               \ V  V /  |  __/  | | | (_   | (_) | | | | | | | |  __/ 
                \_/\_/    \___|  |_|  \___\  \___/  |_| |_| |_|  \___|  ''')
contacts = {}                                       #creating empty dictionary
diaries_name = contacts.keys()
try:                      # Checking wheather text file exist or not 
    with open("Binarybeats_ALLContacts.txt",mode='r') as file:     #-----|
        for line in file:                               #-----|
            x=line.split(",")                           #-----|---->Reading text which contain contact details
            a=x[0]                                      #-----|     and convert and add then to the empty dictionary
            b=x[1]                                      #-----|
            b=b.rstrip()                                #-----|
            contacts[a]=b                               #-----|
except FileNotFoundError :
    print('Some files missing !!! Please keep all files in same folder')


while True :
    print("=======================================================================================================")
    input1 = input('''Search a contact                entre 1\nCreate a new contact            enter 2\nView all contacts               enter 3\nDelete a contact                enter 4\nEdit a contact                  enter 5\nAbout US                        enter 6                    
To Logout                       enter (L)\n=======================================================================================================\nEnter : ''')
    print("=======================================================================================================")
    if input1 == '1' :                      #takin input after giving options and then differentiate the input according to conditions
        while True:
            
            input2=input("Search by name(enter N)\nGo in previous menu(enter B)\n\nEnter : ")
            
            if input2=='N' or input2=='n':
                #print("***************")
                input3=input("Enter the Name of the contact : ")
                #print("***************")
                fcn.search_by_name(input3)      #using search function available in Functions.py
            elif input2=='B'or input2=='b':
                break
            else:
                print("Invalid input!!!\n Please enter correct input!")
    elif input1 == '2':
        fcn.add_contact()       #using add function available in Functions.py
    elif input1=='3': 
        file=open("Binarybeats_ALLContacts.txt",mode='r')                      #instant reading and making dictionary from the text file
        contacts={}
        li=[]
        for line in file: 
            x=line.split(",")
            a=x[0]
            b=x[1]
            b = b.rstrip()
            contacts[a]=b
        print(contacts)
        file.close()
    elif input1=='4':
        y = dele.delete_function(contacts)      #using delete function from delete_function.py
    elif input1=='5':
        y = edit.edit_function(contacts)        #using delete function from delete_function.py
    elif input1=='6':
        about=open("Binarybeats_aboutus.txt", mode='r')       #Reading about us from the about_us.txt
        text=about.read()
        print(text)
        temp = input('Enter any : ')            #give a pause in excecution so user can read about us properly 
    elif input1=='L' or input1=='l':            #exit from loop to close program
        print('Logout!!! Thanks')
        break
    else:
        print('Invalid input!!! ; Please enter a valid input')  #For unwanted input




