from ffConnect import *

# Subroutine
def update_tblFilms():

    idField = input("Enter the filmID of the Film to be updated: ")
    # Provides us with the ID of 

    fieldName = input("Enter the: title, yearReleased, rating, duration or genre to be updated: ")

    fieldValue = input(f"Enter the value for {fieldName} field: ")

    #                                            PART 1
    # mySQL Syntax example: "Update tblFilms set title = 'Teletubbies' where filmID = 27"
                       
    print(fieldValue)

    fieldValue = "'"+fieldValue+"'" #This is incorrect placement. 
    print(fieldValue)

    # specfic record update: 
    "UPDATE tblFilms SET filmID or title or yearReleased or rating or duration or genre = {fieldValue} WHERE filmID = "
    dbffCursor.execute(f"UPDATE tblFilms SET {fieldName} = {fieldValue} WHERE filmID = {idField}")
    dbffCon.commit()

    print(f"Record {idField} updated in the Films Table")

if __name__ == "__main__":
    update_tblFilms()



