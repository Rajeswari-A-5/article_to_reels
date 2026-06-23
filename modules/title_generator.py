import ollama


def generate_title(summary):

    prompt = f"""
    Generate a short and catchy title from this summary.

    Summary:
    {summary}

    Return only the title.
    """

    response = ollama.chat(

        model="llama3.2",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]