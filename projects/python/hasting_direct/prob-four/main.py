import operator

ops = {
    "<": operator.lt,
    ">": operator.gt,
    "<=": operator.le,
    ">=": operator.ge,
    "==": operator.eq,
    "!=": operator.ne,
}

op = ops["<"]
print(op(3, 5))   # True





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


action_counter={
    "REFER":0,
    "DECLINE":0,
    "ACCEPT":0
                }
rule_counter={
    "R1":0,
    "R2":0,
    "R3":0,
    "R4":0,
    "R5":0
}

for i in quotes:
    triggered_quotes=[]
    rules_triggered=[]
    i["triggered_quotes"]=triggered_quotes
    i["rules_triggered"]=rules_triggered
    for j in rules:
        op = ops[j["operator"]]
        if op (i[j["field"]] , j["threshold"]):
            print(f"for {i["quote_id"]} take {j["action"]} based on {j["field"]}")
            triggered_quotes.append(j["action"])
            rules_triggered.append(j["rule_id"])
            rule_counter[j["rule_id"]] += 1
    if "DECLINE" in i["triggered_quotes"]:
        i["final_decision"]="DECLINE"
    elif "REFER" in i["triggered_quotes"]:
        i["final_decision"]="REFER"
    else:
        i["final_decision"]="ACCEPT"
    action_counter[i["final_decision"]] += 1
print(quotes)
print(action_counter)
print(rule_counter)


