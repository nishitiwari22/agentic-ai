from openai import OpenAI

client = OpenAI()

def enhance_resume(data):
    prompt = f"""
    Improve this resume content to be professional and ATS-friendly:
    {data}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
