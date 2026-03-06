# okDriver Live Fleet Monitoring Dashboard

## Overview

This project is a simulated **live fleet monitoring dashboard** designed to demonstrate real-time driver behavior analytics.
The system simulates dashcam events and streams them to a live dashboard using WebSockets.

The platform displays:

* Driver risk score
* Speed analytics
* Violation tracking
* Live fleet metrics
* Recent driver events
* Simulated dashcam video feed

This project demonstrates real-time data streaming architecture similar to modern **AI-driven fleet safety platforms**.

---

# System Architecture

Simulator → FastAPI Backend → WebSocket → Live Dashboard

1. **Dashcam Simulator**

   * Generates random driver behavior events every 2–3 seconds.

2. **FastAPI Backend**

   * Receives events via REST API
   * Processes risk score and violations
   * Broadcasts events via WebSocket

3. **Live Dashboard**

   * Receives real-time updates
   * Displays analytics and charts
   * Shows recent driver events

---

# Tech Stack

Backend:

* FastAPI
* Python
* WebSockets

Frontend:

* HTML
* CSS
* Chart.js

Simulation:

* Python event generator

---

# Features

Real-time dashboard
Speed analytics chart
Driver risk score calculation
Violation monitoring
Recent event logs
Dashcam video simulation

---

# How to Run

### 1 Install dependencies

```
pip install -r backend/requirements.txt
```

---

### 2 Start Backend

```
uvicorn main:app --reload
```

---

### 3 Start Simulator

```
python simulator.py
```

---

### 4 Open Dashboard

Open:

```
frontend/index.html
```

---

# Example Events

Speeding
Harsh braking
Drowsiness alerts

Each violation increases driver risk score dynamically.

---

# Demo

The dashboard automatically updates every 2–3 seconds using WebSocket streaming.

---



