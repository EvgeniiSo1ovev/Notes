class Note:
    def __init__(self, nid, title, data_time):
        self.__id = nid
        self.__title = title
        self.__date_time = data_time

    def print_short_info(self):
        return f"Индивидуальный номер: {self.get_id()}\nЗаголовок заметки: {self.get_title()}"

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_date_time(self):
        return self.__date_time

    def set_title(self, title):
        self.__title = title

    def set_date_time(self, date_time):
        self.__date_time = date_time
