import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [0., 0.],
    [0., 1.],
    [1., 0.],
    [1., 1.]
])

y = np.array([
    [0.],
    [1.],
    [1.],
    [0.]
])

print("X shape:", X.shape)
print("y shape:", y.shape)

def init_params():
    rng = np.random.default_rng(42)

    W1 = rng.normal(0, 0.8, (2, 4))
    b1 = np.zeros((1, 4))

    W2 = rng.normal(0, 0.8, (4, 1))
    b2 = np.zeros((1, 1))

    return W1, b1, W2, b2

W1, b1, W2, b2 = init_params()

def forward_mlp(X, W1, b1, W2, b2):
    z1 = X @ W1 + b1
    h = np.tanh(z1)

    y_pred = h @ W2 + b2

    return h, y_pred

h, y_pred = forward_mlp(X, W1, b1, W2, b2)

print("Prediction:")
print(y_pred)
print("Loss:", np.mean((y_pred - y) ** 2))

def backward_mlp(X, y, h, y_pred, W2):
    N = len(X)

    # 출력층의 손실 기울기
    d_pred = 2 * (y_pred - y) / N

    dW2 = h.T @ d_pred
    db2 = np.sum(d_pred, axis=0, keepdims=True)

    # 은닉층으로 기울기 전달
    dh = d_pred @ W2.T
    dz1 = dh * (1 - h ** 2)

    dW1 = X.T @ dz1
    db1 = np.sum(dz1, axis=0, keepdims=True)

    return dW1, db1, dW2, db2

def train_mlp(lr=0.1, epochs=4000):
    W1, b1, W2, b2 = init_params()
    losses = []

    for epoch in range(epochs):
        h, y_pred = forward_mlp(X, W1, b1, W2, b2)

        loss = np.mean((y_pred - y) ** 2)
        losses.append(loss)

        dW1, db1, dW2, db2 = backward_mlp(
            X, y, h, y_pred, W2
        )

        W1 -= lr * dW1
        b1 -= lr * db1
        W2 -= lr * dW2
        b2 -= lr * db2

    h, y_pred = forward_mlp(X, W1, b1, W2, b2)

    return losses, y_pred

losses, predictions = train_mlp()

print("Final predictions:")
print(predictions.round(3))
print("Final loss:", losses[-1])

plt.figure(figsize=(8, 4))
plt.plot(losses)

plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.title("MLP Training Loss")
plt.grid(True)
plt.show()

for lr in [0.01, 0.1, 0.5]:
    losses, predictions = train_mlp(lr=lr)
    plt.plot(losses, label=f"lr={lr}")

plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.title("Learning Rate Comparison")
plt.yscale("log")
plt.legend()
plt.grid(True)
plt.show()