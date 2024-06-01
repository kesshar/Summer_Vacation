class activties:
    def __init__(self,tasks):
        self.tasks = tasks
    def add_task(self,tasks):
        self.tasks=tasks
        nooftask=int(input("Number of tasks you want to add: "))
        for i in range(nooftask):
            task=input("Enter the task: ")
            (self.tasks).update({i+1:task})
    def remove_task(self):
        ind=int(input("Enter the index of the the task: "))
        self.tasks.pop(ind)
        print("The task is removed...")
    def display_tasks(self):
        for i in (self.tasks).items():
            n=0
            for j in i:
                print(j,end='')
                if n!=1:
                    print(end=') ')
                n+=1
            print('\n')
    def save_tasks(self):
        n=input("Enter the name of the file(with .txt extension): ")
        f=open(n,"w")
        for i in (self.tasks).items():
            n = 0
            for j in i:
                j=str(j)
                f.write(j)
                if n != 1:
                    f.write(') ')
                n += 1
            print('\n')
            f.close()
    def see_my_prev_tasks(self):
        n=input("Enter the name of the file(with .txt extension): ")
        f=open(n,"r")
        tasks=f.read()
        print(tasks)
        print('\n')



tasks={}
a = activties(tasks)
while(True):
    n=0
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------TO-DO LIST---------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    print("Enter 1 Add a task")
    print("Enter 2 Remove a task")
    print("Enter 3 Display the list")
    print("Enter 4 Save the list")
    print("Enter 5 See previous list")
    print("Enter 6 to Exit")
    n=int(input("Enter command to the todo list: "))
    if(n==1):
        a.add_task(tasks)
    if n==2:
        a.remove_task()
    if n==3:
        a.display_tasks()
    if n==4:
        a.save_tasks()
    if n==5:
        a.see_my_prev_tasks()
    if n==6:
        break





