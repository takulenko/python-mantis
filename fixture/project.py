from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.get("http://localhost/mantisbt-1.2.20/manage_proj_page.php")
            # wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector('input[value="Add Project"]').click()
        #self.open_project_page()
        self.project_cashe = None

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        self.project_cashe = []
        for element in wd.find_elements_by_xpath("//td/a[contains(@href,'manage_proj_edit_page.php?project_id=')]"):
            text = element.text
            id = element.get_attribute("href").split('=')[1]
            #id = element.get_attribute("href").replace('http://localhost/mantisbt-1.2.20/manage_proj_edit_page.php?project_id=', '')
            self.project_cashe.append(Project(name=text, id=id))
        return list(self.project_cashe)

    def delete_project_by_id(self, id):
        wd = self.app.wd
        #    self.open_project_page()
        self.open_project_id_page(id)
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        self.open_project_page()
        self.project_cashe = None

    def open_project_id_page(self, id):
        wd = self.app.wd
        wd.get('http://localhost/mantisbt-1.2.20/manage_proj_edit_page.php?project_id=' + id)
