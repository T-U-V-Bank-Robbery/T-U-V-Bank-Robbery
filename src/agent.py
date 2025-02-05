# src/agent.py

import time
import random

class AIHeistAgent:
    def __init__(self, name, mission, difficulty="medium"):
        self.name = name
        self.mission = mission
        self.difficulty = difficulty
        self.status = "idle"

    def start_mission(self):
        print(f"Agent {self.name} is starting the mission: {self.mission}")
        self.status = "in progress"
        self._simulate_progress()

    def _simulate_progress(self):
        progress = 0
        while progress < 100:
            time.sleep(random.uniform(0.5, 1.5))  # Simulating task progression
            progress += random.randint(10, 30)
            print(f"Mission progress: {min(progress, 100)}%")

        self.status = "completed"
        print(f"Agent {self.name} has completed the mission!")

    def report_status(self):
        return f"Agent: {self.name}, Mission: {self.mission}, Status: {self.status}"

# Example usage
if __name__ == "__main__":
    agent = AIHeistAgent(name="Alpha", mission="Bank Heist")
    agent.start_mission()
    print(agent.report_status())
