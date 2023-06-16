from ui.commands.command import Command


class NewTextNote(Command):
    def __init__(self, console_ui):
        super().__init__(console_ui)
        self._description = "Создать новую текстовую заметку"

    def execute(self):
        return self.get_console_ui().new_text_note()
