from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os

from crewai_tools import JSONSearchTool
from ai_solutions.tools.csv_cleaner_merger_to_json_converter_tool import CSVCleanerMergerToJSONConverterTool

project_root = os.getcwd()
json_file_path = os.path.join(project_root, 'data', 'merged_cleaned.json')

@CrewBase
class AiSolutions():
    """AiSolutions crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def agent_etl(self) -> Agent:
      return Agent(
        config=self.agents_config['agent_etl'], 
        verbose=True,
        memory=True,
        reasoning=True,
      )
    
    @agent
    def agent_qa(self) -> Agent:
      return Agent(
        config=self.agents_config['agent_qa'], 
        verbose=True,
        memory=True,
        reasoning=True,
        allow_code_execution=True,
        code_execution_mode="unsafe",
      )

    @task
    def cleaner_merger_task(self) -> Task:
      return Task(
          config=self.tasks_config["cleaner_merger_task"],
          tools=[CSVCleanerMergerToJSONConverterTool()]
      )
  
    @task
    def answer_question_task(self) -> Task:
      return Task(
          config=self.tasks_config["answer_question_task"],
          tools=[JSONSearchTool(json_path=json_file_path)]
    )

    @crew
    def crew(self) -> Crew:
        """Creates the AiSolutions crew"""

        return Crew(
          agents=[
            self.agent_etl(),
            self.agent_qa(),
          ],
          tasks=[
            self.cleaner_merger_task(),
            self.answer_question_task(),
          ],
          process=Process.sequential,
          memory=True,
          verbose=True,
    )
