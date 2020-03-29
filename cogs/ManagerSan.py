from Project import *
from discord.ext import commands

class ManagerSan(): 
    def __init__(self): 
        self.projects = {}

        self.commands = {} 
        self.commands['add'] = self.new_project
        self.commands['complete'] = self.update_chapter_status
        self.commands['assign'] = self.add_assignment
        self.commands['unassign'] = self.remove_assignment
        self.commands['help'] = self.get_help

    def process(self, args): 
        cmd = args[0]

        if cmd not in self.commands:
            res = "That's not a valid command!\n"
            res += self.get_help()
            return res

        res = self.commands[cmd](*args[1:])

        if cmd == 'help': 
            return res
        else:
            return str(self)

    def get_help(self):
        lines = []
        lines.append("Commands:")
        lines.append("Note: Valid tasks include pm, raws, tl, pr, cl, ts, rd, and qc.")
        for cmd in sorted(self.commands):
            if cmd != 'help': 
                lines.append(f"  {self.commands[cmd].__doc__}")
        return "\n".join(lines)

    def new_project(self, name): 
        '''add [project]'''
        if name not in self.projects: 
            self.projects[name] = Project(name)

    def add_assignment(self, project_name, task, user): 
        '''assign [project] [task] [person]'''
        project = self.get_project(project_name)
        
        project.add_assignment(task, user)

    def remove_assignment(self, project_name, task, user): 
        '''unassign [project] [task] [person]'''
        project = self.get_project(project_name)
        
        project.remove_assignment(task, user)

    def update_chapter_status(self, project_name, task, chapter): 
        '''complete [project] [task] [chapter]'''
        project = self.get_project(project_name)
        
        project.update_chapter_status(task, chapter)

    def get_project(self, project_name): 
        try: 
            return self.projects[project_name]
        except: 
            print(f"Project '{project_name}' does not exist!")
            
    def __str__(self): 
        lines = []
        for p in sorted(self.projects): 
            lines.append(str(self.projects[p]))

        return "\n\n".join(lines)