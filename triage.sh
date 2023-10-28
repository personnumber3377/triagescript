#!/bin/sh

rm -r reports/
rm -r all_crashes/
mkdir reports
mkdir all_crashes
cp outputs_new_new/default/crashes/* all_crashes/
python3 triage_script.py "./tcook -w -utc -ng test.svg" all_crashes/


