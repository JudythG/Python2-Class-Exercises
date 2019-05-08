import re

# moving towards parsing titles and authors from the Hugo Awards site
# the exercises here are to parse each line into authors and titles
# the pattern to match titles and authors will build-up in each function
# at the end, check that the new pattern works on all the line variants

# match pattern to line
# if successful, print the part of the line that matches
# else print error message
def testPattern(pattern, line, errorMsg):
    p = re.compile(pattern)
    m = p.search(line)
    if m:
        print (line[m.start():m.end()])
    else:
        print (errorMsg)

# for this exercise, parse out the title, The Stone Sky, 
# and the author, N.K. Jemisin
def parse_title():
    print ("parse_title:")

    line = 'The Stone Sky, by N.K. Jemisin'

    title_pattern = '[a-zA-Z\s]+'
    testPattern(title_pattern, line, "parse_title: title error")

    sep_pattern = ', by\s'
    testPattern (sep_pattern, line, 'parse_title: sep pattern error')

    # Note the author's name has periods but in regex a period is a 
    # metacharacter. It has a special meaning in the pattern.
    # To search for a period, use the backslash as an escape character
    # . matches any single character
    # /. matches only a period
    author_pattern = '[a-zA-Z\.\s]+'
    new_line = 'N.K. Jemisin'
    testPattern (author_pattern, new_line, 'parse_title: author pattern error')

    # whole pattern combines the three patterns
    # Note that the title pattern and author pattern are each
    # surrounded by parentheses. This returns them from group
    pattern = '([a-zA-Z\s]+), by\s([a-zA-Z\.\s]+)'
    p = re.compile (pattern)
    m = p.search(line)
    if m:
        print ('Title: ' + m.group(1))
        print ('Author: ' + m.group(2))

    # an alternate solution is to use the dot operator, matches almost any char
    pattern = '([^,.]+), by\s(.+)'
    p = re.compile (pattern)
    m = p.search(line)
    if m:
        print ('Title: ' + m.group(1))
        print ('Author: ' + m.group(2))

    print ()

# adding complexity until can parse titles from the hugo awards page
# title and author lines start with whitespace
def start_with_whitespace():
    print ('exercise: start with whitespace')

    line = '    The Stone Sky, by N.K. Jemisin'
    pattern = '\s+([a-zA-Z\s]+), by\s([a-zA-Z\.\s]+)'
    pattern = '\s+([^,.]+), by\s(.+)'
    p = re.compile (pattern)
    m = p.search(line)
    if m:
        print ('Title: ' + m.group(1))
        print ('Author: ' + m.group(2))
    else:
        print ('error')

    print ()

# add publisher after title
# parse out title, author, and publisher
# Note: may leave publisher in parentheses
# results:
#  Title:     The Stone Sky
#  Author:    N.K. Jemisin
#  Publisher: (Orbit)
# 
# Note: ( and ) are metacharacters
def add_publisher():
    print ('exercise: add publisher')

    line = '    The Stone Sky, by N.K. Jemisin (Orbit)'

    # note that ( and ) are metacharacters in the pattern
    # they indicate that part of the pattern should be processed 
    # as a group.
    # What do we do when we want to search for parentheses?
    # re interprets \( as a ( character
    testPattern(' \([a-zA-Z]+\)', ' (Orbit)', 'error in publisher pattern')
    p = re.compile('\(([a-zA-Z]+)\)')
    m = p.search (' (Orbit)')
    if m:
        print ("group: " + m.group(1))

    # But we don't have to change the pattern because the open
    # parenthesis isn't in the author search pattern
    pattern = '\s+([a-zA-Z\s]+),\sby\s([a-zA-Z\.\s]+)'
    p = re.compile (pattern)
    m = p.search(line)
    if m:
        print ('Title: ' + m.group(1))
        print ('Author: ' + m.group(2))
    else:
        print ('error')

    # lets parse out the publisher as well

    # pattern without dot operator
    pattern = '\s+([a-zA-Z\s]+),\sby\s([a-zA-Z\.\s]+)\(([a-zA-Z]+)\)'	

    # pattern with dot operator
    pattern = '\s+([^,.]+),\sby\s([a-zA-Z\.\s]+)\((.+)\)'
    p = re.compile (pattern)
    m = p.search(line)
    if m:
        print (m.groups())
    else:
        print ('error')

    print ()

# publishers not just one word i.e (Orbit)
# parse all variants
# results:
# parsing ' (Orbit)' should return 'Orbit' or '(Orbit)'
# parsing '(Uncanny, March/April 2017)' should return 
#    '(Uncanny, March/April 2017)' or 'Uncanny, March/April 2017'
def parse_publishers():
    orbit = ' (Orbit)'
    tor = ' (Tor.com Publishing)'
    uncanny = '(Uncanny, March/April 2017)'
    harper = '(Harper Voyager / Spectrum Literary Agency)'
    twelfth_planet = '(Twelfth Planet Press)'

    pattern = '\s*\([a-zA-Z\.,\d/\s]+\)'
    testPattern (pattern, orbit, 'publisher error')
    testPattern (pattern, tor, 'publisher error')
    testPattern (pattern, uncanny, 'publisher error')
    testPattern (pattern, harper, 'publisher error')
    testPattern (pattern, twelfth_planet, 'publisher error')
    print ()

