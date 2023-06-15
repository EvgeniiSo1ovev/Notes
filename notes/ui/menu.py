from .commands.new_text_note import NewTextNote
from .commands.edit_text_note import EditTextNote
from .commands.delete_text_note import DeleteTextNote
from .commands.print_note_list import PrintNoteList
from .commands.print_text_note import PrintTextNote
from .commands.load_from_file import LoadFromFile
from .commands.save_to_file import SaveToFile
from .commands.quit import Quit



class Menu:
    def __init__(self, console_ui):
        self.__main_commands = []
        self.__main_commands.append(NewTextNote(console_ui))
        self.__main_commands.append(EditTextNote(console_ui))
        self.__main_commands.append(DeleteTextNote(console_ui))
        self.__main_commands.append(PrintTextNote(console_ui))
        self.__main_commands.append(PrintNoteList(console_ui))
        self.__main_commands.append(LoadFromFile(console_ui))
        self.__main_commands.append(SaveToFile(console_ui))
        self.__main_commands.append(Quit(console_ui))

    def get_size_main_commands(self):
        return len(self.__main_commands)

    def execute_main_commands(self, n_menu):
        return self.__main_commands[n_menu - 1].execute()

    def print_main_commands(self):
        result = "Введите что хотите сделать:"
        for i, el in enumerate(self.__main_commands, 1):
            result += f"\n{i}. {el.get_description()}"
        return result
