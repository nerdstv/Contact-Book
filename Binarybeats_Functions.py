'''Here we define the search_by_name function and the add_contact function which we use in main.py

In all the functions we instantly reading and writting in text file to get new updates'''

def add_contact():                                                        #add function
    with open("Binarybeats_ALLContacts.txt","a") as file:                             
        a=input("Enter the contact name: ")                                # append the new contact in the file
        while True:
            b=input("Enter the phone number :")                            
            if len(b)==10 and type(int(b))==int:                          #checking wheater no has 10 digits or not                        
                print('Contact added successfully!!!')
                break
            else:
                print("Please enter a valid phone number!!")
                continue
        file.write(a + ',')
        file.write(b+'\n')

def search_by_name(n):                                                     #search function
    file=open("Binarybeats_ALLContacts.txt",mode='r')
    contacts={}
    li=[]                                                                  #instant reading and making dictionary from the text file
    for line in file: 
        x=line.split(",")
        a=x[0]
        b=x[1]
        c=len(b)-1
        b=b[0:c]
        contacts[a]=b
    file.close()                                                          
#searching in the created dictionary
    name_list=contacts.keys()
    if n in name_list:
        print("The phone number of ",n," is: ",contacts[n])
    else:
        print("Sorry this contact is not this in the directory.")






