class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        # Increment the count of songs and add the song to the respective lists and counts
        Song.count += 1
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        # Increment the count of songs
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Add new genres to the genres list, only if they are not already present
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Add new artists to the artists list, only if they are not already present
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Add to the genre_count histogram
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # Add to the artist_count histogram
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Example usage
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
some_song = Song("Some Song", "Drake", "Rap")
another_song = Song("Another Song", "Beyonce", "Pop")

# Accessing class attributes and methods
print(Song.count)  # Output: 3
print(Song.genres)  # Output: ['Rap', 'Pop']
print(Song.artists)  # Output: ['Jay-Z', 'Drake', 'Beyonce']
print(Song.genre_count)  # Output: {'Rap': 2, 'Pop': 1}
print(Song.artist_count)  # Output: {'Jay-Z': 1, 'Drake': 1, 'Beyonce': 1}
