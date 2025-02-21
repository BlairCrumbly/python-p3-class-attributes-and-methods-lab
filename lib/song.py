

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
    song_genre_count = []
    

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.artists.append(self.artist)
        
        if genre in Song.genres:
            Song.genres[genre] += 1
            Song.
        else:
            Song.genres[genre] = 1

    @classmethod
    def get_count(cls):
        return cls.count
    @classmethod
    def get_genre_count(cls):
        return cls.genres
    
    @classmethod
    def get_artists(cls):
        return cls.artists

TestSong = Song("99 Problems", "Jay Z", "Rap")
TestSong2 = Song("No Role Modelz", "J. Cole", "Rap")

print(Song.get_count())
print(Song.get_genre_count())
print(Song.get_artists())
