Developer Weekly
===============

The content of https://developer-weekly.com/


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

