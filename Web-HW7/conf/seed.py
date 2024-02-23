from faker import Faker
from random import randint, choice
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Teacher, Group, Student, Subject, Grade

engine = create_engine('postgresql://postgres:12345678@localhost:5432/web-hw7')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

fake = Faker()

groups = [Group(name=f'Group {i}') for i in range(1, 4)]

teachers = [Teacher(fullname=fake.name()) for _ in range(3)]

subjects = [Subject(name=fake.word(), teacher=choice(teachers)) for _ in range(5)]

session.add_all(groups)
session.add_all(teachers)
session.add_all(subjects)
session.commit()

students = []
for _ in range(30):
    student = Student(fullname=fake.name(), group=choice(groups))
    students.append(student)

session.add_all(students)
session.commit()


def add_grades_for_students(students, subjects):
    for student in students:
        for subject in subjects:
            for _ in range(randint(1, 4)):
                grade = Grade(
                    grade=randint(1, 12),
                    grade_date=fake.date_between(start_date='-1y', end_date='today'),
                    student_id=student.id,
                    subject_id=subject.id
                )
                session.add(grade)
        session.commit()


add_grades_for_students(students, subjects)
session.commit()

print("Данные успешно добавлены в базу данных.")
