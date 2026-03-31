import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "title": ["iron man", "superman", "titanic", "batman", "red roses", "avengers"],
    "genre": ["action", "action", "romance", "action", "romance", "action"],
}

df = pd.DataFrame(data)
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(df["genre"])

similarity = cosine_similarity(x)


def recommend(movie_name):
    index = df[df["title"] == movie_name].index[0]
    score = list(enumerate(similarity[index]))
    score = sorted(score, key=lambda x: x[1], reverse=True)
    print(f"similar movies are '{movie_name}': ")
    for i in score[1:3]:
        print(df.iloc[i[0]], ["title"])
        recommend("iron man")
