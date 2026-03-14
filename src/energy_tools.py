"""
Simple utilities for basic energy calculations.
"""


def calculate_energy(power_kw: float, hours: float) -> float:
    """Calculate energy consumption in kWh."""
    return power_kw * hours


def calculate_cost(energy_kwh: float, price_per_kwh: float) -> float:
    """Calculate electricity cost."""
    return energy_kwh * price_per_kwh
