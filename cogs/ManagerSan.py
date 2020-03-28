from Project import *

class ManagerSan(): 
    def __init__(self): 
        self.projects = {}

    def new_project(self, name): 
        self.projects[name] = Project(name)

    def add_assignment(self, project_name, task, user): 
        try: 
            project = self.projects[project_name]
        except: 
            print(f"Project '{project_name}' does not exist!")
            return
        
        project.add_assignment(task, user)

    def update_chapter_status(self, project_name, task, chapter): 
        try: 
            project = self.projects[project_name]
        except: 
            print(f"Project '{project_name}' does not exist!")
            return
        
        project.update_chapter_status(task, chapter)

    def __str__(self): 
        lines = []
        for p in sorted(self.projects): 
            lines.append(str(p))

        return "\n\n".join(lines)