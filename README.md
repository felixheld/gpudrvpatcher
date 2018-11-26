# gpudrvpatcher

This is a tool to patch certain binary GPU drivers so that they run on 32 Bit
x86 CPUs without SSE support.
It requires python3 and takes the file to patch as parameter. If you have a
.dl_ or .sy_ file, you need to use the windows tool _expand_ to expand the file
into a .dll or .sys file as the precessing of compressed files isn't supported.


Currently this tool supports these driver versions and files:

* 10-2_legacy_vista32-64_dd_ccc: atikmdag.sys
