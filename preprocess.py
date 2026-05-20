import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm


def clean_text(text):
    return text.encode("utf-8", "ignore").decode("utf-8")


def process_posts(
    raw_file_path,
    processed_file_path="data/processed_posts.json"
):
    enriched_posts = []

    with open(raw_file_path, encoding='utf-8') as file:

        posts = json.load(file)

        for post in posts:

            cleaned_post = clean_text(post['text'])

            metadata = extract_metadata(cleaned_post)

            post["text"] = cleaned_post
            post_with_metadata = post | metadata

            enriched_posts.append(post_with_metadata)

    unified_tags = get_unified_tags(enriched_posts)

    for epost in enriched_posts:

        current_tags = epost['tags']
        new_tags = {unified_tags[tag] for tag in current_tags}
        epost['tags']= list(new_tags)

    with open(processed_file_path, "w", encoding="utf-8") as outfile:
        json.dump(enriched_posts, outfile, indent=4, ensure_ascii=False)

def get_unified_tags(posts_with_metadata):
    unique_tags = set()
    for post in posts_with_metadata:
        unique_tags.update(post['tags'])

    unique_tags_list = ",".join(unique_tags)
    template = '''
    I will give you a list of tags extracted from LinkedIn posts.

    Your task is to unify similar tags.

    Return ONLY valid JSON.

    The JSON should map old tags to unified tags.

    Example:

    Input:
    ["AI", "Artificial Intelligence", "Machine Learning"]

    Output:
    {{
        "AI": "AI",
        "Artificial Intelligence": "AI",
        "Machine Learning": "AI"
    }}

    Rules:
    1. Merge similar tags
    2. Keep names short
    3. No explanation
    4. Return only JSON

    Tags:
    {tags}
    '''

    pt = PromptTemplate.from_template(template)

    chain = pt | llm

    response = chain.invoke({"tags": str(unique_tags_list)})

    try:

        json_parser = JsonOutputParser()

        res = json_parser.parse(response.content)

        return res

    except OutputParserException:

        print("Failed response:")
        print(response.content)


def extract_metadata(post):

    template = '''
        You are given a LinkedIn post.

        Extract:
        1. number of lines
        2. language
        3. tags

        Return ONLY valid JSON.

        JSON format:
        {{
            "line_count": number,
            "language": "English",
            "tags": ["tag1", "tag2"]
        }}

        Rules:
        - maximum 2 tags
        - language should be English or Hinglish
        - no explanation
        - return only JSON

        Post:
        {post}
        '''
   
    pt = PromptTemplate.from_template(template)

    chain = pt | llm

    response = chain.invoke({"post": post})

    try:

        json_parser = JsonOutputParser()

        res = json_parser.parse(response.content)

        return res

    except OutputParserException:

        print("Failed response:")
        print(response.content)

        return {
            "line_count": 0,
            "language": "Unknown",
            "tags": []
        }


if __name__ == "__main__":

    process_posts(
        "data/raw_posts.json",
        "data/processed_posts.json"
    )