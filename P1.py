def credit_card_penalty(credit_card_balance,number_of_days_late):
    result = 0.0
    if credit_card_balance < 15:
        result = credit_card_balance * 0.05
    elif credit_card_balance >= 15 and credit_card_balance <30:
        result = credit_card_balance * 0.10
    elif credit_card_balance >= 31 and credit_card_balance <60:
        result = credit_card_balance * 0.15
    else:
        result = credit_card_balance * 0.20
        return result


print "late_payment 1: ", credit_card_penalty (15000, 18)
print "late_payment 2: ", credit_card_penalty (7000, 31)
print "late_payment 3: ", credit_card_penalty (300, 70)
print "late_payment 4: ", credit_card_penalty (1000, 3)



