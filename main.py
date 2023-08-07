from webserver import keep_alive
import requests

channelID = 980387939085320192
headers = {
    "authorization":
    "MTA2MzgzNjUyNjU1MjgyMTgxMA.Gy6vFt.qeNJz86J_CKb-a7QFzfNMTHtR30FhNpABlbUW4"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
