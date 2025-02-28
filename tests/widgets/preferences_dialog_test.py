from PyQt6.QtWidgets import QPushButton, QTabWidget
from pytestqt.qtbot import QtBot

from buzz.widgets.preferences_dialog import PreferencesDialog


class TestPreferencesDialog:
    def test_create(self, qtbot: QtBot):
        dialog = PreferencesDialog(shortcuts={})
        qtbot.add_widget(dialog)

        assert dialog.windowTitle() == 'Preferences'

        tab_widget = dialog.findChild(QTabWidget)
        assert isinstance(tab_widget, QTabWidget)
        assert tab_widget.count() == 2
        assert tab_widget.tabText(0) == 'General'
        assert tab_widget.tabText(1) == 'Shortcuts'
