__author__ = 'Javier'

import re


def get_testlink_id(tag_list, outline_row_id=None):
    """
    Gets the TestLink ID from tags with this format:
        @TL.<outline_id>.<testlink_id>
        @TL.<testlink_id>
    :param tag_list: (list) List of tags
    :param outline_row_id: (string) Only is mandatory if it is a Scenario Outline and tags are using
        the first patter. Example Row ID.
    :return: (string) TestLink ID
    """

    testlink_id = None
    for tag in tag_list:
        result = re.match(r"TL\.(\d*)\.(\w*\-\d*)", tag)
        if result:
            if outline_row_id == int(result.group(1)):
                testlink_id = result.group(2)
                break
        else:
            result = re.match(r"TL\.(\w*\-\d*)", tag)

            if result:
                testlink_id = result.group(1)
                break

    return testlink_id


def after_scenario(context, scenario):
    """
    Hook. To be executed after each scenario.
        - Processes tags to update TestLink properly.
    :param context: Behave Context
    :param scenario: Behave Scenario
    :return: None
    """

    #print("   >>>>> NAME: ", scenario.name)
    #print("   >>>>> TAG List: ", scenario.tags)

    row_id = scenario._row.index if scenario._row else None
    #print("   >>>>> ROW: ", row_id)
    #print("   >>>>> Active Dataset: ", context.active_outline)

    test_link_id = get_testlink_id(scenario.tags, row_id)
    print("    >>>>>   - TEST LINK ID: ", test_link_id)
    print("    >>>>>   - STATUS: ", scenario.status)
    if scenario.status == 'passed':
        # Call to Web Service to update TestLink: PASSED
        # GET/POST status, test_link_id
        pass
    else:
        # Call to Web Service to update TestLink: FAILED
        # GET/POST status, test_link_id
        pass
