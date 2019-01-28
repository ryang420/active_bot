#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application


def run_bot():
    interpreter = RasaNLUInterpreter('./models/nlu/default/activenlu')
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load('./models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)
    serve_application(agent, channel='cmdline')

    return agent


if __name__ == '__main__':
    run_bot()
