# About

This is the repository of `intuui` webpage. It was made with [sphinx](https://www.sphinx-doc.org/en/master/index.html) using the [sphinxawesome](https://github.com/kai687/sphinxawesome-theme) theme.

# Structure

```
.website/
  |-- src/ ............... .rst and .md files, and conf.py
  |    |-- _static ....... static files, as theme.css, logo.svg
  |    `-- _templates .... jinja2 templates
  `-- dist/ .............. generated static files
```

# Install

1. Clone this repository
2. Execute `make install`

# Configure

1. Get a token for your github user
2. Put your username and your token in `.env`

# Build and Run

1. Execute `make build`.
2. Open `dist/html/index.html` with your browser.

Alternatively, build and run with a local server:

- Just execute `make run`.

# Flow

While pushing to the `main` the runner make the build and update the `gh-pages` branch with `dist/html`, which is then displayed to the user with Github Pages under the domain `intuui.org`.
