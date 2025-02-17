from typing import List
from crewai import Agent, Task, Crew, Process


class AIBTC_Crew:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.agents: List[Agent] = []
        self.tasks: List[Task] = []

    def add_agent(self, agent: Agent):
        self.agents.append(agent)

    def add_task(self, task: Task):
        self.tasks.append(task)

    def create_crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,
        )

    def render_crew(self):
        pass
