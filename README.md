# sumo_learn_project

Source code for a series of SUMO traffic simulation tutorial videos by KaguraTart.

Video series (Bilibili): https://www.bilibili.com/video/BV1V44y1Y7hD/

这是系列蛋挞SUMO使用教学视频的源代码，其视频地址是 https://www.bilibili.com/video/BV1V44y1Y7hD/

---

## Prerequisites

1. **SUMO** — Install SUMO (≥ 1.8.0): https://sumo.dlr.de/docs/Installing/index.html
2. **Python 3.8+**
3. **Python packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Set the `SUMO_HOME` environment variable to your SUMO installation directory before running any scenario.

**Linux / macOS:**
```bash
export SUMO_HOME="/usr/share/sumo"
# or wherever SUMO is installed, e.g.:
export SUMO_HOME="$HOME/sumo-1.10.0"
```

**Windows (Command Prompt):**
```cmd
set SUMO_HOME=C:\Program Files\Eclipse\Sumo
```

**Windows (PowerShell):**
```powershell
$env:SUMO_HOME = "C:\Program Files\Eclipse\Sumo"
```

> If `SUMO_HOME` is not set, the scripts fall back to the hardcoded Windows path in the source file.

---

## Scenarios

### 1. sumo-cardata-output — Vehicle Data Collection

Runs a basic simulation and collects per-step vehicle telemetry (position, speed, acceleration, lane info) into a single CSV file.

```bash
cd sumo-cardata-output
python main.py
# Output: sumo-cardata-output/output_data/Aoutput-1.csv
```

### 2. sumo-cross — Cross-Intersection Simulation

Simulates traffic at a cross intersection and exports aggregated vehicle data.

```bash
cd sumo-cross
python main.py
# Output: sumo-cross/output_data/Aoutput-1.csv
```

### 3. sumo-lane-change — Lane Change Observation

Runs an open-ended simulation to observe lane-change behaviour. Press **Ctrl+C** to stop.

```bash
cd sumo-lane-change
python main.py
```

---

## Project Structure

```
sumo_learn_project/
├── requirements.txt
├── sumo-cardata-output/
│   ├── main.py               # Entry point: runs simulation, saves CSV
│   ├── output_car_data.py    # Saves one CSV per step
│   ├── output_car_data2.py   # Returns DataFrame per step (used by main.py)
│   ├── routes1.rou.xml       # Vehicle route definitions
│   ├── test.net.xml          # Road network
│   └── sumo_photo.sumo.cfg   # SUMO configuration
├── sumo-cross/
│   ├── main.py
│   ├── output_car_data.py
│   ├── output_car_data2.py
│   ├── cross.net.xml
│   ├── routes1.rou.xml
│   └── sumo_simu.sumo.cfg
└── sumo-lane-change/
    ├── main.py
    ├── cross1.net.xml
    ├── routes1.rou.xml
    └── sumo_simu.sumo.cfg
```
