Developer Weekly
===============
[![Build Status](https://travis-ci.org/szabgab/developer-weekly.com.png)](https://travis-ci.org/szabgab/developer-weekly.com)

The content of the [Developer Weekly](https://developer-weekly.com/)


SETUP
------
```
virtualenv venv-dw -p python3
source venv-dw/bin/activate
pip install --editable .
```

Development server
-------------------
```
FLASK_APP=dw.app FLASK_DEBUG=1 flask run --host 0.0.0.0 --port 5000
```

Visit http://127.0.0.1:5000/


Publish
----------
* Run ispell
* Update date in src/next.json
* Update src/issues.json
* Run `bin/tidy_json.py`
* Run bin/verify.py to verify the data

* Push to GitHub, update on the server, restart server 

* Visit https://us4.admin.mailchimp.com/lists/
* https://us4.admin.mailchimp.com/campaigns/
* Select the most recent campaign (checkbx) and select replicate
  Update the "Campaign name"
  the "Email subject"
  template: Code on your own, 
  Send a test-mail
