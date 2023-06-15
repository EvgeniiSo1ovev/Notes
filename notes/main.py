from .presenter.presenter import Presenter
from .ui.console_ui import ConsoleUI
from .notes_api.notes import Notes

console_ui = ConsoleUI()
Presenter(console_ui, Notes([]))

console_ui.start()
