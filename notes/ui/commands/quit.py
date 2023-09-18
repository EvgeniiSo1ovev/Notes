from ui.commands.command import Command


class Quit(Command):
    def __init__(self, console_ui):
        super().__init__(console_ui)
        self._description = "Выход из приложения"

    def execute(self):
        self.get_console_ui().quit()
        return False
