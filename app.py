import gradio as gr

# ============================================================
# CISC 121 Project — Playlist Vibe Builder
# Author: Iris Xie
# Algorithm: Merge Sort
# ============================================================

class Song:
    """
    By using a class here, we can validate the values of each "instance" of a Song!
    """
    def __init__(
            self,
            name: str,
            artist: str,
            energy: int,
            duration: int
        ):

        if energy > 100:
            raise ValueError(f"Energy level '{energy}' is too high, it must be between 0 and 100")
        
        if energy < 0:
            raise ValueError(f"Energy level '{energy}' is too low, it must be between 0 and 100")

        if duration < 0:
            raise ValueError(f"The provided duration '{duration}' is not valid")
            
        self.name = name
        self.artist = artist
        self.energy = energy
        self.duration = duration

class Playlist:
    songs: list[Song] = []

    def __init__(self):
        self.songs = []
    
    def add_song(self, song: Song):
        self.songs.append(song)

    def get_songs(self, sort_by: str | None):
        if sort_by is None:
            return self.songs

        return sort(self.songs, sort_by)

def merge(left: list[Song], right: list[Song], key: str):
    result: list[Song] = []

    """
    Until one of the arrays are empty, we will continue to compare
    the first items of each array which allows us to push the smallest
    ones into our 'result' list first.
    """
    while len(left) > 0 and len(right) > 0:
        left_item = left[0]
        right_item = right[0]

        """
        If our left and right arrays are not even (i.e., left = [1], right = [2, 3])
        then we want to escape the while-loop. We'll need to clean this up later so
        that we don't lose items.
        """
        if left_item is None or right_item is None:
            continue

        """
        Here, we're just accessing the attribute we want to organize
        the array by, in this case either 'energy' or 'duration'

        We would flip the comparison operator here later if we wanted to
        add the ability to sort in ascending or descending order. c:
        """
        if getattr(left_item, key) < getattr(right_item, key):
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

        """
        We're going to iterate over the remaining items in the array
        to ensure that any leftovers (which occurs if either left or right
        are depleted are then pushed to the end of the results array
        """

    for item in left:
        result.append(item)

    for item in right:
        result.append(item)

    return result

def split(array: list[Song]):
    left: list[Song] = []
    right: list[Song] = []

    """
    Above, we created two arrays. These are going to be the arrays
    we're going to return, so we'll use them to split items from the
    original array into. We'll get the midpoint by floor dividing the
    length of the array by 2.
    """
    item_count = len(array)
    midpoint = item_count // 2

    """
    Now we're going to iterate over each item, and if the
    index of the item is less than the midpoint we push it
    to the "left", otherwise, we push it to "right" - so a
    list like [1, 5, 7, 9] would become left = [1, 5] and
    right = [7, 9]
    """
    for i in range(item_count):
        item = array[i]

        if i < midpoint:
            left.append(item)
        else:
            right.append(item)

    return left, right
    

def sort(array: list[Song], key: str):
    """
    This is our base case, when this condition
    is hit, our recursion stops.
    """
    if len(array) <= 1:
        return array
    
    left, right = split(array)

    """
    This is where the magic happens! We recursively call
    "sort" on both halves of the array, which will result
    in a series of arrays that are 1 in length. Once the base
    case is hit, "merge" will be called on each and the two
    items from both sides will be compared and then combined.
    This process is repeated until all the arrays are merged
    and the playlist is sorted.
    """
    return merge(
        sort(left, key),
        sort(right, key),
        key
    )


"""
Some sample songs from my playlist will be added
to this, would recommend checking them out.
"""
playlist = Playlist()

playlist.add_song(Song(
    name="Chainsmoking",
    artist="Jacob Banks",
    duration=202,
    energy=42
))

playlist.add_song(Song(
    name="Toes", 
    artist="Glass Animals", 
    duration=255, 
    energy=30
))

playlist.add_song(Song(
    name="Vois sur ton chemin - Techno Mix",
    artist="BENNETT", 
    duration=178, 
    energy=100
))

with gr.Blocks() as demo:
    gr.Markdown("# Playlist Visualizer")
    sort_by = gr.Radio(["energy", "duration"], label="How would you like to sort your songs?", value="duration")

    @gr.render(inputs=sort_by)
    def render_songs(sort_by: str | None):
        for song in playlist.get_songs(sort_by):
            with gr.Row():
                gr.Markdown("## " + song.name)
                gr.Text(song.artist + " • " + str(song.duration) + " • " + str(song.energy))

demo.launch()
