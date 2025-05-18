import openai
import os
import sys

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chatgpt_comment(commit_message):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for documenting cryptography Git commits."},
                {"role": "user", "content": f"Write a short informative comment about this Git commit: {commit_message}"}
            ]
        )
        comment = response.choices[0].message.content.strip()
        return comment
    except Exception as e:
        return f"API Call Error: {str(e)}"

if __name__ == "__main__":
    commit_message = sys.argv[1]
    print("Debug: Commit message received:", commit_message)
    print("Debug: API Key loaded:", os.getenv("OPENAI_API_KEY") is not None)
    comment = chatgpt_comment(commit_message)
    print("Debug: Comment returned:", comment)

