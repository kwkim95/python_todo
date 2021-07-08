from entity.models import Todo

# menu display
def menu_display():
    print("======= 일정관리 시스템 =======")
    print("1. 전체 목록 보기 ")
    print("2. 등록 ")
    print("3. 수정 ")
    print("4. 삭제 ")
    print("5. 상세보기")
    print("0. 종료")


# submenu display
def submenu_display():
    print("1. 등록")
    print("2. main menu 이동")


# menu select
def menu_select():
    menu = input("메뉴를 선택하세요 : ")
    return menu


# list display
def list_display(persons):
    print("=== 전체 목록 ===")
    for person in persons:
        print(person.info())


# register person input
def input_display(id):
    id = input("아이디를 입력하세요 : ")
    title = input("제목을 입력하세요 : ")
    contents = input("내용을 입력하세요 : ")
    date = input("날짜을 입력하세요 : ")
    done = input("마무리를 입력하세요 : ")

    return Todo(id, title, contents, date, done)


# 수정하거나 삭제 또는 상세보기 위한 id 입력 확인
def id_input_display(command):
    id = input("{0} 수정할 id는 ? ".format(command))
    return id


# update input data
def update_input_display(type, id):
    title = input("이름을 입력하세요 : ")
    contents = input("나이를 입력하세요 : ")
    date = input("날짜을 입력하세요 : ")
    done = input("마무리를 입력하세요 : ")

    if type == "1":
        return Todo(id, title, contents, date, done)


def message_display(message):
    print(message)


# person display
def person_display(person):
    print("=== 상세 정보 ===")
    print(person.info())