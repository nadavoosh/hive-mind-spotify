class SpotifyPlaylist(object):
    def __init__(self, title, tracks):
        self.spotify = None
        self.tracks = tracks
        self.uris = ','.join([t.id for t in self.tracks])
