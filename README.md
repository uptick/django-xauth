# django-xauth

[![PyPI version](https://badge.fury.io/py/django-xauth.svg)](https://badge.fury.io/py/django-xauth)

Some simple AJAX authorisation endpoints for Django.

## Why?

I wanted a package to integrate AJAX authorisation with Django's
standard authorisation views. When a request is made via AJAX it
should be handled as such, and when a standard request is made the
login form should be rendered.


## Installation

`pip` is the easiest way to get the package:

```python
pip install django-xauth
```

Add the package to your Django settings file:

```python
INSTALLED_APPS = [
    'xauth',
    ...
]
```

Replace the standard authorisation URLs in your URL configuration:

```python
urlpatterns = [
    url(r'^', include('xauth.login_ajax_urls'))
]
```


## Usage

Now you can either perform the usual non-AJAX GET and POST to login
as you would normally, or POST using `application/json` encoding to
login over AJAX.

```javascript
import $ from 'jquery'

$.ajax({
  url: '/login',
  method: 'POST',
  contentType: 'application/json',
  data: {
    username: 'harry',
    password: 'henderson123'
  }
})
```

Sometimes you may wish to only allow AJAX logins, in which case set
`XAUTH_AJAX` to `True` in your settings file.
