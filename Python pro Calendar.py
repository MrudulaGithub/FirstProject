from time import sleep,strftime

User_first_name = "Mrudula"
calendar = {}

def welcome():
    print "Welcome, " + User_first_name + "."
    print "Calendar opening..."
    sleep(1)
    print "Today is: " + strftime("%A %B %d, %Y")
    print "Current time is: " + strftime("%H:%M:%S")
    sleep(1)
    print "What would you like to do?"

def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = raw_input("A to add, U to update, V to view, D to delete, X to exit: ")
        user_choice = user_choice.upper()

        if user_choice == 'V':
            if len(calendar.keys()) < 1:
                print "Calendar Empty"
            else:
                print calendar

        elif user_choice == 'U':
            date = raw_input("What date?")
            update = raw_input("Enter the update: ")
            calendar[date] = update
            print "Update successful"
            print calendar

        elif user_choice == 'A':
            event = raw_input("Enter event: ")
            date = raw_input("Enter date: ")
            if (len(date) > 10 ) or (int(date[6:]) < int(strftime("%Y"))):
                print "Invalid Input"
                try_again = raw_input("Try again Y for yes, N for no: ")
                try_again = try_again.upper()
                if try_again == 'Y':
                    continue
                else:
                    start = False
            else:
                calendar[date] = event
                print "Event added"
                print calendar

        elif user_choice == 'D':
            if len(calendar.keys()) < 1:
                print "Calendar empty"
            else:
                event = raw_input("What Event?")
                for date in calendar.keys():
                    if calendar[date] == event:
                        del calendar[date]
                        print "Event deleted"
                        print calendar
                    else:
                        print "Incorrect Event"

        elif user_choice == 'X':
            start = False

        else:
            print "Invalid input"
            break


start_calendar()