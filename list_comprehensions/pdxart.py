#!/usr/bin/env python

import csv
import json as simplejson
import argparse
import re

def transform_dict(header, row):
    return dict(zip(header, row))

def transform_json(header, row):
    transforms = dict(zip(header, row))
    return simplejson.dumps(transforms)

def descriptions(header, arte):
    # Exercise: Transform description for loop into a list comprehension
    descriptions = []
    for row in arte:
        descriptions.append(transform_dict(header, row)['description'])

    for d in descriptions:
        print d

def titles(header, arte):
    # EXAMPLE: Return only titles
    titles = [ transform_dict(header, row)['title'] for row in arte]
    for t in titles:
        print t

def artists(header, arte):
    # Exercise: Return only artists
    artists = [ transform_dict(header, row)['artist'] for row in arte ]
    for a in artists:
        print a

def funding_source(header, arte):
    # Return only funding source
    funding_source = [ transform_dict(header, row)['funding_source'] for row in arte ]
    unique_funding_source = set(funding_source)
    for f in unique_funding_source:
        print f

def locations(header, arte):
    # Exercise: Return only locations
    print "Not implemented"

def artists_by_medium(header, arte, medium_type):
    # EXAMPLE: Return artists by medium type, by regular expression
    all_works = [ transform_dict(header, row) for row in arte ]
    regex = re.compile( '(' + medium_type + ')' )
    # Exercise: Return *unique* artists by medium type
    # Exercise: Transform for loop into a list comprehension
    for work in all_works:
        match = re.search(regex, work['medium'])
        if match:
            print work['artist']

def medium(header, arte):
    # EXAMPLE: Return only mediums
    mediums = [ transform_dict(header, row)['medium'] for row in arte ]
    # Exercise: sort and only print unique mediums -- hint: See sorted and set
    for m in mediums:
        print m

def medium_by_type(header, arte, medium_type):
    # EXAMPLE: Return mediums of a certain type
    mediums = [ transform_dict(header, row)['medium'] for row in arte ]
    regex = re.compile( '(' + medium_type + ')' )
    for m in mediums:
        match = re.search(regex, m)
        if match:
            print m

def artists_by_firstname(header, arte, name):
    # Exercise: search for artists by first name
    artists = [ transform_dict(header, row)['artist'] for row in arte ]
    regex = re.compile( '(' + name + ')' )
    for m in set(artists):
        match = re.search(regex, m)
        if match:
            print m


def thumbnail(header, arte):
    # Exercise: download the thumbnails of all the works of art
    print "not implemented"

def recid(header, arte):
    # Exercise: strip the recid out of the detail_url
    print "not implemented"

def as_json(header, arte):
    # EXAMPLE: Return all as JSON
    alljson = [ transform_json(header, row) for row in arte ]
    for j in alljson:
        print j

def demo(args, arte):

    header = arte.next()

    if args.titles:
        titles(header, arte)
    elif args.descriptions:
        descriptions(header, arte)
    elif args.artists:
        artists(header, arte)
    elif args.artists_by_medium:
        artists_by_medium(header, arte, args.artists_by_medium)
    elif args.artists_by_firstname:
        artists_by_firstname(header, arte, args.artists_by_firstname)
    elif args.funding_source:
        funding_source(header, arte)
    elif args.medium:
        medium(header, arte)
    elif args.medium_type:
        medium_by_type(header, arte, args.medium_type)
    elif args.asjson:
        as_json(header, arte)

# Meta exercise: Only return unique rows for all functions
# Meta exercise: Allow values to be returned sorted by date modified (either most recent, or least recent)
# Meta exercise: Find other interesting attributes of the data and write your own function!
# Meta exercise: Make calling of functions more efficient than using the "if-then-else" loop

if __name__ == '__main__':

    # Meta exercise: Add a configuration file
    conf_parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter, add_help=False)
    conf_parser.add_argument("--config", dest="filename", help="Config File input", metavar="FILE", default=None)
    args, remaining_argv = conf_parser.parse_known_args()

    if args.filename:
        config = ConfigParser.SafeConfigParser()
        config.read([args.filename])
        defaults = dict(config.items("Defaults"))
    else:
        defaults = { "option":"default" }

    argparser = argparse.ArgumentParser(parents=[conf_parser])
    argparser.add_argument("--titles", help="print titles of public art", action="store_true", default=False)
    argparser.add_argument("--descriptions", help="print descriptions of public art", action="store_true", default=False)
    argparser.add_argument("--artists", help="print artists", action="store_true", default=False)
    argparser.add_argument("--artists_by_firstname", help="print artists by first name", action="store", default=None)
    argparser.add_argument("--funding_source", help="print funding_source", action="store_true", default=False)
    argparser.add_argument("--medium", help="print mediums", action="store_true", default=False)
    argparser.add_argument("--asjson", help="return file contents at json", action="store_true", default=False)
    argparser.add_argument("--medium-type", help="print mediums of type TYPE", action="store", default=None)
    argparser.add_argument("--artists-by-medium", help="print artists based on medium of type TYPE", action="store", default=None)
    argparser.set_defaults(**defaults)
    args = argparser.parse_args(remaining_argv)

    # Meta exercise: Make opening a file by filename specified on the command-line
    with open('public_art.csv', 'rb') as csvfile:
        arte = csv.reader(csvfile, delimiter=',', quotechar='"')
        demo(args, arte)


