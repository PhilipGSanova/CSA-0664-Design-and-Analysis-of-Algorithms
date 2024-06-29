def detect_fraud(transactions, threshold_amount=1000, threshold_location_count=3):
    flagged_transactions = []
    
    for transaction in transactions:
        if is_fraudulent(transaction, threshold_amount, threshold_location_count):
            flagged_transactions.append(transaction)
    
    return flagged_transactions

def is_fraudulent(transaction, threshold_amount, threshold_location_count):
    if transaction['amount'] > threshold_amount:
        return True
    
    if transaction['location_count'] <= threshold_location_count:
        return False
    
    return True

if __name__ == "__main__":
    transactions = [
        {'amount': 1200, 'location_count': 1},
        {'amount': 500, 'location_count': 3},
        {'amount': 800, 'location_count': 2},
        {'amount': 1500, 'location_count': 4}
    ]
    
    flagged_transactions = detect_fraud(transactions, threshold_amount=1000, threshold_location_count=3)
    
    print("Flagged transactions due to potential fraud:")
    for transaction in flagged_transactions:
        print(f"Amount: {transaction['amount']}, Location count: {transaction['location_count']}")
