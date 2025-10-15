# Python Multithreading & Multiprocessing Experiments

This repository contains three experimental Python scripts exploring the performance of **multithreading**, **multiprocessing**, and **CPU scheduling** through small-scale simulations and benchmarks.

## Contents

### 1. FIFO_Thread_Test.py
Simulates concurrent appending operations to a custom FIFO (queue-like) data structure using Python threads.  
- Demonstrates synchronization-free thread behavior and timing analysis.

### 2. RoundRobin_Scheduler_Threads.py
Implements a simplified **Round Robin CPU Scheduling** algorithm, executed by 100 threads.  
- Measures average waiting and turnaround times for multiple processes.  
- Useful for understanding OS scheduling concepts.

### 3. Parallel_IO_vs_Normal.py
Compares **parallel I/O writing** using `ProcessPoolExecutor` with **standard sequential I/O** operations.  
- Highlights the performance difference between multiprocessing and single-process I/O.

## Results
Each script prints its execution time, allowing easy comparison between concurrent and sequential approaches.

## Requirements
- Python 3.8+
- Standard library modules: `threading`, `concurrent.futures`, `time`, `random`, `logging`

## License
MIT License

## Author
Özge Karasu  
Computer Engineer & MSc AI Candidate  
Interested in parallel computing, OS-level algorithms,
