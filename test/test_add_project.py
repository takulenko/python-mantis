import random
import string
import time
from model.project import Project


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    app.session.login("administrator", "root")
    time.sleep(5)
    old_list = app.project.get_project_list()
    project = Project(name=random_string("name", 10), description=random_string("description", 20))
    app.project.create(project)
    new_list = app.project.get_project_list()
    old_list.append(project)
    assert sorted(new_list, key=Project.id_or_max) == sorted(old_list, key=Project.id_or_max)
