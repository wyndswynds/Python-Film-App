#STEP 2 - CREATING tables with values already connected 
# with 

from ffConnect import * # import the ffConnect.py module 

dbffCursor.execute(""" 
CREATE TABLE "tblFilms" (
    "filmID"  INTEGER,
    "title" TEXT,
    "yearReleased" INTEGER,
    "rating" INTEGER,
    "duration" INTEGER,
    "genre" TEXT
)""")


# Note:
# CRUD: Create Read Update Delete.
# Only one table in the database with records, which is all 
# you need for this project.
# Database name filmflix.db
# Table name tblfilms
# filmID(integer), title(text), yearReleased(integer),rating(text),
# duration(integer),genre(text)
