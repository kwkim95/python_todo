from exception.exception import DuplicationError, NotFoundError
from dao.file_registry import save_file, init_data_load
persons = []


class TodoController:
    def __init__(self, id, title, contents, date, done):
        self.id = id
        self.title = title
        self.contents = contents
        self.date = date
        self.done = done

    @staticmethod
    def register(person):
        # id 중복 체크 -> 중복될 경우 DuplicateError
        index = TodoController.is_exist_id(person.id)
        if index != -1:
            raise DuplicationError(person.id)
        persons.append(person)

    @staticmethod
    def update(person):
        # id 체크 -> 존재하지 않을 경우 NotFoundError
        index = TodoController.is_exist_id(person.id)
        if index == -1:
            raise NotFoundError(person.id)
        persons[index] = person

    @staticmethod
    def remove(id):
        # id 체크 -> 존재하지 않을 경우 NotFoundError
        index = TodoController.is_exist_id(id)
        if index == -1:
            raise NotFoundError(id)
        persons.pop(index)

    @staticmethod
    def getPerson_id(id):
        # id 체크 -> 존재하지 않을 경우 NotFoundError
        index = TodoController.is_exist_id(id)
        if index == -1:
            raise NotFoundError(id)
        return persons[index]

    @staticmethod
    def getPerson_title(title):
        # title 체크 -> 존재하지 않을 경우 NotFoundError
        index = TodoController.is_exist_title(title)
        if index == -1:
            raise NotFoundError(title)
        return persons[index]

    @staticmethod
    def getPerson_contents(contents):
        # contents 체크 -> 존재하지 않을 경우 NotFoundError
        index = TodoController.is_exist_contents(contents)
        if index == -1:
            raise NotFoundError(contents)
        return persons[index]

    @staticmethod
    def getPerson_date(date):
        # date 체크 -> 존재하지 않을 경우 NotFoundError
        index = TodoController.is_exist_date(date)
        if index == -1:
            raise NotFoundError(date)
        return persons[index]

    @staticmethod
    def getPerson_done(done):
        # id 체크 -> 존재하지 않을 경우 NotFoundError
        index = TodoController.is_exist_done(done)
        if index == -1:
            raise NotFoundError(done)
        return persons[index]

    @staticmethod
    def getAllPersons():
        return persons

    # id 체크
    @staticmethod
    def is_exist_id(id):
        for index, person in enumerate(persons):
            if person.id == id:
                return index
        return -1

        # id 체크
    @staticmethod
    def is_exist_title(title):
        for index, person in enumerate(persons):
            if person.title == title:
                return index
        return -1

    # id 체크
    @staticmethod
    def is_exist_contents(contents):
        for index, person in enumerate(persons):
            if person.contents == contents:
                return index
        return -1

    # id 체크
    @staticmethod
    def is_exist_date(date):
        for index, person in enumerate(persons):
            if person.date == date:
                return index
        return -1

    # id 체크
    @staticmethod
    def is_exist_done(done):
        for index, person in enumerate(persons):
            if person.done == done:
                return index
        return -1

    @staticmethod
    def save_list():
        save_file(persons)

    @staticmethod
    def load_list():
        global persons
        persons = init_data_load()
