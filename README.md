# reading-time

A lightweight Python utility that estimates reading time for any block of text or content.

![PyPI version](https://img.shields.io/pypi/v/reading-time)
![license](https://img.shields.io/badge/license-MIT-blue)
![tests](https://img.shields.io/badge/tests-passing-brightgreen)

## Description

`reading-time` calculates how long it will take to read a given piece of text,
based on an average reading speed of 200–250 words per minute. It supports
plain text, Markdown, and HTML input, and returns the estimated reading time
in minutes along with the word count.

**Features:**
- Fast and dependency-free
- Handles plain text, Markdown, and HTML
- Configurable words-per-minute rate
- Returns word count alongside time estimate

## Requirements

- Python 3.8+

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install reading-time.

```bash
pip install reading-time
```

## Usage

```python
from reading_time import reading_time

text = """
Designing great AI products is about more than just accuracy.
It's about transparency, control, and trust.
"""

result = reading_time(text)

print(result)
# {'minutes': 0.5, 'words': 24, 'text': '1 min read'}
```

With a custom words-per-minute rate:

```python
result = reading_time(text, words_per_minute=300)
print(result["text"])  # '1 min read'
```

With Markdown or HTML input:

```python
markdown = "## Introduction\nThis is a **sample** article with some content."
result = reading_time(markdown, strip_markup=True)
print(result)
# {'minutes': 0.1, 'words': 10, 'text': '1 min read'}
```

## API

| Parameter        | Type  | Default | Description                            |
|------------------|-------|---------|----------------------------------------|
| `text`           | str   | —       | The content to analyze                 |
| `words_per_minute` | int | `230`   | Reading speed used for calculation     |
| `strip_markup`   | bool  | `False` | Strip Markdown/HTML before counting    |

**Returns a dict:**

```python
{
  "minutes": 2.4,       # raw decimal minutes
  "words": 560,         # total word count
  "text": "3 min read"  # human-readable estimate
}
```

## Development

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/reading-time.git
cd reading-time
pip install -e ".[dev]"
```

Run tests:

```bash
pytest
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to
discuss what you'd like to change.

Please make sure to update or add tests as appropriate.

## Roadmap

- [ ] CLI tool (`reading-time article.md`)
- [ ] Support for `.pdf` and `.docx` file input
