class Song(object):
    """Sing, sing sing"""
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

bulls_on_the_parade = Song(["The rally around the family", "with pockets full of shells"])

bulls_on_the_parade.sing_me_a_song()
