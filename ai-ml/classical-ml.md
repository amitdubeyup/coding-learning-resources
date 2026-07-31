# Classical ML & the ML coding round

The GenAI-first material is in [`foundations.md`](foundations.md), [`rag.md`](rag.md),
and [`agents.md`](agents.md). This file covers **classical ML** — still tested for
data-science and many AI-engineering loops — plus the **ML coding round** (implement an
algorithm from scratch) and **ML system design**. If your target role leans DS/ML
rather than pure GenAI, this is your tier.

## Contents
- [Fundamentals](#fundamentals)
- [Core algorithms](#core-algorithms)
- [Model evaluation](#model-evaluation)
- [Feature engineering](#feature-engineering)
- [Imbalanced data](#imbalanced-data)
- [The ML coding round](#the-ml-coding-round)
- [ML system design](#ml-system-design)
- [Trade-offs to voice](#trade-offs-to-voice)

---

## Fundamentals

- **Learning types:** supervised (labeled data → predict), unsupervised (find
  structure), reinforcement (reward-driven).
- **Bias–variance:** high **bias** = underfitting (model too simple, misses signal);
  high **variance** = overfitting (model memorizes noise, fails to generalize). Total
  error trades off between them — the central tension in ML.
- **Fixing overfitting:** more/cleaner data, **regularization** (L1/Lasso drives
  weights to zero → feature selection; L2/Ridge shrinks them), dropout (NNs), early
  stopping, a simpler model, and cross-validation to detect it.
- **Train / validation / test discipline:** train on one split, tune on validation,
  and touch **test only once** at the end. Use **k-fold cross-validation** for a robust
  estimate on limited data.
- **Data leakage — the classic gotcha:** information from the future or the target
  sneaks into training. Causes: fitting a scaler/encoder on the *full* dataset before
  splitting, features that encode the label, or temporal leakage in time series.
  **Fit all transforms on the training split only.**

## Core algorithms

Know each algorithm's one-line intuition, **when to use it**, and its key knobs:

- **Linear regression** — predict a continuous value; minimizes squared error;
  interpretable coefficients.
- **Logistic regression** — binary classification via the sigmoid; outputs
  probabilities; a strong, interpretable baseline (great first model in fintech for
  explainability).
- **Decision tree** — recursive splits by impurity (Gini/entropy); very interpretable;
  overfits unless you limit depth / prune.
- **Random forest** — many bagged trees voting; robust, little tuning, gives feature
  importance.
- **Gradient boosting (XGBoost / LightGBM)** — trees added sequentially, each
  correcting the last's errors; **usually the winner on tabular data**; tune learning
  rate, depth, and n_estimators; watch overfitting.
- **SVM** — maximum-margin classifier; kernels handle non-linear boundaries; strong in
  high-dimensional spaces.
- **k-Nearest Neighbors** — predict from the k closest points; no training cost but slow
  at inference; sensitive to scaling and the choice of k.
- **Naive Bayes** — probabilistic, assumes feature independence; fast; a solid text/spam
  baseline.
- **k-means** — unsupervised clustering into k groups; choose k via elbow/silhouette;
  sensitive to initialization and feature scale.
- **PCA** — linear dimensionality reduction that preserves variance; for
  visualization/denoising and speeding up downstream models.

## Model evaluation

**Choosing the metric is the interview** — it must match the cost of each error type.

- **Classification:** accuracy is misleading under class imbalance; use **precision**
  (of predicted positives, how many are right), **recall** (of actual positives, how
  many you caught), **F1** (their harmonic mean), the **confusion matrix**, **ROC-AUC**,
  and **PR-AUC** (more informative than ROC-AUC when positives are rare). The
  **precision/recall trade-off** is tuned by the decision threshold.
- **Regression:** **RMSE** (penalizes large errors), **MAE** (robust to outliers),
  **R²** (variance explained).
- **Example reasoning (fraud):** missing fraud (false negative) is very costly, but
  blocking legitimate customers (false positive) hurts trust and revenue — so you
  optimize **recall** while keeping precision acceptable, and tune the threshold to the
  business's cost ratio rather than chasing accuracy.

## Feature engineering

- **Scaling/normalization** — required for distance- and gradient-based models (kNN,
  SVM, linear/logistic, NNs); tree models don't need it.
- **Encoding categoricals** — one-hot for low cardinality; target/frequency encoding
  for high cardinality (careful of leakage — encode using training folds only).
- **Missing values** — impute (mean/median/model-based) and often add a "was-missing"
  flag.
- **Feature selection** — correlation filtering, model feature importance, or L1
  regularization.

## Imbalanced data

Ubiquitous in fraud, churn, and defect detection. Don't report accuracy on a 99:1
dataset — a "predict everything negative" model scores 99%. Instead:
- Evaluate with **PR-AUC, recall, F1**, not accuracy.
- Use **class weights**, **resampling** (oversample the minority / SMOTE, or undersample
  the majority), and **threshold tuning**.
- Keep a human-review path for borderline cases in high-stakes systems.

## The ML coding round

Interviewers often ask you to implement a core algorithm in NumPy — testing whether you
understand the math, not just the API. The recurring ones:

**Train/test split + a metric**
```python
import numpy as np

def train_test_split(X, y, test_size=0.2, seed=0):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(X))
    cut = int(len(X) * (1 - test_size))
    tr, te = idx[:cut], idx[cut:]
    return X[tr], X[te], y[tr], y[te]

def precision_recall(y_true, y_pred):
    tp = np.sum((y_pred == 1) & (y_true == 1))
    fp = np.sum((y_pred == 1) & (y_true == 0))
    fn = np.sum((y_pred == 0) & (y_true == 1))
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    return precision, recall
```

**Linear regression via gradient descent**
```python
def linear_regression_gd(X, y, lr=0.01, epochs=1000):
    X = np.c_[np.ones(len(X)), X]           # add bias term
    w = np.zeros(X.shape[1])
    n = len(y)
    for _ in range(epochs):
        preds = X @ w
        grad = (2 / n) * X.T @ (preds - y)  # gradient of MSE
        w -= lr * grad
    return w
```

**k-means**
```python
def kmeans(X, k, iters=100, seed=0):
    rng = np.random.default_rng(seed)
    centroids = X[rng.choice(len(X), k, replace=False)]
    for _ in range(iters):
        dists = np.linalg.norm(X[:, None] - centroids[None], axis=2)
        labels = dists.argmin(axis=1)
        new = np.array([X[labels == j].mean(axis=0) if np.any(labels == j)
                        else centroids[j] for j in range(k)])
        if np.allclose(new, centroids):
            break
        centroids = new
    return labels, centroids
```

**k-Nearest Neighbors**
```python
def knn_predict(X_train, y_train, X_test, k=3):
    preds = []
    for x in X_test:
        d = np.linalg.norm(X_train - x, axis=1)
        nn = y_train[np.argsort(d)[:k]]
        preds.append(np.bincount(nn).argmax())   # majority vote
    return np.array(preds)
```
Be ready to state complexity (kNN inference is O(n·d) per query), explain the
gradient-descent update, and say why you scale features for distance-based models.

## ML system design

A repeatable framework for "design an ML system for X":
1. **Frame the problem** — what you predict, the label, the metric, and whether it's
   **batch or real-time**.
2. **Data & features** — sources, a feature store, and leakage-safe feature computation.
3. **Model** — start simple (logistic/GBM), justify any complexity.
4. **Training & validation** — splits (temporal for time series), CV, retraining cadence.
5. **Serving** — batch vs low-latency online; where features come from at inference.
6. **Monitoring** — **data/concept drift**, performance decay, and a **retraining
   trigger**; a feedback loop from ground-truth labels.

**Worked example — real-time fraud detection (fits a FinTech loop):**
- **Frame:** per-transaction binary classification → fraud probability, served in
  <~100 ms, on an extremely imbalanced, cost-asymmetric problem.
- **Features:** transaction (amount, time, merchant, geo), user velocity/history
  (rolling counts over windows), device/IP signals — served from a low-latency
  **feature store**.
- **Model:** gradient-boosted trees (strong on tabular) with **calibrated**
  probabilities; a logistic baseline for explainability.
- **Decisioning:** threshold into allow / **review** / block; borderline cases go to a
  human-review queue.
- **Imbalance:** class weights, **PR-AUC/recall** focus, threshold tuned to the
  fraud-loss vs false-positive cost ratio.
- **Monitoring:** fraud patterns drift fast → drift detection, frequent retraining, and
  a feedback loop from confirmed fraud/chargebacks.
- **Regulated twist:** finance often demands **explainability** (SHAP / reason codes)
  and audit trails — which can pull you toward more interpretable models. Voice that
  trade-off.

(For a **recommendation system**, name the two-stage pattern — cheap **candidate
generation** then expensive **ranking** — and collaborative vs content-based filtering.)

## Trade-offs to voice
- **Interpretability vs accuracy** — regulated finance often needs explainable models
  (logistic / GBM + SHAP) over an opaque one.
- **Batch vs real-time** — throughput/simplicity vs latency/freshness.
- **More features vs latency / leakage risk** — richer signal vs serving cost and
  leakage.
- **Precision vs recall** — tuned to the business cost of each error, not accuracy.
- **Simple model first** — a logistic baseline you understand beats a fragile deep model
  you can't debug or explain.
