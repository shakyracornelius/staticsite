AUTHOR = 'shak'
SITENAME = 'Shakyra C. Cornelius'
SITEURL = ''
TIMEZONE = 'America/Antigua'
DEFAULT_LANG = 'en'

ABOUT_ME = 'Here to learn. Here to share'
AVATAR = 'extra/site_logo.jpg'

# Paths
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blog']
STATIC_PATHS = ['images','extra']

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}

# Top menus
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True

SIDEBAR_ON_LEFT = True



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://www.python.org/'),
#         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/shakyracc'),
          ('Github', 'https://github.com/shakyracornelius'),
          ('Instagram', 'https://www.instagram.com/shakyracc'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme, environments and plugins
PLUGIN_PATHS = ['pelican-plugins']
THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'cyborg'
PLUGIN_PATHS = ['/Users/shakyracornelius/Development/Pelican/virtualenvs/staticsite/shakyracc/pelican-plugins']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = ['i18n_subsites']
CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'

I18N_TEMPLATES_LANG = 'en'
