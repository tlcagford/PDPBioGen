try:
    response = client.chat.completions.create(...)
except openai.APIError as e:
    print(f"OpenAI API error: {e}")
    return
except Exception as e:
    print(f"Unexpected error: {e}")
    return
