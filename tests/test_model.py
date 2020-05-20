#!/usr/bin/env python
import pytest
from whisk_project_structure.models.model import Model

def test_predict():
    model = Model()
    model.predict([[1,2],[3,4]])
