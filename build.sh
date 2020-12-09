#!/usr/bin/env bash
env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install --force 3.6.8
pipenv install --dev
pipenv run \
    pip install -U pyinstaller && \
    pyinstaller -y --clean --windowed --name main \
        --exclude-module _tkinter \
        --exclude-module Tkinter \
        --exclude-module enchant \
        --exclude-module twisted \
        main.py