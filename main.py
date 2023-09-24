from webserver import keep_alive
import requests

channelID = 980387939085320192
headers = {
    "authorization":
    "ODExMzQyMzIyNjY2NDM4NjU3.GNSXfb.Ko_NqmxYWJCYa_IeLMTZoDv_QTXTcB2DrOSx3g"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{980387939085320192}/messages",
            headers=headers,
            json={"content": line})
