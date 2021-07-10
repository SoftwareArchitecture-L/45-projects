### DataSet

This repository stores the data collected for our 2021 ISSRE work.

This catalog contains the data results of the 45 projects we used. In each project we have two folders, "Version1" and "Version2", corresponding to the two versions of the project(e.g. https://github.com/2021issre/45-projects/tree/master/airflow). 

In the directory of the specific version, there are folders with four architectural anti-patterns(e.g. https://github.com/2021issre/45-projects/tree/master/airflow/Version1)

When entering an anti-pattern folder, it shows all the anti-patterns of this type detected by this project(e.g. https://github.com/2021issre/45-projects/tree/master/airflow/Version1/Crossing). In addition, **root_other.txt** is also in this directory, which shows the core data in this paper. That is, the detection results of **root file** and **other file**. In this file, the first line shows the **root file**, and the second line shows the **other file**.

Finally, entering a specific anti-pattern folder(e.g. https://github.com/2021issre/45-projects/tree/master/airflow/Version1/Crossing/Crossing1), where there is a file: **Crossing1.dv8-issue**. It provides a CRS anti-pattern detected in project Airflow.

### Tool

You can use [DV8](https://archdia.com/) to open the $anti-pattern$.dv8-issue.