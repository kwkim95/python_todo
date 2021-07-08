from todoMgrSystem.entity.models import Todo
from todoMgrSystem.view.templates import menu_display, menu_select, list_display, input_display, id_input_display, \
    message_display, person_display, submenu_display, update_input_display
from todoMgrSystem.controller.views import TodoController
from todoMgrSystem.exception.exception import DuplicationError, NotFoundError

TodoController.load_list()

while True:
    menu_display()
    menu = menu_select()

    if menu == "1":  # 전체 목록 보기
        personList = TodoController.getAllPersons()
        list_display(personList)

    elif menu == "2":  # 등록
        while True:
            submenu_display()
            sub_menu = menu_select()
            if sub_menu == "1":
                person = input_display(sub_menu)
                try:
                    TodoController.register(person)
                    message_display(person.id + " 등록 성공")
                except DuplicationError as e:
                    message_display(e)

            elif sub_menu == "2":
                break
            else:
                print("sub menu 1, 2 중 선택")


    elif menu == "3":
        id = id_input_display("수정")
        try:
            person = TodoController.getPerson(id)
            type = ""
            if isinstance(person, Todo):
                type = "1"

            new_person = update_input_display(type, id)
            TodoController.update(new_person)
            message_display(id + " 수정 성공")
        except NotFoundError as e:
            message_display(e)

    elif menu == "4":
        id = id_input_display("삭제")
        try:
            TodoController.remove(id)
            message_display(id + " 삭제 성공")
        except NotFoundError as e:
            message_display(e)

    elif menu == "5":
        id = id_input_display("검색")
        try:
            person = TodoController.getPerson(id)
            person_display(person)
        except NotFoundError as e:
            message_display(e)

    elif menu == "0":
        TodoController.save_list()
        message_display("인사시스템을 종료합니다.")
        break
    else:
        print()
        message_display("1,2,3,4,5,0번 중 선택하세요")
