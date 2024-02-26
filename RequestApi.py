import requests
import random
import json
import string

#Base URl:-
baseUrl = "http://localhost:3000"

#AuthToken:-
Auth_Token = "Bearer 0d470b07ba2b46f7663edc296ecce36ba7cf667b29bd561d279dd9d39f6d970c"

#get ramdom email id:
def generate_random_email():
    domain = "fancode.com"
    email_length= 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email= random_string + "@" + domain
    return email

#Get Request:-
def get_request():
    url = baseUrl + "/users"
    print("get url: " + url)
    headers = {"Authorization": Auth_Token}
    response=requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    # Calculate percentage of todo tasks completed for each user
    for user in json_data:
        total_tasks = user.get("total_tasks", 0)
        tasks_completed = user.get("tasks_completed", 0)
        if total_tasks > 0:
            completion_percentage = (tasks_completed / total_tasks) * 100
        else:
            completion_percentage = 0
        user["completion_percentage"] = completion_percentage
        # Check if the user belongs to the FanCode city based on latitude and longitude
        if -40 <= user.get("latitude", 0) <= 5 and 5 <= user.get("longitude", 0) <= 100:
            user["belongs_to_fancode"] = True
        else:
            user["belongs_to_fancode"] = False
    json_str=json.dumps(json_data, indent=4)
    print("Json Get Response body:",json_str)
    print("..............Get User is Done.........")
    print("....................++++++++++++++...............")

#Post Request:-
def post_request():
    url = baseUrl + "/users"
    print("post url: " + url)
    headers = {"Authorization": Auth_Token}
    data = {
        "name": "Aayushi",
        "city": "FanCode",
        "email": generate_random_email(),
        "tasks_completed": 3,
        "total_tasks": 5,
        "latitude": 30,
        "longitude": 50
    }
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("Json Post Response body:", json_str)
    user_id = json_data["id"]
    print ("user id ----->>" , user_id)
    assert response.status_code == 201
    assert "name" in json_data
    assert json_data["name"] == "Aayushi"
    return user_id


#PUT Requests:-

def put_request(user_id):
    url = baseUrl + f"/users/{user_id}"
    print("put url: " + url)
    headers = {"Authorization": Auth_Token}
    data = {
        "name": "Anoop",
        "city": "FanCode",
        "email": generate_random_email(),
        "tasks_completed": 3,
        "total_tasks": 5,
        "latitude": 30,
        "longitude": 50
    }
    response=requests.put(url, json=data, headers=headers)
    assert response.status_code== 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("Json Put Response body:", json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "Anoop"
    print("..............Update User is Done.........")
    print("....................++++++++++++++...............")



#DELETE Requests:-

def delete_request(user_id):
    url = baseUrl + f"/users/{user_id}"
    print("Delete url: " + url)
    headers = {"Authorization": Auth_Token}
    response=requests.delete(url, headers=headers)
    #assert response.status_code== 204
    print("..............Delete User is Done.........")
    print("....................++++++++++++++...............")


#Calling Requests:-

get_request() #To Do the Get Request
#post_request() #To Do the Post Request In Users
user_id = post_request()  #To store the User id of Post Request
put_request(user_id)   #To update the User by given User ID
delete_request(user_id) # To Delete the User of given User ID

