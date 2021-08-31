Shield is a personal file server that runs on RPi.

**Hardware requirements:** Raspberry Pi 4 (running 64-bit Raspbian), an external hard drive mounted to the RPi.

Installation is a mess. There are some steps to follow before running the Docker container such as installing the dependencies for the server and the client and mounting the hard drive correctly. I am way too lazy (or busy building other things?) to write a documentation but you can contact me if you're interested in running it. I am only open sourcing it so that people can reuse some portions of the code.

I've tested the client on both x86 and ARM architectures (Intel/M1). Running PyTorch for the image classification function was a bit tricky on my M1, but it ended up working. I couldn't figure out a way to run it on the Pi so the classification is done client side (better for privacy if you intend to encrypt the files on the server?)
