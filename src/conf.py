from dataclasses import asdict
from sphinxawesome_theme import ThemeOptions, LinkIcon

project = 'intuui'
copyright = '2025, intuui'
author = 'intuuiers'

extensions = ['myst_parser', 'changelog']

templates_path = ['_templates']
exclude_patterns = []

html_title = 'intuui'
html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']
pygments_style_dark = "github-dark"
pygments_style = "xcode"
html_permalinks_icon = "<span>#</span>"

svg_github = '''
<svg height="22px" style="margin-top:-2px;display:inline" viewBox="0 0 45 44" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M22.477.927C10.485.927.76 10.65.76 22.647c0 9.596 6.223 17.736 14.853 20.608 1.087.2 1.483-.47 1.483-1.047 0-.516-.019-1.881-.03-3.693-6.04 1.312-7.315-2.912-7.315-2.912-.988-2.51-2.412-3.178-2.412-3.178-1.972-1.346.149-1.32.149-1.32 2.18.154 3.327 2.24 3.327 2.24 1.937 3.318 5.084 2.36 6.321 1.803.197-1.403.759-2.36 1.379-2.903-4.823-.548-9.894-2.412-9.894-10.734 0-2.37.847-4.31 2.236-5.828-.224-.55-.969-2.759.214-5.748 0 0 1.822-.584 5.972 2.226 1.732-.482 3.59-.722 5.437-.732 1.845.01 3.703.25 5.437.732 4.147-2.81 5.967-2.226 5.967-2.226 1.185 2.99.44 5.198.217 5.748 1.392 1.517 2.232 3.457 2.232 5.828 0 8.344-5.078 10.18-9.916 10.717.779.67 1.474 1.996 1.474 4.021 0 2.904-.027 5.247-.027 5.96 0 .58.392 1.256 1.493 1.044C37.981 40.375 44.2 32.24 44.2 22.647c0-11.996-9.726-21.72-21.722-21.72" fill="currentColor"></path></svg>
'''

svg_discord = '''
<svg height="18px" style="margin-top:-2px;display:inline" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 127.14 96.36"><path fill="#e1e7ef" d="M107.7,8.07A105.15,105.15,0,0,0,81.47,0a72.06,72.06,0,0,0-3.36,6.83A97.68,97.68,0,0,0,49,6.83,72.37,72.37,0,0,0,45.64,0,105.89,105.89,0,0,0,19.39,8.09C2.79,32.65-1.71,56.6.54,80.21h0A105.73,105.73,0,0,0,32.71,96.36,77.7,77.7,0,0,0,39.6,85.25a68.42,68.42,0,0,1-10.85-5.18c.91-.66,1.8-1.34,2.66-2a75.57,75.57,0,0,0,64.32,0c.87.71,1.76,1.39,2.66,2a68.68,68.68,0,0,1-10.87,5.19,77,77,0,0,0,6.89,11.1A105.25,105.25,0,0,0,126.6,80.22h0C129.24,52.84,122.09,29.11,107.7,8.07ZM42.45,65.69C36.18,65.69,31,60,31,53s5-12.74,11.43-12.74S54,46,53.89,53,48.84,65.69,42.45,65.69Zm42.24,0C78.41,65.69,73.25,60,73.25,53s5-12.74,11.44-12.74S96.23,46,96.12,53,91.08,65.69,84.69,65.69Z"/></svg>
'''

html_favicon = '_static/logo.svg'
html_logo = '_static/logo.svg'

html_sidebars = {
  "**": ["sidebar.html", "sidebar_main_nav_links.html", "sidebar_toc.html"]
}

html_context = {
    'sidebar_links': {
        'docs': {
            'title': 'about',
            'links': [
                {'name': 'README.md', 'url': 'docs/about'},
                {'name': 'philosophy', 'url': 'docs/philosophy'},
                {'name': 'contributing', 'url': 'docs/contrib'},
            ]
        },
        'libs': {
            'title': 'topics',
            'links': [
                {'name': 'philosophy', 'url': 'docs/libs/primitive'},
                {'name': 'mathematics', 'url': 'docs/libs/primitive'},
                {'name': 'development', 'url': 'docs/libs/secondary'},
                {'name': 'artificial inteligence', 'url': 'docs/libs/other'}
            ]
        }
    }
}


html_css_files=['theme.css']

theme_options = ThemeOptions(
    show_breadcrumbs=True,
    extra_header_link_icons = {
        "github": LinkIcon(
            icon=svg_github,
            link='https://github.com/intuui'
        ),
        "discord": LinkIcon(
            icon=svg_discord,
            link='https://discord.gg/waANUyCUGE'
        )
    },
    main_nav_links={
        "home": "index",
        "topics": "topics",
        "changelog": "changelog"
    },
    awesome_headerlinks=True,
    show_prev_next=True
)

html_theme_options = asdict(theme_options)

