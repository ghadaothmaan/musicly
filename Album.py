import sqlite3

# connecting to our super duper database
conn = sqlite3.connect('musicly.db')


class Album:
    def __init__(self, albumID=0, title="", numOfSongs=0):
        self.albumID = albumID
        self.title = title
        self.numOfSongs = numOfSongs

    def findID(self, albumName):
        values = [albumName]
        cursor = conn.execute("SELECT albumID FROM album WHERE albumTitle = (?)", values)
        for row in cursor:
            albumID = row[0]
        return albumID

    # view all albums
    def viewAlbums(self):
        # print(self.title, "tracks:", self.numOfSongs)
        # print(self.album)
        cursor = conn.execute("SELECT albumTitle, albumNumOfSongs FROM album")
        print("---------------------------------------------------------------------")
        print("Albums: ")
        for row in cursor:
            print("*", row[0], "\t tracks:", row[1])

    # view specific album
    def viewAlbumTracks(self, albumID, albumName):
        print("---------------------------------------------------------------------")
        print(albumName)
        values = [albumID]
        cursor = conn.execute("SELECT trackName, trackLength "
                              "FROM track "
                              "WHERE albumID = (?)", values)
        for row in cursor:
            print("*", row[0], "\t Duration: ", row[1])

    # add new album
    def addAlbum(self, title, bandID, numOfSongs):
        values = [bandID, title, numOfSongs]
        conn.execute("INSERT INTO album (bandID, albumTitle, albumNumOfSongs) VALUES (?, ?, ?)", values)
        conn.commit()

    # delete album
    def deleteAlbum(self, albumID):
        values = [albumID]
        conn.execute("DELETE FROM album WHERE albumID = (?)", values)
        conn.commit()

# testing
# a = Album()
# a.viewAlbum(1, "Seventh Heaven")
# a.viewAlbums()
# a.addAlbum("test",3, 1)      # pass into it album name and number of songs
# a.deleteAlbum(8)         # pass into it album id you want to delete
