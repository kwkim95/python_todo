from todoMgrSystem.entity.models import Todo
from todoMgrSystem.exception.exception import DuplicationError, NotFoundError
from todoMgrSystem.dao.file_registry import save_file, init_data_load
persons = []


class TodoController:
    def __init__(self, id):
        self.id = id

    @staticmethod
    def register(person):
        # id 중복 체크 -> 중복될 경우 DuplicateError
        index = TodoController.is_exist(person.id)
        if index != -1:
            raise DuplicationError(person.id)
        persons.append(person)

    @staticmethod
    def update(person):
        # id 체크 -> 존재하지 않을 경우 NotFoundError
        index = TodoController.is_exist(person.id)
        if index == -1:
            raise NotFoundError(person.id)
        persons[index] = person

    @staticmethod
    def remove(id):
        # id 체크 -> 존재하지 않을 경우 NotFoundError
        index = TodoController.is_exist(id)
        if index == -1:
            raise NotFoundError(id)
        persons.pop(index)

    @staticmethod
    def getPerson(id):
        # id 체크 -> 존재하지 않을 경우 NotFoundError
        index = TodoController.is_exist(id)
        if index == -1:
            raise NotFoundError(id)
        return persons[index]

    @staticmethod
    def getAllPersons():
        return persons

    # id 체크
    @staticmethod
    def is_exist(id):
        for index, person in enumerate(persons):
            if person.id == id:
                return index
        return -1

    @staticmethod
    def save_list():
        save_file(persons)

    @staticmethod
    def load_list():
        global persons
        persons = init_data_load()
