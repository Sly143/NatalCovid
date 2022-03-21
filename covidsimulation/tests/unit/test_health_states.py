
import pytest
import covidsimulation.common.health_states as health_states

# example test
def test_infectious_states():

    assert health_states.asymptomatic in health_states.infectious_states
    assert health_states.symptomaticLight in health_states.infectious_states
    assert health_states.symptomaticMedium in health_states.infectious_states
    assert health_states.hospital in health_states.infectious_states
    assert health_states.ICU in health_states.infectious_states