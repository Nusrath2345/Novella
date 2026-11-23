# Novella

A spoiler-free reading companion. Pick a book, set the chapter you're on, and see a character map and chapter summaries for only the chapters you've read.

Novella uses classical NLP (spaCy plus my own rules) rather than large language models.

## Setup (Mac)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Run

```bash
python run_pipeline.py 1342
```

1342 is the Project Gutenberg ID for Pride and Prejudice.

## Tests

```bash
pytest
```

## Project structure

- `pipeline/` the offline processing steps (download, clean, split, find names)
- `tests/` automated tests
- `data/raw/` downloaded books (not committed)
