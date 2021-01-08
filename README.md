# Django Logging Middleware

The extension for [django](https://github.com/django/django) to log requests and responses using [loguru](https://github.com/Delgan/loguru).

Sometimes code in django views becomes messy because we log requests and response. Also it takes a lot of time to write logs in every view. Using this extension for django, logging becomes simple: all you need is five minutes of installing this package and setting configuration!

**Note this package is not tested with a bunch of python and django versions. Package is under active development**

## Requirements
* python 3.6
* django 3.1
* django rest framework 3.12

## Installation

1. Install using `pip`...

   ```pip install django-logging-middleware```

2. Add `'logging_middleware'` to your `INSTALLED_APPS` setting.

    ```
    INSTALLED_APPS = [ 
        ... 
        'logging_middleware'
    ]
    ```

4. Add setting in your `settings.py`:

    ```
    DJANGO_LOGGING_MIDDLEWARE = {
        'DEFAULT_FORMAT': False,
        'MESSAGE_FORMAT': "<b><green>{time}</green> <cyan>{message}</cyan></b>"
    }
    ```

5. Add `'logging_middleware.middlewares.DjangoLoggingMiddleware'` to your `MIDDLEWARE` setting.

    ```
    MIDDLEWARE = {
        ...
        'logging_middleware.middlewares.DjangoLoggingMiddleware'
    }
    ```

**Note `'logging_middleware.middlewares.DjangoLoggingMiddleware'` should be last in the list `MIDDLEWARE`**

You are ready to see log messages like ones below!
```
...
2021-01-08T23:39:33.597138 Request URL: http://localhost:8000/restframework/simple/class/with_query_string/?data=data
2021-01-08T23:39:33.597530 Request METHOD: PUT
2021-01-08T23:39:33.597874 Request HEADERS: {'Cookie': '', 'Content-Length': '26', 'Content-Type': 'application/json'}
...
```

## Configuration
If you missed 4th step in [installation](#installation), default settings would be:
```
DJANGO_LOGGING_MIDDLEWARE = {
    'DEFAULT_FORMAT': True,
    'MESSAGE_FORMAT': "<b><green>{time}</green> <cyan>{message}</cyan></b>"
}
```

### Settings
**`'DEFAULT_FORMAT'`**

`'DEFAULT_FORMAT'` by default is `True`. It means middleware will use default string format for log messages. By setting it to `False`, you should provide in `'MESSAGE_FORMAT'` your own string format.

**`'MESSAGE_FORMAT'`**

`'MESSAGE_FORMAT'` sets the format of log messages. By default is `'<b><green>{time}</green> <cyan>{message}</cyan></b>'`. For making your own format string, please look the [loguru docs](https://loguru.readthedocs.io/en/stable/api/logger.html#color). Note if you set `'DEFAULT_FORMAT'` as `True`, but also set custom string format in `'MESSAGE_FORMAT'`, the log messages will take the default format. Also by setting `'DEFAULT_FORMAT'` as False without providing the `'MESSAGE_FORMAT'`, the format of messages will be default.

## License
MIT-License, see LICENSE file.
