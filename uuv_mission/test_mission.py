import pytest
import numpy as np
from uuv_mission.dynamic import Mission

def test_mission_from_csv():
    # Load mission from CSV
    mission = Mission.from_csv("data/mission.csv")
    
    # Check data types
    assert isinstance(mission.reference, np.ndarray)
    assert isinstance(mission.cave_height, np.ndarray)
    assert isinstance(mission.cave_depth, np.ndarray)
    
    # Check arrays have same length
    assert len(mission.reference) == len(mission.cave_height) == len(mission.cave_depth)
    
    # Check some known values from the CSV
    assert mission.reference[0] == 0.0
    assert mission.cave_height[0] == 30.0
    assert mission.cave_depth[0] == -30.0