from ffConnect import *

# subroutine for delete 
def delete_tblFilms():

    idField = input(" Enter the Track ID of the record to be deleted: ")

    # Delete from songs where Song ID is
    dbffCursor.execute(f"Delete from songs where Song ID = {idField}")
    dbffCon.commit()

    print(f"Record {idField} deleted from the songs table")

if __name__ == "__main__":
     delete_tblFilms()
# delete_tblFilms()