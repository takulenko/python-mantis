import random
import string
import time
from model.project import Project


def test_del_project(app):
    app.session.login("administrator", "root")
    time.sleep(5)
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name=random_string("name", 10), description=random_string("description", 20)))
    old_list = app.project.get_project_list()
    project = random.choice(old_list)
    app.project.delete_project_by_id(project.id)
    new_list = app.project.get_project_list()
    old_list.remove(project)
    assert sorted(new_list, key=Project.id_or_max) == sorted(old_list, key=Project.id_or_max)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
