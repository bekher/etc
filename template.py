#!/usr/bin/env python
#
# scriptNameHere.py
#
# Description: This script does nothing. It is a template for the consistent
# development of Python scripts.
# Find/replace the string "scriptNameHere" with the name of the script you are
# writing. NOTE that if you run this script it will write to
# /var/log/scriptNameHere
#
# Usage: scriptNameHere.py --help for more detailed info
#
# Sample usage:
#	./scriptNameHere.py arg0 arg1 --option1
#
# Version: 01.16.15

# This line is exactly 80 characters, use as a guide for line character length.

import logging
import os, sys
# import the deprecated optparse for backwards compatibility w/Python 2.6
import optparse

# main method, gets called with parsed arguments
def main(options, args):

	### Write your code here ###

	# dealing with arguments/options:
	# parsed options:
	# 	parsedOptionValue = options.logpath #store logpath
	# unparsed arguments (split by space)
	# 	argument1 = args[0]
	# 	argument2 = args[1]

# called upon execution
if __name__ == "__main__":

	# set script name for logging
	scriptName = "scriptNameHere"

	# set up optparse
	usage = "Usage: %prog arg0 arg1 [options] "
	epilog = "Note: add additional notes and caveats to program usage here"
	
	parser = optparse.OptionParser(usage=usage, epilog=epilog)
	parser.add_option('--verbose', action='store_true', default = False, help='be verbose')
	parser.add_option('--logpath', action='store', default ='/var/log/'+scriptName, help='change log path')

	(options, args) = parser.parse_args()

	# set up logging
	loggingLevel = None

	# logging level
	if options.verbose:
    loggingLevel = logging.DEBUG
	else:
    loggingLevel = logging.INFO

	logging.basicConfig(format='%(asctime)s ' + scriptName +
    ' (%(levelname)s): %(message)s', filename=options.logpath,
    level=loggingLevel)

	# this message will write to log only if verbose is enabled
	logging.debug("verbose/debug logging mode enabled")

	# change arg numbers as needed, or comment out completely
	if len(args) <0:
    # parser.error("...") will terminate the program w/usage error
    parser.error("Not enough arguments")
	elif len(args) >0:
    parser.error("Too many arguments")

	# main is called here.
	try:
    print "logging to: " + options.logpath
    logging.info(scriptName + " init")
    main(options,args)
    logging.info(scriptName + " terminated\n")

	# catch keyboard interrupt exceptions to avoid trace printing
	except KeyboardInterrupt:
    logging.warning("Keyboard interrupt")
    logging.info(scriptName + " terminated\n")
    
	# all other exceptions caught here
	except:
    # logging.exception("...") prints stack trace to log
    logging.exception(scriptName + " terminated by exception:")
    # raise prints stack trace to stderr
    raise
