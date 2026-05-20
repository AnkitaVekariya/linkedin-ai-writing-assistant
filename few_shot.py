import pandas as pd
from db import get_connection


class FewShotPosts:

    def __init__(self):

        self.df = None

        self.unique_tags = None

        self.load_posts()

    def load_posts(self):

        conn = get_connection()

        self.df = pd.read_sql_query(
            "SELECT * FROM posts",
            conn
        )

        conn.close()

        all_tags = []

        for tags in self.df["tags"]:

            split_tags = tags.split(",")

            all_tags.extend(split_tags)

        self.unique_tags = set(all_tags)

    def get_tags(self):

        return self.unique_tags

    def get_filtered_post(
        self,
        length,
        language,
        tag
    ):

        df_filtered = self.df[

            (self.df['length'] == length) &

            (self.df['language'] == language) &

            (
                self.df['tags'].apply(
                    lambda tags:
                    tag.lower() in tags.lower()
                )
            )
        ]

        # fallback 1
        if df_filtered.empty:

            df_filtered = self.df[
                (self.df['length'] == length) &
                (self.df['language'] == language)
            ]

        # fallback 2
        if df_filtered.empty:

            df_filtered = self.df[
                self.df['language'] == language
            ]

        # fallback 3
        if df_filtered.empty:

            df_filtered = self.df.sample(
                min(3, len(self.df))
            )

        # sort by engagement
        df_filtered = df_filtered.sort_values(
            by="engagement",
            ascending=False
        )

        return df_filtered.head(3).to_dict(
            orient="records"
        )


if __name__ == "__main__":

    fs = FewShotPosts()

    posts = fs.get_filtered_post(
        "Long",
        "English",
        "Motivation"
    )

    print(posts)