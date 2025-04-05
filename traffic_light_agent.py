# agents/traffic_light_agent.py

import random
import asyncio
from datetime import datetime

class TrafficLightAgent:
    def __init__(self, intersection_id):
        self.id = intersection_id
        self.state = "RED"  # Initial state
        self.traffic_queue = 0  # Number of vehicles waiting
        self.emergency_detected = False
        self.last_updated = datetime.now()

    def receive_event(self, event_type, data=None):
        if event_type == "TRAFFIC_UPDATE":
            self.traffic_queue = data.get("vehicle_count", 0)
        elif event_type == "EMERGENCY_VEHICLE":
            self.emergency_detected = True
        elif event_type == "CLEAR_EMERGENCY":
            self.emergency_detected = False

    async def process(self):
        while True:
            await asyncio.sleep(2)  # Simulate decision-making delay
            self.decide_signal()
            self.display_status()

    def decide_signal(self):
        if self.emergency_detected:
            self.state = "GREEN"
        elif self.traffic_queue > 10:
            self.state = "GREEN"
        elif self.traffic_queue < 3:
            self.state = "RED"
        else:
            self.state = "YELLOW"

        self.last_updated = datetime.now()

    def display_status(self):
        print(f"[{self.id}] State: {self.state} | Queue: {self.traffic_queue} | Emergency: {self.emergency_detected} | Time: {self.last_updated.strftime('%H:%M:%S')}")
