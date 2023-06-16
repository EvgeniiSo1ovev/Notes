from ui.commands.new_text_note import NewTextNote
from ui.commands.edit_text_note import EditTextNote
from ui.commands.delete_text_note import DeleteTextNote
from ui.commands.print_note_list import PrintNoteList
from ui.commands.print_text_note import PrintTextNote
from ui.commands.load_from_file import LoadFromFile
from ui.commands.save_to_file import SaveToFile
from ui.commands.quit import Quit



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
        result = "Введите что хотите сделать:\n"
        for i, el in enumerate(self.__main_commands, 1):
            result += f"{i}. {el.get_description()}\n"
        return result
