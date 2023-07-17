#!/usr/bin/env bash
# exit on error
set -o errexit

pipenv install --dev

pipenv run python manage.py collectstatic --no-input
pipenv run python manage.py migrate
pipenv run python manage.py create_test_books 2000
