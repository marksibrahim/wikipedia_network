contents = """# This job needs 1 compute node with 1 processor per node.
#PBS -l nodes=1:ppn=1,pmem=8gb,pvmem=9gb
# It should be allowed to run for up to 6 hours.
#PBS -l walltime=06:00:00
# Name of job.
#PBS -N combine_paths
# Join STDERR TO STDOUT.  (omit this if you want separate STDOUT AND STDERR)
#PBS -j oe   
# Send me mail on job start, job end and if job aborts
#PBS -M mark.s.ibrahim@uvm.edu
#PBS -m bea

cd /users/m/s/msibrahi/v4/code/
echo "This is myjob running on " `hostname`
python combine_paths.py """

import subprocess, os


log_path = "/users/m/s/msibrahi/v4/code/vacc_logs/"
os.chdir(log_path)

chunks = [(0,20), (20, 40), (40, 60), (60, 80), (80,100), (100,112)]

for chunk in chunks:
    with open("combinepathsjob"+ str(chunk[0])+ ".script", "w") as f:
        f.write(contents + str(chunk[0]) + " " + str(chunk[1]))

    command = "qsub " + "combinepathsjob" + str(chunk[0]) + ".script"
    subprocess.call(command, shell=True)
