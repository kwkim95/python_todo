class Todo:
    def __init__(self, id, title, contents, date, done):
        self.id = id
        self.title = title
        self.contents = contents
        self.date = date
        self.done = done

    def info(self):
        return "아이디 : " + self.id + " 제목 : " + self.title + " 내용 : " + self.contents + " 날짜 : " + self.date + " 마감 : " + self.done

