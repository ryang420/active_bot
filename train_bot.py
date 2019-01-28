import logging
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

logger = logging.getLogger(__name__)


def train_dialogue(domain_file='domain.yml',
                   model_path='./models/dialogue',
                   train_data='./data/core/stories.md'):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(), KerasPolicy(max_history=3, epochs=200, batch_size=50)])

    data = agent.load_data(train_data)
    agent.train(data)
    agent.persist(model_path)
    return agent


if __name__ == '__main__':
    train_dialogue()
