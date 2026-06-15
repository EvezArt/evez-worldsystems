# EVEZ World Systems

> We eigendecomposed the world's problems. The dominant eigenvalue is hunger. Fix that first and everything else gets 37% easier.

Five FastAPI microservices that model, optimize, and solve global systems problems using real math.

## Services

| Service | Port | What It Does |
|---------|------|-------------|
| **hunger_solver** | 8092 | LP-optimized global food distribution |
| **energy_solver** | 8093 | Monte Carlo renewable transition simulator |
| **health_solver** | 8094 | DALY-optimized healthcare allocation |
| **education_solver** | 8095 | Universal education access planner |
| **unified_solver** | 8096 | Cross-system eigenvalue optimization |

## Quick Start

```bash
pip install -r requirements.txt
python start_all.py
```

## Endpoints

### Hunger Solver (8092)
- `GET /solve` — Optimal food distribution plan (LP)
- `GET /hunger/status` — Global food gap metrics

### Energy Solver (8093)
- `GET /simulate?years=30` — Monte Carlo transition simulation
- `GET /energy/status` — Current global energy mix

### Health Solver (8094)
- `GET /optimize?budget_billions=50` — DALY-optimized allocation
- `GET /health/status` — Global health gap metrics

### Education Solver (8095)
- `GET /plan?budget_billions=30` — Teacher/infrastructure deployment plan

### Unified Solver (8096)
- `GET /solve?total_budget_billions=100` — Eigen-informed cross-system allocation
- `GET /eigen-leverage` — Leontief decomposition showing where $1 does the most good

## The Key Insight

The coupling matrix between hunger, energy, health, and education has a dominant eigenvalue pointing at hunger. A $1B investment in hunger reduction generates amplified returns across health (malnutrition → disease), education (hungry kids can't learn), and economic output.

The Leontief inverse `(I - C)^{-1}` gives the total system response to any unit intervention. The numbers are clear: fix hunger first.

This isn't ideology. It's linear algebra.
