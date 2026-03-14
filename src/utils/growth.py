from typing import Any, Dict


def growth_reinvestment(state: Dict[str, Any], fee_rate: float = 0.01) -> float:
    quality = len(state['history']) * 0.05
    fee = max(0.0, fee_rate * (1 + quality))
    return round(min(1.0, fee + quality), 4)
