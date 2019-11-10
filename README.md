## Motivation
Loop reports are written out as a markdown file. This project aims to develop a parser to parse 
the markdown and return a python Dictionary. This will allow broader programmatic use of the data coming 
from the loop report. 

## Usage
Requires loop report and python 3.6+

Create and activate a virtual Environment:
```
python3 -m venv loop_venv
source loop_venv/bin/activate # linux/mac
loop_venv\Scripts\activate # windows 
pip install git+https://github.com/tidepool-org/loop-issue-report@{Branch Name} -vvv
```
Execute the following with a valid file_path and file_name:
``` 
from loop.issue_report import parser

lr = parser.LoopReport()
file_path = "filePathForLoopReport"
file_name = "nameOfLoopReport.md"
loop_dict = lr.parse_by_file(path=file_path, file_name=file_name)
```
 Or
 
 Use the parser_client located within loop/issue_report 
 ToDo: fill in instructions on using the client. 
 ``` ```