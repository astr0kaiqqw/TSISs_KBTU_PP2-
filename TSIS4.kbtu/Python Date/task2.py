import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Yesterday:", yesterday.strftime("%A"))
print("Today:", today.strftime("%A"))
print("Tomorrow:", tomorrow.strftime("%A"))