import sqlite3

# connecting to our super duper database
conn = sqlite3.connect('musicly.db')


class Playlist:
    def __init__(self, playlistID=0, name="", description=""):
        self.playlistID = playlistID
        self.name = name
        self.description = description

    def findID(self, playlistName):
        values = [playlistName]
        cursor = conn.execute("SELECT playlistID FROM playlist WHERE playlistName = (?)", values)
        for row in cursor:
            playlistID = row[0]
        return playlistID

    # view all playlists
    def viewPlaylists(self):
        cursor = conn.execute("SELECT playlistName, COUNT(playlist_track.trackID) "
                              "FROM playlist "
                              "LEFT JOIN playlist_track "
                              "ON playlist_track.playlistID = playlist.playlistID "
                              "GROUP BY (playlist.playlistID)")
        print("---------------------------------------------------------------------")
        print("Playlists:")
        for row in cursor:
            print(row[0], "\t tracks:", row[1])

    # add new playlist
    def addPlaylist(self, name, description):
        values = [name, description]
        conn.execute("INSERT INTO playlist (playlistName, playlistDescription) VALUES (?, ?)", values)
        conn.commit()

    # view one specific playlist with its tracks by freaking order
    def viewPlaylistTracks(self, playlistID, orderBy, option):
        value = [playlistID]
        # values = [playlistID, orderBy, option]
        cursor = conn.execute("SELECT playlistName, playlistDescription "
                              "FROM playlist "
                              "WHERE playlistID = (?)", value)
        print("---------------------------------------------------------------------")

        for row in cursor:
            print(row[0], "\n", row[1], "\n")

        query = "SELECT track.trackName, track.trackLength " \
                "FROM playlist_track " \
                "JOIN track ON track.trackID = playlist_track.trackID " \
                "WHERE playlist_track.playlistID = " + str(playlistID) + " ORDER BY " + str(orderBy) + " " + str(option)

        cursor = conn.execute(query)
        for row in cursor:
            print(row[0], "\t Duration: ", row[1])

    # delete playlist
    def deletePlaylist(self, playlistID):
        values = [playlistID]
        conn.execute("DELETE FROM playlist WHERE playlistID = (?)", values)
        conn.commit()

# testing
# p = Playlist()
# p.viewPlaylists()
# p.viewPlaylistTracks(2)
# p.addPlaylist("name", "desc")     # pass into it playlist name and description
# p.deletePlaylist(8)            # pass into it playlist id you want to delete


class Playlist_Track:
        def __init__(self, playlistID=0, trackID=0):
            self.playlistID = playlistID
            self.trackID = trackID

        # add new tracks to playlist
        def addTrackToPlaylist(self, playlistID, trackID):
            values = [playlistID, trackID]
            conn.execute("INSERT INTO playlist_track (playlistID, trackID) VALUES (?, ?)", values)
            conn.commit()

        # remove track from playlist
        def removeTrackFromPlaylist(self, playlistID, trackID):
            values = [playlistID, trackID]
            conn.execute("DELETE FROM playlist_track WHERE playlistID = (?) AND trackID = (?)", values)
            conn.commit()

# testing
# pt = Playlist_Track()
# pt.addTrackToPlaylist(2, 3)    # pass into it playlist id and track id
# pt.removeTrackFromPlaylist(2, 3)

