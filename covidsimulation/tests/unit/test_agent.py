import pytest

from covidsimulation.simulation.agent import Agent
import covidsimulation.common.health_states as health_states

@pytest.fixture()
def t_agent():
    yield Agent(0, health_states.asymptomatic, 5)

def test__cycleIncubated(t_agent, sim):

    initial_state = health_states.incubated
    t_agent.health_state = initial_state

    # check no immeadiate advance to asymptomatic
    t_agent._cycleIncubated(sim)
    assert t_agent.health_state == initial_state

    # check eventual advance to asymptomatic
    t_agent.days_exposed = t_agent.incubation_time
    t_agent._cycleIncubated(sim)
    assert t_agent.health_state == health_states.asymptomatic

def test__cycleAsymptomatic(t_agent, sim):

    initial_state = health_states.asymptomatic
    t_agent.health_state = initial_state

    # check no change
    t_agent._cycleAsymptomatic(sim)
    assert t_agent.health_state == initial_state

    # check no change after increase in time (future health state dependent)
    t_agent.health_outcome = health_states.asymptomatic
    t_agent.days_exposed = t_agent.incubation_time
    t_agent._cycleAsymptomatic(sim)
    assert t_agent.health_state == initial_state

    # check change with new future health state
    t_agent.health_outcome = health_states.symptomaticLight
    t_agent.days_exposed = t_agent.incubation_time
    t_agent._cycleAsymptomatic(sim)
    assert t_agent.health_state == health_states.symptomaticLight

    # check immunity if enough time passes
    t_agent.health_state = initial_state
    t_agent.health_outcome = health_states.asymptomatic

    t_agent.days_exposed = t_agent.incubation_time
    t_agent._cycleAsymptomatic(sim)
    assert t_agent.health_state == initial_state

    t_agent.days_exposed = t_agent.incubation_time + 7
    t_agent._cycleAsymptomatic(sim)
    assert t_agent.health_state == health_states.immune

def test__cycleSymptomaticLight(t_agent, sim):
    
    initial_state = health_states.symptomaticLight
    t_agent.health_state = initial_state
    t_agent.health_outcome = initial_state
    
    # check no change if outcome symptomatic light
    t_agent._cycleSymptomaticLight(sim)
    assert t_agent.health_state == initial_state

    # check transition to immune after configured time has elapsed
    t_agent.days_with_symptoms = sim.t_discharge[0]
    t_agent._cycleSymptomaticLight(sim)
    assert t_agent.health_state == health_states.immune

    # check disease progression otherwise
    t_agent.days_with_symptoms = 0
    possible_outcomes = [health_states.symptomaticMedium, health_states.hospital, health_states.ICU, health_states.dead]
    for outcome in possible_outcomes:
        t_agent.health_state = initial_state
        t_agent.health_outcome = outcome
        t_agent._cycleSymptomaticLight(sim)
        assert t_agent.health_state == health_states.symptomaticMedium

def test__cycleSymptomaticMedium(t_agent, sim):

    initial_state = health_states.symptomaticMedium
    t_agent.health_state = initial_state
    t_agent.health_outcome = initial_state
    
    # check no change if outcome symptomatic medium
    t_agent._cycleSymptomaticMedium(sim)
    assert t_agent.health_state == initial_state

    # check transition to immune after configured time has elapsed
    t_agent.days_with_symptoms = sim.t_discharge[0]
    t_agent._cycleSymptomaticMedium(sim)
    assert t_agent.health_state == health_states.immune

    # check disease progression otherwise
    t_agent.days_with_symptoms = sim.t_hospital
    possible_outcomes = [health_states.hospital, health_states.ICU, health_states.dead]
    for outcome in possible_outcomes:
        t_agent.health_state = initial_state
        t_agent.health_outcome = outcome
        t_agent._cycleSymptomaticMedium(sim)

        if outcome == health_states.hospital:
            assert t_agent.health_state == health_states.hospital
        else:
            assert t_agent.health_state == health_states.ICU

def test__cycleHospital(t_agent, sim):
    
    initial_state = health_states.hospital
    t_agent.health_state = initial_state

    # no change because no days with symptoms
    t_agent._cycleHospital(sim)
    assert t_agent.health_state == initial_state

    # become immune after parameter number of days
    t_agent.days_with_symptoms = sim.t_discharge[1]
    t_agent._cycleHospital(sim)
    assert t_agent.health_state == health_states.immune

def test__cycleICU(t_agent, sim):
    
    initial_state = health_states.ICU

    possible_outcomes = [health_states.ICU, health_states.dead]
    for outcome in possible_outcomes:
        t_agent.health_state = initial_state
        t_agent.health_outcome = outcome
        
        # no change because no days with symptoms
        t_agent.days_with_symptoms = 0
        t_agent._cycleICU(sim)
        assert t_agent.health_state == initial_state

        # transition to death or hospital
        t_agent.days_with_symptoms = sim.t_discharge[2]
        t_agent._cycleICU(sim)

        if outcome == health_states.ICU:
            assert t_agent.health_state == health_states.hospital
        else:
            assert t_agent.health_state == health_states.dead



