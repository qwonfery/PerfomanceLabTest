import argparse
import json


def tests_parser(tests: dict, values: dict) -> dict:
    for test in tests:
        print(test)
        if test.get('value', '') == '':
            test['value'] = values.get(test['id'])
        if test.get('values', '') != '':
            test['values'] = tests_parser(test['values'], values)
    return tests


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("values_filepath")
    parser.add_argument("tests_filepath")
    parser.add_argument("report_filepath")

    args = parser.parse_args()

    with open(args.values_filepath) as f:
        raw_values = f.read()

    values_dict = {}
    for raw_value in json.loads(raw_values)['values']:
        values_dict[raw_value['id']] = raw_value['value']

    with open(args.tests_filepath) as f:
        raw_tests = f.read()

    with open(args.report_filepath, mode="w") as f:
        f.write(json.dumps(tests_parser(json.loads(raw_tests)['tests'], values_dict)))