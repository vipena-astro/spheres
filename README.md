# spheres
A simple function for generating colour plots of functions of time, over a sphere using pyplot.
Representing the function as radial deviations in a unit sphere is also possible.

Steps to generate a gif file representing an arbitrary f function of time and position,
plotted over the surface of a sphere:
  1. create a folder named 'tmp' in your work directory
  2. define f and feed it to genframes, defined below. This will take a while, and
     will eventually generate save your frames into the tmp folder.
  3. go to your preferred gif maker (e.g., ezgif.com/maker), and generate your gif
     file using the frames generated with genframe.
  4. you may now delete the tmp folder.

You might want to read the warning at the end of line 68 in spheres.py
