class DuplicationError(Exception):
    def __init__(self, message):
        super().__init__(message + " 이미 존재합니다.")
        # self.message = message

    def __str__(self):
        return super().__str__()


class NotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message+" 존재하지 않습니다.")

    def __str__(self):
        return super().__str__()

