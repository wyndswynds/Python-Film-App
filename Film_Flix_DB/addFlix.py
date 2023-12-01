# STEP 3 - Update data 

# Creating import function from ddConnect
from ffConnect import * 

# Creating data input subroutine: 
def insert_tblFilms():
    
    #filmID is primary key autoincrement - no entry/ update required
    # ask for user Input for: Title, Year Released, Rating, Duration, Genre
    filmID = int(input("Enter Film ID to be Added: "))
    title = input("Enter Title: ")
    yearReleased = int(input("Enter Year Released: "))
    rating = input("Enter Rating: ")
    duration = int(input("Enter Duration: "))
    genre = input("Enter Genre:  ")

    # #dbCursor.execute used to input data into Films table. 
    # dbffCursor.execute("INSERT INTO tblFilms(filmID, title, yearReleased, rating, duration, genre) VALUES(?, ?, ?, ?, ?, ?)",  
    #                    (filmID, title, yearReleased, rating, duration, genre))
    
    dbffCursor.execute("INSERT INTO tblFilms VALUES(?, ?, ?, ?, ?, ?)",  
                       (filmID, title, yearReleased, rating, duration, genre))

    dbffCon.commit()

    print(f"{title} Inserted into the songs table")

if __name__ == "__main__":
    insert_tblFilms()

# -----------------------------------------------

