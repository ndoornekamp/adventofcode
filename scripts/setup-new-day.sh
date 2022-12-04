#!/bin/bash

folder_name=day$1
mkdir $folder_name -p
touch $folder_name/input.txt
touch $folder_name/test_input.txt
touch $folder_name/$folder_name.py