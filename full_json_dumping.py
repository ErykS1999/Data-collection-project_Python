import json


class Security:

    def __init__(self,safe_data=None):
        self.safe_data = safe_data if safe_data else {}



    def workforce(self):
        

        self.safe_data = {
            "mike":"jambo1",
            "sam":"sun1",
            "eric":"sushi2",
            "pat":"cati",
            "bob":"dogi1"
        }

        

    def save_new_file(self,filename = "employee_data.json"):
        if not self.safe_data:
            print("No data to save. Run workforce() first.")
            return
        try:
            with open(filename,'w',encoding='UTF-8') as f:
                json.dump(self.safe_data,f,indent=4)
            print(f"The data has been successfully saved to {filename}")
        except Exception as e: # exception handles all of the general problems 
            print(f"An error has occured while saving this file: {e}")


    def admin_login(self):

        while True: 
            admin_login = input("Admin username:  ").strip()

            if not self.safe_data:
                print("Error:No data found")
                return
            
            if admin_login in self.safe_data:
                admin_password = input(f"Password for {admin_login}: ").strip()
                if self.safe_data[admin_login] == admin_password:
                    print(f"\n Welcome in {admin_login}! \n ")
                    break
                else:
                    print("Incorrect password.Try again")
            
            else:
                print("Inwalid username. Try again")



try:
    with open('database.json','r',encoding='UTF-8') as f:
        data = json.load(f)
except(FileNotFoundError,json.JSONDecodeError):
    data = {}


class Database:

    def __init__(self,data):
        self.data = data




    def information(self):

        print("This is the data which we currently have about your database")
        print(self.data)

    
    def input_information(self):
        ask = input(" What is your username on the website?  ")
        if ask not in self.data:
            self.data[ask] = {}
            print(f"\nDear {ask}, your information will be put through. ")
        else:
            print("\nWe already have this username.")
                

    def save_information(self):
        try:
            with open('database.json','w',encoding='UTF-8') as f:
                json.dump(data,f,indent=4)
        except(FileNotFoundError,json.JSONDecodeError):
            print("You have some error in reading the code. ")

    
    def add_more_users(self):
        exit = ()
        while exit != 'q':
            more_users = input("Would you like to add more users? yes/no ")
            if more_users =='yes':
                user_input = input("What is your username:  ")
                self.data[user_input] = {}

            else:
                print("END")
                break

    def delete_information(self):
        while True:
            print(f"Currently we have the following datasets {self.data}\n")
            who_delete = input("Would you like to delete some data? yes/no  ")
            if who_delete =='no':
                print("\n We should continue then. ")
                break
            else:
                delete_what = input("What user would you like to delete?  ")
                if delete_what in self.data:
                    del self.data[delete_what]
                    print(f"\n{delete_what} has been deleted.\n ")
                    break
                else:
                    print("No data as such exists, maybe a spelling error? Try again please. ")
    
    def change_information(self):
        print(json.dumps(self.data, indent=4))
        while True:
            option = input("\nWould you like to change some information in the database? As shown above? yes/no  ")
            if option.lower() == 'yes':
                name_database = input("\nWhat is the name you would like to change?  ")
                if name_database in self.data:
                    print(f'Current data:{json.dumps(self.data[name_database],indent=4)}')
                    
                    for key in ["phone","broadband","internet","opinion"]:
                        if key in self.data[name_database]:
                            new_value = input(f"Enter new value for {key} (press enter to keep current value: {self.data[name_database][key]}) ")
                            if new_value:
                                self.data[name_database][key] = new_value if key != "internet" else int(new_value)
                    print("Information updated successfully")
                
                else:
                    print("No name exists, please try again.")
            
            else:
                print("Great lets move on to the next question.")
                break


    def populate_database(self):
        print(self.data)
        choose = input("\n From the list above, please choose your data.  ")
        if choose not in self.data:
            print("You are not listed in the database, please try again later.")
        
        else:
            print(f"Great, we will add the data to {choose}")
            
            phone = input("What phone do you currently have?  ")
            self.data[choose]["phone"] = phone

            broadband = input("Thanks! In what broadband are you currently with?  ")
            self.data[choose]["broadband"] = broadband

            try:
                internet = int(input("Added. Now how much internet do you have with your plan?  "))
                self.data[choose]["internet"] = internet
            except(ValueError):
                print("Make sure to type numbers not letters!")
                return internet
                
            opinion = input("What is your opinion about your contract, please let us know!  ")
            self.data[choose]["Personal opinion"] = opinion





admin = Security()
admin.workforce()
admin.save_new_file()
admin.admin_login()


my_project = Database(data)
my_project.change_information()
my_project.delete_information()
my_project.information()
my_project.input_information()
my_project.populate_database()
my_project.add_more_users()





my_project.save_information()

    