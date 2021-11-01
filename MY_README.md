# Billboard Guessing Game!

The goal of this project is to pull random songs from the Billboard Hot 100 chart and allow the user to the guess the order that they appear on the chart.

## Operating Instructions

This program is initally run using the *main_window.py* file.  This file contains the initial window that is used when starting the game.  This program immediately transitions to *guess_window.py* which is where the user is able to guess the right order of the songs.  The compiler then transitions to *results_window.py*, which contains most of the code for the file.  This file mostly calls upon the *backend.py* file which contains all the functions for reading, comparing, and determining the results.  The file then displays a window based on whether the guess was accurate and then gives the correct song order and their positional numbers.

## How this Program Works

The program utilizes web scraping from the BeautifulSoup function, which sifts through an HTML file and pulls out all the songs based on HTML "keywords".  The *requests* package pulls the HTML from the website itself and stores it into a variable which the BeautifulSoup function can then use to find the keywords.  Then, running a *for-loop*, the song names and artists can be pulled and placed into a list.  Finally, the *random* class pulls three distinct random songs from the list which are the songs that the user guesses the order of.

This program then uses the *PyQT* package to create a GUI for the user to see the songs and input the order.  The package then takes in the data and passes it to the backend file which compares the song guess with the actual order of the songs.  The PyQT class also transitions the code between files so that the various windows are displayed in the correct order.  Note: the second window is intentionally left open so that the user can compare the answer that they input with the true answer that is provided in the third window.  By closing the second window, the user is no longer able to see which order they chose.

The backend file easily works with list and array manipulation to make the random song list, determine if it equals the song guess, and then output the lists correctly.  

## Challenges Faced

In this project, the hardest part was learning how to web scrape and get the songs from the website and store them in a list.  Also, learning the PyQT package was somewhat difficult and ensuring that all the figures are in the right place.  The backend file was definitely the easiest to create; by using the *output.csv* file to have a pre-produced list of the songs, I was able to make nearly the entire project without ever building the web scraping API.

Had I more time on this project, I would like to input song covers into the PyQT interface and allow them to be easily and beautifully printed.  Also, I would like to modify the programs to be able to print more than three songs (this number based on a user input), and then let them guess the number of songs based on this input.  This would definitely take a lot more time working with the PyQT class; I think that this would be a very doable task if working inside a terminal and not using a GUI, but working with the GUI takes a lot more time to complete.

I do believe that I gained a lot from this project.  Having my only CS course completed being CS-1104, this was a big step up in creating a full project that performed a real-life task.  I am very proud of the results that I produced and would love to continue this project further in the future.