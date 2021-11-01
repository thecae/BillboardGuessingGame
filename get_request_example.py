### get request example - python ###

### Introduction ###
# Hello Change++ applicant! We made this for you in case you have no clue what the *@#! a REST API is.
# We hope this helps you get a sense for how to interact with a backend server including
#   a) how to test it is working
#   b) how to use it from the front end program.
#
# Disclaimer: This is not a comprehensive tutorial on APIs, but should help give you some direction if you're stuck


### Part 1: Using the browser to see an example response from free API ###
# To start getting a sense of what it is like to make GET requests, go to https://apipheny.io/free-api/.
# This site has a list of free APIs which are accessible from anywhere. Simply choose one from the list
# and type the example url into the browser of your choice. You can also go to the documentation to play
# around with the different paths and parameters which you can add to the url
#
# example: Agify - guesses someone's age based on their name.
#          url: https://api.agify.io/?name=abby
#          note: you can change the name parameter to be any name (try your own!)


### Part 2: Using the browser to test your own API ###
# Similarly, once you create your own API and want to test to make sure it works, you can use the browser.
# 1. Your first step is to write the appropriate code for a basic REST API. I will not go into more detail
# here, because this is part of the assignment you should figure out without our help. Definitely use
# Google though!
# 2. Next, make sure your server is running by typing the appropriate terminal command
# 3. Finally, open a browser and type in the url associated with your server. It might be "http://localhost:8080/" 
# 4. You should see some output on the browser! 


### Part 3: GET requests in python ###
# Finally, it will be important to be able to make these types of requests from your front end.
# For this part, I will revert back to the agify API

# The appropriate import
import requests

# Make a GET request (similar to what we did in the browser)
response = requests.get("https://api.agify.io/?name=abby")

# print out the response
print(response.text)

# If you run this program ("python3 get_request_example.py" in your terminal, if you have python3 installed),
# you should see the same response as you would see in the browser.
# That is: {"name":"abby","age":38,"count":2935}