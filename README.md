The Game Of Life of Conway
========

Python game of life


Build
-----

    $ XSOCK=/tmp/.X11-unix
    $ XAUTH=/tmp/.docker.xauth
    $ xauth nlist :0 | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -

    $ docker build . -t game_of_life_image
    $ docker run -it -d --name game_of_life -v $XSOCK:$XSOCK -v $XAUTH:$XAUTH -e XAUTHORITY=$XAUTH -v $(pwd):/shared game_of_life_image /bin/bash
    $ docker exec -ti game_of_life bash
    $ gameOfLife