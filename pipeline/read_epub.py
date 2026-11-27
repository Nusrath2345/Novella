import ebooklib
from ebooklib import epub


def list_parts(epub_path):
    """Print every part of the EPUB in reading order, with its size."""
    book = epub.read_epub(epub_path)

    for item_id, _ in book.spine:
        item = book.get_item_with_id(item_id)
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            print(item.get_name(), len(item.get_content()))