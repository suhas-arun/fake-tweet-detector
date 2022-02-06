from joblib import dump
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from preprocess import create_df

MODEL_PATH = "models/svc.joblib"
VECT_PATH = "models/count_vect.joblib"

words, dataframe = create_df()
count_vect = CountVectorizer(max_features=dataframe.shape[0])
X = count_vect.fit_transform(words).toarray()
y = dataframe.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

svc = SVC()
svc.fit(X_train, y_train)

y_pred = svc.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

dump(svc, MODEL_PATH)
dump(count_vect, VECT_PATH)
