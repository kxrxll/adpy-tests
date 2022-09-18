from app import App
import unittest

documents = [
    {"type": "doc", "number": "1", "name": "test1"},
    {"type": "doc", "number": "2", "name": "test2"},
    {"type": "doc", "number": "3", "name": "test3"}
]

directories = {
    '1': ['1', '2'],
    '2': ['3'],
    '3': []
}

app = App(documents, directories)


class TestApp(unittest.TestCase):
    def test_check_document_existence(self):
        self.assertEqual(app.check_document_existence("1"), True)

    def test_get_all_doc_owners_names(self):
        self.assertEqual(app.get_all_doc_owners_names(), {"test1", "test2", "test4"})

    def test_get_doc_owner_name(self):
        self.assertEqual(app.get_doc_owner_name("1"), "test1")

    def test_remove_doc_from_shelf(self):
        self.assertEqual(app.remove_doc_from_shelf("1"), None)

    def test_add_new_shelf(self):
        self.assertEqual(app.add_new_shelf("4"), ("4", True))

    def test_append_doc_to_shelf(self):
        self.assertEqual(app.append_doc_to_shelf("7", "2"), None)

    def test_delete_doc(self):
        self.assertEqual(app.delete_doc("3"), ("3", True))

    def test_get_doc_shelf(self):
        self.assertEqual(app.get_doc_shelf("1"), "1")

    def test_move_doc_to_shelf(self):
        self.assertEqual(app.move_doc_to_shelf("2", "2"), 'Документ номер "2" был перемещен на полку номер "2"')

    def test_show_all_docs_info(self):
        self.assertEqual(app.show_all_docs_info(), 'Список всех документов:\ndoc "1" "test1"doc "2" "test2"9 "doc" "test4"')

    def test_add_new_doc(self):
        self.assertEqual(app.add_new_doc('doc', '9', 'test4', '3'), '3')
