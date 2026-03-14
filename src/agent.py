import random
import logging
from typing import Dict, Any

from .config import AgentConfig
from .models import load_multimodal_genome_model
from .tools import predict_binding, perturb_gene, simulate_fate_trajectory, virtual_screen
from .utils import AgentLogger, growth_reinvestment

logger = AgentLogger.get_logger('CellFateAgent')


class CellFateAgent:
    """Autonomous in silico cell fate agent."""

    def __init__(self, config: AgentConfig) -> None:
        self.config = config
        random.seed(config.random_seed)
        self.model = load_multimodal_genome_model()  # placeholder
        self.state: Dict[str, Any] = {'dish': config.virtual_dish_id, 'history': []}

    def plan(self, task: str) -> Dict[str, Any]:
        logger.info('Planning task: %s', task)
        return {'task': task, 'focus': 'epigenetic regulator landscape', 'hints': ['TF binding', 'chromatin loops']}

    def execute_step(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        logger.debug('Execute step with plan: %s', plan)

        binding = predict_binding(self.model, plan['focus'])
        perturbation = perturb_gene(self.model, binding, budget=self.config.perturbation_budget)
        trajectory = simulate_fate_trajectory(self.model, perturbation)
        screens = virtual_screen(self.model, trajectory, top_k=2)

        self.state['history'].append({'binding': binding, 'perturbation': perturbation, 'trajectory': trajectory, 'screens': screens})

        reward = growth_reinvestment(self.state, fee_rate=self.config.protocol_fee_rate)
        self.config.perturbation_budget = max(0, self.config.perturbation_budget - 1)

        output = {
            'binding': binding,
            'perturbation': perturbation,
            'trajectory': trajectory,
            'screens': screens,
            'reward': reward,
            'remaining_budget': self.config.perturbation_budget,
        }

        logger.debug('Step output: %s', output)
        return output

    def run(self, task: str) -> Dict[str, Any]:
        logger.info('Run begins for task: %s', task)
        plan = self.plan(task)
        result = {}

        for step in range(self.config.max_steps):
            if self.config.perturbation_budget <= 0:
                logger.warning('Perturbation budget depleted at step %d', step)
                break
            logger.info('Running step %d/%d', step + 1, self.config.max_steps)
            result = self.execute_step(plan)

        logger.info('Run complete. Total steps %d', len(self.state['history']))
        return {'final': result, 'history': self.state['history']}
