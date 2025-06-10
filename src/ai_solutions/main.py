#!/usr/bin/env python
import sys
import warnings
import os
import glob

from datetime import datetime

from ai_solutions.crew import AiSolutions
from dotenv import load_dotenv
load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(question: str):
    """
    Run the crew.
    """
    
    try:
        project_root = os.getcwd()
        data_dir = os.path.join(project_root, "data", "uploads") 
        os.makedirs(data_dir, exist_ok=True)

        pattern = os.path.join(data_dir, "**", "*.csv")
        csv_paths = glob.glob(pattern, recursive=True)

        crew_instance = AiSolutions()
        result = crew_instance.crew().kickoff(inputs={
          'question': question,
          "file_paths": csv_paths,
        })
        print("Task Results:", result)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        AiSolutions().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AiSolutions().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        AiSolutions().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
