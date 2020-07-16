# SRAMgenerator
SRAM generator project

This project has all the files needed in order to develope your own SRAM generator, a script for the compiler is included plus sample GDS files. 
For this project I used (Electric)[http://cmosedu.com/videos/electric.html] in order to build the building blocks of the SRAM, using a 180nm technology.
If you are replicating this project with a different technology you need to modify the compiler with the compiler and build your own SRAM building blocks.

# GdsMill

This (library)[http://michaelwieckowski.com/software/] is used in the generation of the SRAM and is really usefull, if you are not using cadence and using python 3 please use the library I provided as I modified it so
it is compatible with python3 and will work fine with any technology as long as you have your building blocks in gds files.

## To use the GdsMill

Useful functions that I used:

- self = gdsMill.VlsiLayout(name="") A tuple that maps layout units to physical units, which you need in order to define the structure in order to import your gds file in and manipulate

- self.addInstance() I used this function in order to  manipulate the layouts

- gdsMill.Gds2writer(self) this class is to define the writer you are going to use in order to write the layout back to a gds file

- .writeToFile("<file>.gds) this function is used in order to write in the new gds file

- Optional:
  - Use the self.rename("name") in order to change the name
  
  To write more than one layout in the same gds file, they have to have different names, make sure to use different names, but only use rename. When defining the variables
  make sure you are using the names given in the GDS2, otherwise it won't work. For me I used "arrayExample" and then renamed it as most of my modules were arrays. For my
  top module I used "filledLayout".
  
  Due to time constrains I couldn't modify the GdsMill in order to support the path function so in order to draw wires I used the box function. The path function has a bug
  but would be extremely usefull to use in order to draw wires.

# Compiler

The compiler is an example of a SRAM generator. I developed the building blocks and ran the DRV and LVS tests on Electric, it is possible and actually recommended to use cadence
as GdsMill library uses cadence and can run the DRC and LVS tests from the library. For more info about how to do that you can look at the manual. I used a 180nm SCMOS technology,
the (Design Rules)[https://blackboard.aucegypt.edu/bbcswebdav/pid-1605830-dt-content-rid-12225956_1/courses/CSCE330401_2020Su/scmos_DRM.pdf] can be found here. The technology spice
is also included in my repo.

