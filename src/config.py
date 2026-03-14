from dataclasses import dataclass

@dataclass
class AgentConfig:
    virtual_dish_id: str = 'VirtualDish-01'
    perturbation_budget: int = 3
    max_steps: int = 12
    protocol_fee_rate: float = 0.015
    random_seed: int = 42
