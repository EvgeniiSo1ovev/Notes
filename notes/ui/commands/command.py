class Command:
    _description = ""

    def __init__(self, console_ui):
        self.__console_ui = console_ui

    def get_description(self):
        return self._description

    def get_console_ui(self):
        return self.__console_ui
