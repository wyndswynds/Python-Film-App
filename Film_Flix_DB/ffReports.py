from ffConnect import *

    # 1. Print details of all films
    # 2. Print all films of a particular genre
    # 3. Print all films of a particular year
    # 4. Print all films of a particular rating

def reportSearch():
    # enter the name of the search field
    searchField = input("Which field would you Search: (filmId, title, rating, genre, yearReleased)?")
    # enter the value of the field you are searching through

    searchValue = input(f"Enter the value for the {searchField} you want to search ")
    print(f"The search value enter by user is {searchValue} ")

    searchValue = "'" + searchValue + "'"
    print(f" Amended search value {searchValue} ")

    dbffCursor.execute("SELECT * FROM tblFilms WHERE " + searchField + "=" + searchValue)
    dbffCon.commit()

    row = dbffCursor.fetchall()
    # casting(row) convert one datatype to another data type
    # casting the record(row) as a string to ensure we
    # are able to out put a msg
    # if the search string value not in databse
    strRow = str(row)
    if searchValue in strRow:  # .title()
        for record in row:
            print(record)
    else:
        print(
            f"The field {searchField} does not contain a {searchValue} in the database!"
        )


if __name__ =="__main__":
    reportSearch()
