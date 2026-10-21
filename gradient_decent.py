import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x):
    return x**2 - 6*x

def df(x):
    return 2*x - 6

def gradient_descent(init_x, learning_rate=0.1, stop_condition=0.1):
    x = init_x
    i = 0
    history = [(i, x, f(x), df(x), learning_rate)]  # luu lai (iter, x, cost, grad) sau moi buoc de ve hoat hoa

    while True:
        grad = df(x)
        tmp = x - learning_rate * grad

        if df(tmp)*df(x) <0:
            learning_rate /= 2
            continue
        else:
            learning_rate *= 2

        i += 1
        cost = f(tmp)
        print(f"iteration={i} | x={tmp} | cost={cost}")
        history.append((i, tmp, cost, grad,learning_rate))

        if abs(grad) < stop_condition:
            x = tmp
            break

        x = tmp

    return x, history


init_x = -950
x_res, history = gradient_descent(init_x)

xs = np.linspace(-1000, 1000, 400)
ys = f(xs)

fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(xs, ys, 'b-')
point, = ax.plot([], [], 'ro', markersize=10)
trail, = ax.plot([], [], 'r--', linewidth=1, alpha=0.5)  # duong ve vet di cua qua bong
old_balls, = ax.plot([], [], 'ro', markersize=10)  # giu lai anh qua bong o cac vi tri cu

ax.set_title(f"$f(x)=x^2-6x$ | $x={init_x}$ | $learning \ rate=0.1$ | $iter=0$")
status_text = ax.text(0.5, -0.12, "", transform=ax.transAxes, ha="center")

n_frames = len(history)

def update(frame):
    i, x, cost, grad, lr = history[frame]
    point.set_data([x], [cost])

    # lay lai toan bo x, cost tu dau den frame hien tai de ve vet
    trail_xs = [h[1] for h in history[:frame+1]]
    trail_ys = [h[2] for h in history[:frame+1]]
    trail.set_data(trail_xs, trail_ys)

    # giu lai anh qua bong o cac vi tri truoc do (khong tinh vi tri hien tai)
    old_balls.set_data(trail_xs[:-1], trail_ys[:-1])

    status_text.set_text(f"iter {i}/{n_frames}: x={x:.3f}, cost={cost:.3f}, grad={grad:.4f}")
    ax.set_title(f"$f(x)=x^2-6x$ | $x={x:.3f}$ | $learning \ rate$=${lr:.4f}$ | $iter={i}$")
    return point, trail, old_balls, status_text

ani = animation.FuncAnimation(
    fig, update, frames=n_frames, interval=400, repeat=False
)

plt.tight_layout()
plt.show()