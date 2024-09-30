#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:52:46 2024

@author: affan
"""



def calculate_homework(homework_assignment_args):
    sum_of_grades = 0
    for homework in homework_assignment_args.values():
        sum_of_grades += homework
    final_grade = round(sum_of_grades/len(homework_assignment_args),2)
    print(final_grade)
    