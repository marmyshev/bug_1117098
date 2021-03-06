# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=120 tabstop=4 softtabstop=4

###############################################################################
# OpenLP - Open Source Lyrics Projection                                      #
# --------------------------------------------------------------------------- #
# Copyright (c) 2008-2013 Raoul Snyman                                        #
# Portions copyright (c) 2008-2013 Tim Bentley, Gerald Britton, Jonathan      #
# Corwin, Samuel Findlay, Michael Gorven, Scott Guerrieri, Matthias Hub,      #
# Meinert Jordan, Armin Köhler, Erik Lundin, Edwin Lunando, Brian T. Meyer.   #
# Joshua Miller, Stevan Pettit, Andreas Preikschat, Mattias Põldaru,          #
# Christian Richter, Philip Ridout, Simon Scudder, Jeffrey Smith,             #
# Maikel Stuivenberg, Martin Thompson, Jon Tibble, Dave Warnock,              #
# Frode Woldsund, Martin Zibricky, Patrick Zimmermann                         #
# --------------------------------------------------------------------------- #
# This program is free software; you can redistribute it and/or modify it     #
# under the terms of the GNU General Public License as published by the Free  #
# Software Foundation; version 2 of the License.                              #
#                                                                             #
# This program is distributed in the hope that it will be useful, but WITHOUT #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or       #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for    #
# more details.                                                               #
#                                                                             #
# You should have received a copy of the GNU General Public License along     #
# with this program; if not, write to the Free Software Foundation, Inc., 59  #
# Temple Place, Suite 330, Boston, MA 02111-1307 USA                          #
###############################################################################

from PyQt4 import QtCore, QtGui

from openlp.core.lib import UiStrings, build_icon, translate
from openlp.core.lib.ui import create_button_box, create_button
from openlp.plugins.songs.lib.ui import SongStrings


