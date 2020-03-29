

class Project():
    def __init__(self, name):
        self.PM = "pm"
        self.RAWS = "raws"
        self.TL = "tl"
        self.PR = "pr"
        self.CL = "cl"
        self.TS = "ts"
        self.RD = "rd"
        self.QC = "qc"
        self.ALL_TASKS = [self.PM, self.RAWS, self.TL, self.PR, self.CL, self.TS, self.RD, self.QC]

        self.name = name

        self.total_chapters = 0

        self.assignments = {}
        for i in self.ALL_TASKS: 
            self.assignments[i] = []

        self.chapter_status = {} 
        for i in self.ALL_TASKS: 
            self.chapter_status[i] = 0

        self.todo = {}

    def update_num_chapters(self, num): 
        self.total_chapters = int(num)
        
    def add_assignment(self, task, user): 
        try: 
            self.assignments[task].append(user)
        except: 
            print(f"Not a valid task. Valid tasks include {', '.join(self.ALL_TASKS)}")

    def remove_assignment(self, task, user): 
        raise NotImplementedError

    def update_chapter_status(self, task, chapter): 
        try: 
            self.chapter_status[task] = int(chapter)
        except: 
            print(f"Not a valid task. Valid tasks include {', '.join(self.ALL_TASKS)}")

    def print_assignments(self, print_name=False):
        lines = [] 
        if print_name: 
            lines.append(f"Project: {self.name}")
        lines.append("Assignments:")
        for task in self.ALL_TASKS: 
            if len(self.assignments[task]) != 0: 
                lines.append(f"  {task}: {', '.join(self.assignments[task])}")

        return "\n".join(lines)

    def print_status(self, print_name=False, print_all=True): 
        lines = [] 
        if print_name: 
            lines.append(f"Project: {self.name}")
        # lines.append(f"Total chapters: {self.total_chapters}")
        lines.append("Current status: ")
        for task in self.ALL_TASKS: 
            if task != self.PM: 
                if print_all or len(self.assignments[task]) != 0: 
                    lines.append(f"  {task}: ch {self.chapter_status[task]} complete")

        return "\n".join(lines)

    def print_todo(self, print_name=False):
        self.update_todo() 

        lines = []
        if print_name: 
            lines.append(f"Project: {self.name}")
        lines.append(f" Todo:")
        for task in self.ALL_TASKS:
            if task in self.todo: 
                lines.append(f"  {task}: ch {self.todo[task]} {', '.join(self.assignments[task])}")
        return "\n".join(lines)

    def update_todo(self): 
        todo = {}

        raw_status = self.chapter_status[self.RAWS]
        tl_status = self.chapter_status[self.TL]
        pr_status = self.chapter_status[self.PR] # optional
        pr_exists = len(self.assignments[self.PR]) != 0
        cl_status = self.chapter_status[self.CL]
        ts_status = self.chapter_status[self.TS]
        rd_status = self.chapter_status[self.RD] # optional
        rd_exists = len(self.assignments[self.RD]) != 0
        qc_status = self.chapter_status[self.QC]

        ts_ready = min(tl_status, cl_status)

        if self.total_chapters > raw_status: 
            todo[self.RAWS] = raw_status + 1
        if raw_status > tl_status: 
            todo[self.TL] = tl_status + 1
        if pr_exists:
            if tl_status > pr_status: 
                todo[self.PR] = tl_status + 1
            ts_ready = min(ts_ready, pr_status)
        if raw_status > cl_status: 
            todo[self.CL] = cl_status + 1
        if ts_ready > ts_status: 
            todo[self.TS] = ts_status + 1
        if rd_exists:
            if ts_status > rd_status:
                todo[self.RD] = rd_status + 1
            if rd_status > qc_status: 
                todo[self.QC] = qc_status + 1
        else: 
            if ts_status > qc_status: 
                todo[self.QC] = qc_status + 1
        
        self.todo = todo

    def __str__(self):
        lines = []
        lines.append(self.print_assignments(print_name=True))
        lines.append(self.print_status())
        lines.append(self.print_todo())
        return "\n\n".join(lines)
        