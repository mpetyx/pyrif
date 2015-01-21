from lettuce import step, world
from pyrif import parser
from pprint import pprint

@step("a valid rif empty xml document")
def step_impl(step):
    """
    :type step lettuce.core.Step
    """

    world.xml = ""


@step("I retrieve python rule class")
def step_impl(step):
    """
    :type step lettuce.core.Step
    """
    assert world.xml == ""


@step("I parse it")
def step_impl(step):
    """
    :type step lettuce.core.Step
    """
    if world.url:
        world.rules = parser.xml_parsing(world.url)
        pprint(world.rules)
    else:
        pass



@step('that i have the document "(.*)"')
def step_impl(step, url):
    """
    :type step lettuce.core.Step
    """
    world.url = url