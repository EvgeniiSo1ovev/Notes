from .command import Command


class SaveToFile(Command):
    def __init__(self, console_ui):
        super().__init__(console_ui)
        self._description = "Сохранить в файл"

    def execute(self):
        return self.get_console_ui().save_to_file()
