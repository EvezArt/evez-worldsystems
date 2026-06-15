#!/usr/bin/env python3
"""EVEZ World Systems — Start all solvers."""
import subprocess, sys

SERVICES = [
    ("hunger_solver:app", 8092),
    ("energy_solver:app", 8093),
    ("health_solver:app", 8094),
    ("education_solver:app", 8095),
    ("unified_solver:app", 8096),
]

procs = []
for module, port in SERVICES:
    p = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", module, "--host", "0.0.0.0", "--port", str(port)],
        cwd="/home/openclaw/evez-worldsystems"
    )
    procs.append(p)
    print(f"Started {module} on port {port} (PID {p.pid})")

print("\nAll 5 EVEZ World Systems running.")
print("  Hunger:    http://localhost:8092/solve")
print("  Energy:    http://localhost:8093/simulate?years=30")
print("  Health:    http://localhost:8094/optimize?budget_billions=50")
print("  Education: http://localhost:8095/plan?budget_billions=30")
print("  Unified:   http://localhost:8096/solve?total_budget_billions=100")
print("  Eigen:     http://localhost:8096/eigen-leverage")

for p in procs:
    p.wait()
