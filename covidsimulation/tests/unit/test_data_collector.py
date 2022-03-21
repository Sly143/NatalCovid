

import pytest
import covidsimulation.simulation.data_collector
import covidsimulation.common.health_states as health_states


def test_countHealthStates(population):
    result = covidsimulation.simulation.data_collector.countHealthStates(population)

    assert len(result) == health_states.NUM_INTERNAL_STATES
