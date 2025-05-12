from openai import OpenAI
import streamlit as st




openai_api_key = st.secrets['OPENAI_API_KEY']


def get_answer(question):
    try:
        
        client = OpenAI(api_key=openai_api_key)
        response = client.responses.create(
            model="gpt-4.1-nano",
            input=[
            {
                "role": "system",
                "content": [
                {
                    "type": "input_text",
                    "text": "You are an intelligent assistant. Answer the following question: \
                    - If it is a math problem, provide the answer with detailed steps. \
                    - If it is a theoretical question, provide a clear and concise explanation."
                }
                ]
            },
            {
                "role": "user",
                "content": [
                {
                    "type": "input_text",
                    "text": question
                }
                ]
            }
            ],
            text={
            "format": {
                "type": "text"
            }
            },
            reasoning={},
            tools=[],
            temperature=1,
            max_output_tokens=2048,
            top_p=1,
            store=True
        )
        temp = response.to_dict()["output"]
        answer = temp[0].get("content")[0].get("text")
        return answer 
        #return answer

    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    question = "What is the capital of India?"
    answer = get_answer(question)
    print(answer)
    