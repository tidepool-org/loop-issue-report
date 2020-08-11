from loop.issue_report import parser
import json
from datetime import datetime


def issue_report_date_parser(date_string):
    return datetime.strptime(date_string.strip(), "%Y-%m-%d %H:%M:%S %z").strftime(
        "%Y-%m-%dT%H:%M:%S"
    )


def save_output(output, output_path):
    with open(output_path, "w") as p:
        json.dump(output, p, indent=2)


def parse_report(path, file_name):
    try:
        lr = parser.LoopReport()
        parsed_issue_report_dict = lr.parse_by_file(path, file_name)
    except:
        raise RuntimeError("Unable to parse report")

    return parsed_issue_report_dict


def create_insulin_effect_fixture(report_dict):
    try:
        insulin_effects = report_dict["insulin_effect"]
    except:
        raise RuntimeError("Unable find key 'insulin_effect'")

    output = []

    for effect in insulin_effects:
        parsed_effect = {}
        parsed_effect["date"] = issue_report_date_parser(effect["start_time"])
        parsed_effect["amount"] = effect["value"]
        parsed_effect["unit"] = effect["units"]
        output.append(parsed_effect)

    return output


def create_carb_effect_fixture(report_dict):
    try:
        carb_effects = report_dict["carb_effect"]
    except:
        raise RuntimeError("Unable find key 'carb_effect'")

    output = []

    for effect in carb_effects:
        parsed_effect = {}
        parsed_effect["date"] = issue_report_date_parser(effect["start_time"])
        parsed_effect["unit"] = effect["units"]
        parsed_effect["amount"] = effect["value"]
        output.append(parsed_effect)

    return output


def create_momentum_effect_fixture(report_dict):
    try:
        momentum_effects = report_dict["glucose_momentum_effect"]
    except:
        raise RuntimeError("Unable find key 'glucose_momentum_effect'")

    output = []

    for effect in momentum_effects:
        parsed_effect = {}
        parsed_effect["date"] = issue_report_date_parser(effect["startDate"])
        parsed_effect["unit"] = effect["quantity_units"]
        parsed_effect["amount"] = effect["quantity"]
        output.append(parsed_effect)

    return output


def create_counteraction_effect_fixture(report_dict):
    try:
        counteraction_effects = report_dict["insulin_counteraction_effects"]
    except:
        raise RuntimeError("Unable find key 'insulin_counteraction_effects'")

    output = []

    for effect in counteraction_effects:
        parsed_effect = {}
        parsed_effect["startDate"] = issue_report_date_parser(effect["start_time"])
        parsed_effect["endDate"] = issue_report_date_parser(effect["end_time"])
        parsed_effect["unit"] = "mg\/min·dL"
        parsed_effect["value"] = effect["value"]
        output.append(parsed_effect)

    return output


def create_retrospective_effect_fixture(report_dict):
    try:
        retrospective_effects = report_dict["retrospective_glucose_effect"]
    except:
        raise RuntimeError("Unable find key 'retrospective_glucose_effect'")

    output = []

    for effect in retrospective_effects:
        parsed_effect = {}
        parsed_effect["date"] = issue_report_date_parser(effect["startDate"])
        parsed_effect["unit"] = effect["quantity_units"]
        parsed_effect["amount"] = effect["quantity"]
        output.append(parsed_effect)

    return output


def create_predicted_glucose_fixture(report_dict):
    try:
        predicted_glucose = report_dict["predicted_glucose"]
    except:
        raise RuntimeError("Unable find key 'predicted_glucose'")

    output = []

    for glucose in predicted_glucose:
        parsed = {}
        parsed["date"] = issue_report_date_parser(glucose["start_time"])
        parsed["unit"] = glucose["units"]
        parsed["amount"] = glucose["value"]
        output.append(parsed)

    return output
