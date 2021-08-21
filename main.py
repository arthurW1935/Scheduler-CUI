from tabulate import tabulate
from datetime import datetime as dt
import pickle

class Scheduler:
  def __init__(self,name,table=[["Serial No.","Task/Work/Event","Time"]]):
    self.schedule_table = table
    self.name = name

  def add_event(self):
    task = input("Please enter the name of the event which you want to add...\n")
    print("When is this event?")
    date_event = input("Enter the date in DD/MM/YYYY format:\n(date, month and year should be separated by '/')\n")
    time_event = input("Enter the time in HH:MM format \n(hours and minutes should be separated by ':')\n")
    try:
      date_event = [int(i) for i in date_event.split("/")]
      time_event = [int(i) for i in time_event.split(":")]
      thetime = dt(date_event[2],date_event[1],date_event[0],time_event[0],time_event[1])
      if thetime<dt.now():
        print("The date and time you entered is invalid!")
        raise ValueError
      self.schedule_table.append([(len(self.schedule_table)),task,thetime])
      print("Added Successfully!\n")
    except:
      print("Incorrect Input! Event could not be added! Please Try Again!\n")
  
  def delete_event(self):
    self.show()
    theevent = input("Enter the serial number of the event which you want to delete\n")
    for i in range(len(self.schedule_table)):
      if str(self.schedule_table[i][0])==theevent:
        del self.schedule_table[i]
        print("Deleted Successfully!\n")
    else:
      print("The serial number was not found! pLease try again!\n")
  
  def modify_event (self):
    self.show()
    serial = input("Enter the serial number of the event which you want to modify\n")
    for i in range(len(self.schedule_table)):
      if str(self.schedule_table[i][0])==serial:
        print("Press 1 to update the name of the event\nPress 2 to update the timings of the event")
        inp = input()
        if inp == '1':
          newname = input("Enter the name of the event: ")
          self.schedule_table[i][1]=newname
          print("Modified Successfully!\n")
        elif inp=='2':
          date_new = input("Enter the date in DD/MM/YYYY format:\n(date, month and year should be separated by '/')\n")
          time_new = input("Enter the time in HH:MM format \n(hours and minutes should be separated by ':')\n")
          try:
            date_new = [int(x) for x in date_new.split("/")]
            time_new = [int(x) for x in time_new.split(":")]
            thetime = dt(date_new[2],date_new[1],date_new[0],time_new[0],time_new[1])
            if thetime<dt.now():
              print("The date and time you entered is invalid!")
              raise ValueError
            self.schedule_table[i][2]==thetime
            print("Modified Successfully!\n")
            break
          except Exception as e:
            print("Incorrect Input! Event could not be modified! Please try again!")
            break
    else:
      print("The serial number was not found! pLease try again!")

  def show(self):
    print(tabulate(self.schedule_table, headers='firstrow', tablefmt='fancy_grid'))
    print()

  def exit(self):
    with open('user.txt','w') as user:
      user.write(self.name)
    with open('userlist.txt','wb') as schedulesave:
      pickle.dump(self.schedule_table,schedulesave)


if (__name__ == "__main__"):
  print("Welcome to Scheduler!")
  with open('user.txt') as w:
    user = w.read()
    if user=='':
      name = input("Please enter your name: ")
      person = Scheduler(name)
    else:
      print("Hello,",user)
      with open("userlist.txt",'rb') as table_saved:
        person = Scheduler(user,table=pickle.load(table_saved))
      
  while True:
    print()
    print("Press 1 to add event in schedule")
    print("Press 2 to delete event in schedule")
    print("Press 3 to modify event in schedule")
    print("Press 4 to see all the events in schedule")
    print("Press E to EXIT") 
    user_input = input()
    if user_input == '1':
      person.add_event()
    elif user_input == '2':
      person.delete_event()
    elif user_input == '3':
      person.modify_event()
    elif user_input == '4':
      person.show()
    elif user_input.lower()=='e':
      person.exit()
      print("Thank You for using Scheduler!")
      break
