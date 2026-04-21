import gradio as gr

# ============================================================
# CISC 121 Project — Playlist Vibe Builder
# Author: Iris Xie
# Algorithm: Merge Sort
# ============================================================

class Log:
    step: int
    steps: list[str]

    def __init__(self):
        self.step = 0
        self.steps = []

    def add_step(self, text: str):
        self.step += 1
        self.steps.append(f"Step {self.step}: {text}")

    def get_steps(self):
        return self.steps

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

    def get_songs(self, sort_by: str | None, log: Log = Log()):
        if sort_by is None:
            return self.songs

        return sort(self.songs, sort_by, log)

def merge(left: list[Song], right: list[Song], key: str, log: Log):
    result: list[Song] = []

    log.add_step(f"merge() called with {str(len(left))} items in 'left' and {str(len(right))} items in 'right'")

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
            log.add_step("left_item or right_item was None, exiting while-loop")
            continue

        """
        Here, we're just accessing the attribute we want to organize
        the array by, in this case either 'energy' or 'duration'

        We would flip the comparison operator here later if we wanted to
        add the ability to sort in ascending or descending order. c:
        """
        left_item_attr = getattr(left_item, key)
        right_item_attr = getattr(right_item, key)
        
        if left_item_attr < right_item_attr:
            log.add_step(f"left_item's '{key}' attribute ({left_item_attr}) is less than right_item's '{key}' attribute ({right_item_attr}), removing right_item from right array and adding to result")
            result.append(left.pop(0))
            log.add_step(f"result has {len(result)} items")
        else:
            log.add_step(f"left_item's '{key}' attribute ({left_item_attr}) is greater than or equal to right_item's '{key}' attribute ({right_item_attr}), removing left_item from left array and adding to result")
            result.append(right.pop(0))

        """
        We're going to iterate over the remaining items in the array
        to ensure that any leftovers (which occurs if either left or right
        are depleted are then pushed to the end of the results array
        """

    log.add_step(f"{len(left)} leftovers in left")

    for item in left:
        log.add_step(f"appending leftover item from left to result")
        result.append(item)

    log.add_step(f"{len(right)} leftovers in right")

    for item in right:
        log.add_step(f"appending leftover item from right to result")
        result.append(item)

    return result

def split(array: list[Song], log: Log):
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

    log.add_step(f"{item_count} items in array, midpoint is {midpoint}")

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
            log.add_step(f"item at position {i} is less than the midpoint ({midpoint}), appending to left")
            left.append(item)
        else:
            log.add_step(f"item at position {i} is greater than or equal to the midpoint ({midpoint}), appending to right")
            right.append(item)

    log.add_step(f"left has {len(left)} items, right has {len(right)} items")

    return left, right
    

def sort(array: list[Song], key: str, log: Log):
    """
    This is our base case, when this condition
    is hit, our recursion stops.
    """
    if len(array) <= 1:
        return array
    
    left, right = split(array, log)

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
        left=sort(left, key, log),
        right=sort(right, key, log),
        key=key,
        log=log
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
    energy=58
))

playlist.add_song(Song(
    name="Toes", 
    artist="Glass Animals", 
    duration=255, 
    energy=35
))

playlist.add_song(Song(
    name="Vois sur ton chemin - Techno Mix",
    artist="BENNETT", 
    duration=178, 
    energy=100
))

playlist.add_song(Song(
    name="Yes I'm Changing",
    artist="Tame Impala", 
    duration=271, 
    energy=46
))

playlist.add_song(Song(
    name="Innerbloom",
    artist="Rüfüs Du Sol", 
    duration=578, 
    energy=52
))

with gr.Blocks() as demo:
    gr.Markdown("# Playlist Visualizer")
    sort_by = gr.Radio(["energy", "duration"], label="How would you like to sort your songs?", value="duration")

    gr.Markdown("## View Songs")

    @gr.render(inputs=sort_by)
    def render_songs(sort_by: str | None):
        log = Log()
        
        for song in playlist.get_songs(sort_by, log):
            with gr.Column():
                gr.Markdown(f"## {song.name}")
                with gr.Row():
                    gr.Markdown(f"by {song.artist}")
                    gr.Markdown(f"{str(round(song.duration / 60, 1))} minutes")
                    gr.Markdown(f"{str(song.energy)} energy points")

        gr.Markdown(f"## Detailed Breakdown")
        gr.Markdown("This is a breakdown of the steps that were involved in sorting the array.")

        for item in log.get_steps():
            with gr.Column():
                gr.Markdown(f"```{item}```")
            

demo.launch()
