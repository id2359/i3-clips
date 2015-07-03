import os
import clips

def i3(command_string):
    print "calling i3 func: %s" % command_string
    command_line = "i3-msg -t command '%s'" % command_string
    os.popen(command_line)

clips.RegisterPythonFunction(i3, "i3")
clips.Load("i3-rules.clp")
clips.LoadFacts("i3-facts.clp")

clips.Run()

