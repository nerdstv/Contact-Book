'''This is edit function  it firstly open file and making dictionary
and then doing the update in dictionary and then write the updated diction in that file'''

def edit_function(contacts):
    with open("Binarybeats_ALLContacts.txt",mode='r') as file:         #creating dictionary by reading a text file
        for line in file:
            x=line.split(",")
            a=x[0]
            b=x[1]        
            b=b.rstrip()
            contacts[a]=b
        print(contacts)
        while True :
            var = input('Enter the contact name to edit : ')
            if var in contacts.keys():                         #checking wheater contact exits or not
                print("Existing Contact Number --> ",var,';',contacts[var])
                while True :
                    inp_num = input('Enter the new number : ')
                    if len(inp_num) == 10:
                        contacts[var] = inp_num                 #it update the dictionary
                        print("\nContact edit successfully" )
                        print(contacts)
                        with open('Binarybeats_ALLContacts.txt', 'w') as file:     #if update occur then writng the update one         
                            for i in contacts.keys():
                                file.write(i+',')
                                file.write(contacts[i]+'\n')
                        break
                    else :
                        print('Please enter a valid number!!!')
                break
            else :
                print("Conatct didn't found !! please enter a valid name")
