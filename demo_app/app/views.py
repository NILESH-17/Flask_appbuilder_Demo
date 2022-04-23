from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from . import appbuilder, db
from .models import  Department, Student, StudentHistory


def department_query():
    return db.session.query(Department)


class StudentHistoryView(ModelView):
    datamodel = SQLAInterface(StudentHistory)
    # base_permissions = ['can_add', 'can_show']
    list_columns = ["department", "begin_date", "end_date"]


class StudentView(ModelView):
    datamodel = SQLAInterface(Student)

    list_columns = ["full_name", "department.name"]
    edit_form_extra_fields = {
        "department": QuerySelectField(
            "Department",
            query_factory=department_query,
            widget=Select2Widget(extra_classes="readonly"),
        )
    }

    related_views = [StudentHistoryView]
    show_template = "appbuilder/general/model/show_cascade.html"


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [StudentView]


db.create_all()

appbuilder.add_view(
    StudentView, "Students", icon="fa-folder-open-o", category="College"
)
appbuilder.add_separator("College")
appbuilder.add_view(
    DepartmentView, "Departments", icon="fa-folder-open-o", category="College"
)


