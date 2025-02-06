# src/main.py

from agent import AIHeistAgent

def main():
    print("Welcome to the AI Heist Agent System!")
    
    # Prompt user for agent setup
    agent_name = input("Enter the agent's name: ")
    mission_name = input("Enter the mission name: ")
    difficulty = input("Select mission difficulty (easy, medium, hard): ")

    # Create and start the AI agent
    agent = AIHeistAgent(name=agent_name, mission=mission_name, difficulty=difficulty)
    print("\nInitializing mission...")
    agent.start_mission()
    
    # Report final status
    print("\nMission completed. Final status report:")
    print(agent.report_status())

if __name__ == "__main__":
    main()
