# Modules #
import os, warnings

###############################################################################
class SongCollection(object):

    def __init__(self, file_path):
        handle      = open(input_path, 'rb')
        header_line = handle.next()
        self.songs  = [Song(self, *line.strip('\n').split(',')) for line in handle]
        # Post parsing #
        for i in range(1, len(self.songs)):
            c_song = self.songs[i-1]
            n_song = self.songs[i]
            c_song.next_song = n_song

    def total_time(self):
        return sum(s.duration for s in self.songs)

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        return "A collection with %d songs" % len(self)

    def __nonzero__(self):
        return False

    def __getitem__(self, num):
        return self.songs[num]

    def __iter__(self):
        return iter([1,2,3,4])

###############################################################################
class Song(object):
    """A class used to complete the exercise of day 4 in the
    python EBC course of year 2016."""

    def __init__(self, owner, title, artist, duration):
        # Base parameters #
        self.title  = title
        self.artist = artist
        self.owner  = owner
        # Attempt conversion to int #
        try:
            self.duration = int(duration)
        except ValueError:
            warnings.warn("The song '%s' had a non-number duration. It's set to zero." % self.title)
            self.duration = 0
        # Check duration is not negative #
        if self.duration < 0:
            raise Exception("You can't have a negative duration on song: " + self.title)

    def pretty_duration(self):
        secs     = self.duration
        mins     = secs / 60
        hours    = mins / 60
        return "%02i hours %02i minutes %02i seconds" % (hours, secs % 60, mins % 60)

    @property
    def next_song(self):
        my_index =[i,s for s in enumerate(self.owner.songs) if s.name == self.name][0][1]
        if len(self.owner.songs) == my_index: return
        return self.owner.songs[my_index+1]

    def play(self):
        """Idea: Use webbrowser instead to be cross-platform."""
        # Build the URL #
        base_url = "https://www.youtube.com/results?search_query="
        complete_url = base_url + self.title.replace(' ','+')
        # Depends on your operating system #
        import webbrowser
        webbrowser.open(complete_url)

###############################################################################
# Get the path to the CSV file #
home = os.environ['HOME']
input_path = home + "/lulu_mix_16.csv"

# Parse it #
collection = SongCollection(input_path)

# Insert into database #
