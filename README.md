---
title: Playlist Demo
emoji: 🔥
colorFrom: purple
colorTo: blue
sdk: gradio
sdk_version: 6.13.0
app_file: app.py
pinned: false
license: mit
---

# Playlist Sorter 

## Chosen Problem
A playlist sorter that organizes songs by either energy score or duration with merge sort. We use a log to visualize each step in the process for the user.

## Chosen Algorithm
**Merge Sort**. This algorithm was chosen because it performs well with insofar as time complexity goes, regardless of input order (always O(n log n)). Merge sort's divide-and-merge structure also cleanly performs the task of reordering playlists, lending itself well to visualizing each stage as we log discrete steps. It produces a stable sort, which means that songs with equal durations or times stay in their original relative order, which is optimal in the context of sorting songs in a playlist (where users may wish to preserve input order). 

## Demo
https://github.com/user-attachments/assets/d34e7bbb-d956-4b0f-b98b-a02a3474ae58

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
  - **Process***: Provided in Decomposition, above.

### Flowchart
<img width="4698" height="2638" alt="Flowchart - Playlist Sorter" src="https://github.com/user-attachments/assets/3d136d32-4ed9-431b-a0e8-9e37f4fed040" />


## Steps to Run (Locally) and requirements.txt
*to add!!!* 


## Hugging Face Link
(https://huggingface.co/spaces/eilixirs/playlist-demo)

## Testing
With edge cases derived from the above, within algorithmic thinking: 
- Case(1): a song with a very long duration
  - Expected Output = Song gets sorted as usual, app/code can handle larger numbers
  - Result = Passed
- Case(2): a song where the duration is a negative number
  - Expected Output = ValueError thrown, message displays that duration is not valid
  - Result = Passed
- Case(3): a song where the energy level is a negative number
  - Expected Output = ValueError thrown, message displays that the energy level is not valid, too low
  - Result = Passed
- Case(4): a song where the energy level is over 100
  - Expected Output = ValueError thrown, message displays that the energy level is not valid, too high
  - Result = Passed
- Case(5): an empty playlist (no songs)
  - Expected Output = no songs or breakdown displayed, app does not run without end
  - Result = Passed
- Case(6): a playlist with duplicates (two songs have the same values on duration or energy level)
  - Expected Output = stable sort, order of duplicates remains the same as the entry
  - Result = Passed

## Author & AI Acknowledgment

**Author:** Iris Xie
**Course:** CISC121 001 Intro. to Computing Science I W26
**Instructor:** Dr. Ruslan Kain

**AI Use:** Used various AI tools at varied levels:
- Claude: Primarily used to debug code. Also used to outline where to place log.add_steps. Used additionally to create test case inputs and identifiers within gradio to verify test cases passed. All concepts understood by, and all code written by the author. 
- Google Gemini: used to explain concepts, confirm python syntax, and expand function repitoire.

**Additional Notes:**
Requirements under this problem idea of "animate comparisons/moves so the re-ordering is easy to follow" are completed through the "Detailed Breakdown" portion of the app, following the example provided by Dr. Rahatara Ferdousi, where "Search Steps" were used to visualize the process. 
