import datetime

from flask_appbuilder import Model
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship


class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


def today():
    return datetime.datetime.today().strftime("%Y-%m-%d")


class StudentHistory(Model):
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey("department.id"), nullable=False)
    department = relationship("Department")
    student_id = Column(Integer, ForeignKey("student.id"), nullable=False)
    student = relationship("Student")
    begin_date = Column(Date, default=today)
    end_date = Column(Date)


class Student(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    address = Column(Text(250), nullable=False)
    department_id = Column(Integer, ForeignKey("department.id"), nullable=False)
    department = relationship("Department")
    begin_date = Column(Date, default=datetime.date.today(), nullable=True)
    end_date = Column(Date, default=datetime.date.today(), nullable=True)

    def __repr__(self):
        return self.full_name

