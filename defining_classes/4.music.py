class Music:
    def __init__(self, Title, artist, Lyrics):
        self.Title = Title
        self.artist = artist
        self.Lyrics = Lyrics

    def print_info(self):
        return f'This is "{self.Title}" from "{self.artist}"'

    def play(self):
        return self.Lyrics


song = Music("Title", "Artist", "Lyrics")

print(song.print_info())
print(song.play())
