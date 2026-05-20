from llm_helper import llm


def get_length_str(length):

    if length == "Short":
        return "1 to 5 lines"

    if length == "Medium":
        return "5 to 10 lines"

    if length == "Long":
        return "11 to 15 lines"


def generate_post(length, language, topic, tone, few_shot_examples):

    length_str = get_length_str(length)

    examples_text = ""

    for i, post in enumerate(few_shot_examples[:2]):

        examples_text += f'''

Example {i+1}:

{post["text"]}

'''

    prompt = f'''
    Generate a LinkedIn post using the following requirements.

    Topic: {topic}
    Length: {length_str}
    Language: {language}
    Tone: {tone}

    Rules:
    - No preamble
    - Human-like tone
    - Professional LinkedIn style
    - Use short readable paragraphs
    - Hook the reader in the first line
    - Use English script only
    - Follow the selected tone consistently

    Tone Guidelines:

    - Professional:
    formal and polished

    - Casual:
    conversational and friendly

    - Motivational:
    inspiring and emotional

    - Storytelling:
    narrative-driven and personal

    - Technical:
    educational and knowledge-focused

    Here are some example posts to mimic writing style:

    {examples_text}

    Now generate a new post.
    '''

    response = llm.invoke(prompt)

    return response.content
