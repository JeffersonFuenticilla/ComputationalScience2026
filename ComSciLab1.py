from decimal import Decimal, getcontext, ROUND_DOWN, ROUND_HALF_UP

# 1. Setup precision (110 digits to be safe)
getcontext().prec = 110

# 2. Pi to 105 digits
PI_RAW = "3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798"
pi_full = Decimal(PI_RAW)

def calculate_formula(p):
    # Using the Normal Distribution Peak formula: 1 / sqrt(2 * pi)
    return Decimal(1) / (p * Decimal(2)).sqrt()

# The milestones from your notes
milestones = [20, 40, 60, 100]

print(f"{'Places':<8} | {'Type':<12} | {'Result Value':<25} | {'Error vs True'}")
print("-" * 80)

# True value for comparison
true_val = calculate_formula(pi_full)

for n in milestones:
    # Create a 'pattern' for the decimal places (e.g., '0.0000...')
    pattern = Decimal('1.' + '0' * n)
    
    # TRUNCATION (Chopping off)
    trunc_pi = pi_full.quantize(pattern, rounding=ROUND_DOWN)
    res_trunc = calculate_formula(trunc_pi)
    diff_trunc = abs(true_val - res_trunc)
    
    # ROUNDING (Looking at the next digit)
    round_pi = pi_full.quantize(pattern, rounding=ROUND_HALF_UP)
    res_round = calculate_formula(round_pi)
    diff_round = abs(true_val - res_round)

    print(f"{n:<8} | Truncated   | {str(res_trunc)[:20]}... | {diff_trunc:.2e}")
    print(f"{n:<8} | Rounded     | {str(res_round)[:20]}... | {diff_round:.2e}")
    print("-" * 80)

print("\nGoal Check: Is there really a difference?")
print("At 20 places, the error is tiny. By 100 places, the difference is virtually zero.")