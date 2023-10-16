#!/usr/bin/env bash
set -x
set -e
black src tests
ruff check src tests --fix
