# django\_time\_series

Small, mostly abstract (for now) django application for creating time-series data.

## Installation

### Prerequisites

- install pip

        (sudo) easy_install pip

- install django

        (sudo) pip install django

- install South (data migration tool), if it isn't already installed.

        (sudo) pip install South

- in your work directory, create a django site.

        django-admin.py startproject <site_directory>
    
- cd into the site\_directory

        cd <site_directory>

## Installation

- Configure your django project to talk to a database (chances are, the application that wants you to install this will have already told you how to do this).
- Clone this repository into your django project's directory.
- in settings.py, add 'django\_time\_series' to the INSTALLED\_APPS list.  Example:
    
        INSTALLED_APPS = (
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            # Uncomment the next line to enable the admin:
            # 'django.contrib.admin',
            # Uncomment the next line to enable admin documentation:
            # 'django.contrib.admindocs',
            'reddit_collect',
            'south',
            'reddit_data',
            'django_time_series',
        )

- once you get settings.py configured, then run `python manage.py migrate django_time_series` in your site directory to create database tables.

## Usage

For now, the abstract classes in this project are intended to be extended by models that contain specifics of time-series data in a given project.  Having these abstract models lets you re-use code that interacts with this data across projects should you choose.

## License:

Copyright 2013 Jonathan Morgan

This file is part of [http://github.com/jonathanmorgan/django\_time\_series](http://github.com/jonathanmorgan/django_time_series).

django\_time\_series is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

django\_time\_series is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with [http://github.com/jonathanmorgan/django\_time\_series](http://github.com/jonathanmorgan/django_time_series).  If not, see
[http://www.gnu.org/licenses/](http://www.gnu.org/licenses/).