import requests
 
url = "https://www.fast2sms.com/dev/bulk"
 
payload = "sender_id=FSTSMS&message=Namaste Padmajii &language=english&route=p&numbers=9440775280"
headers = {
 'authorization': "V25UfZh6R0H7rBzuQL4ECXNWSDlnFp1bdyMvJqYaicOxt9IoAkKyew5u7q1T0QxGEliaAI2Fpm39SB4k",
 'Content-Type': "application/x-www-form-urlencoded",
 'Cache-Control': "no-cache",
 }
 
response = requests.request("POST", url, data=payload, headers=headers)
 
print(response.text)
