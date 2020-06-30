from github3 import login

username = 'heejung-choi'
password = 'gmlwjd1008!'
github = login(username=username, password=password)
sigmavirus24 = github.me()

print(sigmavirus24.name)

githubent = login(
    url='https://heejung-choi.github.io/',
    token='9cab848980beedfbdecb',
)

print(githubent)