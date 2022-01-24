# python-messenger
Python Service for Messenger API

*note: make sure you finished setup your facebook and instagram account <br>
https://developers.facebook.com/docs/messenger-platform/introduction*

# Setup

- fill verify token <br>
  VERIFY_TOKEN = 'ur verify token' //random string or number that has been added to callback url on your facebook apps developers page
  
- fill page access token <br>
  PAGE_ACCESS_TOKEN = 'ur page access token' //generated token from your facebook apps developers page
  
- create virtualenv <br>
virtualenv -p python3 {name of env}

- install requirements.txt <br>
pip install -r requirements.txt 

# Run
- source {name of env}/bin/activate
- python test.py
- chat your bot with selected or random keyword
