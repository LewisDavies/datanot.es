#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lewis Davies'
SITENAME = 'LewisDavi.es'
SITEURL = 'http://lewisdavi.es'
THEME = 'theme'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Full Stack Python', 'https://www.fullstackpython.com/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']

PLUGINS = [
    'random_article',
    'render_math',
    'sitemap',
    'tipue_search'
    ]

RANDOM = 'random.html'

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

EXTRA_PATH_METADATA = {
    'extra/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extra/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extra/browserconfig.xml': {'path': 'browserconfig.xml'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/manifest.json': {'path': 'manifest.json'},
    'extra/mstile-150x150.png': {'path': 'mstile-150x150.png'},
    'extra/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'}
}

STATIC_PATHS = [
    'extra/android-chrome-192x192.png',
    'extra/android-chrome-512x512.png',
    'extra/apple-touch-icon.png',
    'extra/browserconfig.xml',
    'extra/favicon-16x16.png',
    'extra/favicon-32x32.png',
    'extra/favicon.ico',
    'extra/manifest.json',
    'extra/mstile-150x150.png',
    'extra/safari-pinned-tab.svg',
    'matplotlib/bar-plots_files',
    'matplotlib/histograms_files',
    'matplotlib/line-plots_files',
    'matplotlib/making-subplots_files',
    'matplotlib/scatter-plots_files',
    'pandas/visual-exploratory-data-analysis_files',
    'seaborn/box-and-whisker-plots-with-alternatives_files',
    'seaborn/pairplots_files',
    'seaborn/plotting-two-continuous-variables_files',
    'seaborn/scatter-plots-with-regression_files'
]

