from tkinter import *
import os
#the star means everything










def register_user():  #what happens with the information collected
  username_info = username.get()
  password_info = password.get()
  #assigns values from the entrys to information that then be put in txt

  file = open(username_info  , "w")
  #the w puts it into write mode
  #file is also a variable
  file.write(username_info + "\n")
  file.write(password_info)
  file.close()
  #write file

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  #clears field after users has clicked register

  Label(screen1,text="Registartion Complete!",fg="green",font=("calibri", 11)).pack()


def login_verify():

  
  username1 = username_verify.get()
  password1 = password_verify.get()

  #assigns input of fields to variables for later use 

  username_entry1.delete(0,END)
  password_entry1.delete(0,END)

  #clears field

  list_of_files = os.listdir()
  #lists all files in the current directory

  if username1 in list_of_files:
    file1=open(username1, "r")
    #r is for read
    verify = file1.read().splitlines()
    #reads file splitlines ignore the /n enter in the file
    if password1 in verify: 
     Label(screen2,text="Login Sucess",fg="green",font=("calibri", 11)).pack()
    else:
      Label(screen2,text="Password Not Recognised",fg="red",font=("calibri", 11)).pack()
  else:
    Label(screen2,text="Username not Recognised",fg="red",font=("calibri", 11)).pack()
    

    
  #outcome is assigned to a varaible 








def register():  #this is for the field or entry
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")
  #now starting to create entries
  global username
  global password
  global username_entry
  global password_entry

  username = StringVar()
  password = StringVar()

  #shows that variable is a string variable

  Label(screen1, text="Please Enter Details Below ").pack()
  Label(screen1, text="").pack()

  Label(screen1, text="Username *").pack()
  username_entry = Entry(screen1, textvariable=username)
  username_entry.pack()

  #Assigns lable entry to variable

  Label(screen1, text="Password *").pack()
  password_entry = Entry(screen1, textvariable=password)
  password_entry.pack()

  Label(screen1, text="").pack()

  #button to register
  Button(screen1, text="Register", width=10, height=1,
         command=register_user).pack()

  #entrys are the input boxes lables are the text above them


def login():
  global screen2
  screen2= Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x250")

  global username_verify
  global password_verify

  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2, text= "Please enter your credentails below").pack()
  Label(screen2, text="").pack()

  Label(screen2, text="Username *").pack()
  username_entry1= Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  
  Label(screen2, text = "").pack()
  

  Label(screen2, text="Password *").pack()
  password_entry1= Entry(screen2, textvariable = password_verify)
  password_entry1.pack()

  Label(screen2, text = "").pack()

  Button(screen2, text ="Login", width=10, height =1 ,command = login_verify).pack()
  
  

def main_screen():
  global screen
  #globalises so it can be acessed else where in code
  screen = Tk()
  #using tkinker
  screen.geometry("300x250")
  #how big it is
  screen.title("Notes 1.0")
  #This fucntion takes notes
  Label(text="Notes 1.0",
        bg="grey",
        width="300",
        height="2",
        font=("Calibri", 13)).pack()
  #how it looks fonts etc

  Label(text="").pack()
  #This leaves a line

  Button(text="Login", height="2", width="30", command=login).pack()
  Label(text="").pack()
  Button(text="Register", height="2", width="30", command=register).pack()

  #the command = at the end associates buttons with the fucntions above

  #Defining buttons

  screen.mainloop()


main_screen()
