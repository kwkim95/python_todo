from todoMgrSystem.entity.models import Todo
import os.path


def save_file(persons):
    save_file = open("list.dat", "w")
    for index, p in enumerate(persons):
        if isinstance(p, Todo):
            save_file.write("1,{0},{1},{2},{3},{4}\n".format(p.id, p.title, p.contents, p.date, p.done))

    save_file.close()


def init_data_load():
    persons = []
    fileExist = os.path.isfile("list.dat")
    if fileExist:
        read_file = open("list.dat", "r")
        while True:
            data = read_file.readline()
            data_list = data.split(",")
            if data_list[0] == "1":
                person = Todo(data_list[1], data_list[2], data_list[3], data_list[4], data_list[5].strip("\n"))
                persons.append(person)

            if not data:
                break
        read_file.close()
    return persons

