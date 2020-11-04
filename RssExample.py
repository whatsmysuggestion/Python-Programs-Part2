import requests
def loadRSS():

    url = 'https://www.w3schools.com/angular/customers.php'
    resp = requests.get(url)

    f=open('topnewsfeed.json', 'wb')
    f.write(resp.content)
    f.close()


loadRSS()