from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = ([
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 131.25,
    "uptime_pct": 98.134,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 169.33,
    "uptime_pct": 98.167,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 179.2,
    "uptime_pct": 99.001,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 132.27,
    "uptime_pct": 97.176,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 132.55,
    "uptime_pct": 97.716,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 150.12,
    "uptime_pct": 98.702,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 220.33,
    "uptime_pct": 98.394,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 199.7,
    "uptime_pct": 99.001,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 119.57,
    "uptime_pct": 97.443,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 150.91,
    "uptime_pct": 99.104,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 179.03,
    "uptime_pct": 98.975,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 120.97,
    "uptime_pct": 97.607,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 179.85,
    "uptime_pct": 97.133,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 201.78,
    "uptime_pct": 97.577,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 137.57,
    "uptime_pct": 99.396,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 102.58,
    "uptime_pct": 99.036,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 203.87,
    "uptime_pct": 98.316,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 163.26,
    "uptime_pct": 97.114,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 214.29,
    "uptime_pct": 98.963,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 163.77,
    "uptime_pct": 98.567,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 144.75,
    "uptime_pct": 97.523,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 163.72,
    "uptime_pct": 99.094,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 146.79,
    "uptime_pct": 98.947,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 128.22,
    "uptime_pct": 98.829,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 158.16,
    "uptime_pct": 97.863,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 150.51,
    "uptime_pct": 99.078,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 209.49,
    "uptime_pct": 98.266,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 215.41,
    "uptime_pct": 97.88,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 163.55,
    "uptime_pct": 99.325,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 117.25,
    "uptime_pct": 97.888,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 206.81,
    "uptime_pct": 99.194,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 221.26,
    "uptime_pct": 99.307,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 141.79,
    "uptime_pct": 99.208,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 178.33,
    "uptime_pct": 98.348,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 218.7,
    "uptime_pct": 97.522,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 212.59,
    "uptime_pct": 97.109,
    "timestamp": 20250312
  }
])

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
