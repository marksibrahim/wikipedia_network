
contents1 = """# This job needs 1 compute node with 1 processor per node.
#PBS -l nodes=1:ppn=1,pmem=4gb,pvmem=5gb
# It should be allowed to run for up to 1 hour.
#PBS -l walltime=08:00:00
# Name of job.
#PBS -N traverse"""

contents2="""# Join STDERR TO STDOUT.  (omit this if you want separate STDOUT AND STDERR)
#PBS -j oe   
# Send me mail on job start, job end and if job aborts
#PBS -M mark.s.ibrahim@uvm.edu
#PBS -m bea

cd /users/m/s/msibrahi/v3/code/
echo "This is myjob running on " `hostname`
python chopped_traverse.py """

import subprocess, os


log_path = "/users/m/s/msibrahi/v3/code/vacc_logs/"
os.chdir(log_path)

for i in [112,113, 114]:
    with open('traverse_job'+str(i)+".script", "w") as f:
        f.write(contents1 + str(i) +"\n" + contents2 + str(i))

for i in [112, 113, 114]:
    command = "qsub traverse_job" + str(i) + ".script" 
    subprocess.call(command, shell=True)
