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
from insta_py import InstagramAPI

access_token = "YOUR_ACCESS_TOKEN"
api = InstagramAPI(access_token=access_token)
response  = api.user.self_recent_media(count=5)

```

###Parsing responses

Build a data model from response
```python
from insta_py import InstagramAPI, parse_comment

raw_response = api.comments.get_comments("MEDIA_ID")
comment, pagination = parse_comment(raw_response)
print comment[0].name

response = api.locations.locations_info(1)
location = parse_location(raw_response)
print location.longitude

````
Get JSON of envelope/meta/data/pagination
``` python
from insta_py import get_meta, get_pagination, get_data, get_envelope

envelope =  get_envelope(raw_response)
metadata = get_meta(raw_response)
data = get_data(raw_response)
pagination_data = get_pagination(raw_response)
```

###Running tests

First you must set your own access token in insta_py/test/app_info

```
python setup.py test
```

Acknowledgment
-----
Data models are taken from [pyhton-instagram](https://github.com/facebookarchive/python-instagram)