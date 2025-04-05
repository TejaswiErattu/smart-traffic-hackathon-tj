# tests/test_traffic_light_agent.py

import unittest
from traffic_light_agent import TrafficLightAgent

class TestTrafficLightAgent(unittest.TestCase):

    def setUp(self):
        self.agent = TrafficLightAgent("Intersection-Test")

    def test_initial_state(self):
        self.assertEqual(self.agent.state, "RED")
        self.assertEqual(self.agent.traffic_queue, 0)
        self.assertFalse(self.agent.emergency_detected)

    def test_low_traffic_red_light(self):
        self.agent.receive_event("TRAFFIC_UPDATE", {"vehicle_count": 2})
        self.agent.decide_signal()
        self.assertEqual(self.agent.state, "RED")

    def test_medium_traffic_yellow_light(self):
        self.agent.receive_event("TRAFFIC_UPDATE", {"vehicle_count": 5})
        self.agent.decide_signal()
        self.assertEqual(self.agent.state, "YELLOW")

    def test_high_traffic_green_light(self):
        self.agent.receive_event("TRAFFIC_UPDATE", {"vehicle_count": 15})
        self.agent.decide_signal()
        self.assertEqual(self.agent.state, "GREEN")

    def test_emergency_vehicle_override(self):
        self.agent.receive_event("TRAFFIC_UPDATE", {"vehicle_count": 1})
        self.agent.receive_event("EMERGENCY_VEHICLE")
        self.agent.decide_signal()
        self.assertEqual(self.agent.state, "GREEN")
        self.assertTrue(self.agent.emergency_detected)

    def test_clear_emergency_resets_logic(self):
        self.agent.receive_event("EMERGENCY_VEHICLE")
        self.agent.receive_event("CLEAR_EMERGENCY")
        self.agent.receive_event("TRAFFIC_UPDATE", {"vehicle_count": 1})
        self.agent.decide_signal()
        self.assertFalse(self.agent.emergency_detected)
        self.assertEqual(self.agent.state, "RED")

if __name__ == '__main__':
    unittest.main()
