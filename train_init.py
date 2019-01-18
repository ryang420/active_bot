import logging
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

if __name__ == '__main__':
    logging.basicConfig(level='INFO')

    train_data_file = './data/stories.md'
    model_path = './models/dialogue'

    agent = Agent('domain.yml',
                  policies=[MemoizationPolicy(), KerasPolicy(max_history=3, epochs=200, batch_size=50)])

    data = agent.load_data(train_data_file)
    agent.train(data)
    agent.persist(model_path)
