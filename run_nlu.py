#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rasa_nlu.model import Metadata, Interpreter


def run_nlu():
    interpreter = Interpreter.load('./models/nlu/default/activenlu')
    print(interpreter.parse("What's the weather like today in London?"))


if __name__ == '__main__':
    run_nlu()
