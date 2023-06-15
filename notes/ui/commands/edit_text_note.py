from .command import Command


class EditTextNote(Command):
    def __init__(self, console_ui):
        super().__init__(console_ui)
        self._description = "Редактировать текстовую заметку"

    def execute(self):
        return self.get_console_ui().edit_text_note()
