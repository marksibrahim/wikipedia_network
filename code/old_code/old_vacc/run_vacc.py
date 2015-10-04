
contents = """# This job needs 1 compute node with 1 processor per node.
#PBS -l nodes=1:ppn=1
# It should be allowed to run for up to 1 hour.
#PBS -l walltime=06:00:00
# Name of job.
#PBS -N myjob
# Join STDERR TO STDOUT.  (omit this if you want separate STDOUT AND STDERR)
#PBS -j oe   
# Send me mail on job start, job end and if job aborts
#PBS -M mark.s.ibrahim@uvm.edu
#PBS -m bea

cd /users/m/s/msibrahi/v3/code/
echo "This is myjob running on " `hostname`
python process_xml_v3.py """

import subprocess, os


log_path = "/users/m/s/msibrahi/v3/code/vacc_logs/"
os.chdir(log_path)

for i in range(0, 112):
    with open('wikijob'+str(i)+".script", "w") as f:
        f.write(contents + str(i))

for i in range(0,112):
    command = "qsub wikijob" + str(i) + ".script" 
    subprocess.call(command, shell=True)
