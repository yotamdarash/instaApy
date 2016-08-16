insta_py - bare-bones Python wrapper for Instagram API
======

Unoffical wrapper for Instagram's REST API

Installation
-----
```
pip install insta_py
```
Requires
-----
  * requests

Usage
-----

### Making requests

``` python
from insta_py import InstagramAPI, get_data

access_token = "YOUR_ACCESS_TOKEN"
api = InstagramAPI(access_token=access_token)
response  = api.user.self_recent_media(count=5)

```

###Parsing responses

``` python
from insta_py import get_meta, get_pagination, get_data, get_envelope

envelope =  get_envelope(response)
metadata = get_meta(response)
data = get_data(response)
pagination_data = get_pagination(response)
```

###Running tests

First you must set your own access token in insta_py/test/app_info

```
python setup.py test
```
