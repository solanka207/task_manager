class Task:
    def __init__(self, task_id: int, title: str, status: str = "new"):
        self.id = task_id
        self.title = title
        self.status = status

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
        }

    def from_dict(self, data: dict):
        self.id = data["id"]
        self.title = data["title"]
        self.status = data["status"]
        return self

    def __str__(self):
        return f"[{self.id}] {self.title} ({self.status})"
