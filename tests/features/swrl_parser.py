from lettuce import step, world


@step("the empty xml swrl document")
def step_impl(step):
    """
    :type step lettuce.core.Step
    """
    pass

@step("I retrieve (\d+)")
def step_impl(step, expected):
    """
    :type step lettuce.core.Step
    """
    assert int(expected) == 1