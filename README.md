# OC_P7
# GrandPyBot

# Main features :
The program uses AJAX to send a request to a Flask server which processes the Data received by the user. It returns a short extract of a wikipedia page based on the query of the user, as well as the wikipedia url of said target. If the intention of the user if determined to be a location, the server also returns the user a 400x400px map centered of the assumed coordinates of the target.

# API usage : 
The software uses Google Maps API and media wiki API (from wikipedia). Media Wiki is used to get the url of a user's request, Google Maps is used to get lat/lon of a target, then a map image URL is generated based on those settings.
On windows, use flask_run_init.ps1 to create the env variable directly and use Flask run, on Unix : export FLASK_APP="grandpyapp/views.py"

# Stage : 
Deployed on Heroku @ https://grandpyapp-sempp.herokuapp.com/

# Note :
In script.js line 9, "url: "http://localhost:5000/process"," is used. Localhost is kept to launch and use the server locally. It has been modified for deployment.

# Background art :
The background art is made by artist Benjamin Last @https://www.artstation.com/blast
all rights of the background image (https://index.artstation.com/artwork/wOnJY) belongs to him.

# Pivotal Tracker Link (email me for access):
