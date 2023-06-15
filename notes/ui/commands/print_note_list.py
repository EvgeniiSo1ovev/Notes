from .command import Command


class PrintNoteList(Command):
    def __init__(self, console_ui):
        super().__init__(console_ui)
        self._description = "Показать список заметок"

    def execute(self):
        return self.get_console_ui().print_note_list()
