# Color Switch Read Test

Developed by Richie Zhang for the 2017 IB Biology Internal Assessment.

**WARNING: THIS EXPERIMENT INVOLVES RAPIDLY FLASHING COLORS AND TEXT (Ranging from 2Hz to 10Hz). DO NOT RUN ANY
SCRIPTS IN THIS PROJECT IF YOU ARE IN ANY WAY SENSITIVE TO FLASHING COLORS, IMAGES
OR TEXT!!**

The Color Switch Read Test is a simple web based program that aims to test a user's
ability to read rapidly flashing text. The program displays a text block of randomly
generated numbers while foreground and background changes colors at specific frequencies
(Control/No flashing, 2Hz, 4Hz, 6Hz, 8Hz, and 10Hz). The user then is instructed to
read the numbers on screen as fast as they can, and their reading time is recorded for
each test group.

****

This project consists of two parts, a static HTML page (found at `Static Site/`) which
is simply a demo webpage for anyone who does not have Python or Django installed, and
the Django website (found at `Django Project/`) which was the program that was actually
used during experimentation for my IA. More information on either version is listed below.

## The Static Site

For anyone who simply wants to see how the program works, opening `Static Site\index.html`
in your browser after cloning the repository will open the project without the data recording functionalities
that requires Django. [The static site is also hosted on Github Pages.](https://staticallytypedrice.github.io/Color-Switch-Read-Test/Static%20Site/)

## The Django Project

The main difference of the Django website is simply that it automates the tracking of what
numbers each user was assigned, so their reading can be recorded and checked for errors.
I chose to code this program using Django simply because I was already somewhat familiar with both Django
as well as web design.
I simply ran the site on my local computer using Django's development server.

Because I never intended for the Django program to hosted on the internet, I cannot guarantee
that it is 100% secure, though I believe it is reasonably so. However, if anyone does want to host
it online, make sure to *at least* set, in `settings.py`, `DEBUG=False`, and change the
`SECRET_KEY` to something properly secure and well... secret.

The Django site project requires Python >= 3.5.0 and Django >= 1.10.3 to be installed on
your computer or in a virtual environment. Make sure to also run `python manage.py migrate` and
`python manage.py createsuperuser` so that there is a database present and properly configured.
You may also wish to run `python manage.py collectstatic`, but the project seems to also work without it.

If you are on windows, simply run `setup.bat` to set up the project, and `runserver.bat` to start the development server.
Run these in an activated virtualenv if applicable.
