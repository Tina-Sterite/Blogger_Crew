# Importing dependencies

from langchain_groq import ChatGroq
from pathlib import Path
from langchain_community.tools import DuckDuckGoSearchRun
from fpdf import FPDF
from crewai import Agent, Task, Crew, Process
from datetime import datetime
from dotenv import load_dotenv
import os


# Environment Variables
load_dotenv()

USER_AGENT = os.getenv("USER_AGENT")

llm = ChatGroq(
        model="llama3-70b-8192",
        api_key=os.getenv('GROQ_API_KEY')
)

# Initialize the DuckDuckGo search tool
search_tool = DuckDuckGoSearchRun()

# Initialize the cache
search_cache = {}

class BlogCrew:
    def __init__(self, blog_topic: str, content_type: str, output_placeholder):
        self.topic = blog_topic
        self.content_type = content_type
        self.output_placeholder = output_placeholder

    def run(self):
        # Define agents
        researcher = Agent(
            role='Senior Research Analyst',
            goal='Uncover cutting-edge developments in AI and data science',
            backstory="""You work at a leading tech think tank. Your expertise lies in identifying emerging trends. You have a knack for dissecting complex data and presenting actionable insights.""",
            verbose=True,
            allow_delegation=False,
            tools=[search_tool],
            llm=llm
        )

        writer = Agent(
            role='Tech Content Strategist',
            goal='Craft compelling content on tech advancements',
            backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles. You transform complex concepts into compelling narratives.""",
            verbose=True,
            allow_delegation=True,
            llm=llm
        )

        # Define tasks
        task1 = Task(
            description=f"""Conduct a comprehensive analysis of the latest advancements in {self.topic}. Identify key trends, breakthrough technologies, and potential industry impacts.""",
            expected_output="Full analysis report in bullet points",
            agent=researcher
        )

        task2 = Task(
            description=f"""Using the insights provided, develop an engaging {self.content_type.lower()} that highlights the most significant advancements in {self.topic}. Your post should be informative yet accessible, catering to a tech-savvy audience. Make it sound cool, avoid complex words so it doesn't sound like AI.""",
            expected_output=f"Full {self.content_type.lower()} of at least 4 paragraphs",
            agent=writer
        )

        # Instantiate the crew with a sequential process
        crew = Crew(
            agents=[researcher, writer],
            tasks=[task1, task2],
            process=Process.sequential,
            verbose=2
        )

        # Get the crew to work
        result = crew.kickoff()
        self.output_placeholder.markdown(result)
        result_str = str(result)
        
        
        # Create the Result_Files directory if it doesn't exist
        result_dir = Path("Result_Files")
        result_dir.mkdir(exist_ok=True)

        # Generate the timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Define file names
        txt_file = str(result_dir / f"{self.topic}_{timestamp}.txt")
        pdf_file = str(result_dir / f"{self.topic}_{timestamp}.pdf")

        # Write the result to a text file
        with open(txt_file, "w") as file:
            file.write(result_str)
        # Create a PDF and write the output to it
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for line in result_str.split("\n"):
            line = line.encode('latin-1', 'replace').decode('latin-1')
            pdf.write(5, line)
            pdf.ln()  # move to next line

        # Save the PDF file
        pdf.output(pdf_file)

        with open(pdf_file, 'rb') as file:
            file_content = file.read()

        return result_str, pdf_file, file_content

