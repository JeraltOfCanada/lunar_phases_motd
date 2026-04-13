LUNAR_PHASE_LENGTH = 29.53

PHASE_QUARTERS_DAY_LENGTH = 1

def phase_boundaries():
    """Function calculates boundaries for the 4 lunar quarters including a full
    day buffer before each. Then converts all variables into a constant to be copy
    pasted into the other scripts."""
    new_moon_high = LUNAR_PHASE_LENGTH
    new_moon_low = LUNAR_PHASE_LENGTH - PHASE_QUARTERS_DAY_LENGTH
    full_moon_high = LUNAR_PHASE_LENGTH * 0.5
    full_moon_low = full_moon_high - PHASE_QUARTERS_DAY_LENGTH
    first_quarter_high = LUNAR_PHASE_LENGTH * 0.25
    first_quarter_low = first_quarter_high - PHASE_QUARTERS_DAY_LENGTH
    third_quarter_high = LUNAR_PHASE_LENGTH * 0.75
    third_quarter_low = third_quarter_high - PHASE_QUARTERS_DAY_LENGTH
    for name, value in locals().items():
        print(f"{name.upper()} = {value}")

phase_boundaries()