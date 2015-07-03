(defrule start-prog 
    (workspace ?w ?prog)
=>
    (bind ?cmd (str-cat "workspace " ?w ";exec " ?prog))
    (python-call i3 ?cmd))



