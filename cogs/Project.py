

class Project():
    def __init__(self, name):
        self.RAWS = "raws"
        self.TL = "ts"
        self.CLEAN = "cl"
        self.RD = "rd"
        self.TS = "ts"
        self.QC = "qc"
        self.ALL_TASKS = [self.RAWS, self.TL, self.CLEAN, self.RD, self.TS, self.QC]

        self.name = name

        self.assignments = {}
        for i in self.ALL_TASKS: 
            self.assignments[i] = []

        self.chapter_status = {} 
        for i in self.ALL_TASKS: 
            self.assignments[i] = 0
        
    def add_assignment(self, task, user): 
        try: 
            self.assignments[task].append(user)
        except: 
            print(f"Not a valid task. Valid tasks include {', '.join(self.ALL_TASKS)[-2]}.")

    def update_chapter_status(self, task, chapter): 
        try: 
            self.chapter_status[task] = chapter
        except: 
            print(f"Not a valid task. Valid tasks include {', '.join(self.ALL_TASKS)[-2]}.")

    def __str__(self):
        lines = [] 
        lines.append(f"Project: {self.name}")
        for task in self.ALL_TASKS: 
            lines.append(f"  {task}: ch {self.chapter_status[task]}; ({', '.join(self.assignments[task])})")

        return "\n".join(lines)
        