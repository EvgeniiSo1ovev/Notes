from ui.menu import Menu
from datetime import datetime
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
        try:
            n_menu = int(input(self.__menu.print_main_commands()))
            if 0 < n_menu <= self.__menu.get_size_main_commands():
                self.__menu.execute_main_commands(n_menu)
            else:
                print("Введен неверный пункт меню.")
        except ValueError:
            print("Введено что-то отличное от пунктов меню.")
        finally:
            print("\n")

    def quit(self):
        self.__work = False

    def new_text_note(self):
        title = input("Введите заголовок заметки: ")
        text = input("Введите тело заметки: ")
        if self.get_presenter().add_text_note(title, text):
            msg = "Заметка добавлена в список заметок." \
                  "\nСписок заметок готов для дальнейшего сохранения в файл."
        else:
            msg = "Ошибка! Заметка не добавлена в список заметок."
        print(msg)

    def edit_text_note(self):
        try:
            nid = int(input("Введите индивидуальный номер (id) заметки: "))
            if self.get_presenter().is_find_text_note(nid):
                content_text_note = self.get_presenter().get_content_text_note(nid)
                title = inline.input("Отредактируйте заголовок заметки:\n", inp=content_text_note.get("title"))
                text = inline.input("Отредактируйте тело заметки:\n", inp=content_text_note.get("text"))
                if self.get_presenter().edit_text_note(nid, title, text):
                    msg = "Заметка отредактирована и добавлена в список заметок." \
                          "\nСписок заметок готов для дальнейшего сохранения в файл."
                else:
                    msg = "Ошибка редактирования."
                print(msg)
            else:
                print("Введен неверный индивидуальный номер (id) заметки.")
        except ValueError:
            print("Введено что-то отличное от индивидуального номера (id) заметки.")

    def delete_text_note(self):
        try:
            nid = int(input("Введите индивидуальный номер (id) заметки: "))
            if self.get_presenter().is_find_text_note(nid):
                if self.get_presenter().delete_text_note(nid):
                    msg = "Заметка удалена из списка заметок." \
                          "\nСписок заметок готов для дальнейшего сохранения в файл."
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
        try:
            str_begin_date_time = input("Введите начало периода создания/изменения заметок (ДД.ММ.ГГГГ Час:Мин): ")
            begin_date_time = datetime.strptime(str_begin_date_time + ":00", '%d.%m.%Y %H:%M:%S')
            str_end_date_time = input("Введите окончание периода создания/изменения заметок (ДД.ММ.ГГГГ Час:Мин): ")
            end_date_time = datetime.strptime(str_end_date_time + ":59", '%d.%m.%Y %H:%M:%S')
            result = "------------------------"
            for t_n in self.get_presenter().get_filtered_notes(begin_date_time, end_date_time):
                result += f"\nИндивидуальный номер: {t_n.get('id')}" \
                          f"\nЗаголовок заметки: {t_n.get('title')}"
                result += "\n------------------------"
            print(result)
        except ValueError:
            print("Введено что-то отличное от индивидуального номера (id) заметки.")

    def print_text_note(self):
        try:
            nid = int(input("Введите индивидуальный номер (id) заметки: "))
            if self.get_presenter().is_find_text_note(nid):
                content_text_note = self.get_presenter().get_content_text_note(nid)
                result = "------------------------"
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
