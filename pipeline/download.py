from pathlib import Path
from urllib.request import Request, urlopen

RAW_DIR = Path("data/raw")


def download_book(gutenberg_id):
    """Download a book from Project Gutenberg and return where it was saved."""

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    path = RAW_DIR / f"{gutenberg_id}.epub"

    if path.exists():
        print(f"Already downloaded: {path}")
        return path

    url = f"https://www.gutenberg.org/cache/epub/{gutenberg_id}/pg{gutenberg_id}.epub"
    print(f"Downloading {url}")

    request = Request(url, headers={"User-Agent": "Novella student project"})

    with urlopen(request) as response:
        data = response.read()

    path.write_bytes(data)
    print(f"Saved to {path}")
    return path