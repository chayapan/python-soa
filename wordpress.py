# -*- encoding: utf-8 -*-
##############################################################################
#
#	Chayapan Khannabha	<chayapan@gmail.com>
#	Copyright (C) 2013
#
"""
soa_content.py module
from content_soa import wordpress


argparse module
  wordpress --help | -h
  wordpress connect -H www.disqrete.com -P 80
"""

def command_line():
	from argparse import ArgumentParser
	parser = ArgumentParser()
	parser.add_argument("action", help="Action: connect		to Wordpress instance tags 		list tags""")
	parser.add_argument("-H", "--host", help="Host")
	parser.add_argument("-P", "--port", help="Port", type=int)
	parser.add_argument("--logging", help="logging", action='store_true')
	parser.add_argument("--verbose", help="verbosity", action='count')
	args = parser.parse_args()
	print args.host, args.port

	if args.action:
	  if args.action == 'connect': 
		print "connecting to %s %s" % (args.host, args.port)

if __name__ == '__main__':
	command_line()