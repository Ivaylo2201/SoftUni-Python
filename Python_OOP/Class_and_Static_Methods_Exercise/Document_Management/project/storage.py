from typing import List
from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self) -> None:
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        for c in self.categories:
            if c.id == category_id:
                c.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        for t in self.topics:
            if t.id == topic_id:
                t.topic = new_topic
                t.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        for d in self.documents:
            if d.id == document_id:
                d.file_name = new_file_name

    def delete_category(self, category_id: int) -> None:
        for c in self.categories:
            if c.id == category_id:
                self.categories.remove(c)

    def delete_topic(self, topic_id: int) -> None:
        for t in self.topics:
            if t.id == topic_id:
                self.topics.remove(t)

    def delete_document(self, document_id: int) -> None:
        for d in self.documents:
            if d.id == document_id:
                self.documents.remove(d)

    def get_document(self, document_id: int) -> Document:
        for d in self.documents:
            if d.id == document_id:
                return d

    def __repr__(self) -> str:
        documents = [d.__repr__() for d in self.documents]
        return '\n'.join(documents)
