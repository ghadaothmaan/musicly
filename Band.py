import sqlite3

# connecting to our super duper database
conn = sqlite3.connect('musicly.db')


class Band:
    def __init__(self, bandID=0, name=""):
        self.bandID = bandID
        self.name = name

    def findID(self, bandName):
        values = [bandName]
        cursor = conn.execute("SELECT bandID FROM band WHERE bandName = (?)", values)
        for row in cursor:
            bandID = row[0]
        return bandID

    def viewBands(self):
        cursor = conn.execute("SELECT bandName FROM band")
        print("\n---------------------------------------------------------------------")
        print("Bands:")
        for row in cursor:
            print(row[0])

    def viewBandArtists(self, bandID, bandName):
        values = [bandID]
        cursor = conn.execute("SELECT artistName "
                              "FROM artist "
                              "WHERE bandID = (?)", values)
        print("---------------------------------------------------------------------")
        print(bandName)
        for row in cursor:
            print("*", row[0])

    def addBand(self, bandName):
        values = [bandName]
        conn.execute("INSERT INTO band (bandName) VALUES (?)", values)
        conn.commit()

    def deleteBand(self, bandID):
        values = [bandID]
        conn.execute("DELETE FROM band WHERE bandID = (?)", values)
        conn.commit()


class Band_Track:
    def __init__(self, bandID, trackID):
        self.bandID = bandID
        self.trackID = trackID
