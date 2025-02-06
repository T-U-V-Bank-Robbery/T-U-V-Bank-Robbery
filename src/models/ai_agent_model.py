# src/models/ai_agent_model.py

import random

class AIAgentModel:
    def __init__(self, knowledge_base=None):
        # Initialize with a knowledge base or create an empty one
        self.knowledge_base = knowledge_base if knowledge_base else {}

    def learn_from_mission(self, mission_name, outcome):
        """Store mission outcomes in the knowledge base to optimize future strategies."""
        if mission_name not in self.knowledge_base:
            self.knowledge_base[mission_name] = {"success": 0, "failure": 0}
        
        # Update based on outcome
        if outcome == "success":
            self.knowledge_base[mission_name]["success"] += 1
        else:
            self.knowledge_base[mission_name]["failure"] += 1

    def predict_outcome(self, mission_name):
        """Use previous mission outcomes to predict future performance."""
        if mission_name not in self.knowledge_base:
            return "Prediction unavailable (no data)"
        
        success_rate = self.knowledge_base[mission_name]["success"]
        failure_rate = self.knowledge_base[mission_name]["failure"]

        # Simple probability-based prediction
        if success_rate > failure_rate:
            return "High chance of success"
        elif success_rate < failure_rate:
            return "High chance of failure"
        else:
            return "Uncertain outcome"

    def suggest_strategy(self):
        """Suggest a strategy based on the current knowledge base."""
        strategies = ["stealth", "direct assault", "negotiation", "hacking"]
        return random.choice(strategies)

# Example usage
if __name__ == "__main__":
    model = AIAgentModel()
    model.learn_from_mission("Bank Heist", "success")
    model.learn_from_mission("Bank Heist", "failure")

    print(model.predict_outcome("Bank Heist"))
    print(f"Suggested strategy: {model.suggest_strategy()}")
