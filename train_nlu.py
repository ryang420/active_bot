#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer


def train_nlu(data, configs, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    trainer.persist(model_dir, fixed_model_name="activenlu")


if __name__ == "__main__":
    train_nlu('./data/nlu/data.json', 'nlu_config.yml', './models/nlu')
