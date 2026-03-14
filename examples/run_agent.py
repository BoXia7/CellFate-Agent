from cellfate_agent import CellFateAgent, AgentConfig


def main() -> None:
    config = AgentConfig(virtual_dish_id='VD-01', perturbation_budget=3, max_steps=4)
    agent = CellFateAgent(config=config)

    result = agent.run('reprogram exhausted T cell to stem-like state')
    print('Final outcome', result['final'])
    print('History length', len(result['history']))


if __name__ == '__main__':
    main()
