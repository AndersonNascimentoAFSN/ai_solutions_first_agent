from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os

from crewai_tools import JSONSearchTool
from ai_solutions.tools.CSVtoJSONConverterTool import CSVtoJSONConverterTool


project_root = os.getcwd()
json_file_path = os.path.join(project_root, 'data', 'merged_cleaned.json')

llm = LLM(model="gpt-4.1", temperature=0)

@CrewBase
class AiSolutions():
    """AiSolutions crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def manager_agent(self) -> Agent:
      return Agent(
        config=self.agents_config['manager_agent'], 
        verbose=True,
        llm=llm,
        tools=[
          CSVtoJSONConverterTool(),
          JSONSearchTool(json_path=json_file_path),
        ],
        memory=True,
        reasoning=True,
        allow_code_execution=True,
        code_execution_mode="unsafe",
      )

    @task
    def cleaner_merger_task(self) -> Task:
      return Task(config=self.tasks_config["cleaner_merger_task"])
  
    @task
    def answer_question_task(self) -> Task:
      return Task(
          config=self.tasks_config["answer_question_task"],
    )

    @crew
    def crew(self) -> Crew:
        """Creates the AiSolutions crew"""

        return Crew(
          agents=[
            self.manager_agent(),
          ],
          tasks=[
            self.cleaner_merger_task(),
            self.answer_question_task(),
          ],
          process=Process.sequential,
          memory=True,
          verbose=True,
    )
