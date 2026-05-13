'''
Nesne oluşturma mantığını istemciden (client) gizleyerek, nesnelerin bir arayüz üzerinden oluşturulmasını sağlar.

'''

class Agent:
    def move(self): pass

class AirAgent(Agent):
    def move(self): return "Uçuyor..."

class LandAgent(Agent):
    def move(self): return "Yürüyor..."


''' 
Pattern uygulama kısmı
'''
class AgentFactory:
    @staticmethod
    def get_agent(agent_type):
        if agent_type == "hava":
            return AirAgent()
        elif agent_type == "kara":
            return LandAgent()

# Kullanım
agent = AgentFactory.get_agent("hava")
print(agent.move())