# 🤖 devops_bot

### setup venv
```
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ deactivate
```

### pip install
```
(venv) $ pip3 install -Iv slackclient==2.2.1
(venv) $ pip3 install Flask
```
```
(venv) $ pip3 freeze | tee requirements.txt
(venv) $ pip3 install -r requirements.txt
```

### more information about slack
* https://github.com/slackapi/python-slackclient
* https://api.slack.com/
* https://api.slack.com/tools/block-kit-builder

### more information about Flask
* https://palletsprojects.com/p/flask/

### settings
* PyCharm setting interpreter in venv
* Project setting Source Root

### function list
* list
* roll
* check
* rolling
* exec
