#!/bin/bash

PRE='export $(cat '
POST='/.env | xargs)'
CMD=$PRE$1$POST
echo $CMD >> ~/.bashrc

git config --global --add safe.directory /workspace
git config core.fileMode false
poetry config virtualenvs.in-project true
poetry install
