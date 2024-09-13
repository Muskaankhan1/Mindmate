
# import openai
# import gradio as gr
# import os

# # Load OpenAI API key from environment variables
# openai.api_key = os.getenv("sk-ATE0cyoQfz1omTgDJuX-np4bQgzc4L6XB1jICcGKd1T3BlbkFJILes5fVAfbFmMi9x7YG5WCLf36eerANaa33SQcZVoA")

# # Function to interact with the OpenAI API
# def chatgpt_response(user_input):
#     try:
#         response = openai.Completion.create(
#             engine="text-davinci-003",  # Ensure you're using the correct engine
#             prompt=user_input,
#             max_tokens=150,
#             temperature=0.7,
#             n=1,
#             stop=None
#         )
#         return response.choices[0].text.strip()
#     except openai.error.OpenAIError as e:
#         # Capture OpenAI API errors and return a meaningful message to the user
#         return f"Error: {str(e)}"

# # Create a Gradio interface
# interface = gr.Interface(
#     fn=chatgpt_response,
#     inputs=gr.Textbox(label="Ask anything..."),
#     outputs=gr.Textbox(label="Response"),
#     title="ChatGPT Chatbot",
#     description="Ask anything and get a response from ChatGPT!"
# )

# # Launch the interface with public sharing enabled
# interface.launch(share=True)
import openai
import gradio as gr
import os

# Load OpenAI API key from environment variables
openai.api_key = os.getenv("sk-ATE0cyoQfz1omTgDJuX-np4bQgzc4L6XB1jICcGKd1T3BlbkFJILes5fVAfbFmMi9x7YG5WCLf36eerANaa33SQcZVoA")

# Function to interact with the OpenAI API
def chatgpt_response(user_input):
    try:
        print(f"User input: {user_input}")  # Print user input to console for debugging
        response = openai.Completion.create(
            engine="text-davinci-003",  # Ensure you're using the correct engine
            prompt=user_input,
            max_tokens=150,
            temperature=0.7,
            n=1,
            stop=None
        )
        response_text = response.choices[0].text.strip()
        print(f"API response: {response_text}")  # Print response from API to console
        return response_text
    except openai.error.OpenAIError as e:
        print(f"Error: {str(e)}")  # Print any errors to the console
        return f"Error: {str(e)}"

# Create a Gradio interface
interface = gr.Interface(
    fn=chatgpt_response,
    inputs=gr.Textbox(label="Ask anything..."),
    outputs=gr.Textbox(label="Response"),
    title="ChatGPT Chatbot",
    description="Ask anything and get a response from ChatGPT!"
)

# Launch the interface with public sharing enabled
interface.launch(share=True)
