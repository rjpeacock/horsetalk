from peak_utility.enumeration.parsing_enum import ParsingEnum

class Obstacle(ParsingEnum):
    NONE: int
    HURDLE: int
    STEEPLECHASE: int
    CROSS_COUNTRY: int
    FLAT = NONE
    H = HURDLE
    HRD = HURDLE
    HRDLE = HURDLE
    C = STEEPLECHASE
    CH = STEEPLECHASE
    CHS = STEEPLECHASE
    CHSE = STEEPLECHASE
    CHASE = STEEPLECHASE
    CC = CROSS_COUNTRY
    XC = CROSS_COUNTRY