# adding characters to title pattern
# parse title and author
# the title pattern has new characters: " ( ) -
# results (printed as m.group())
#    ('And Then There Were (N-One)', 'Sarah Pinsker ')
#    ('Binti: Home', 'Nnedi Okorafor ')
def update_title_format():
    print ("update title format exercise")

    line = '"And Then There Were (N-One)," by Sarah Pinsker (Uncanny, March/April 2017)'

    pattern = '\s*\"*([a-zA-Z\s\-\(\):]+),"*\sby\s([a-zA-Z\.\s]+)'
    pattern = '\s+([^,.]+),\sby\s([a-zA-Z\.\s]+)\((.+)\)'

    p = re.compile(pattern)
    m = p.search (line)
    if m:
        print (m.groups())

    line = 'Binti: Home, by Nnedi Okorafor (Tor.com Publishing)'
    p = re.compile(pattern)
    m = p.search (line)
    if m:
        print (m.groups())
    print ()

# note the comma in the title. Ending title search at a title won't work
# apparently need to use a negative lookahead assertion
# which must be put into the title part of the string
def comma_in_title():
    print ('comma in title exercise')

    line = '"Children of Thorns, Children of Water," by Aliette de Bodard (Uncanny, July-August 2017)'

    pattern = '\s*\"+([a-zA-Z\s,]+(?!, by $)),"+\sby\s([a-zA-Z\.\s]+)'
    pattern = '\s*\"+(.+(?!, by $)),"+\sby\s([a-zA-Z\.\s]+)\((.+)\)'
    p = re.compile(pattern)
    m = p.search (line)
    if m:
        print (m.groups())
    print ()

def testSepPattern(line):
    print(line)
    sep_pattern = ',”?( [a-zA-Z])* by [^\(]+'
    sep_pattern = ',”?( [a-zA-Z])* by [a-zA-Z]+,?[^\(]+'
    sep_pattern = '\sby\s'
    p = re.compile(sep_pattern)
    m = p.search(line)
    if m:
        print('Title: ' + line[:m.start()])
        print ('Author: ' + line[m.start():m.end()])
        print('Publisher: ' + line[m.end():])
    print()

# separator can be ', by' or ', edited by'
def different_separators():
    print ('different separators exercise')

    line = '    Luminescent Threads: Connections to Octavia E. Butler, edited by Alexandra Pierce, and Mimi Mondal (Twelfth Planet Press)'
    print (line)

    pattern = '\sby\s'
    p = re.compile(pattern)
    m = p.search(line)
    if m:
        title = parse_title (line[:m.start()])
        print('Title: ' + title)

        author_pattern = '(.+[^\(]) '
        pub_pattern = '\((.+[^\)])\)'
        regex = author_pattern + pub_pattern
        p = re.compile(regex)
        m = p.search(line[m.end():])
        if m:
            print ('Creator(s): ' + m.group(1))
            print('Publisher: ' + m.group(2))
            print()
    return

    #sep_pattern = ',( [a-zA-Z]*) by [a-zA-Z \.]+'
    sep_pattern = ',( [a-zA-Z]*) by [^\(]+'
    p = re.compile(sep_pattern)
    m = p.search(line)
    if m:
        print (line)
        print(line[:m.start()])
        print (line[m.start():m.end()])
        print(line[m.end():])
    return

    pattern = '\s*\"*([a-zA-Z\s\-\(\):\.]+),"*\s[\w\s]+\s([a-zA-Z\.\s,]+)\((.+)\)'
    #pattern = '\s*\"+(.+(?!, by $)),"+\sby\s([a-zA-Z\.\s]+)\((.+)\)'
    pattern = '(.*(^,(\s\w+)? by)),(\s\w+)? by(.*)'
    pattern = '(.*(^,(\s\w+)? by))'
    pattern = '(.*[^,])'
    p = re.compile(pattern)
    m = p.search (line)
    if m:
        print (line)
        print (m.groups())
    print ()

def test ():
    line = '    “Sun, Moon, Dust” by Ursula Vernon, (Uncanny, May/June 2017)'
    testSepPattern(line)

def parse_title(s):
    pattern = '\s*(.+[^,]),'
    p = re.compile(pattern)
    m = p.search(s)
    if m:
        title = m.group(1)
        if title.startswith('“'):
            title = title + '”'
        return title
    return s

# new pattern has issues with 'edited by', 'written by', 'illustrated by' strings but I think the old pattern may handle them better
def parsefile (f_name):
    pattern = '\sby\s'

    f_out = open('parsed.txt', 'w')
    f_in = open (f_name, 'r')
    for line in f_in:
        p = re.compile(pattern)
        m = p.search(line)
        if m:
            print (line, file=f_out)
            title = parse_title (line[:m.start()])
            print('Title: ' + title, file=f_out)

            author_pattern = '(.+[^\(]) '
            pub_pattern = '\((.+[^\)])\)'
            regex = author_pattern + pub_pattern
            p = re.compile(regex)
            m = p.search(line[m.end():])
            if m:
                print ('Creator(s): ' + m.group(1), file=f_out)
                print('Publisher: ' + m.group(2), file=f_out)
                print(' ', file=f_out)

# main

#classDemo()
#parse_title()
#start_with_whitespace()
#add_publisher()
#parse_publishers()
#update_title_format()
#comma_in_title()
different_separators()
#parsefile('./hugo_2018.txt')
#test()
