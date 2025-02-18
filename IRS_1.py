def calculate_swap_npv(notional, fixed_rate, sofr_rates, discount_factors, spread=0.005):
    '''
    Inputs:

notional: The principal amount ($100M).
fixed_rate: The fixed interest rate (3%).
sofr_rates: Forward SOFR rates for each year,  derived from the SOFR Overnight Index Swap (OIS) curve using bootstrapping..
discount_factors: SOFR-based discount factors.
Computes:

Fixed leg PV by discounting fixed cash flows.
Floating leg PV by discounting floating cash flows.
Net Present Value (NPV) of the swap.
Outputs:

PV of Fixed Leg.
PV of Floating Leg.
NPV of the Swap (positive means floating-rate receiver benefits).
    '''
    years = len(sofr_rates)
    fixed_cash_flows = [notional * fixed_rate for _ in range(years)]
    floating_cash_flows = [notional * (sofr_rates[i] + spread) for i in range(years)]
    
    # Calculate PV of Fixed Leg
    pv_fixed_leg = sum(fixed_cash_flows[i] * discount_factors[i] for i in range(years))
    
    # Calculate PV of Floating Leg
    pv_floating_leg = sum(floating_cash_flows[i] * discount_factors[i] for i in range(years))
    
    # Net Present Value (NPV) of the swap
    npv = pv_floating_leg - pv_fixed_leg
    
    return pv_fixed_leg, pv_floating_leg, npv

# Example Data
notional = 100_000_000  # $100 million
fixed_rate = 0.03  # 3%
sofr_rates = [0.025, 0.027, 0.03, 0.032, 0.034]  # SOFR forward rates
sofr_discount_factors = [0.99, 0.97, 0.94, 0.91, 0.88]  # SOFR discount factors

# Run Calculation
pv_fixed, pv_floating, swap_npv = calculate_swap_npv(notional, fixed_rate, sofr_rates, sofr_discount_factors)

# Output Results
print(f"Present Value of Fixed Leg: ${pv_fixed:,.2f}")
print(f"Present Value of Floating Leg: ${pv_floating:,.2f}")
print(f"Net Present Value (NPV) of Swap: ${swap_npv:,.2f}")
