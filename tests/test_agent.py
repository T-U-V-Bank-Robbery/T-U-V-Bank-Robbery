# tests/test_agent.py

import pytest
from src.agent import AIHeistAgent

@pytest.fixture
def sample_agent():
    return AIHeistAgent(name="TestAgent", mission="TestMission", difficulty="medium")

def test_agent_initialization(sample_agent):
    assert sample_agent.name == "TestAgent"
    assert sample_agent.mission == "TestMission"
    assert sample_agent.difficulty == "medium"
    assert sample_agent.status == "idle"

def test_start_mission(sample_agent):
    sample_agent.start_mission()
    assert sample_agent.status == "completed"

def test_report_status(sample_agent):
    sample_agent.start_mission()
    status = sample_agent.report_status()
    assert "TestAgent" in status
    assert "TestMission" in status
    assert "completed" in status
