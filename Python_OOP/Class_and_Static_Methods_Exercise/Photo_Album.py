from math import ceil
from typing import Self


class PhotoAlbum:
    MAX_PHOTOS = 4

    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> Self:
        return cls(ceil(photos_count / PhotoAlbum.MAX_PHOTOS))

    def add_photo(self, label: str) -> str:
        for page_index, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.MAX_PHOTOS:
                page.append(label)
                return f"{label} photo added successfully on page {page_index + 1} slot {page.index(label) + 1}"

        return "No more free slots"

    def display(self) -> str:
        result = ""

        for page in self.photos:
            result += "-----------\n"
            result += f"{' '.join(['[]' for _ in page])}\n"

        result += "-----------\n"
        return result.strip()
