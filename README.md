# Playlist Sorter 

## Chosen Problem
A playlist sorter that organizes songs by either energy score or duration with merge sort. We use a log to visualize each step in the process for the user.

## Chosen Algorithm
**Merge Sort**. This algorithm was chosen because it performs well with insofar as time complexity goes, regardless of input order (always O(n log n)). Merge sort's divide-and-merge structure also cleanly performs the task of reordering playlists, lending itself well to visualizing each stage as we log discrete steps. It produces a stable sort, which means that songs with equal durations or times stay in their original relative order, which is optimal in the context of sorting songs in a playlist (where users may wish to preserve input order). 

## Demo
*to add* 

## Problem Breakdown & Computational Thinking

- **Decomposition:**
We take a song list containing the song name, artist name, song energy level, and duration. We accept sort key from the user (either song duration or energy level). Since we are using merge sort with the intended ending of each array containing only one value, we assert a base case (list of 0 or 1 is already sorted). If this base case is not met, we then split the list at the midpoint, recursively sort each half and merge the two sorted halves by comparing elements one-by-one. We also log each merge step to satisfy the animation requirements (visual steps to aid the user in understanding how the sorting is happening) and display all steps and the final result in the GUI.

- **Pattern Recognition:** Every merge step follows the exact same repeating pattern. We look at the first remaining element in each of two sublists, and compare them on the chosen key (energy or duration). We then move the smaller element into the result, and repeat until one sublist is exhausted, finally appending whatever is left. The recursive split also repeats where every sublist is divided in half until only single-element lists remain.

- **Abstraction:** The user  eeds to see the progression of the sort, as in which songs are moving and what the stages are in the sort, requiring a visual element to showcase this progress. The length of the list, contents in strings (song name and artist), are not relevant so long as they exist. The actual values of the song duration or energy are also not relevant so long as they pass two validation checks: whether the duration is more than 0, and whether the energy is between 0-100. 

- **Algorithmic Thinking:** 
  - **Input:** A playlist containing four details (song name, artist, energy level, duration) and a sorting key (energy level or duration) selected by the user via Gradio.
  - **Output:** Gradio displays the step log (each merge numbered and explained) and the final sorted playlist in a listed order, with details alongside each song.
  - **Constraints:**
    - Energy scores must be integers in the range 0-100.
    - Duration is provided in whole seconds.
    - Song titles and artist names are strings and not used as sort keys.
    - Sort keys are exclusively duration or energy level, not both.
  - **Edge Cases:** Lists containing:
    - (1) a song with a very long duration
    - (2) a song where the duration is a negative number
    - (3) a song where the energy level is a negative number
    - (4) a song where the energy level is over 100
    - (5) an empty playlist (no songs)
    - (6) a playlist with duplicates (two songs are the same) 

### Flowchart
*to add*  

## Steps to Run (Locally) and requirements.txt
*to add!!!* 


## Hugging Face Link
*to add*

## Testing
With edge cases derived from the above, within algorithmic thinking: 
- Case(1): a song with a very long duration | Expected Output = | Result = Passed
- Case(2): a song where the duration is a negative number | Expected Output = | Result = Passed
- Case(3): a song where the energy level is a negative number | Expected Output = | Result = Passed
- Case(4): a song where the energy level is over 100 | Expected Output = | Result = Passed
- Case(5): an empty playlist (no songs) | Expected Output = | Result = Passed
- Case(6): a playlist with duplicates (two songs are the same) | Expected Output = | Result = Passed

## Author & AI Acknowledgment

**Author:** Iris Xie
**Course:** CISC-121, Queen's University
**Instructor:** Dr. Ruslan Kain

**AI Use:** Used various AI tools at varied levels:
- Claude Code: used to debug code and outline where to place log.add_steps. 
- Google Gemini: used to explain concepts, confirm python syntax, and expand function repitoire.

**Sources:**
*to add!! some links* 
