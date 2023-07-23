from notes_api.handler.file_handler import FileHandler
from notes_api.text_note.text_note import TextNote
from datetime import datetime


class Notes:

    def __init__(self, note_list, unique_id=1):
        self.__note_list = note_list
        self.__unique_id = unique_id

    def get_note_list(self):
        return self.__note_list

    def get_unique_id(self):
        return self.__unique_id

    def set_unique_id(self):
        self.__unique_id += 1

    def find_text_note(self, nid):
        for el in self.get_note_list():
            print(el)
            print(el.get_id())
            if el.get_id == nid:
                return el
        return None

    def is_find_text_note(self, nid):
        return False if self.find_text_note(nid) == None else True

    def add_text_note(self, title, text):
        try:
            self.get_note_list().append(TextNote(self.get_unique_id(), title, text, datetime.now()))
            self.set_unique_id()
            return True
        except Exception as e:
            FileHandler().check_errors(e)
            return False

    def edit_text_note(self, nid, title, text):
        try:
            text_note = self.find_text_note(nid)
            text_note.set_title(title)
            text_note.set_text(text)
            text_note.set_date_time(datetime.now())
            return True
        except Exception as e:
            FileHandler().check_errors(e)
            return False

    def delete_text_note(self, nid):
        try:
            self.get_note_list().remove(self.find_text_note(nid))
            return True
        except Exception as e:
            FileHandler().check_errors(e)
            return False

    def get_content_text_note(self, nid):
        return self.find_text_note(nid).to_dict()

    @staticmethod
    def to_dicts_list(note_list):
        result = []
        for el in note_list:
            result.append(el.to_dict())
        return result

    @staticmethod
    def to_text_note(dicts):
        result = []
        for t_n in dicts:
            result.append(TextNote(t_n.get("id"), t_n.get("title"), t_n.get("text"), t_n.get("date_time")))
        return result

    def load(self, file_name):
        objs = FileHandler().read_from_json(file_name)
        return None if objs == None else [self.to_text_note(objs.get('notes')), objs.get('unique_id')]

    def save(self, file_name):
        objs = {'notes': self.to_dicts_list(self.get_note_list()), 'unique_id': self.get_unique_id()}
        f_h = FileHandler()
        return f_h.write_to_json(file_name, objs)

    def get_filter(self, begin_date_time, end_date_time):
        result = []
        for t_n in self.get_note_list():
            if begin_date_time <= t_n.get_date_time() <= end_date_time:
                result.append(t_n)
        return result

    def get_filtered_dicts_list(self, begin_date_time, end_date_time):
        return self.to_dicts_list(self.get_filter(begin_date_time, end_date_time))
