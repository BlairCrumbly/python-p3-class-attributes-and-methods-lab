

class Song:
    #todo
    #init name artist and genre
    #create isntance
    #add count in top of class at 0, then the incrementor where the song is created
    #add classmethod to access class variable
    #* Class "Song" in song.py keeps count of Songs for each genre. - KeyError: 'Rap'

    count = 0
    genres = {}
    artists = []
    songsperartist = {}
    

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.artists.append(self.artist)
        
        if genre in Song.genres:
            Song.genres[genre] += 1
        else:
            Song.genres[genre] = 1
        
        if artist in Song.songsperartist:
            Song.songsperartist[artist] += 1
        else:
            Song.songsperartist[artist] = 1

    @classmethod
    def get_count(cls):
        return cls.count
    @classmethod
    def get_genre_count(cls):
        return cls.genres
    @classmethod
    def get_artists(cls):
        return cls.artists
    @classmethod
    def get_song_per_artist(cls):
        return cls.songsperartist

TestSong = Song("99 Problems", "Jay Z", "Rap")
TestSong2 = Song("No Role Modelz", "J. Cole", "Rap")
TestSong3 = Song("Snooze", "SZA", "R&B")
TestSong4 = Song("No more hiding", "SZA", "R&B")
TestSong5 = Song("Banned in D.C.", "Bad Brains", "Punk")

print(Song.get_count())
print(Song.get_genre_count())
print(Song.get_artists())
print(Song.get_song_per_artist())
