"""
Fast & Smooth Pandemic Simulation (SIR Model)
----------------------------------------------
Python Jackfruit Project : 
Team Members:
1) Sohan D Shetty - PES1UG25EC264
2) Sanjey Raj - PES1UG25AM350
3) Utkarsh Javalkar - PES1UG25AM431
4) Vedant Gupta - PES1UG25EC295
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk

# =============================
# GUI INPUT WINDOW
# =============================
def start_simulation():
    global PEOPLE, INIT_INFECTED, RECOVERY_DAYS
    PEOPLE = int(entry_people.get())
    INIT_INFECTED = int(entry_infected.get())
    RECOVERY_DAYS = float(entry_recovery.get())
    root.destroy()

root = tk.Tk()
root.title("Pandemic Simulation Input")

tk.Label(root, text="Total number of people").grid(row=0, column=0, pady=5)
tk.Label(root, text="Initially infected people").grid(row=1, column=0, pady=5)
tk.Label(root, text="Recovery time (days)").grid(row=2, column=0, pady=5)

entry_people = tk.Entry(root)
entry_people.insert(0, "300")
entry_people.grid(row=0, column=1)

entry_infected = tk.Entry(root)
entry_infected.insert(0, "8")
entry_infected.grid(row=1, column=1)

entry_recovery = tk.Entry(root)
entry_recovery.insert(0, "14")
entry_recovery.grid(row=2, column=1)

tk.Button(root, text="Start Simulation", command=start_simulation)\
    .grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()

# =============================
# TIME & SPEED SETTINGS
# =============================
FPS = 30                       # faster & smoother
DAYS_PER_SECOND = 2
FRAMES_PER_DAY = FPS // DAYS_PER_SECOND   # 15
INTERVAL = int(1000 / FPS)

TOTAL_DAYS = 120
TOTAL_FRAMES = TOTAL_DAYS * FRAMES_PER_DAY

# =============================
# MODEL PARAMETERS
# =============================
INFECTION_RADIUS = 0.035
INFECTION_PROB = 0.01
MOVE_SPEED = 0.03
RECOVERY_FRAMES = int(RECOVERY_DAYS * FRAMES_PER_DAY)

np.random.seed(42)

# =============================
# INITIALIZATION
# =============================
positions = np.random.rand(PEOPLE, 2)
velocities = (np.random.rand(PEOPLE, 2) - 0.5) * MOVE_SPEED

state = np.zeros(PEOPLE, dtype=int)  # 0=S, 1=I, 2=R
state[:INIT_INFECTED] = 1

infection_time = np.zeros(PEOPLE, dtype=int)

days = [0]
S = [(state == 0).sum()]
I = [(state == 1).sum()]
R = [(state == 2).sum()]

colors = np.array(["blue", "red", "green"])

# =============================
# PLOTTING
# =============================
fig, (ax_sim, ax_graph) = plt.subplots(1, 2, figsize=(12, 5))

scatter = ax_sim.scatter(
    positions[:, 0],
    positions[:, 1],
    c=colors[state],
    s=28
)

ax_sim.set_title("Fast Pandemic Simulation")
ax_sim.set_xlim(0, 1)
ax_sim.set_ylim(0, 1)
ax_sim.set_xticks([])
ax_sim.set_yticks([])

line_S, = ax_graph.plot([], [], label="Susceptible")
line_I, = ax_graph.plot([], [], label="Infected")
line_R, = ax_graph.plot([], [], label="Recovered")

ax_graph.set_xlim(0, TOTAL_DAYS)
ax_graph.set_ylim(0, PEOPLE)
ax_graph.set_xlabel("Days")
ax_graph.set_ylabel("People")
ax_graph.legend()
ax_graph.grid(alpha=0.3)

# =============================
# UPDATE FUNCTION
# =============================
def update(frame):
    global positions, velocities, state, infection_time

    # Move people
    positions += velocities

    # Bounce off walls
    hit = (positions < 0) | (positions > 1)
    velocities[hit] *= -1
    positions[:] = np.clip(positions, 0, 1)

    # Infection spread
    infected = np.where(state == 1)[0]
    susceptible = np.where(state == 0)[0]

    if infected.size and susceptible.size:
        pi = positions[infected]
        ps = positions[susceptible]

        diff = pi[:, None, :] - ps[None, :, :]
        dist2 = np.sum(diff ** 2, axis=2)

        min_dist = dist2.min(axis=0)
        close = min_dist < INFECTION_RADIUS ** 2

        rand = np.random.rand(close.sum())
        new_inf = susceptible[close][rand < INFECTION_PROB]

        state[new_inf] = 1
        infection_time[new_inf] = 0

    # Recovery
    infection_time[state == 1] += 1
    recovered = np.where(
        (state == 1) & (infection_time >= RECOVERY_FRAMES)
    )[0]
    state[recovered] = 2

    # Update graph once per day
    if frame % FRAMES_PER_DAY == 0:
        day = frame // FRAMES_PER_DAY
        days.append(day)
        S.append((state == 0).sum())
        I.append((state == 1).sum())
        R.append((state == 2).sum())

        line_S.set_data(days, S)
        line_I.set_data(days, I)
        line_R.set_data(days, R)

    scatter.set_offsets(positions)
    scatter.set_color(colors[state])

    return scatter, line_S, line_I, line_R

# =============================
# RUN SIMULATION
# =============================
ani = FuncAnimation(
    fig,
    update,
    frames=TOTAL_FRAMES,
    interval=INTERVAL,
    blit=False
)

plt.tight_layout()
plt.show()

print("Simulation complete.")
print("Final S, I, R:", S[-1], I[-1], R[-1])
