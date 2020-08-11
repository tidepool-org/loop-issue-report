import utils
import json
import os


def get_fixtures_from_report(path, name, prefix):
    """ 
    Create Loop test fixtures from an issue report 

    path - path to file
    name - file name
    prefix - file prefix
    """
    parsed_report = utils.parse_report(path, name + "." + prefix)
    outputs = []
    file_names = [
        "momentum_effect",
        "insulin_effect",
        "counteraction_effect",
        "carb_effect",
        "retrospective_effect",
        "predicted_glucose",
    ]

    outputs.append(utils.create_momentum_effect_fixture(parsed_report))
    outputs.append(utils.create_insulin_effect_fixture(parsed_report))
    outputs.append(utils.create_counteraction_effect_fixture(parsed_report))
    outputs.append(utils.create_carb_effect_fixture(parsed_report))
    outputs.append(utils.create_retrospective_effect_fixture(parsed_report))
    outputs.append(utils.create_predicted_glucose_fixture(parsed_report))

    for i in range(len(file_names)):
        utils.save_output(outputs[i], os.path.join(path, name + "_" + file_names[i] + ".json"))


get_fixtures_from_report("YOUR_PATH", "FILE_NAME", "FILE_EXTENSION")
