import os
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama


def generate_cover_letter_open_source(job_description, resume, selected_model, context_length=8000):
    # print(f"selected_model: {selected_model}, "
    #       f"{AVAILABLE_MODELS_GGUF[selected_model]['model_file']}, {AVAILABLE_MODELS_GGUF[selected_model]['model_type']}")
    # print(f"context_length: {context_length}")

    prompt = (f"Do the following steps: "
              f"1. Read the following job description,"
              f"2. Read the following resume, "
              f"3. Write a formal cover letter to the hiring manager for the job description based on the given resume, "
              # f"4. The cover letter MUST BE within {output_size_range[0]} to {output_size_range[1]} words. "
              # f"4. The cover letter MUST BE within 100 words. "
              f"4. Return ONLY the cover letter ONCE, nothing else. "
              f"Job Description: '{job_description}'. Resume: '{resume}'")

    # prompt = "What is an LLM"

    llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0,
    # other params...
)

    llm_response = llm.invoke(prompt)

    return llm_response



