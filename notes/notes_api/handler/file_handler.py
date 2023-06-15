import json


class FileHandler:
    def write_to_json(self, file_name, obj):
        try:
            with open(file_name, 'w', encoding='utf-8') as f_n:
                json.dump(obj, f_n, sort_keys=True, indent=4)
            return True
        except Exception as e:
            self.check_errors(e)
            return False

    def read_from_json(self, file_name):
        try:
            with open(file_name, encoding='utf-8') as f_n:
                return json.load(f_n)
        except Exception as e:
            self.check_errors(e)
            return None

    @staticmethod
    def check_errors(e):
        with open('errors.json', encoding='utf-8') as err_f:
            objs = json.load(err_f)
            objs.get('errors').append(e)
        with open('errors.json', 'w', encoding='utf-8') as err_f:
            json.dump(objs, err_f, indent=4)
