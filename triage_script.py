
import os
import subprocess
import shlex
import sys






DEBUG = True

def debug(debug_str: str):
	if DEBUG:
		print("[DEBUG] "+str(debug_str))
	return

if __name__=="__main__":

	# This runs the fuzzed binary for each crash testcase and then logs the output to asan_logs/

	#command = "./csgo_linux64 -console -dev -condebug -textmode -novid -noshaderapi ./grgreg"

	if len(sys.argv) < 2:
		print("Usage: python3 "+str(sys.argv[0])+" \"COMMAND WHICH TAKES INPUT FROM STDIN\" CRASHDIR")
		exit(1)


	command = sys.argv[1]

	crash_dir = sys.argv[2]

	debug("Command is this: "+str(command))

	if crash_dir[-1] != "/":
		crash_dir += "/"



	crash_files = os.listdir(crash_dir)


	for i, crash_file in enumerate(crash_files):
		crash_file = shlex.quote(crash_file)

		crash_file = crash_dir+crash_file

		#print("Now running file number "+str(count)+" filename : "+str(crash_file))

		debug("Reading this file now: "+str(crash_file))

		fh = open(crash_file, "rb") # Read in binary mode

		stdin_input = fh.read()

		fh.close()

		full_crash_filename = crash_dir+str(crash_file)

		report_filename = "reports/reportnum"+str(i)+".txt"
		fh = open(report_filename, "wb")
		fh.write(bytes(crash_file, encoding="ascii"))
		fh.write(b"\n\n")


		command_list = command.split(" ")
		debug("command_list == "+str(command_list))

		#try:
		subprocess.run(command_list, timeout=60*5, stderr=fh, stdout=fh, input=stdin_input) # Input from stdin.
		#except:
		#	debug("Skipping testcase...")


		debug("Done!")
		fh.close()



	debug("Done")






