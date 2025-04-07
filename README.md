# Django Simple Catalog

[![Badge: Version]][pypi]
[![Badge: License]][license]
[![Badge: Supported Python Versions]][pypi]
[![Badge: Supported Django Versions]][pypi]
![Badge: pre-commit]
[![Badge: pre-commit.ci status]][pre-commit.ci status]
[![Badge: Code Style: black]][black code formatter documentation]
[![Badge: Automated Tests]][automated tests on github]
[![Badge: Code Coverage]][codecov]

Django Simple Catalog

## Installation

sudo apt-get install python3.12 python3.12-dev python3.12-venv
sudo adduser --disabled-login catalog --shell /bin/bash
sudo mkdir -p /var/www/catalog/static
sudo chown -R catalog:catalog /var/www/catalog/static/
sudo su catalog
cd ~
python3 -m venv venv
source venv/bin/activate
pip install django
mkdir catalog
django-admin startproject catalog catalog

```bash
pip install git+https://github.com/swashman/django-simple-catalog.git
```

1. Add "django_simple_catalog" to your INSTALLED_APPS setting like this::

```python
INSTALLED_APPS = [
    ...,
    "django_simple_catalog",
]
```

MEDIA_URL = "/media/" # The URL that will serve media files

"django_simple_catalog.context_processors.navbar_menu",
"django_simple_catalog.context_processors.site_settings",

DATABASES["default"] = {
"ENGINE": "django.db.backends.mysql",
"NAME": "catdev",
"USER": "admin",
"PASSWORD": "jn24863951!",
"HOST": "127.0.0.1",
"PORT": "3306",
"OPTIONS": {"charset": "utf8mb4"},
"TEST": {"CHARSET": "utf8mb4"},
}

1. Include the simple catalog URLconf in your project urls.py like this::

```python
from django.conf.urls import include

path("", include("django_simple_catalog.urls")),
```

1. Run

```bash
python manage.py migrate
python manage.py collectstatic
```

1. visit the site!

server {
listen 80;
server_name your_domain.com;

```
location / {
    proxy_pass http://127.0.0.1:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}

location /static/ {
    alias /home/myproject/myproject/static/;
}

location /media/ {
    alias /home/myproject/myproject/media/;
}
```

}

sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo systemctl restart nginx

pip install gunicorn

<!-- Links -->

[automated tests on github]: https://github.com/swashman/django-simple-catalog/actions/workflows/automated-checks.yml
[badge: automated tests]: https://github.com/swashman/django-simple-catalog/actions/workflows/automated-checks.yml/badge.svg "Automated Tests"
[badge: code coverage]: https://codecov.io/gh/swashman/django-simple-catalog/branch/master/graph/badge.svg "Code Coverage"
[badge: code style: black]: https://img.shields.io/badge/code%20style-black-000000.svg "Code Style: black"
[badge: license]: https://img.shields.io/github/license/swashman/django-simple-catalog "License"
[badge: pre-commit]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white "pre-commit"
[badge: pre-commit.ci status]: https://results.pre-commit.ci/badge/github/swashman/django-simple-catalog/master.svg "pre-commit.ci status"
[badge: supported django versions]: https://img.shields.io/pypi/djversions/django-simple-catalog?label=django "Supported Django Versions"
[badge: supported python versions]: https://img.shields.io/pypi/pyversions/django-simple-catalog "Supported Python Versions"
[badge: version]: https://img.shields.io/pypi/v/django-simple-catalog?label=release "Version"
[black code formatter documentation]: http://black.readthedocs.io/en/latest/
[codecov]: https://codecov.io/gh/swashman/django-simple-catalog
[license]: https://github.com/swashman/django-simple-catalog/blob/master/LICENSE
[pre-commit.ci status]: https://results.pre-commit.ci/latest/github/swashman/django-simple-catalog/master "pre-commit.ci"
[pypi]: https://pypi.org/project/django-simple-catalog/
