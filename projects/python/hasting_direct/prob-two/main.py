expected_quotes = [
    {"quote_id": "Q1", "price": 100.00, "version": "v1", "timestamp": "2026-04-14T10:00:00"},
    {"quote_id": "Q2", "price": 150.00, "version": "v1", "timestamp": "2026-04-14T10:01:00"},
    {"quote_id": "Q3", "price": 200.00, "version": "v2", "timestamp": "2026-04-14T10:02:00"},
    {"quote_id": "Q3", "price": 200.00, "version": "v2", "timestamp": "2026-04-14T10:02:30"}
]

actual_quotes = [
    {"quote_id": "Q1", "price":100.005 , "version": "v1", "timestamp": "2026-04-14T10:00:02"},
    {"quote_id": "Q2", "price": 151.50, "version": "v2", "timestamp": "2026-04-14T10:01:02"},
    {"quote_id": "Q4", "price": 175.00, "version": "v1", "timestamp": "2026-04-14T10:03:00"},
    {"quote_id": "Q4", "price": 175.00, "version": "v1", "timestamp": "2026-04-14T10:03:30"}
]

keys_to_test={"quote_id":str,"price":float,"version":str,"timestamp":str}

def check_values_null_missing_type(quotes,keys):
    for i in quotes:
        for j,l in keys.items():
            if i[j] is None or i[j] == "":
                print(f"{j} is missing")
            if not isinstance(i[j], l):
                print(f"wrong type for {i[j]}, type is {type(i[j])} ")



def version_mismatch(q1,q2):
    for i in range(len(q1)):
        if q1[i]["version"] != q2[i]["version"]:
            print(f"version issue in row {i+1} for where {q1[i]["version"],q2[i]["version"]} are mismatched")

def compare_prices(q1,q2,price_tolerance=0.01):
    for i in range(len(q1)):
        if abs(q1[i]["price"] - q2[i]["price"]) > price_tolerance:
            print(f"quote {i+1} has price higher than price tolerance")


def duplicate_quotes(q1):
    quotes_set=set()
    for i in q1:
        if i["quote_id"] not in quotes_set:
            quotes_set.add(i["quote_id"])
        else:
            print(f"quote contains duplicate values {i["quote_id"]}")


check_values_null_missing_type(expected_quotes,keys_to_test)
check_values_null_missing_type(actual_quotes,keys_to_test)
version_mismatch(expected_quotes,actual_quotes)
compare_prices(expected_quotes,actual_quotes)
duplicate_quotes(expected_quotes)
duplicate_quotes(actual_quotes)


