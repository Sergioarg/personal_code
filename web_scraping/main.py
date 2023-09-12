#!/usr/bin/env -S powershell.exe -c python3
from schedule_clases import schedule_clases


if __name__ == '__main__':

    user = '1000162785'
    password = 'SmartSchool'
    next_reps = 10
    schedule_clases(user, password, 5)
