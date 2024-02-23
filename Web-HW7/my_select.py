from sqlalchemy import func, desc, select, and_

from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session


def select_01():
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Student).join(Grade).group_by(Student.id).order_by(desc('average_grade')).limit(5).all()
    return result


def select_02(subject_id):
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).join(Student).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(
        desc('average_grade')).limit(1).all()
    return result


def select_03(subject_id):
    result = session.query(Group.id, Group.name, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).join(Student).join(Group).filter(Grade.subject_id == subject_id).group_by(Group.id).all()
    return result


def select_04():
    result = session.query(func.round(func.avg(Grade.grade), 2).label('average_grade')).scalar()
    return result


def select_05(teacher_id):
    result = session.query(Subject.id, Subject.name) \
        .filter(Subject.teacher_id == teacher_id).all()
    return result


def select_06(group_id):
    result = session.query(Student.id, Student.fullname) \
        .filter(Student.group_id == group_id).all()
    return result


def select_07(group_id, subject_id):
    result = session.query(Student.id, Student.fullname, Grade.grade) \
        .select_from(Grade).join(Student).filter(
        and_(Student.group_id == group_id, Grade.subject_id == subject_id)).all()
    return result


def select_08(teacher_id):
    result = session.query(func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).join(Subject).filter(Subject.teacher_id == teacher_id).scalar()
    return result


def select_09(student_id):
    result = session.query(Subject.id, Subject.name) \
        .join(Grade).filter(Grade.student_id == student_id).all()
    return result


def select_10(student_id, teacher_id):
    result = session.query(Subject.id, Subject.name) \
        .join(Grade).join(Teacher).filter(and_(Grade.student_id == student_id, Subject.teacher_id == teacher_id)).all()
    return result


if __name__ == '__main__':
    print(select_01())
    print(select_02(1))
    print(select_03(1))
    print(select_04())
    print(select_05(1))
    print(select_06(1))
    print(select_07(1, 1))
    print(select_08(1))
    print(select_09(1))
    print(select_10(1, 1))
