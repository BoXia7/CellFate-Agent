from typing import Any, Dict
import random


def simulate_fate_trajectory(model: Any, perturbation: Dict[str, Any]) -> Dict[str, Any]:
    base = 0.35 if perturbation['mode'] == 'CRISPRi' else 0.65
    return {
        'fate': 'stem-like' if base > 0.5 else 'exhausted',
        'probability': round(min(1.0, base + random.uniform(-0.12, 0.12)), 3),
        'trajectory_curve': [0.0, 0.2, 0.45, base],
        'comments': 'Virtual dish state fluctuates with synthetic noise',
    }
