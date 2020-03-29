

class Project():
    def __init__(self, name):
        self.PM = "pm"
        self.RAWS = "raws"
        self.TL = "tl"
        self.PR = "pr"
        self.CLEAN = "cl"
        self.TS = "ts"
        self.RD = "rd"
        self.QC = "qc"
        self.ALL_TASKS = [self.PM, self.RAWS, self.TL, self.PR, self.CLEAN, self.TS, self.RD, self.QC]

        self.name = name

        self.assignments = {}
        for i in self.ALL_TASKS: 
            self.assignments[i] = []

        self.chapter_status = {} 
        for i in self.ALL_TASKS: 
            self.chapter_status[i] = 0
        
    def add_assignment(self, task, user): 
        try: 
            self.assignments[task].append(user)
        except: 
            print(f"Not a valid task. Valid tasks include {', '.join(self.ALL_TASKS)[-2]}.")

    def remove_assignment(self, task, user): 
        raise NotImplementedError

    def update_chapter_status(self, task, chapter): 
        try: 
            self.chapter_status[task] = chapter
        except: 
            print(f"Not a valid task. Valid tasks include {', '.join(self.ALL_TASKS)[-2]}.")

    def __str__(self):
        lines = [] 
        lines.append(f"Project: {self.name}")
        for task in self.ALL_TASKS: 
            if len(self.assignments[task]) != 0: 
                lines.append(f"  {task}: ch {self.chapter_status[task]} complete ({', '.join(self.assignments[task])})")

        return "\n".join(lines)
        