# Generation of HTML Documentation from XSD

The `xquery` code to generate the `html` Documentation of a XSD is copied from here:
https://github.com/VDVde/OJP/tree/develop/docs

It can be run with the `generate.sh` script - all output is written to a `generated` subfolder excluded from git. 

## Usage Examples

### StopPlace Example 

A small example I use for testing...
``` shell
./generate.sh ./stop_place_custom.xml ../StopPlace.xsd      
```     

### The Big NeTEx

This needs some time...

``` shell
./generate.sh ./netex_custom.xml ../../xsd/xsd/NeTEx_publication.xsd
```

### Code Changes

Changes in the `xquery` code are marked with `(: NeTEx ... :)` comments, mainly in the following files of the xcore directory:
- `xco-html.xqm`
- `xcore.xq`
The shell script generate.sh is adapted from original generate_tables.sh.