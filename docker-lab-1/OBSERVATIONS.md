1. The size of the alpine:3.19 image is 11.6 MB (disk usage), while the actual content size is 3.51 MB. The size is much smaller compared to other images like MongoDB(1.19GB).

2. The alpine:3.19 has 2 layers. 
The first layer adds the Alpine minimal root filesystem, which contains the basic Linux system files. The second layer defines the default command, which allows the container to run a shell by default.
Each layer represents a step in building the image.

3. From the docker inspect, alpine:3.19 image uses:
-Operating System: Linux
-Architecture:amd64

4. When I installed curl inside the Alpine container, it worked during that session. 
After exiting and starting a new container, curl was not installed anymore because a new container starts from the original image. 
This shows that changes inside a container are not persistent.

5. What surprised me the most in this lab is how small mistakes like wrong ports or missing dependencies can completely break the app also how important it is to manage environments properly instead of relying on things working locally by default.