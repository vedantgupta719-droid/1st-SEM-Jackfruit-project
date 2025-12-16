# Fast & Smooth Pandemic Simulation (SIR Model)

## 📌 Project Overview
This project is a **Python-based pandemic simulation** that demonstrates the **SIR epidemiological model** using an **agent-based approach**.  
Each person is represented as a moving dot, and the spread of infection is visualized in real time along with **S, I, R graphs**.

The project was developed as part of a **Python / Computational Problem Solving / Engineering Mini Project**.

---

## 👨‍💻 Team Members
- **Sohan D Shetty** – PES1UG25EC264  
- **Sanjey Raj** – PES1UG25AM350  
- **Utkarsh Javalkar** – PES1UG25AM431  
- **Vedant Gupta** – PES1UG25EC295  

---

## 🎯 Objectives
- To understand the **SIR (Susceptible–Infected–Recovered)** model  
- To simulate **pandemic spread dynamically**
- To visualize:
  - Human movement
  - Infection spread
  - Recovery process
  - SIR curves over time
- To apply Python concepts such as:
  - NumPy
  - Matplotlib animations
  - Tkinter GUI
  - Functions and arrays

---

## 🧠 Concept Used: SIR Model
The population is divided into:
- **S – Susceptible** (Healthy but can get infected)
- **I – Infected** (Currently infected and can spread disease)
- **R – Recovered** (Recovered and immune)

Transitions:
- S → I (based on distance and probability)
- I → R (after recovery time)

---

## 🖥️ Features
✔ GUI input using **Tkinter**  
✔ Smooth animation using **Matplotlib FuncAnimation**  
✔ Real-time **moving agents**  
✔ Live **SIR graph**  
✔ Adjustable parameters  
✔ Beginner-friendly logic  

---

## 🧾 User Inputs (GUI)
When the program starts, a window appears asking for:

| Input | Description | Example |
|-----|------------|--------|
| Total number of people | Population size | 300 |
| Initially infected people | Starting infected count | 8 |
| Recovery time (days) | Days to recover | 14 |

---

## ⚙️ Parameters Used Internally
- Infection Radius
- Infection Probability
- Movement Speed
- Frames per Day
- Total Simulation Days

These control how fast and realistically the disease spreads.

---

## 📊 Output
1. **Left Panel** – Moving people  
   - 🔵 Blue → Susceptible  
   - 🔴 Red → Infected  
   - 🟢 Green → Recovered  

2. **Right Panel** – SIR graph  
   - Shows population change over time

3. **Final Output in Terminal**


