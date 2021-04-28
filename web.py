import requests

def SendFile(url, filename):
    with open(filename, 'rb') as f:
        req = requests.post(url, files={filename: f})
        print(req.Response)