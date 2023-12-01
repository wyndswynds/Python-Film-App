from ffConnect import *

    # 1. Print details of all films
    # 2. Print all films of a particular genre
    # 3. Print all films of a particular year
    # 4. Print all films of a particular rating

def reportSearch():
    # enter the name of the search field
    searchField = input("Which field would you Search: (filmID, title, rating, duration, genre, yearReleased)?")
    # enter the value of the field you are searching through

    # if searchField  == "yearReleased" or searchField == "filmID" or searchField == "duration":
    if searchField  == "filmID":
            print(searchField)

            yrInput = input(f"Enter the Value for {searchField}: ")
            dbffCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {yrInput}")
            anID = dbffCursor.fetchone()

            if anID == None: 
                print(f"No record exist with {anID} in the database!")

            else: 
                for aRecord in anID:
                    print(aRecord)

    elif searchField  == "yearReleased":
        yrR = input(f"Enter the Value for {searchField}: ")
        print(searchField)
        dbffCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = {yrR}")
        yrRecords = dbffCursor.fetchall()
        for yrRecord in yrRecords:
                print(yrRecord)

    elif searchField  == "duration":
        filmDuration = input(f"Enter the Value for {searchField}: ")
        dbffCursor.execute(f"SELECT * FROM tblFilms WHERE duration = {filmDuration}")
        movieDuration = dbffCursor.fetchall()
        for minDuration in movieDuration:
                print(minDuration)
                 
            # dbffCursor.execute("SELECT * FROM tblFilms WHERE " + searchField + "=" + numInput)
            # dbffCursor.execute(f"SELECT * FROM tblFilms WHERE {searchField} = {numInput}")
            # print(f"The search value enter by user is {numInput} ")
            # numericRecords = dbffCursor.fetchall()
            # if numInput in numericRecords:
            #     for aNumericRecord in numericRecords:
            #         print(aNumericRecord)
            # else:
            #     print(f"The field {searchField} does not contain a {numInput} in the database!")

    else: 
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
            print(f"The field {searchField} does not contain a {searchValue} in the database!")

if __name__ =="__main__":
    reportSearch()
