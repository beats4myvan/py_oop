class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album.name not in self.albums:
            self.albums.append(album)
            return f'Band {self.name} has added their newest album {album.name}.'
        else:
            return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name):
        for album in self.albums:
            if album_name == album.name:
                if album.published == True:
                    return f'Album has been published. It cannot be removed.'
                else:
                    self.albums.remove(album)
                    return f'Album {album_name} has been removed.'
        return f'Album {album_name} is not found.'

    def details(self):
        band_details = f'Band {self.name}\n'
        for i in self.albums:
            band_details += f'{i.details()}\n'
            return band_details
