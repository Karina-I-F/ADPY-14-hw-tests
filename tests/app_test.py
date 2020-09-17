import unittest
import app
from unittest.mock import patch


class Test(unittest.TestCase):

    def setUp(self):
        self.directories, self.documents = app.update_date()
        app.documents == self.documents
        app.directories == self.directories

    def test_get_info(self):
        with patch('app.input', return_value='10006'):
            self.assertEqual('Аристарх Павлов', app.get_doc_owner_name())

    def test_add_new_doc(self):
        self.assertNotIn('5555', app.directories.get('987', []))
        with patch('app.input', side_effect=['5555', 'insurance', 'Iv So', '987']):
            app.add_new_doc()
        self.assertIn('5555', app.directories.get('987', []))

    def test_delete_doc(self):
        self.assertIn('2207 876234', app.documents[0]['number'])
        with patch('app.input', result_value='2207 876234'):
            app.delete_doc()

    def test_remove_doc_from_shelf(self):
        self.assertIn('11-2', app.directories.get('1'))
        app.remove_doc_from_shelf('11-2')
        self.assertNotIn('11-2', app.directories.get('1'))


if __name__ == '__main__':
    unittest.main()
