import sqlite3

# connecting to our super duper database
import pygame

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

    def playBandTracks(self, bandID):
        query = "SELECT track.trackPath, track.trackName " \
                "FROM band_track " \
                "JOIN track ON track.trackID = band_track.trackID " \
                "WHERE band_track.bandID = " + str(bandID)

        cursor = conn.execute(query)
        for row in cursor:
            file = row[0]
            print("->", row[1])
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(5)

    def playArtistTracks(self, bandID, artistID):
        query = "SELECT track.trackPath, track.trackName " \
                "FROM band_track " \
                "JOIN track ON track.trackID = band_track.trackID " \
                "OR track.artistID = " + str(artistID) + " " \
                "WHERE band_track.bandID = " + str(bandID)

        cursor = conn.execute(query)
        for row in cursor:
            file = row[0]
            print("->", row[1])
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(5)

class Band_Track:
    def __init__(self, bandID, trackID):
        self.bandID = bandID
        self.trackID = trackID
