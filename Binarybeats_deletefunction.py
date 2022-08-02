'''This is delete function .At  first this finction open file and make a using contacts of text file dictionary
and then check wheater contact exist or not in dictionary 
if yes then it deletes the contact and write the updated dictionary in that file'''

def delete_function(contacts):
    while True :
        print("****************")
        inp_temp = input('Next(N)  Back(B)\n\nEnter : ')
        print("****************")
        if inp_temp == 'N' or inp_temp == 'n':
            with open("Binarybeats_ALLContacts.txt",mode='r') as file:     #making dictionary
                for line in file:
                    x=line.split(",")
                    a=x[0]
                    b=x[1]        
                    b=b.rstrip()
                    contacts[a]=b
                print("Available Contacts",contacts)
                while True :
                    var = input('Enter the contact name to delete : ')
                    if var in contacts.keys() :                     # checking the number exits or not
                        contacts.pop(var)
                        print("\nContact deleted successfully" )
                        print("Available Contacts",contacts)
                        break
                    else :
                        print("No Contact  found !! please enter a valid name")
                with open('Binarybeats_ALLContacts.txt', 'w') as file:
                    for i in contacts.keys():                   #writing the updated one
                        file.write(i+',')
                        file.write(contacts[i]+'\n')
        
        elif inp_temp == 'B' or inp_temp == 'b':
            break

        else :
            print('Invalid input!!! Please enter a valid input')
