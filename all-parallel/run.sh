## 1 process
time python main_popen.py out/proc1.csv 1 > out/proc1.time 2>&1

## 4 processes (shared work queue)
time python main_popen.py out/proc4.csv 4 > out/proc4.time 2>&1

## 8 processes (shared work queue)
time python main_popen.py out/proc8.csv 8 > out/proc8.time 2>&1
