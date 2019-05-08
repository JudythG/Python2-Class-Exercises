# Python2-Class-Exercises
Exercises from in-class demos

## lambda functions
### Done
<table>
  <tr><td>factorial</td><td>Done</td></tr>
  <tr><td>mean</td><td>Done</td></tr>
  <tr><td>fibonacci</td><td></td></tr>
  <tr><td>filter</td><td>Done</td></tr>
  </table>

## list comprehensions
### Done
1. create a 2D matrix
2. flatten a 2D list
3. flatten a 2D list and only include strings whose len < 6
4. flip keys and values in a dictionary

## generators
### Done
### Not Done
1. write a generator function to return to fibonacci series
2. use your generator in the given code

## exceptions
### Done
Raise an exception - raise.py

## regular expressions
### Done
Parse out title and author: 'The Stone Sky, by N.K. Jemisin'

Parse out title and author, whitespace added at front: '    The Stone Sky, by N.K. Jemisin'

Parse out title, author, and publisher: '    The Stone Sky, by N.K. Jemisin (Orbit)'

Create a regex that parses each of these publishers:
* ' (Orbit)'
* ' (Tor.com Publishing)'
* '(Uncanny, March/April 2017)'
* '(Harper Voyager / Spectrum Literary Agency)'
* '(Twelfth Planet Press)'

Parse out title and author when line has metacharacters:
* '"And Then There Were (N-One)," by Sarah Pinsker (Uncanny, March/April 2017)'
* 'Binti: Home, by Nnedi Okorafor (Tor.com Publishing)'

', by' used to split title from author. Now title has a comma: 
* '"Children of Thorns, Children of Water," by Aliette de Bodard (Uncanny, July-August 2017)'

Separator can be ', by' or ', edited by'
* '    Luminescent Threads: Connections to Octavia E. Butler, edited by Alexandra Pierce, and Mimi Mondal (Twelfth Planet Press)'

Parse file hugo_2018.txt
Working for all lines except one that has a different format (We were told raw data is tricky. ):
* “Sun, Moon, Dust” by Ursula Vernon, (Uncanny, May/June 2017)
