from Album import Album
from Artist import Artist
from Band import Band
from Playlist import Playlist, Playlist_Track
from Track import Track

playlist = Playlist()
artist = Artist()
album = Album()
track = Track()
band = Band()
pt = Playlist_Track()


def viewPlaylistOptions():
    choice = input("\n1. View Playlist\t\t2. Add Playlist\n3. Delete Playlist\t\t4. Back to Home\n>> ")
    # play tracks ----> DONE!
    return choice


def viewArtistOptions():
    choice = input("\n1. View Band\t\t2. Add Band\n3. Delete Band\t\t4. Back to Home\n>> ")
    # view band artists ----> DONE!
    # TODO: play tracks in band, singles
    return choice


def viewAlbumOptions():
    choice = input("\n1. View Album\t\t2. Add Album\n3. Delete Album\t\t4. Back to Home\n>> ")
    # play tracks -----> DONE!
    return choice


def viewTrackOptions():
    choice = input("\n1. View Track\t\t2. Delete Track\n3. Play\t\t\t\t4. Back to Home\n>> ")
    return choice
# -------------------------------------------------------------------------------------------------------------------- #


# our humpty dumpty main function
def viewHome():
    print("---------------------------------------------------------------------")
    print("Welcome to Musicly!")
    choice = input("1. Playlists\n2. Bands\n3. Albums\n4. Tracks\n5. Quit\n>> ")

    # --------------------------------------------------------------------------------------------------------- #
    # playlists
    if choice == "1":
        while True:
            playlist.viewPlaylists()
            choice = viewPlaylistOptions()

            # view specific playlist
            if choice == "1":
                playlistName = input("Playlist Name: ")
                playlistID = playlist.findID(playlistName)

                print("\nView Tracks by...")
                orderBy = input("1. Name\t\t\t2. Artist\n3. Album\t\t4. Genre\n5. Release Date\n>> ")

                # this qualifies as dirty work
                if orderBy == "1":
                    orderBy = "track.trackName"
                elif orderBy == "2":
                    orderBy = "track.trackFeaturedArtist"
                elif orderBy == "3":
                    orderBy = "track.albumID"
                elif orderBy == "4":
                    orderBy = "track.trackGenre"
                elif orderBy == "5":
                    orderBy = "track.trackReleaseDate"

                opt = input("1. Ascending\t2. Descending\n>> ")

                if opt == "1":
                    opt = "asc"
                elif opt == "2":
                    opt = "desc"

                playlist.viewPlaylistTracks(playlistID, orderBy, opt)

                option = input("\n1. Play\t\t\t\t2. Shuffle\n3. Add Track\t\t4. Remove Track\n5. Back\n>> ")

                # play entire playlist
                if option == "1":
                    # test play -----> DONE!
                    track.playPlaylistTracks(playlistID, orderBy, opt)

                # play entire playlist in shuffle mode
                elif option == "2":
                    track.playShuffle(playlistID)

                # add track to this playlist
                elif option == "3":
                    track.viewTracks()
                    trackName = input("Track Name: ")
                    trackID = track.findID(trackName)
                    pt.addTrackToPlaylist(playlistID, trackID)

                # remove track from this playlist
                elif option == "4":
                    trackName = input("Track Name: ")
                    trackID = track.findID(trackName)
                    pt.removeTrackFromPlaylist(playlistID, trackID)

            # add new playlist
            elif choice == "2":
                playlistName = input("Playlist Name: ")
                playlistDescription = input("Playlist Description: ")
                playlist.addPlaylist(playlistName, playlistDescription)

            # delete existing playlist
            elif choice == "3":
                playlistName = input("Playlist Name: ")
                playlistID = playlist.findID(playlistName)
                playlist.deletePlaylist(playlistID)

            # back to main menu
            elif choice == "4":
                viewHome()
    # --------------------------------------------------------------------------------------------------------- #
    # bands
    elif choice == "2":
        while True:
            band.viewBands()
            choice = viewArtistOptions()

            # view band artists
            if choice == "1":
                bandName = input("\nBand Name: ")
                bandID = band.findID(bandName)
                band.viewBandArtists(bandID, bandName)

                option = input("\n1. Play Band\t\t2. Play Artist\n2. Add Artist\t\t4. Delete Artist\n5. Back\n>> ")
                # play songs
                if option == "1":
                    band.playBandTracks(bandID)
                elif option == "2":
                    artistName = input("Artist Name: ")
                    artistID = artist.findID(artistName)
                    band.playArtistTracks(bandID, artistID)
                # add artist
                elif option == "3":
                    artistName = input("Artist Name: ")
                    artistDOB = input("Artist Date of Birth: ")
                    bandID = band.findID(bandName)
                    artist.addArtist(artistName, artistDOB, bandID)

                # delete artist
                elif option == "4":
                    artistName = input("Artist Name: ")
                    artistID = artist.findID(artistName)
                    artist.deleteArtist(artistID)

            # add band
            elif choice == "2":
                bandName = input("\nBand Name: ")
                band.addBand(bandName)

            # delete band
            elif choice == "3":
                bandName = input("Band Name: ")
                bandID = band.findID(bandName)
                band.deleteBand(bandID)

            # back to main menu
            elif choice == "4":
                viewHome()
    # --------------------------------------------------------------------------------------------------------- #
    # albums
    elif choice == "3":
        while True:
            album.viewAlbums()
            choice = viewAlbumOptions()

            # view specific album
            if choice == "1":
                albumName = input("\nAlbum Name: ")
                albumID = album.findID(albumName)
                album.viewAlbumTracks(albumID, albumName)

                # test play -----> DONE!
                option = input("\n1. Play\t\t2. Back\n>> ")
                if option == "1":
                    track.playAlbum(albumID)

            # add new album
            elif choice == "2":
                albumName = input("Album Name: ")
                numOfSongs = input("Number of Songs: ")

                bandName = ""
                option = input("\n1. View Bands\t\t2. Create Band\n>> ")

                # view bands
                if option == "1":
                    band.viewBands()
                    bandName = input("\nBand Name: ")

                # add new band
                elif option == "2":
                    bandName = input("\nBand Name: ")
                    band.addBand(bandName)

                print(bandName)
                bandID = band.findID(bandName)

                album.addAlbum(albumName, bandID, numOfSongs)

            # delete existing album
            elif choice == "3":
                albumName = input("Album Name: ")
                albumID = album.findID(albumName)
                album.deleteAlbum(albumID)

            # back to main menu
            elif choice == "4":
                viewHome()
    # --------------------------------------------------------------------------------------------------------- #
    # tracks
    elif choice == "4":
        while True:
            track.viewTracks()
            choice = viewTrackOptions()

            if choice == "1":
                trackName = input("\nTrack Name: ")
                trackID = track.findID(trackName)
                track.viewTrack(trackID)

                option = input("\n1. Play\t\t2. Back\n>> ")
                if option == "1":
                    track.playTrack(trackID)

            elif choice == "2":
                trackName = input("Track Name: ")
                trackID = track.findID(trackName)
                track.deleteTrack(trackID)

            elif choice == "3":
                option = input("\n1. Play All\t\t2. By Genre\n3. Back\n>> ")

                if option == "1":
                    track.playAll()

                elif option == "2":
                    genre = input("\nGenre: ")
                    # test -------> DONE!
                    track.playGenre(genre)

            elif choice == "4":
                viewHome()
    # --------------------------------------------------------------------------------------------------------- #
    # quit
    elif choice == "5":
        raise SystemExit

    return choice


# this is our super duper musicly program w/o gui and a flow that gives you cancer
# but this is what they asked for and this is what they'll get
viewHome()
