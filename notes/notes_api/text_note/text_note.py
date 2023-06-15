from ..note.note import Note


class TextNote(Note):
    def __init__(self, nid, title, text, date_time):
        super().__init__(nid, title, date_time)
        self.__text = text

    def print_all_info(self):
        return f"{self.print_short_info()}\nТело заметки: {self.get_text()}\n" \
               f"Дата/время создания/изменения: {self.get_date_time()}"

    def get_text(self):
        return self.__text

    def set_text(self, text):
        self.__text = text

    def to_dict(self):
        return {"id": self.get_id, "title": self.get_title, "text": self.get_text, "date_time": self.get_date_time}
