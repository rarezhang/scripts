#!/bin/bash
database="ecigHigh"
mongodump -d $database -o mongodump/
