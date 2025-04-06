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

```bash
pip install git+https://github.com/swashman/django-simple-catalog.git
```

1. Add "django_simple_catalog" to your INSTALLED_APPS setting like this::

```python
INSTALLED_APPS = [
    ...,
    "django_polls",
]
```

1. Include the simple catalog URLconf in your project urls.py like this::

```python
path("", include("django_simple_catalog.urls")),
```

1. Run

```bash
python manage.py migrate
python manage.py collectstatic
```

1. visit the site!

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
