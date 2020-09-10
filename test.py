import requests
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=test&language=english&route=p&numbers=9999999999,888888888"
headers = {
'authorization': "bL5Dha7qPvE9R6lScBzsteGpJKrCWQxuNTgkUZIynjHo0M14fdFORYv9rP508qLoSdzl2kxyIV3hgKb1",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)