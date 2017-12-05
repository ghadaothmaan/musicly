import sqlite3

# connecting to our super duper database
conn = sqlite3.connect('musicly.db')


class Artist:
    def __init__(self, artistID=0, name="", dateOfBirth=""):
        self.artistID = artistID
        self.name = name
        self.dateOfBirth = dateOfBirth

    def findID(self, artistName):
        values = [artistName]
        cursor = conn.execute("SELECT artistID FROM artist WHERE artistName = (?)", values)
        for row in cursor:
            artistID = row[0]
        return artistID

    # view all artists
    def viewArtists(self):
        cursor = conn.execute("SELECT artistName FROM artist")
        print("---------------------------------------------------------------------")
        print("\nArtists:")
        for row in cursor:
            print("*", row[0])

    # add new artist
    def addArtist(self, artistName, artistdob, bandID):
        values = [bandID, artistName, artistdob]
        conn.execute("INSERT INTO artist (bandID, artistName, artistDOB) VALUES (?, ?, ?)", values)
        conn.commit()

    # delete album
    def deleteArtist(self, artistID):
        values = [artistID]
        conn.execute("DELETE FROM artist WHERE artistID = (?)", values)
        conn.commit()

# testing
# a = Artist()
# a.viewArtists()
# a.addArtist("salma", "01/12/1996", 1)      # pass into it artist name and dob
# a.deleteArtist(5)                # pass into it artist id you want to delete
