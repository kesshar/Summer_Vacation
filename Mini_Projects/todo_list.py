class activties:
    def add_task(self,tasks):
        self.tasks=tasks
        nooftask=int(input("Number of tasks you want to add"))
        for i in range(nooftask):
            task=input("Enter the task")
            self.tasks.update({i+1:task})
    def remove_task(self):
        ind=int(input("Enter the index of the the task"))
        self.tasks.pop(ind)
        print("The task is removed...")
    def display_tasks(self):
        for i in self.tasks:
            print(*i)
'''Things needed to add to this project
1. to search more features like either website or appliction or gui or django
2. save in notepad
3. reopening'''


