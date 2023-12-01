# file import command to import file modules. 
import readflix, addFlix, updateFlix, deleteFlix, ffReportsV2

def menuFFfile():
    with open("Film_Flix_DB/filmflixMenu.txt") as flixFile: #context manager 'with' operator 
        userMenu = flixFile.read()
    return userMenu

# print(menuFFfile())

#Creating the Flix Menu - SYSTEM CHECK 
def filmflixMenu():

    option = 0 # 0 initialises/ defines option var w/ integer data type
    optionsList = ["1","2","3","4","5","6"] #List data with string data type
    choiceMenu = menuFFfile() # initialise the menu file function with the choiceMenu variable

    # Create a while loop
    while option not in optionsList:
        #call/ invoke the menuFFfile function through the choiceMenu variable
        print(choiceMenu) # Displays options from Menu File.

        #re-assign the option variable with the input function
        option = input("Please enter an Option from the Flix Menu: ")

        #check if teh use input option variable is a match with 
        # anything in the optionsList. 
        if option not in optionsList:
            #print below function to execute the code below: 
            print(f"{option} This option is not a valid choice. Please choose 1 to 6. ")
    return option
# print(menuFFfile()) #Runs the function. 

# Creating a Boolean var called mainProgram
mainProgram = True

while mainProgram: 
       mainMenu = filmflixMenu()
   
       if mainMenu == "1":
           readflix.read_films()
   
       elif mainMenu == "2":
           addFlix.insert_tblFilms()
   
       elif mainMenu == "3":
           updateFlix.update_tblFilms()
   
       elif mainMenu == "4": 
           deleteFlix.delete_tblFilms()
   
       elif mainMenu == "5":
            ffReportsV2.reportSearch()
        #    reportsFF.tblFilms_reportsFF()
   
       else: # this should exit the program
           # by re-assigning the boolean variable of 'mainProgram' to False
        mainProgram = False
input ("Enter to quit the songs App")



        