# agents/traffic_light_agent.py

import asyncio
from datetime import datetime
import joblib
import os

class TrafficLightAgent:
    def __init__(self, intersection_id):
        self.id = intersection_id
        self.state = "RED"  # Initial state
        self.traffic_queue = 0
        self.emergency_detected = False
        self.last_updated = datetime.now()

        # Load trained AI model
        model_path = os.path.join(os.path.dirname(__file__), "ai_model.pkl")
        self.model = joblib.load(model_path)

    def receive_event(self, event_type, data=None):
        if event_type == "TRAFFIC_UPDATE":
            self.traffic_queue = data.get("vehicle_count", 0)
        elif event_type == "EMERGENCY_VEHICLE":
            self.emergency_detected = True
        elif event_type == "CLEAR_EMERGENCY":
            self.emergency_detected = False

    async def process(self):
        while True:
            await asyncio.sleep(2)
            self.decide_signal()
            self.display_status()

    def decide_signal(self):
        # Use AI model to decide
        X = [[self.traffic_queue, int(self.emergency_detected)]]
        prediction = self.model.predict(X)[0]

        self.state = {0: "RED", 1: "YELLOW", 2: "GREEN"}[prediction]
        self.last_updated = datetime.now()

    def display_status(self):
        print(f"[{self.id}] State: {self.state} | Queue: {self.traffic_queue} | Emergency: {self.emergency_detected} | Time: {self.last_updated.strftime('%H:%M:%S')}")
