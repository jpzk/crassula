# crassula

crassula is a lightweight Python coding companion for agile programming. crassula is inspired by [jarvis](https://github.com/madlag/jarvis) and originally by [Light Table](http://www.kickstarter.com/projects/ibdknox/light-table). In contrast to jarvis, crassula should be a very lightweight solution to implement a short feedback-loop. Therefore absolutely no dependencies are needed. 

## Example

Open a terminal and start crassula to trace a certain file, there's an example file traced.py included. 

<pre>
$ cd crassula
$ python crassula.py traced.py 
</pre>

traced.py content is:

<pre>
1 def foo():
2   a = [] 
3   for i in range(0,10):
4       a.append(i) 
5 foo()        
</pre>

crassula watches the file traced.py for any modifications. If you modify traced.py the local variables with line numbers are enumerated in crassula.

<pre>
traced.py: 1: 
traced.py: 2: 
traced.py: 3: a => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] i => 9 
traced.py: 4: a => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] i => 9 
traced.py: 5: foo => function foo at 0x1e96398
</pre>

## Hacking

I need your support to hack a VIM plugin, which registers as hook on line-changing and firing an action of notifying crassula which line the programmer selected. Implementing this could filter the output of crassula in a helpful way.

## License 

This file is part of crassula.

crassula is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

crassula is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with crassula. If not, see <http://www.gnu.org/licenses/>.



