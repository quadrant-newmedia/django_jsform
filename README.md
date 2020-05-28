# django_jsform
Django integration for [jsform](https://github.com/quadrant-newmedia/jsform). In a nutshell, this package:

- includes jsform scripts as static files
- provides a js_response utility module for use with jsform_execresponse
- provides form-rendering templates which play nicely with jsform_elementmerge
- provides a suite of tests for jsform

## The Tests
The tests are all integration tests, and need to be run manually. 

`python manage.py runserver`, open '/' in your browser, and follow the instructions on the test pages.

## Project Status
This project is the next-generation version of some internal tools we've used on previous production Django sites, but has yet to see significant production usage.

## Contact
If you have any comments or questions about the project, please [create an issue on the issue tracker](https://github.com/quadrant-newmedia/django_jsform/issues).

