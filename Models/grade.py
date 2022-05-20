class Grades:

    def __init__(self, grade_type, Status):
        self.grade_type = grade_type
        self.Status = Status

    def __repr__(self):
        str({
            'gradeType': self.grade_type,
            'status': self.Status,
        })

    def json(self):
        return {'gradeType': self.grade_type,
                'gradeStatus': self.Status
                }
