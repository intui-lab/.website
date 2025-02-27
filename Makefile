# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = src
BUILDDIR      = dist

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) -v $(O)

install:
	@if [ ! -d ".venv" ]; then python3 -m venv .venv; fi
	@. .venv/bin/activate && \
	pip install -r requirements.txt && \
	if [ ! -f ".env" ]; then cp .env.local .env; fi && \
	deactivate

build:
	@. .venv/bin/activate && \
	make clean && \
	make html && \
	deactivate

run:
	@. .venv/bin/activate && \
	make clean && \
	sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)" & \
	sleep 3 && \
	xdg-open http://localhost:8000 && \
	wait && \
	deactivate
