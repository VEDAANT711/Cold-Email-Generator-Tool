# import os
# from langchain_groq import ChatGroq
# from langchian_core.promots import PromotTemplate
# from langchain_core.paeser import OutputParserException
# from dotenv import load_dotenv

# load_dotenv()

# class Chain:

#     def __init__(self):
#         self.llm = ChatGroq(temperature=0,groq_api_key=os.getenv("groq_api_key"),model_name="llama-3.1-70b-versatile")



#     def extract_jobs(self, cleaned_text):
#         prompt_extract = PromptTemplate.from_template(

#             """
#              ### SCRAPED TEXT FROM WEBSITE 
#              {page_data}
#              ### INSTRUCTION:
#              The scraped text is from the career's page of website.
#              Your job is to extract the job postings and return them in JSON format containing the 
#              following keys : `role`, `experience`, `skill`, `description`.
#              only return the valid JSON.
#              ## VALID JSON (NO PREAMBLE):
             
#             """  
#         )

#         chain_extract = prompt_extract | llm
#         res = chain_extract.invoke(input={'page_data':cleaned_text})
#         try:
#              json_parser = JsonOutputParser()
#              res = json_parser.parse(res.content)
#         except OutputParserException:
#              raise OutputParserException("Context too big. Unable to parse jobs.")
#         return res if isinstance(res, list) else [res]
    

#     def write_mail(self,job,links):
#         promt_email = PromptTemplate.from_template(
#                """
#              #JOB DESCRIPTION:
#              {job_description}

#              ##INSTRUCTION:
#              Your task is to compose a professional cold email addressed to an Hiring manager nike regarding potential 
#              job opportunities. The email should introduce the candidate, Vedant Gaikwad, 
#              and emphasize his key skills(fresher -1 yr), including expertise in Python, SQL, data analysis with 
#              tools like Power BI, machine learning, and web development. The email should demonstrate genuine interest 
#              in discussing relevant roles, and articulate how the candidate’s experience and qualifications align with the company's needs. 
#              The tone should be courteous, concise, and focused on encouraging a positive response from the recruiter. 
#              also showcase my portfolio : {link_list}
#              Do not provide a preamble.
#              ###EMAIL (NO PREAMBLE):
    
#              """    
#         )
             
#     chain_email = prompt_email |self. llm
#     res = chain_email.invoke({"job_description":str(job), "link_list":links})
#     return res.content

        


# if __name__ == "__main__":
#     print(os.getenv("groq_api_key"))


import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("groq_api_key"), model_name="llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(

            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ##INSTRUCTION:
              Your task is to compose a professional cold email addressed to an Hiring manager nike regarding potential 
              job opportunities. The email should introduce the candidate, Vedant Gaikwad, 
              and emphasize his key skills(fresher -1 yr), including expertise in Python, SQL, data analysis with 
              tools like Power BI, machine learning, and web development. The email should demonstrate genuine interest 
              in discussing relevant roles, and articulate how the candidate’s experience and qualifications align with the company's needs. 
              The tone should be courteous, concise, and focused on encouraging a positive response from the recruiter. 
              also showcase my portfolio : {link_list}
              Do not provide a preamble.
              ###EMAIL (NO PREAMBLE):
    
             """ 
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("groq_api_key"))