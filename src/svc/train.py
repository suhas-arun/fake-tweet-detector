from sklearn.metrics import confusion_matrix, accuracy_score
from preprocess import create_df
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from joblib import dump

words, dataframe = create_df()
count_vect = CountVectorizer(max_features=6424)
X = count_vect.fit_transform(words).toarray()
y = dataframe.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=21
)

svc = SVC()
svc.fit(X_train, y_train)

y_pred = svc.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

dump(svc, "models/svc.joblib")
