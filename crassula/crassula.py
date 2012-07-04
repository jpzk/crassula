''' 
This file is part of crassula.

Copyright 2012, Jendrik Poloczek

crassula is free software: you can redistribute it
and/or modify it under the terms of the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

crassula is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along with
crassula.  If not, see <http://www.gnu.org/licenses/>.
'''

import time
import sys
import inspect 
import runpy
import os

class Crassula():
    
    class Tracer(object):        
        ''' This class is used to trace the local variables while executing
        the traced code. '''

        class NullDevice(object):
            ''' This class is used to mute the stdout output while executing 
            the traced code. '''
            def write(self, s):
                pass

        def __init__(self, filename):
            self.run_info = {}
            self.filename = filename
            self.start_time = os.stat(self.filename).st_mtime
            self.orginal_stdout = sys.stdout

        def watchdog(self, seconds):
            while(True):
                if(os.stat(self.filename).st_mtime > self.start_time):
                    self.run_info = {}
                    self.set_trace()
                    sys.stdout = self.NullDevice()        
                    try:
                        execfile(self.filename, {}, {})
                        sys.stdout = self.orginal_stdout
                        self.output()
                    except Exception as e:
                        sys.stdout = self.orginal_stdout
                        print "Exception raised: " + str(e)
                    finally:
                        self.uninstall_trace()
                        self.start_time = os.stat(self.filename).st_mtime
                else:
                    time.sleep(seconds)

        def tracefunc(self, frame, event, arg): 
            filename = inspect.getfile(frame)
            line = frame.f_lineno

            if filename not in self.run_info:
                self.run_info[filename] = {}
            if line not in self.run_info[filename]:
                self.run_info[filename][line] = {}
    
            for k, v in frame.f_locals.iteritems():            
                self.run_info[filename][line][k] = v

            return self.tracefunc

        def output(self):
            for k, v in self.run_info[self.filename].iteritems():
                line = self.filename + ": " + str(k) + ": "
                for var, val in v.iteritems():
                    line += str(var) + " => " + str(val) + " "
                print line

        def set_trace(self):
            sys.settrace(self.tracefunc)

        def uninstall_trace(self):
            sys.settrace(None)       

    def __init__(self):
        if(len(sys.argv) < 2):
            print("use: "+ sys.argv[0] + " traced.py")
        else:
            self.tracer = self.Tracer(sys.argv[1])
            self.tracer.watchdog(1)

crassula = Crassula()
