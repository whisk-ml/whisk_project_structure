#!/usr/bin/env python
import pytest
from demo.models.model import Model

def test_predict():
    model = Model()
    model.predict([[1,2],[3,4]])
