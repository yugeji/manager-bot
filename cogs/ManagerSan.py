from Project import *
from discord.ext import commands

class ManagerSan(bot): 
    def __init__(self): 
        self.projects = {}
        self.bot = bot

    def new_project(self, name): 
        if name not in self.projects: 
            self.projects[name] = Project(name)

    def add_assignment(self, project_name, task, user): 
        project = self.get_project(project_name)
        
        project.add_assignment(task, user)

    def remove_assignment(self, project_name, task, user): 
        project = self.get_project(project_name)
        
        project.remove_assignment(task, user)

    def update_chapter_status(self, project_name, task, chapter): 
        project = self.get_project(project_name)
        
        project.update_chapter_status(task, chapter)

    def get_project(self, project_name): 
        try: 
            return self.projects[project_name]
        except: 
            print(f"Project '{project_name}' does not exist!")

    def process(self, args): 
        cmd = args[0]
        if cmd == 'complete': 
            project_name, task, chapter = args[1:] 

            self.update_chapter_status(project_name, task, chapter)

        if cmd == 'assign': 
            project_name, task, user = args[1:]

            self.add_assignment(project_name, task, user)

        if cmd == 'unassign':
            project_name, task, user = args[1:]

            self.remove_assignment(project_name, task, user)
        
        if cmd == 'add': 
            self.new_project(args[1])

        if cmd == 'print': 
            
    def __str__(self): 
        lines = []
        for p in sorted(self.projects): 
            lines.append(str(self.projects[p]))

        return "\n\n".join(lines)