from crewai import Agent, Task, Crew

researcher = Agent(
    role="Researcher",
    goal="Find facts about AI",
    backstory="Expert researcher"
)

task = Task(
    description="Research the future of AI",
    agent=researcher
)

crew = Crew(
    agents=[researcher],
    tasks=[task]
)

result = crew.run()
print(result)
