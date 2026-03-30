import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = {
    "message": [
        "you won money",
        "free money",
        "input password",
        "how are you doing",
        "hello dear",
        "how was your day",
    ],
    "label": ["spam", "spam", "spam", "not_spam", "not_spam", "not_spam"],
}
df = pd.DataFrame(data)
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(df["message"])
y = df(["label"])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = MultinomialNB()
model.fit(x_train, y_train)
predictions = model.predict(x_test)

print("detected: ", accuracy_score(y_test, predictions))
