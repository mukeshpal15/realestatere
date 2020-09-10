import requests
ph=7906722499
msg='hello'
url = "https://www.fast2sms.com/dev/bulk"

querystring = {"authorization":"pJFuR4e1ZXH7UgOsjdNkmoWwtCEqfYn5v0iS9aVGxKc6M83yThf5ZwkME37e8ODYcXiq0bNrzh4Jx2Pm","sender_id":"SHRIRA","message":msg,"language":"english","route":"p","numbers":ph}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)