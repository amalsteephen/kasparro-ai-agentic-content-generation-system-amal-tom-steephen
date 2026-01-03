class OrchestratorAgent:
    """
    Coordinates agent execution without enforcing order.
    Agents act autonomously based on shared state.
    """
    def __init__(self, agents, bus):
        self.agents = agents
        self.bus = bus

    def run(self):
        while not self.bus.exists("pages"):
            for agent in self.agents:
                if agent.decide():
                    agent.act()
