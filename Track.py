import random
import sqlite3
import pygame

# connecting to our super duper database
conn = sqlite3.connect('musicly.db')


class Track:
    def __init__(self, trackID=0, name="", bandID="", featuredArtist="",
                 albumID=0, releaseDate="", genre="", lyrics="", length=0):
        self.trackID = trackID
        self.name = name
        self.bandID = bandID
        self.featuredArtist = featuredArtist
        self.albumID = albumID
        self.releaseDate = releaseDate
        self.genre = genre
        self.lyrics = lyrics
        self.length = length

    # view all tracks
    def viewTracks(self):
        query = "SELECT trackName, trackLength, trackGenre FROM track"
        cursor = conn.execute(query)
        print("---------------------------------------------------------------------")
        print("Tracks: ")
        for row in cursor:
            print("*", row[0], '\t\t\t', row[2], '\t\t\t', row[1])

    # view track description
    def viewTrack(self, trackID):
        value = [trackID]
        cursor = conn.execute("SELECT * FROM track WHERE trackID = (?)", value)
        print("---------------------------------------------------------------------")
        for row in cursor:
            print("Title:", row[2])
            print("Featured artist:", row[3])
            print("Release date:", row[4])
            print("Genre:", row[5])
            print("Length:", row[6])
            print("Lyrics:", row[7], "\n")

    def findID(self, trackName):
        values = [trackName]
        cursor = conn.execute("SELECT trackID FROM track WHERE trackName = (?)", values)
        for row in cursor:
            trackID = row[0]
        return trackID

    # play a track
    def playTrack(self, trackID):
        values = [trackID]
        cursor = conn.execute("SELECT trackPath "
                              "FROM track "
                              "WHERE trackID = (?)", values)
        for row in cursor:
            file = row[0]
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(5)

    # play all tracks
    def playAll(self):
        values = []
        cursor = conn.execute("SELECT trackPath, trackName FROM track", values)
        for row in cursor:
            file = row[0]
            print("->", row[1])
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            pygame.mixer.pause()
            while pygame.mixer.music.get_busy():
                pygame.time.delay(5)

    # play tracks grouped by genre
    def playGenre(self, genre):
        values = [genre]
        cursor = conn.execute("SELECT trackPath, trackName FROM track WHERE trackGenre = (?)", values)
        for row in cursor:
            file = row[0]
            print("->", row[1])
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(5)

    # play entire album
    def playAlbum(self, albumID):
        values = [albumID]
        cursor = conn.execute("SELECT trackPath, trackName FROM track WHERE albumID = (?)", values)
        for row in cursor:
            file = row[0]
            print("->", row[1])
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(5)

    # play entire playlist
    def playPlaylistTracks(self, playlistID, orderBy, opt):
        query = "SELECT track.trackPath, track.trackLength, track.trackName " \
                "FROM playlist_track " \
                "JOIN track ON track.trackID = playlist_track.trackID " \
                "WHERE playlist_track.playlistID = " + str(playlistID) + " ORDER BY " + str(orderBy) + " " + str(opt)

        cursor = conn.execute(query)
        for row in cursor:
            file = row[0]
            print("->", row[2])
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(5)

    # -------------------------------------------------------------------------------------- #
    # play in shuffle mode
    def playShuffle(self, playlistID):
        query = "SELECT track.trackPath, track.trackName " \
                "FROM playlist_track " \
                "JOIN track ON track.trackID = playlist_track.trackID " \
                "WHERE playlist_track.playlistID = " + str(playlistID)
        cursor = conn.execute(query)
        trackList = []
        for row in cursor:
            trackPath = row[0]
            trackList.append(trackPath)

        random.shuffle(trackList)
        trackList = list(map(str, trackList))

        for i in trackList:
            print("->", "msh 3rfa ageb el esm")
            pygame.mixer.init()
            pygame.mixer.music.load(i)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(5)

    # -------------------------------------------------------------------------------------- #
    # delete track
    def deleteTrack(self, trackID):
        values = [trackID]
        conn.execute("DELETE FROM track WHERE trackID = (?)", values)
        conn.commit()

    def getOrderedTracks(self, orderBy, option):
        query = "SELECT trackName FROM track ORDER BY " + orderBy + " " + option
        # print(query)
        cursor = conn.execute(query)
        for row in cursor:
            print("*", row[0])


# testing
# t = Track()
# t.viewTracks()
# t.playTrack(1)         # pass into it track id
# t.playWhatever("albumID", "1")
# t.deleteTrack(3)    # pass into it track id you want to delete
# t.getOrderedTracks("trackName", "desc")
# t.playShuffle()
# t.play_songs(test)

