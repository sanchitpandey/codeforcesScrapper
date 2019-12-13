import urllib.parse
import requests

url = "https://codeforces.com/api/user.info?handles="

while True:
    handle = input("Enter your handle?(Type q to exit) ")
    if handle == "q" or handle == "quit":
        break
    data = requests.get(url+handle).json()
    if data['status'] == "OK":
        x = data['result'][0]
        print("Handle: {}\nCurrent Rating: {}\nRank: {}\nMax Rating: {}\nMax Rank: {}\n".format(handle, x['rating'], x['rank'], x['maxRating'], x['maxRank']))
    else:
        print("User doesn't exist!")
