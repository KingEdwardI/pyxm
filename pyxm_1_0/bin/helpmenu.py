from docopt import docopt

helpmsg = """
Usage:
    pyxm download (-a | -l | -t) QUERY
    pyxm search (-a | -l | -t) QUERY
    pyxm [-h | --help] 
    pyxm --version
    
Options:
    --help -h   Show this screen.
    -a          specify artist query
    -l          specify album query
    -t          specify track query
    --version   show program version
    
"""

helpmenu = docopt(helpmsg, version='PyXm 1.2')

PYXM = """
::::::::   :::        ::: :::       ::: ::::::       ::::::        @@@@@@@@@@@@@@
:::   :::   :::      :::   :::     :::  ::: :::     ::: :::        @@@@@@@@@@@@@@
::      ::   :::    :::     :::   :::   :::  :::   :::  :::        @@          @@
:::   :::     :::  :::       ::: :::    :::   ::: :::   :::        @@          @@
:::::::        ::::::         :::::     :::    :::::    :::   .....@@     .... @@
:::             ::::         ::: :::    :::             :::  @@@@@@@@    @@@@@@@@
:::             ::::        :::   :::   :::             ::: @@@@@@@@@   @@@@@@@@@
:::             ::::       :::     :::  :::             :::  @@@@@@@     @@@@@@@
:::             ::::      :::       ::: :::             :::   @@@@        @@@@   
    """
