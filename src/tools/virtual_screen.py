from typing import Any, Dict, List


def virtual_screen(model: Any, trajectory: Dict[str, Any], top_k: int = 2) -> List[Dict[str, Any]]:
    return [
        {'candidate': 'TF1', 'score': 0.8, 'effect': 'stabilize stemness'},
        {'candidate': 'TF2', 'score': 0.75, 'effect': 'reduce exhaustion'},
    ][:top_k]
