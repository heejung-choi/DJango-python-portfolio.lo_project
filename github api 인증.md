# github api 인증

이건가? 한번더 보긴 해야함

http://egloos.zum.com/mcchae/v/11202107



export HOMEBREW_GITHUB_API_TOKEN=0bd8d78fa4e7e57a76f2c7cab22636cffb5a0d00

```bash
curl -u "heejung" https://api.github.com
curl -u 9cab848980beedfbdecb:a365a80d1e78e483f242d4a440b943509e4e4b85 'https://api.github.com/user/repos'
export HOMEBREW_GITHUB_API_TOKEN=[fb70c49a48f41bca14c043eb2e5753bb3ffd924b]
 curl -i https://api.github.com/users/heejung-ch 
oi
```



https://api.github.com/users/heejung-choi/repos

https://api.github.com/users/heejung-choi/events

https://api.github.com/users/heejung-choi/gits



# 설치

```
pip install git+https://github.com/praw-dev/praw.git
```

```
    repo_name = []
    repo_url = []
    for r in range(len(repo_load)):
        #pprint(repo_load[r]['name'])
        #pprint(repo_load[r]['html_url'])
        repo_name.append(repo_load[r]['name']+": "+repo_load[r]['html_url'])
        repo_url.append(repo_load[r]['html_url'])   
    
    pprint("---------------------")
    pprint(repo_name)  
```

