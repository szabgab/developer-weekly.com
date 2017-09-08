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
* Run bin/generate.py to verify the data
* 
