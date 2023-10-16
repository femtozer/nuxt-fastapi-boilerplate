#!/usr/bin/env bash
set -x
set -e

ruff check src tests
black src tests --check
mypy src tests
