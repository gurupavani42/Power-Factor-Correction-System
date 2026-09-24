# Power Factor Correction System
# EEE Python Mini Project

import math


def power_factor_correction(voltage, current, pf_old, pf_target, frequency):
    
    print("\n======================================")
    print("     POWER FACTOR CORRECTION SYSTEM")
    print("======================================")

    # Calculate apparent power
    apparent_power = voltage * current

    # Calculate active power
    active_power = apparent_power * pf_old

    # Calculate reactive power before correction
    reactive_old = active_power * math.tan(math.acos(pf_old))

    # Calculate reactive power after correction
    reactive_new = active_power * math.tan(math.acos(pf_target))

    # Capacitive reactive power required
    capacitor_kvar = reactive_old - reactive_new

    # Convert kVAR to VAR
    capacitor_var = capacitor_kvar * 1000

    # Calculate capacitance for single-phase system
    capacitance = capacitor_var / (
        2 * math.pi * frequency * voltage ** 2
    )

    # Display results
    print(f"Voltage                  : {voltage:.2f} V")
    print(f"Current                  : {current:.2f} A")
    print(f"Initial Power Factor     : {pf_old:.2f}")
    print(f"Target Power Factor      : {pf_target:.2f}")
    print(f"Frequency                : {frequency:.2f} Hz")

    print("\n----------- RESULTS -----------")

    print(f"Active Power             : {active_power:.2f} W")
    print(f"Initial Reactive Power   : {reactive_old:.2f} VAR")
    print(f"Final Reactive Power     : {reactive_new:.2f} VAR")
    print(f"Required Capacitor       : {capacitor_kvar:.2f} kVAR")
    print(f"Capacitance Required     : {capacitance:.6f} F")
    print(f"Capacitance Required     : {capacitance * 1e6:.2f} µF")

    print("\nPower factor correction completed.")


# Main program

print("======================================")
print("      POWER FACTOR CORRECTION")
print("======================================")

voltage = float(input("Enter Voltage (V): "))
current = float(input("Enter Current (A): "))
pf_old = float(input("Enter Existing Power Factor: "))
pf_target = float(input("Enter Target Power Factor: "))
frequency = float(input("Enter Frequency (Hz): "))


# Input validation

if not (0 < pf_old <= 1):
    print("\nInvalid existing power factor.")

elif not (0 < pf_target <= 1):
    print("\nInvalid target power factor.")

elif pf_target < pf_old:
    print("\nTarget power factor should be greater than existing power factor.")

elif voltage <= 0 or current <= 0 or frequency <= 0:
    print("\nVoltage, current and frequency must be positive.")

else:
    power_factor_correction(
        voltage,
        current,
        pf_old,
        pf_target,
        frequency
    )
