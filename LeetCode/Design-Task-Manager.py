class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.task_prios = {}

        for u, t, p in tasks:
            self.add(u, t, p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heappush(self.heap, (-priority, -taskId, userId))
        self.task_prios[taskId] = (priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        old_priority, userId = self.task_prios[taskId]
        heappush(self.heap, (-newPriority, -taskId, userId))
        self.task_prios[taskId] = (newPriority, userId)

    def rmv(self, taskId: int) -> None:
        del self.task_prios[taskId]

    def execTop(self) -> int:
        while (
            self.heap and (
                -self.heap[0][1] not in self.task_prios or 
                -self.heap[0][0] != self.task_prios[-self.heap[0][1]][0] or
                self.heap[0][2] != self.task_prios[-self.heap[0][1]][1]
            )
        ):
            heappop(self.heap)
        if self.heap:
            priority, taskId, userId = heappop(self.heap)
            del self.task_prios[-taskId]
            return userId
        else:
            return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()