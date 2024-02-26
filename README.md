# Fancode_API
Api for SDET Assignment

##Prerequisite:-
NodeJs installed in Machine to run JSON Server on Local host
Python latest version Installed
Pycharm or VScode as Code Editor
Postman to Locally test the API with URL
Command Prompt to start the Json Server
Localhost is 3000

##Step 1:-
Open the COmmand Prompt and give command **npm install -g json-server**(If json-server is not installed with NodeJs).
Once JSON server is installed use Command:- **json-server db.json** from the path where db.json file is stored.
Once the JSON server is live on the localhost:3000 you can use the URL to hit the Users store in db.json file.
Once your JSON server is ready we are ready to hit the APi from python terminal or from local browser.

##Step 2:-
Open the file in VS code or Pycharm and run the project(RequestApi.py).
Initially We can do the Single get_request() to fetch all the users which present in db.json.
In that get_request() Call We will be fetching the all the employee from different company.
In Get Call I had initiated with the total task completion percentage in terms of fancode company and also Fancode city is getting identified in terms of lat and long.

##Step 3:-
Post Call is also defined if we want to add some user in db.json file.

##Step 4:-
Put Call is also defined if we want to update some user in db.json File.

##Step 5:-
Delete call is also defined if we want to delete some user in db.json file.


