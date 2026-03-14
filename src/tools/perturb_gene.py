from typing import Any, Dict
import random


def perturb_gene(model: Any, binding: Dict[str, Any], budget: int = 1) -> Dict[str, Any]:
    candidates = ['IL2RA', 'GATA3', 'TBX21', 'FOXP3']
    selection = random.choice(candidates)
    return {
        'target': selection,
        'mode': 'CRISPRi' if budget % 2 == 0 else 'CRISPRa',
        'intensity': round(random.uniform(0.2, 0.8), 3),
        'binding_confidence': binding['score'],
        'budget_used': 1,
    }
