from notes_api.notes import Notes


class Presenter:
    def __init__(self, console_ui, notes):
        self.__console_ui = console_ui
        self.__notes = notes
        console_ui.set_presenter(self)

    def get_notes(self):
        return self.__notes

    def set_notes(self, notes):
        self.__notes = notes
        return True

    def get_console_ui(self):
        return self.__console_ui

    def add_text_note(self, title, text):
        return self.get_notes().add_text_note(title, text)

    def edit_text_note(self, nid, title, text):
        return self.get_notes().edit_text_note(nid, title, text)

    def delete_text_note(self, nid):
        return self.get_notes().delete_text_note(nid)

    def is_find_text_note(self, nid):
        return self.get_notes().is_find_text_note(nid)

    def get_content_text_note(self, nid):
        return self.get_notes().get_content_text_note(nid)

    def get_filtered_notes(self, begin_date_time, end_date_time):
        return self.get_notes().get_filtered_dicts_list(begin_date_time, end_date_time)

    def load(self, file_name):
        objs = self.get_notes().load(file_name)
        return False if objs == None else self.set_notes(Notes(objs[0], objs[1]))

    def save(self, file_name):
        return self.get_notes().save(file_name)
