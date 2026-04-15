#	Linux-Based System Intergration & Automation

A systems engineering project built on a raspberry pi 5 to learn the basics of system intergration. The goal of this project was connect multiple automated componets into a unfied pipeline



## Project Overview

This projects works on core system engineering concepts including:
- Real-Time hardware monitoring
- automated log process and anomaly detection
- file system automation and organization
- cross-platform scripting (Python + PowerShell)
- End-to-end pipeline integration



## Componets

1. System monitor (scripts/system_monitor.py)
-	reads cpu, memory, and disk usage
-	timestamps entries to log file every 30 seconds

2. Log Processor (Scripts/log_processor.py)
- 	reads system log
-	flags if cpu usage is above 80 percent
