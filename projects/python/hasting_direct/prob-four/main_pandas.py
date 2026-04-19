import pandas as pd

rules = [
    {"rule_id": "R1", "field": "driver_age", "operator": "<", "threshold": 18, "action": "DECLINE"},
    {"rule_id": "R2", "field": "vehicle_value", "operator": ">", "threshold": 50000, "action": "REFER"},
    {"rule_id": "R3", "field": "risk_score", "operator": ">", "threshold": 0.85, "action": "DECLINE"},
    {"rule_id": "R4", "field": "years_no_claims", "operator": "<", "threshold": 2, "action": "REFER"},
    {"rule_id": "R5", "field": "driver_age", "operator": ">", "threshold": 80, "action": "REFER"},
]

quotes = [
    {"quote_id": "Q1", "driver_age": 17, "vehicle_value": 12000, "risk_score": 0.55, "years_no_claims": 3},
    {"quote_id": "Q2", "driver_age": 35, "vehicle_value": 62000, "risk_score": 0.42, "years_no_claims": 5},
    {"quote_id": "Q3", "driver_age": 42, "vehicle_value": 28000, "risk_score": 0.91, "years_no_claims": 8},
    {"quote_id": "Q4", "driver_age": 29, "vehicle_value": 15000, "risk_score": 0.61, "years_no_claims": 1},
    {"quote_id": "Q5", "driver_age": 83, "vehicle_value": 9000, "risk_score": 0.38, "years_no_claims": 0},
    {"quote_id": "Q6", "driver_age": 31, "vehicle_value": 34000, "risk_score": 0.78, "years_no_claims": 4},
    {"quote_id": "Q7", "driver_age": 16, "vehicle_value": 55000, "risk_score": 0.92, "years_no_claims": 0},
]

