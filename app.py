import gradio as gr

# ============================================================
# CISC 121 Project — Playlist Sorter
# Author: Iris Xie
# Algorithm: Merge Sort
# ============================================================

"""
Using a Log class here, to visualize all the steps that are 
taking place when sorting each song in the playlist. Log.add_step 
throughout to indicate which steps require notation for the user.
"""
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

        """
        Here, we assert error messages for raised value errors such as if the energy level
        is not in between 0 and 100, or if the duration of the song is invalid, as in less
        than 0 to validate the inputs.
        """
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
    songs: list[Song]

    def __init__(self):
        self.songs = []

    """
    Adds a song to this "instance's" songs array
    """
    def add_song(self, song: Song):
        self.songs.append(song)

    """
    Clears all songs from this playlist
    """
    def clear(self):
        self.songs = []

    def get_songs(self, sort_by: str | None, log: Log = Log()):
        """
        If we don't pass in a sort key, we return the songs in the
        same order that `add_song` was called for this playlist instance
        """
        if sort_by is None:
            return self.songs

        """
        Otherwise, this is where we call sort and pass in the
        sort_by, which triggers the recursive sorting. We pass
        in log to ensure that log items are all added to the list.
        """
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
    This is where the magic happens! We recursively call "sort" on both 
    halves of the array, which will result in a series of arrays that are
    1 in length. Once the base case is hit, "merge" will be called on 
    each and the two items from both sides will be compared and then combined.
    This process is repeated until all the arrays are merged and the playlist
    is sorted.
    """
    return merge(
        left=sort(left, key, log),
        right=sort(right, key, log),
        key=key,
        log=log
    )

"""
Helper that builds a Playlist from a sequence of Songs.
Each test case factory calls this so it returns a Playlist instance.
"""
def _make_playlist(*songs: Song) -> Playlist:
    p = Playlist()
    for s in songs:
        p.add_song(s)
    return p

"""
Each test case is a factory keyed by a string identifier that returns a Playlist.
Selecting a different key just swaps the input playlist — the rest of the UI is unchanged.
Factories that create invalid songs will raise a ValueError, which the render function
catches and displays as an error boundary.
"""
test_cases: dict[str, callable] = {
    "empty": lambda: _make_playlist(),
    "default": lambda: _make_playlist(
        Song(name="Chainsmoking", artist="Jacob Banks", duration=202, energy=58),
        Song(name="Toes", artist="Glass Animals", duration=255, energy=35),
        Song(name="Vois sur ton chemin - Techno Mix", artist="BENNETT", duration=178, energy=100),
        Song(name="Yes I'm Changing", artist="Tame Impala", duration=271, energy=46),
        Song(name="Innerbloom", artist="Rüfüs Du Sol", duration=578, energy=52),
    ),
    "long_duration": lambda: _make_playlist(
        Song(name="The Longest Song Ever", artist="Test Artist", energy=50, duration=10000),
    ),
    "negative_duration": lambda: _make_playlist(
        Song(name="Backwards Song", artist="Test Artist", energy=50, duration=-1),
    ),
    "negative_energy": lambda: _make_playlist(
        Song(name="Low Energy Song", artist="Test Artist", energy=-10, duration=200),
    ),
    "energy_over_100": lambda: _make_playlist(
        Song(name="Hyper Song", artist="Test Artist", energy=101, duration=200),
    ),
    "duplicates": lambda: _make_playlist(
        Song(name="Echo", artist="Test Artist", energy=70, duration=200),
        Song(name="Echo", artist="Test Artist", energy=70, duration=200),
        Song(name="Quiet Intro", artist="Test Artist", energy=30, duration=150),
    ),
}

"""
Here, gradio comes into play to render the UI.
"""
with gr.Blocks() as demo:
    playlist_state = gr.State(test_cases["default"]())
    error_state = gr.State(None)

    gr.Markdown("# Playlist Visualizer")

    with gr.Row():
        test_case = gr.Radio(list(test_cases.keys()), label="Test case", value="default")
        sort_by = gr.Radio(["energy", "duration"], label="How would you like to sort your songs?", value="duration")

    gr.Markdown("## View Songs")

    text_area = gr.TextArea(label="Add New Songs", placeholder="Song Name,Artist Name,duration,energy")
    add_button = gr.Button("Add New Songs")

    def on_test_case_change(key):
        try:
            return test_cases[key](), None
        except ValueError as e:
            return None, str(e)

    test_case.change(fn=on_test_case_change, inputs=[test_case], outputs=[playlist_state, error_state])

    def on_add_click(csv_text, playlist):
        try:
            name, artist, duration, energy = [p.strip() for p in csv_text.split(",")]
            new_playlist = _make_playlist(*playlist.songs)
            new_playlist.add_song(Song(name, artist, int(energy), int(duration)))
            return new_playlist, None
        except ValueError as e:
            return playlist, str(e)

    add_button.click(fn=on_add_click, inputs=[text_area, playlist_state, error_state], outputs=[playlist_state, error_state])

    @gr.render(inputs=[sort_by, playlist_state, error_state])
    def render_songs(sort_by: str | None, playlist: Playlist | None, error: str | None):
        log = Log()

        """
        We call the selected test case factory to get the input playlist.
        If it raised a ValueError (e.g. a song with an invalid energy or duration),
        we display the message as an error boundary and stop rendering.
        """
        if error is not None:
            gr.Markdown(f"ValueError: `{error}`")
            if playlist is None:
             return

        """
        Here, we iterate over each song — using playlist.get_songs() which handles
        both the unsorted and sorted cases internally.
        """
        for song in playlist.get_songs(sort_by, log):
            with gr.Column():
                gr.Markdown(f"## {song.name}")
                with gr.Row():
                    """
                    Here, we display song details in our preferred format
                    - we just format each one in a way that makes sense for the data
                    point.
                    """
                    gr.Markdown(f"by {song.artist}")
                    gr.Markdown(f"{str(round(song.duration / 60, 1))} minutes")
                    gr.Markdown(f"{str(song.energy)} energy points")

        gr.Markdown(f"## Detailed Breakdown")
        gr.Markdown("This is a breakdown of the steps that were involved in sorting the array.")

        """
        Speaking of internally accessible logs, here we iterate over each
        step that comes from Log.get_steps, which we then render in codeblocks
        in markdown
        """
        for item in log.get_steps():
            with gr.Column():
                gr.Markdown(f"```{item}```")

demo.launch()
