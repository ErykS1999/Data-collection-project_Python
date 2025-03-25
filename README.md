# Managing data between py & json


## Top tips ( from an amateur) when creating a local database in python using json:

1- Always remember the PEP-8 method when writing your code. The document needs appropriate indentation as well as clear readability. 

  ```
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



  ```
2- When working in classes, make sure to group every different section into methods(functions). This will help you not to get lost whilst working on your project.

  ```
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

  ```
3- Find learn to master try and except:
   During this small project, I had some challenges with adapting the right techniques when it comes to try and except. Remember that 
   the 'exception' clause as below handles all of the general problems. Make sure to mention in your try and except the potential errors that can come up
   such as ValueError or FileNotFound and adapt the print message to each. 

  ```
        try:
            with open(filename,'w',encoding='UTF-8') as f:
                json.dump(self.safe_data,f,indent=4)
            print(f"The data has been successfully saved to {filename}")
        except Exception as e: # exception handles all of the general problems 
            print(f"An error has occured while saving this file: {e}")
  ```

Instead try this:

  ```
        try:
            with open('database.json','w',encoding='UTF-8') as f:
                json.dump(data,f,indent=4)
        except(FileNotFoundError,json.JSONDecodeError):
            print("You have some error in reading the code. ")
  ```


4- Repeat even the basics. In this project, I had some issues with extracting specific data from the dictionaries within the json files. 
   I had an empty gap within my brain which forced me to ask myself a question 'do I know how to extract the data from the dictionaries?'.
   The answer was 'no', So i opened a new file and practiced until I understood it again. Always come back to the basics and ask yourself rhetorical question.


5- Over-complication.
   Never add more than you need to. I had the tendancy to add 'else' clauses everytime the 'if' came up but that is not always necessary.
   Go over the code couple of times and ask yourself 'how can I make this simpler'? 




## Please create pull requests if you feel that something is done wrong. I love to learn from my mistakes. 
