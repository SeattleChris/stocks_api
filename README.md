# stocks_api

**Author**: Chris L Chapman
**Version**: 0.3.13 (increment the patch/fix version number up if you make more commits past your first submission)

## Overview

We will be the start of a RESTful API which you will be building for the remainder of the first half of the course. We will build an application that consumes data from a 3rd party API and provides our users with the ability to create stock portfolios. Once we’ve built the basic functionality of the application, we’ll introduce data science, visualizations, and machine learning into the application so we can analyze and make basic predictions based on historical data!

## Getting Started

Setting up on AWS.

Create your Pyramid scaffold using the cookiecutter template for a SQLAlchemy scaffold
Navigate into the new project directory and create a new git repository: git init
Create a new repository on GitHub called stocks_api, and connect your repos using git remote add origin <url-to-your-repo.git> from within the project directory
Create a well named branch for today’s work in your stocks_api repository
Configure the root of your repository with the following files and directories. Thoughtfully name and organize any additional configuration or module files
README.md - Containing good documentation for how to setup, install, and run your application
Copy all of your standard config files into the root of the project, such as .editorconfig and .gitignore (even though there’s already one there)
stocks_api/stocks_api/tests/ - Contains unit tests for your application
Create a virtual environment with pipenv, and run pipenv install -e ".[testing]" to install the dependencies from the scaffold’s setup.py

## Tools used

Pyramid, cookiecutter, git, python 3.6, pipenv, pserve, httppie, pyramid_restful, sqlalchemy, marshmallow

## API

GET a homoe page request at localhost:6543/
GET a api route at localhost:6543/api/v1/stocks

## Change Log

<!-- Ctrl+Shift+I (on Win & Linux) Inserts current DateTime, -->
