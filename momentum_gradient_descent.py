import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x):
    return x**2 + 10 * np.sin(x)

def df(x):
    return 2 * x + 10 * np.cos(x)

def gradient_descent(init_x, learning_rate=0.1, stop_condition=0.1, max_iter=10000):
    x = init_x
    i = 0
    history = [(i, x, f(x), df(x), learning_rate)]  # luu lai (iter, x, cost, grad) sau moi buoc de ve hoat hoa

    vt = 0
    ganma=0.9
    while i < max_iter:
        grad = df(x)
        vt = ganma*vt + learning_rate*grad
        tmp = x - vt

        if df(tmp)*df(x) <0:
            learning_rate /= 2
            continue
        else:
            learning_rate *= 2

        i += 1
        cost = f(tmp)
        print(f"iteration={i} | x={tmp} | cost={cost}")
        history.append((i, tmp, cost, grad,learning_rate))

        if abs(df(tmp)) < stop_condition:
            x = tmp
            break

        x = tmp
    else:
        raise RuntimeError(f"Gradient descent did not converge after {max_iter} iterations")

    return x, history


init_x =5
x_res, history = gradient_descent(init_x)

xs = np.linspace(-4, 6, 400)
ys = f(xs)

fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(xs, ys, 'b-')
point, = ax.plot([], [], 'ro', markersize=10)
final_point, = ax.plot([], [], 'bo', markersize=10, zorder=5)
trail, = ax.plot([], [], 'r--', linewidth=1, alpha=0.5)  # duong ve vet di cua qua bong
old_balls, = ax.plot([], [], 'ro', markersize=10)  # giu lai anh qua bong o cac vi tri cu

ax.set_title(f"$f(x)=x^2+10\\sin(x)$ | $x={init_x}$ | $learning \\ rate=0.1$ | $iter=0$")
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
    ax.set_title(f"$f(x)=x^2+10\\sin(x)$ | $x={x:.3f}$ | $learning \\ rate$=${lr:.4f}$ | $iter={i}$")
    return point, trail, old_balls, status_text

_old_update = update

def update_with_final(frame):
    artists = _old_update(frame)  # run original drawing logic unchanged
    if frame == n_frames - 1:
        # last frame: show the final position in blue
        final_point.set_data([history[frame][1]], [history[frame][2]])
        point.set_data([], [])  # hide the red ball so blue is visible
    else:
        final_point.set_data([], [])
    return (*artists, final_point)


ani = animation.FuncAnimation(
    fig, update, frames=n_frames, interval=400, repeat=False
)
ani = animation.FuncAnimation(
    fig, update_with_final, frames=n_frames, interval=400, repeat=False
)
plt.tight_layout()
plt.show()
