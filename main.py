# main.py

import asyncio
from traffic_light_agent import TrafficLightAgent

async def run_simulation():
    # Create agents for 3 intersections
    agents = [TrafficLightAgent(f"Intersection-{i}") for i in range(3)]

    # Schedule agent loops
    tasks = [agent.process() for agent in agents]

    # Simulate random events
    async def simulate_events():
        while True:
            for agent in agents:
                traffic_data = {"vehicle_count": random.randint(0, 20)}
                agent.receive_event("TRAFFIC_UPDATE", traffic_data)

                if random.random() < 0.1:  # 10% chance of emergency
                    agent.receive_event("EMERGENCY_VEHICLE")
                elif random.random() < 0.3:
                    agent.receive_event("CLEAR_EMERGENCY")

            await asyncio.sleep(3)

    tasks.append(simulate_events())

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    import random
    asyncio.run(run_simulation())
