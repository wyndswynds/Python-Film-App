from ffConnect import *
# from deleteFlix import * #commented out section of import documentation.
# If it delteImport is commented in. It creates hierachy issues. 

#subroutine
def read_films():
    
    # Select all records available -> 
    dbffCursor.execute("SELECT * from tblFilms")
    # execute is an interface function between python and sql.
    
    # ALT. search queries: 
    # dbffCursor.execute("select * from tblFilms where yearReleased <2000")
    # dbffCursor.execute("select * from tblFilms order by duration desc")


    # fetch/ get all songs from table 
    allRecords = dbffCursor.fetchall()

    for eachRecord in allRecords:
        print(eachRecord)

if __name__ == "__main__":
    read_films()
    # delete_tblFilms()