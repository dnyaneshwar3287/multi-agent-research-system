from langchain_groq import ChatGroq
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama3-8b-8192", temperature=0)

react_prompt = PromptTemplate.from_template("""
You are an intelligent agent.

You have access to the following tools:
{tools}

Use the following format:

Question: {input}
Thought: you should think about what to do
Action: one of [{tool_names}]
Action Input: the input to the action
Observation: result of the action
... (repeat Thought/Action/Action Input/Observation as needed)

Thought: I now know the final answer
Final Answer: the final answer to the original question
""")

def build_search_agent():
    agent = create_react_agent(llm, [web_search], react_prompt)
    return AgentExecutor(agent=agent, tools=[web_search], verbose=True)

def build_reader_agent():
    agent = create_react_agent(llm, [scrape_url], react_prompt)
    return AgentExecutor(agent=agent, tools=[scrape_url], verbose=True)
                         
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer."),
    ("human", """Write a detailed research report.

Topic: {topic}

Research:
{research}

Structure:
- Introduction
- Key Findings
- Conclusion
- Sources""")
])

writer_chain = writer_prompt | llm | StrOutputParser()

critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a strict reviewer."),
    ("human", """Improve the following report:

{report}""")
])

critic_chain = critic_prompt | llm | StrOutputParser()