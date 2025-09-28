import dotenv

dotenv.load_dotenv()

from crewai import Crew, Agent, Task
from crewai.project import CrewBase, agent, task, crew
from tools import search_tool, scrape_tool

@CrewBase
class NewsReaderAgent:

    @agent
    def news_hunter_agent(self):
        return Agent(
            config=self.agents_config["news_hunter_agent"],
            tools=[search_tool, scrape_tool],
        )

    @agent
    def summarizer_agent(self):
        return Agent(
            config=self.agents_config["summarizer_agent"],
            tools=[scrape_tool],
        )

    @agent
    def curator_agent(self):
        return Agent(
            config=self.agents_config["curator_agent"],
        )

    @task
    def content_harvesting_task(self):
        return Task(
            config=self.tasks_config["content_harvesting_task"],
        )

    @task
    def summarization_task(self):
        return Task(
            config=self.tasks_config["summarization_task"],
        )

    @task
    def final_report_assembly_task(self):
        return Task(
            config=self.tasks_config["final_report_assembly_task"],
        )

    @crew
    def crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )

result = NewsReaderAgent().crew().kickoff(
    inputs={
        "topic": "Latest advancements in renewable energy technologies and language: Korean",
    }
)

for task_output in result.tasks_output:
    print(task_output)

# @CrewBase
# class TranslatorCrew:
#
#     @agent
#     def translator_agent(self):
#         return Agent(
#             config=self.agents_config["translator_agent"],
#         )
#
#     @agent
#     def counter_agent(self):
#         return Agent(
#             config=self.agents_config["counter_agent"],
#             tools=[count_letters],
#         )
#
#     @task
#     def translate_task(self):
#         return Task(
#             config=self.tasks_config["translate_task"],
#         )
#
#     @task
#     def retranslate_task(self):
#         return Task(
#             config=self.tasks_config["retranslate_task"],
#         )
#
#     @task
#     def count_task(self):
#         return Task(
#             config=self.tasks_config["count_task"],
#         )
#
#     @crew
#     def assemble_crew(self):
#         return Crew(
#             agents=self.agents,
#             tasks=self.tasks,
#             verbose=True,
#         )


# TranslatorCrew().assemble_crew().kickoff(
#     inputs={
#         "sentence": "I'm Geun and I like to ride my bicicle in Napoli",
#     }
# )