# Tell a Joke Action

A GitHub Action that prints a random programming joke to your workflow logs.

## Usage

Add the following to your workflow YAML (e.g., `.github/workflows/joke.yml`):

```yaml
name: Tell a Joke

on: [push]

jobs:
  joke:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Tell a Joke
        uses: ./
```

## How it works

This action runs a Python script (`src/main.py`) that selects and prints a random programming joke.

## Requirements

- Python 3.12 or higher (set up automatically in the workflow)
- (Optional) Add dependencies to `requirements.txt` if needed

## Author

Arnab Sau

---
Enjoy your daily dose