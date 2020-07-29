<p align="center">
<img src="https://github.com/bayek0fsiwa/privacychurch/blob/master/static/images/photo.png?raw=true"
height="130">
</p>

You are being watched. Private and state-sponsored organizations are monitoring and recording your online activities. PrivacyChurch provides services, tools and knowledge to protect your privacy against global mass surveillance.

𝙀𝙣𝙘𝙧𝙮𝙥𝙩𝙞𝙤𝙣 𝘼𝙜𝙖𝙞𝙣𝙨𝙩 𝙂𝙡𝙤𝙗𝙖𝙡 𝙈𝙖𝙨𝙨 𝙎𝙪𝙧𝙫𝙚𝙞𝙡𝙡𝙖𝙣𝙘𝙚.

## Developing

<p align="center">
<img alt="Contributions Welcome" src="https://camo.githubusercontent.com/da04b11eb09a13269b08225b3b88851ddb705e78/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f6e747269627574696f6e732d77656c636f6d652d677265656e3f7374796c653d666c6174" data-canonical-src="https://img.shields.io/badge/contributions-welcome-green?style=flat" style="max-width:100%;" width="210px" height="27"></a>
</p>
<p align="center">
<img alt="GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/bayek0fsiwa/privacychurch?logo=Python&logoColor=Yellow&style=plastic">
</p>
<p align="center">
<img alt="PyPI - Django Version" src="https://img.shields.io/pypi/djversions/djangorestframework?logo=django&style=for-the-badge">
</p>

1. Install the latest stable version of [Python 3.7](https://www.python.org/downloads/)
1. Download Pipenv(Assuming You Are On Windows!)
	* `pip install pipenv`
1. Install the required dependencies:
	* `pipenv install`
1. Build the website (Migrate):
	* `python manage.py makemigrations && python manage.py migrate`
1. Create Superuser to manage Admin Dashboard:
	* `python manage.py createsuperuser`
1. Serve the website locally with live reloading:
	* `python manage.py runserver`


## TO-DO
- [x] Add Search Functionality
- [ ] Implement SPA
- [ ] Make It Look Little Bit Nicer!
- [ ] Comment section?
