from pip._vendor import requests

urlpost = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=7c7fbbb85dde7c8389734066872e52afe51482fd'
file = {"answer": open("answer.json", "rb")}
requests.post(urlpost, files=file)


