from .command import Command


class LoadFromFile(Command):
    def __init__(self, console_ui):
        super().__init__(console_ui)
        self._description = "Загрузить из файла"

    def execute(self):
        return self.get_console_ui().load_from_file()