class Ui_EditSongDialog(object):
    """
    The :class:`~openlp.plugins.songs.forms.editsongdialog.Ui_EditSongDialog` class defines the user interface for the
    EditSongForm dialog.
    """
    def setupUi(self, edit_song_dialog):
        edit_song_dialog.setObjectName('edit_song_dialog')
        edit_song_dialog.resize(650, 400)
        edit_song_dialog.setWindowIcon(build_icon(':/icon/openlp-logo-16x16.png'))
        edit_song_dialog.setModal(True)
        self.dialog_layout = QtGui.QVBoxLayout(edit_song_dialog)
        self.dialog_layout.setSpacing(8)
        self.dialog_layout.setContentsMargins(8, 8, 8, 8)
        self.dialog_layout.setObjectName('dialog_layout')
        self.song_tab_widget = QtGui.QTabWidget(edit_song_dialog)
        self.song_tab_widget.setObjectName('song_tab_widget')
        # lyrics tab
        self.lyrics_tab = QtGui.QWidget()
        self.lyrics_tab.setObjectName('lyrics_tab')
        self.lyrics_tab_layout = QtGui.QGridLayout(self.lyrics_tab)
        self.lyrics_tab_layout.setObjectName('lyrics_tab_layout')
        self.title_label = QtGui.QLabel(self.lyrics_tab)
        self.title_label.setObjectName('title_label')
        self.lyrics_tab_layout.addWidget(self.title_label, 0, 0)
        self.title_edit = QtGui.QLineEdit(self.lyrics_tab)
        self.title_edit.setObjectName('title_edit')
        self.title_label.setBuddy(self.title_edit)
        self.lyrics_tab_layout.addWidget(self.title_edit, 0, 1, 1, 2)
        self.alternative_title_label = QtGui.QLabel(self.lyrics_tab)
        self.alternative_title_label.setObjectName('alternative_title_label')
        self.lyrics_tab_layout.addWidget(self.alternative_title_label, 1, 0)
        self.alternative_edit = QtGui.QLineEdit(self.lyrics_tab)
        self.alternative_edit.setObjectName('alternative_edit')
        self.alternative_title_label.setBuddy(self.alternative_edit)
        self.lyrics_tab_layout.addWidget(self.alternative_edit, 1, 1, 1, 2)
        self.lyrics_label = QtGui.QLabel(self.lyrics_tab)
        self.lyrics_label.setFixedHeight(self.title_edit.sizeHint().height())
        self.lyrics_label.setObjectName('lyrics_label')
        self.lyrics_tab_layout.addWidget(self.lyrics_label, 2, 0, QtCore.Qt.AlignTop)
        self.verse_list_widget = SingleColumnTableWidget(self.lyrics_tab)
        self.verse_list_widget.setAlternatingRowColors(True)
        self.verse_list_widget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.verse_list_widget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.verse_list_widget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.verse_list_widget.setObjectName('verse_list_widget')
        self.lyrics_label.setBuddy(self.verse_list_widget)
        self.lyrics_tab_layout.addWidget(self.verse_list_widget, 2, 1)
        self.verse_order_label = QtGui.QLabel(self.lyrics_tab)
        self.verse_order_label.setObjectName('verse_order_label')
        self.lyrics_tab_layout.addWidget(self.verse_order_label, 3, 0)
        self.verse_order_edit = QtGui.QLineEdit(self.lyrics_tab)
        self.verse_order_edit.setObjectName('verse_order_edit')
        self.verse_order_label.setBuddy(self.verse_order_edit)
        self.lyrics_tab_layout.addWidget(self.verse_order_edit, 3, 1, 1, 2)
        self.verse_buttons_layout = QtGui.QVBoxLayout()
        self.verse_buttons_layout.setObjectName('verse_buttons_layout')
        self.verse_add_button = QtGui.QPushButton(self.lyrics_tab)
        self.verse_add_button.setObjectName('verse_add_button')
        self.verse_buttons_layout.addWidget(self.verse_add_button)
        self.verse_edit_button = QtGui.QPushButton(self.lyrics_tab)
        self.verse_edit_button.setObjectName('verse_edit_button')
        self.verse_buttons_layout.addWidget(self.verse_edit_button)
        self.verse_edit_all_button = QtGui.QPushButton(self.lyrics_tab)
        self.verse_edit_all_button.setObjectName('verse_edit_all_button')
        self.verse_buttons_layout.addWidget(self.verse_edit_all_button)
        self.verse_delete_button = QtGui.QPushButton(self.lyrics_tab)
        self.verse_delete_button.setObjectName('verse_delete_button')
        self.verse_buttons_layout.addWidget(self.verse_delete_button)
        self.verse_buttons_layout.addStretch()
        self.lyrics_tab_layout.addLayout(self.verse_buttons_layout, 2, 2)
        self.song_tab_widget.addTab(self.lyrics_tab, '')
        # authors tab
        self.authors_tab = QtGui.QWidget()
        self.authors_tab.setObjectName('authors_tab')
        self.authors_tab_layout = QtGui.QHBoxLayout(self.authors_tab)
        self.authors_tab_layout.setObjectName('authors_tab_layout')
        self.authors_left_layout = QtGui.QVBoxLayout()
        self.authors_left_layout.setObjectName('authors_left_layout')
        self.authors_group_box = QtGui.QGroupBox(self.authors_tab)
        self.authors_group_box.setObjectName('authors_group_box')
        self.authors_layout = QtGui.QVBoxLayout(self.authors_group_box)
        self.authors_layout.setObjectName('authors_layout')
        self.author_add_layout = QtGui.QHBoxLayout()
        self.author_add_layout.setObjectName('author_add_layout')
        self.authors_combo_box = create_combo_box(self.authors_group_box, 'authors_combo_box')
        self.author_add_layout.addWidget(self.authors_combo_box)
        self.author_add_button = QtGui.QPushButton(self.authors_group_box)
        self.author_add_button.setObjectName('author_add_button')
        self.author_add_layout.addWidget(self.author_add_button)
        self.authors_layout.addLayout(self.author_add_layout)
        self.authors_list_view = QtGui.QListWidget(self.authors_group_box)
        self.authors_list_view.setAlternatingRowColors(True)
        self.authors_list_view.setObjectName('authors_list_view')
        self.authors_layout.addWidget(self.authors_list_view)
        self.author_remove_layout = QtGui.QHBoxLayout()
        self.author_remove_layout.setObjectName('author_remove_layout')
        self.author_remove_layout.addStretch()
        self.author_remove_button = QtGui.QPushButton(self.authors_group_box)
        self.author_remove_button.setObjectName('author_remove_button')
        self.author_remove_layout.addWidget(self.author_remove_button)
        self.authors_layout.addLayout(self.author_remove_layout)
        self.authors_left_layout.addWidget(self.authors_group_box)
        self.maintenance_layout = QtGui.QHBoxLayout()
        self.maintenance_layout.setObjectName('maintenance_layout')
        self.maintenance_button = QtGui.QPushButton(self.authors_tab)
        self.maintenance_button.setObjectName('maintenance_button')
        self.maintenance_layout.addWidget(self.maintenance_button)
        self.maintenance_layout.addStretch()
        self.authors_left_layout.addLayout(self.maintenance_layout)
        self.authors_tab_layout.addLayout(self.authors_left_layout)
        self.authors_right_layout = QtGui.QVBoxLayout()
        self.authors_right_layout.setObjectName('authors_right_layout')
        self.topics_group_box = QtGui.QGroupBox(self.authors_tab)
        self.topics_group_box.setObjectName('topics_group_box')
        self.topics_layout = QtGui.QVBoxLayout(self.topics_group_box)
        self.topics_layout.setObjectName('topics_layout')
        self.topic_add_layout = QtGui.QHBoxLayout()
        self.topic_add_layout.setObjectName('topic_add_layout')
        self.topicsComboBox = create_combo_box(self.topics_group_box, 'topicsComboBox')
        self.topic_add_layout.addWidget(self.topicsComboBox)
        self.topic_add_button = QtGui.QPushButton(self.topics_group_box)
        self.topic_add_button.setObjectName('topic_add_button')
        self.topic_add_layout.addWidget(self.topic_add_button)
        self.topics_layout.addLayout(self.topic_add_layout)
        self.topics_list_view = QtGui.QListWidget(self.topics_group_box)
        self.topics_list_view.setAlternatingRowColors(True)
        self.topics_list_view.setObjectName('topics_list_view')
        self.topics_layout.addWidget(self.topics_list_view)
        self.topic_remove_layout = QtGui.QHBoxLayout()
        self.topic_remove_layout.setObjectName('topic_remove_layout')
        self.topic_remove_layout.addStretch()
        self.topic_remove_button = QtGui.QPushButton(self.topics_group_box)
        self.topic_remove_button.setObjectName('topic_remove_button')
        self.topic_remove_layout.addWidget(self.topic_remove_button)
        self.topics_layout.addLayout(self.topic_remove_layout)
        self.authors_right_layout.addWidget(self.topics_group_box)
        self.song_book_group_box = QtGui.QGroupBox(self.authors_tab)
        self.song_book_group_box.setObjectName('song_book_group_box')
        self.song_book_layout = QtGui.QFormLayout(self.song_book_group_box)
        self.song_book_layout.setObjectName('song_book_layout')
        self.song_book_name_label = QtGui.QLabel(self.song_book_group_box)
        self.song_book_name_label.setObjectName('song_book_name_label')
        self.song_book_combo_box = create_combo_box(self.song_book_group_box, 'song_book_combo_box')
        self.song_book_name_label.setBuddy(self.song_book_combo_box)
        self.song_book_layout.addRow(self.song_book_name_label, self.song_book_combo_box)
        self.song_book_number_label = QtGui.QLabel(self.song_book_group_box)
        self.song_book_number_label.setObjectName('song_book_number_label')
        self.song_book_number_edit = QtGui.QLineEdit(self.song_book_group_box)
        self.song_book_number_edit.setObjectName('song_book_number_edit')
        self.song_book_number_label.setBuddy(self.song_book_number_edit)
        self.song_book_layout.addRow(self.song_book_number_label, self.song_book_number_edit)
        self.authors_right_layout.addWidget(self.song_book_group_box)
        self.authors_tab_layout.addLayout(self.authors_right_layout)
        self.song_tab_widget.addTab(self.authors_tab, '')
        # theme tab
        self.theme_tab = QtGui.QWidget()
        self.theme_tab.setObjectName('theme_tab')
        self.theme_tab_layout = QtGui.QHBoxLayout(self.theme_tab)
        self.theme_tab_layout.setObjectName('theme_tab_layout')
        self.theme_left_layout = QtGui.QVBoxLayout()
        self.theme_left_layout.setObjectName('theme_left_layout')
        self.theme_group_box = QtGui.QGroupBox(self.theme_tab)
        self.theme_group_box.setObjectName('theme_group_box')
        self.theme_layout = QtGui.QHBoxLayout(self.theme_group_box)
        self.theme_layout.setObjectName('theme_layout')
        self.theme_combo_box = create_combo_box(self.theme_group_box, 'theme_combo_box')
        self.theme_layout.addWidget(self.theme_combo_box)
        self.theme_add_button = QtGui.QPushButton(self.theme_group_box)
        self.theme_add_button.setObjectName('theme_add_button')
        self.theme_layout.addWidget(self.theme_add_button)
        self.theme_left_layout.addWidget(self.theme_group_box)
        self.rights_group_box = QtGui.QGroupBox(self.theme_tab)
        self.rights_group_box.setObjectName('rights_group_box')
        self.rights_layout = QtGui.QVBoxLayout(self.rights_group_box)
        self.rights_layout.setObjectName('rights_layout')
        self.copyright_layout = QtGui.QHBoxLayout()
        self.copyright_layout.setObjectName('copyright_layout')
        self.copyright_edit = QtGui.QLineEdit(self.rights_group_box)
        self.copyright_edit.setObjectName('copyright_edit')
        self.copyright_layout.addWidget(self.copyright_edit)
        self.copyright_insert_button = QtGui.QToolButton(self.rights_group_box)
        self.copyright_insert_button.setObjectName('copyright_insert_button')
        self.copyright_layout.addWidget(self.copyright_insert_button)
        self.rights_layout.addLayout(self.copyright_layout)
        self.ccli_layout = QtGui.QHBoxLayout()
        self.ccli_layout.setObjectName('ccli_layout')
        self.ccli_label = QtGui.QLabel(self.rights_group_box)
        self.ccli_label.setObjectName('ccli_label')
        self.ccli_layout.addWidget(self.ccli_label)
        self.ccli_number_edit = QtGui.QLineEdit(self.rights_group_box)
        self.ccli_number_edit.setValidator(QtGui.QIntValidator())
        self.ccli_number_edit.setObjectName('ccli_number_edit')
        self.ccli_layout.addWidget(self.ccli_number_edit)
        self.rights_layout.addLayout(self.ccli_layout)
        self.theme_left_layout.addWidget(self.rights_group_box)
        self.theme_left_layout.addStretch()
        self.theme_tab_layout.addLayout(self.theme_left_layout)
        self.comments_group_box = QtGui.QGroupBox(self.theme_tab)
        self.comments_group_box.setObjectName('comments_group_box')
        self.comments_layout = QtGui.QVBoxLayout(self.comments_group_box)
        self.comments_layout.setObjectName('comments_layout')
        self.comments_edit = QtGui.QTextEdit(self.comments_group_box)
        self.comments_edit.setObjectName('comments_edit')
        self.comments_layout.addWidget(self.comments_edit)
        self.theme_tab_layout.addWidget(self.comments_group_box)
        self.song_tab_widget.addTab(self.theme_tab, '')
        # audio tab
        self.audio_tab = QtGui.QWidget()
        self.audio_tab.setObjectName('audio_tab')
        self.audio_layout = QtGui.QHBoxLayout(self.audio_tab)
        self.audio_layout.setObjectName('audio_layout')
        self.audio_list_widget = QtGui.QListWidget(self.audio_tab)
        self.audio_list_widget.setObjectName('audio_list_widget')
        self.audio_layout.addWidget(self.audio_list_widget)
        self.audio_buttons_layout = QtGui.QVBoxLayout()
        self.audio_buttons_layout.setObjectName('audio_buttons_layout')
        self.from_file_button = QtGui.QPushButton(self.audio_tab)
        self.from_file_button.setObjectName('from_file_button')
        self.audio_buttons_layout.addWidget(self.from_file_button)
        self.from_media_button = QtGui.QPushButton(self.audio_tab)
        self.from_media_button.setObjectName('from_media_button')
        self.audio_buttons_layout.addWidget(self.from_media_button)
        self.audio_remove_button = QtGui.QPushButton(self.audio_tab)
        self.audio_remove_button.setObjectName('audio_remove_button')
        self.audio_buttons_layout.addWidget(self.audio_remove_button)
        self.audio_remove_all_button = QtGui.QPushButton(self.audio_tab)
        self.audio_remove_all_button.setObjectName('audio_remove_all_button')
        self.audio_buttons_layout.addWidget(self.audio_remove_all_button)
        self.audio_buttons_layout.addStretch(1)
        self.up_button = create_button(self, 'up_button', role='up', click=self.on_up_button_clicked)
        self.down_button = create_button(self, 'down_button', role='down', click=self.on_down_button_clicked)
        self.audio_buttons_layout.addWidget(self.up_button)
        self.audio_buttons_layout.addWidget(self.down_button)
        self.audio_layout.addLayout(self.audio_buttons_layout)
        self.song_tab_widget.addTab(self.audio_tab, '')
        # Last few bits
        self.dialog_layout.addWidget(self.song_tab_widget)
        self.bottom_layout = QtGui.QHBoxLayout()
        self.bottom_layout.setObjectName('bottom_layout')
        self.warning_label = QtGui.QLabel(edit_song_dialog)
        self.warning_label.setObjectName('warning_label')
        self.bottom_layout.addWidget(self.warning_label)
        self.button_box = create_button_box(edit_song_dialog, 'button_box', ['cancel', 'save'])
        self.bottom_layout.addWidget(self.button_box)
        self.dialog_layout.addLayout(self.bottom_layout)
        self.retranslateUi(edit_song_dialog)

    def retranslateUi(self, edit_song_dialog):
        """
        Translate the UI on the fly.
        """
        edit_song_dialog.setWindowTitle(translate('SongsPlugin.EditSongForm', 'Song Editor'))
        self.title_label.setText(translate('SongsPlugin.EditSongForm', '&Title:'))
        self.alternative_title_label.setText(translate('SongsPlugin.EditSongForm', 'Alt&ernate title:'))
        self.lyrics_label.setText(translate('SongsPlugin.EditSongForm', '&Lyrics:'))
        self.verse_order_label.setText(translate('SongsPlugin.EditSongForm', '&Verse order:'))
        self.verse_add_button.setText(UiStrings().Add)
        self.verse_edit_button.setText(UiStrings().Edit)
        self.verse_edit_all_button.setText(translate('SongsPlugin.EditSongForm', 'Ed&it All'))
        self.verse_delete_button.setText(UiStrings().Delete)
        self.song_tab_widget.setTabText(self.song_tab_widget.indexOf(self.lyrics_tab),
            translate('SongsPlugin.EditSongForm', 'Title && Lyrics'))
        self.authors_group_box.setTitle(SongStrings.Authors)
        self.author_add_button.setText(translate('SongsPlugin.EditSongForm', '&Add to Song'))
        self.author_remove_button.setText(translate('SongsPlugin.EditSongForm', '&Remove'))
        self.maintenance_button.setText(translate('SongsPlugin.EditSongForm', '&Manage Authors, Topics, Song Books'))
        self.topics_group_box.setTitle(SongStrings.Topic)
        self.topic_add_button.setText(translate('SongsPlugin.EditSongForm', 'A&dd to Song'))
        self.topic_remove_button.setText(translate('SongsPlugin.EditSongForm', 'R&emove'))
        self.song_book_group_box.setTitle(SongStrings.SongBook)
        self.song_book_name_label.setText(translate('SongsPlugin.EditSongForm', 'Book:'))
        self.song_book_number_label.setText(translate('SongsPlugin.EditSongForm', 'Number:'))
        self.song_tab_widget.setTabText(self.song_tab_widget.indexOf(self.authors_tab),
            translate('SongsPlugin.EditSongForm', 'Authors, Topics && Song Book'))
        self.theme_group_box.setTitle(UiStrings().Theme)
        self.theme_add_button.setText(translate('SongsPlugin.EditSongForm', 'New &Theme'))
        self.rights_group_box.setTitle(translate('SongsPlugin.EditSongForm', 'Copyright Information'))
        self.copyright_insert_button.setText(SongStrings.CopyrightSymbol)
        self.ccli_label.setText(UiStrings().CCLINumberLabel)
        self.comments_group_box.setTitle(translate('SongsPlugin.EditSongForm', 'Comments'))
        self.song_tab_widget.setTabText(self.song_tab_widget.indexOf(self.theme_tab),
            translate('SongsPlugin.EditSongForm', 'Theme, Copyright Info && Comments'))
        self.song_tab_widget.setTabText(self.song_tab_widget.indexOf(self.audio_tab),
            translate('SongsPlugin.EditSongForm', 'Linked Audio'))
        self.from_file_button.setText(translate('SongsPlugin.EditSongForm', 'Add &File(s)'))
        self.from_media_button.setText(translate('SongsPlugin.EditSongForm', 'Add &Media'))
        self.audio_remove_button.setText(translate('SongsPlugin.EditSongForm', '&Remove'))
        self.audio_remove_all_button.setText(translate('SongsPlugin.EditSongForm', 'Remove &All'))
        self.not_all_verses_used_warning = \
            translate('SongsPlugin.EditSongForm', '<strong>Warning:</strong> Not all of the verses are in use.')
        self.no_verse_order_entered_warning =  \
            translate('SongsPlugin.EditSongForm', '<strong>Warning:</strong> You have not entered a verse order.')


def create_combo_box(parent, name):
    """
    Utility method to generate a standard combo box for this dialog.

    ``parent``
        The parent widget for this combo box.

    ``name``
        The object name.
    """
    combo_box = QtGui.QComboBox(parent)
    combo_box.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
    combo_box.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
    combo_box.setEditable(True)
    combo_box.setInsertPolicy(QtGui.QComboBox.NoInsert)
    combo_box.setObjectName(name)
    return combo_box


class SingleColumnTableWidget(QtGui.QTableWidget):
    """
    Class to for a single column table widget to use for the verse table widget.
    """
    def __init__(self, parent):
        """
        Constructor
        """
        super(SingleColumnTableWidget, self).__init__(parent)
        self.horizontalHeader().setVisible(False)
        self.setColumnCount(1)

    def resizeEvent(self, event):
        """
        Resize the first column together with the widget.
        """
        QtGui.QTableWidget.resizeEvent(self, event)
        if self.columnCount():
            self.setColumnWidth(0, event.size().width())
            self.resizeRowsToContents()
