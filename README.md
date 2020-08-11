# Tools to Generate Loop Fixtures

This script can be used to generate Loop-compatible fixtures for momentum effect, insulin effect, counteraction effect, carb effect, retrospective effect, and predicted glucose utilizing the Loop issue report parser.

## Usage
1. Export issue report from Loop.
2. Activate the virtual environment.
3. To create the fixtures, call the `get_fixtures_from_report` function with the path to the issue report, the issue report name, and the file extension. An example would be `get_fixtures_from_report("/Users/novalegra", "loop-report", "md")`.
4. The fixtures will be exported to the same directory as the issue report is in.
