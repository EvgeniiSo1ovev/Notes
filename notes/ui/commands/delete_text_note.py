from ui.commands.command import Command


class DeleteTextNote(Command):
    def __init__(self, console_ui):
        super().__init__(console_ui)
        self._description = "Удалить текстовую заметку"

    def execute(self):
        return self.get_console_ui().delete_text_note()
