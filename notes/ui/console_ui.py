from ui.menu import Menu
import datetime
import inline


class ConsoleUI:
    def __init__(self):
        self.__work = True
        self.__menu = Menu(self)
        self.__presenter = None

    def get_presenter(self):
        return self.__presenter

    def set_presenter(self, presenter):
        self.__presenter = presenter

    def start(self):
        while (self.__work):
            self.main_requests()

    def main_requests(self):
        user_input = input(self.__menu.print_main_commands())
        try:
            n_menu = int(user_input)
            if 0 < n_menu <= self.__menu.get_size_main_commands():
                self.__menu.execute_main_commands(n_menu)
            else:
                print("Введен неверный пункт меню.")
        except ValueError:
            print("Введено что-то отличное от пунктов меню.")

    def quit(self):
        self.__work = False

    def new_text_note(self):
        title = input("Введите заголовок заметки: ")
        text = input("Введите тело заметки: ")
        date_time = datetime.datetime
        if self.get_presenter().add_text_note(title, text, date_time):
            msg = "Заметка добавлена в список заметок. " \
                  "\n Список заметок готов для дальнейшего сохранения в файл."
        else:
            msg = "Ошибка! Заметка не добавлена в список заметок."
        print(msg)

    def edit_text_note(self):
        user_input = input("Введите индивидуальный номер (id) заметки: ")
        try:
            nid = int(user_input)
            if self.get_presenter().is_find_text_note(nid):
                content_text_note = self.get_presenter().get_content_text_note(nid)
                title = inline.input("Отредактируйте заголовок заметки: "
                                     "\n", inp=content_text_note.get("title"))
                text = inline.input("Отредактируйте тело заметки: "
                                    "\n", inp=content_text_note.get("text"))
                date_time = datetime.datetime
                if self.get_presenter().edit_text_note(nid, title, text, date_time):
                    msg = "Заметка отредактирована и добавлена в список заметок.\n " \
                          "Список заметок готов для дальнейшего сохранения в файл."
                else:
                    msg = "Ошибка редактирования."
                print(msg)
            else:
                print("Введен неверный индивидуальный номер (id) заметки.")
        except ValueError:
            print("Введено что-то отличное от индивидуального номера (id) заметки.")

    def delete_text_note(self):
        user_input = input("Введите индивидуальный номер (id) заметки: ")
        try:
            nid = int(user_input)
            if self.get_presenter().is_find_text_note(nid):
                if self.get_presenter().delete_text_note(nid):
                    msg = "Заметка удалена из списка заметок.\n " \
                          "Список заметок готов для дальнейшего сохранения в файл."
                else:
                    msg = "Ошибка удаления."
                print(msg)
            else:
                print("Введен неверный индивидуальный номер (id) заметки.")
        except ValueError:
            print("Введено что-то отличное от индивидуального номера (id) заметки.")

    def load_from_file(self):
        if self.get_presenter().load(input("Введите имя файла: ")):
            msg = "Список заметок загружен."
        else:
            msg = "Ошибка чтения файла."
        print(msg)

    def save_to_file(self):
        if self.get_presenter().save(input("Введите имя файла: ")):
            msg = "Список заметок сохранен."
        else:
            msg = "Ошибка сохранения файла."
        print(msg)

    def print_note_list(self):
        begin_date_time = input("Введите начало периода создания/изменения заметок: ")
        end_date_time = input("Введите окончание периода создания/изменения заметок: ")
        result = ""
        for t_n in self.get_presenter().get_filtered_notes(begin_date_time, end_date_time):
            result += f"\nИндивидуальный номер: {t_n.get('id')}" \
                      f"\nЗаголовок заметки: {t_n.get('title')}"
            result += "\n------------------------"
        print(result)

    def print_text_note(self):
        user_input = input("Введите индивидуальный номер (id) заметки: ")
        try:
            nid = int(user_input)
            if self.get_presenter().is_find_text_note(nid):
                content_text_note = self.get_presenter().get_content_text_note(nid)
                result = "\n------------------------"
                result += f"\nИндивидуальный номер: {content_text_note.get('id')}" \
                          f"\nЗаголовок заметки: {content_text_note.get('title')}" \
                          f"\nТело заметки: {content_text_note.get('text')}" \
                          f"\nДата/время создания/изменения: {content_text_note.get('date_time')}"
                result += "\n------------------------"
                print(result)
            else:
                print("Введен неверный индивидуальный номер (id) заметки.")
        except ValueError:
            print("Введено что-то отличное от индивидуального номера (id) заметки.")
