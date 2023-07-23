class TextNote:
    def __init__(self, nid, title, text, date_time):
        self.__id = nid
        self.__title = title
        self.__date_time = date_time
        self.__text = text

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_text(self):
        return self.__text

    def get_date_time(self):
        return self.__date_time

    def set_title(self, title):
        self.__title = title

    def set_text(self, text):
        self.__text = text

    def set_date_time(self, date_time):
        self.__date_time = date_time

    # def to_dict(self):
    #     print({'id': self.get_id, 'title': self.get_title, 'text': self.get_text, 'date_time': self.get_date_time})
    #     return {"id": self.get_id, "title": self.get_title, "text": self.get_text, "date_time": self.get_date_time}

    def to_dict(self):
        dict = {"id": self.__id, "title": self.__title, "text": self.__text, "date_time": self.__date_time}
        print(type(dict.get("id")))
        print(dict.get("date_time"))
        return {"id": self.__id, "title": self.__title, "text": self.__text, "date_time": self.__date_time}
