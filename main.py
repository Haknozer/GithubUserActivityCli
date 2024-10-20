import requests
import argparse

parser = argparse.ArgumentParser(description="Github User Activity : ")
parser.add_argument("username", type=str, help="Username")
args = parser.parse_args()

url = f"https://api.github.com/users/{args.username}/events"

response = requests.get(url)

thisdict = {}

responseJson = response.json()
for x in responseJson:
    name = x["repo"]["name"]
    type = x["type"]
    if name not in thisdict:
        thisdict[name] = {
            "commits" : 1,
            "type" : "",  
            "createdAt" : ""
        }
        if type == "CreateEvent":
            thisdict[name]["type"] = "CreateEvent"
            thisdict[name]["createdAt"] = x["created_at"]
        if type == "ForkEvent":
            thisdict[name]["type"] = "ForkEvent"
            thisdict[name]["createdAt"] = x["created_at"]

    else:
        thisdict[name]["commits"] += 1
        if type == "CreateEvent":
            thisdict[name]["createdAt"] = x["created_at"]


for y in thisdict:
    print("Pushed ",thisdict[y]["commits"]," commits to ",y)
    if thisdict[y]["type"] == "ForkEvent":
        print("ForkEvent ",thisdict[y]["createdAt"],"",y,"\n")
    else:
        print("Started ",thisdict[y]["createdAt"],"",y,"\n")


    