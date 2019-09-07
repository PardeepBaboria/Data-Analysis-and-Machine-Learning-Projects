from sklearn.datasets import fetch_20newsgroups_vectorized
from lightning.classification import CDClassifier

# Load News20 dataset from scikit-learn.
bunch = fetch_20newsgroups_vectorized(subset="all")
X = bunch.data
y = bunch.target

# Set classifier options.
clf = CDClassifier(penalty="l1/l2",
                   loss="squared_hinge",
                   multiclass=True,
                   max_iter=20,
                   alpha=1e-4,
                   C=1.0 / X.shape[0],
                   tol=1e-3)

# Train the model.
clf.fit(X, y)

# Accuracy
print(clf.score(X, y))

# Percentage of selected features
print(clf.n_nonzero(percentage=True))