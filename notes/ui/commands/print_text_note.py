from .command import Command


class PrintTextNote(Command):
    def __init__(self, console_ui):
        super().__init__(console_ui)
        self._description = "Показать текстовую заметку"

    def execute(self):
        return self.get_console_ui().print_text_note()
