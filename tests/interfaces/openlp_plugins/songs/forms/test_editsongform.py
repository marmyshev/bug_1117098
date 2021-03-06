"""
Package to test the openlp.plugins.songs.forms.editsongform package.
"""
from mock import MagicMock
from unittest import TestCase

from PyQt4 import QtGui

from openlp.core.lib import Registry
from openlp.plugins.songs.forms.editsongform import EditSongForm


class TestEditSongForm(TestCase):
    """
    Test the EditSongForm class
    """

    def setUp(self):
        """
        Create the UI
        """
        Registry.create()
        self.app = QtGui.QApplication([])
        self.main_window = QtGui.QMainWindow()
        Registry().register('main_window', self.main_window)
        Registry().register('theme_manager', MagicMock())
        self.form = EditSongForm(MagicMock(), self.main_window, MagicMock())

    def tearDown(self):
        """
        Delete all the C++ objects at the end so that we don't have a segfault
        """
        del self.form
        del self.main_window
        del self.app

    def ui_defaults_test(self):
        """
        Test that the EditSongForm defaults are correct
        """
        self.assertFalse(self.form.verse_edit_button.isEnabled(), 'The verse edit button should not be enabled')
        self.assertFalse(self.form.verse_delete_button.isEnabled(), 'The verse delete button should not be enabled')
        self.assertFalse(self.form.author_remove_button.isEnabled(), 'The author remove button should not be enabled')
        self.assertFalse(self.form.topic_remove_button.isEnabled(), 'The topic remove button should not be enabled')

    def is_verse_edit_form_executed_test(self):
        pass

    def verse_order_no_warning_test(self):
        """
        Test if the verse order warning is not shown
        """
        # GIVEN: Mocked methods.
        given_verse_order = 'V1 V2'
        self.form.verse_list_widget.rowCount = MagicMock(return_value=2)
        # Mock out the verse.
        first_verse = MagicMock()
        first_verse.data = MagicMock(return_value='V1')
        second_verse = MagicMock()
        second_verse.data = MagicMock(return_value= 'V2')
        self.form.verse_list_widget.item = MagicMock(side_effect=[first_verse, second_verse])
        self.form._extract_verse_order = MagicMock(return_value=given_verse_order.split())

        # WHEN: Call the method.
        self.form.on_verse_order_text_changed(given_verse_order)

        # THEN: No text should be shown.
        assert self.form.warning_label.text() == '', 'There should be no warning.'

    def verse_order_incomplete_warning_test(self):
        """
        Test if the verse-order-incomple warning is shown
        """
        # GIVEN: Mocked methods.
        given_verse_order = 'V1'
        self.form.verse_list_widget.rowCount = MagicMock(return_value=2)
        # Mock out the verse.
        first_verse = MagicMock()
        first_verse.data = MagicMock(return_value='V1')
        second_verse = MagicMock()
        second_verse.data = MagicMock(return_value= 'V2')
        self.form.verse_list_widget.item = MagicMock(side_effect=[first_verse, second_verse])
        self.form._extract_verse_order = MagicMock(return_value=[given_verse_order])

        # WHEN: Call the method.
        self.form.on_verse_order_text_changed(given_verse_order)

        # THEN: The verse-order-incomplete text should be shown.
        assert self.form.warning_label.text() == self.form.not_all_verses_used_warning, \
            'The verse-order-incomplete warning should be shown.'

    def bug_1170435_test(self):
        """
        Regression test for bug 1170435 (test if "no verse order" message is shown)
        """
        # GIVEN: Mocked methods.
        given_verse_order = ''
        self.form.verse_list_widget.rowCount = MagicMock(return_value=1)
        # Mock out the verse. (We want a verse type to be returned).
        mocked_verse = MagicMock()
        mocked_verse.data = MagicMock(return_value='V1')
        self.form.verse_list_widget.item = MagicMock(return_value=mocked_verse)
        self.form._extract_verse_order = MagicMock(return_value=[])
        self.form.verse_order_edit.text = MagicMock(return_value=given_verse_order)
        # WHEN: Call the method.
        self.form.on_verse_order_text_changed(given_verse_order)

        # THEN: The no-verse-order message should be shown.
        assert self.form.warning_label.text() == self.form.no_verse_order_entered_warning,  \
            'The no-verse-order message should be shown.'
