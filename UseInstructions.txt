# xmlCompression
Use Instructions:

1. Download PPMD Backend Compressor From the website and install it in Linux: http://ports.ubuntu.com/ubuntu-ports/pool/universe/p/ppmd/
2. Copy the desired XML to b.xml using command "cp S14.xml b.xml"
3. Execute the command "python3 CreateTablesFast.py"
4. Execute the command "python3 SubstituteCheck.py > TATEnc.txt"
5. Execute the command "javac Compress.java". I am using Java-14.
6. Execute the command "java Compress"
7. Execute the command "ppmd e Compress". This creates a file named "Compress.pmd"
8. CR = sizeOf(b.xml)/sizeOf(Compress.pmd)

Note:
1. To make the code more understandable, we have used only 0 instead of A or T in XMLn.
2. Here "TATEnc.txt" is the XMLn.
3. The file named "Compress" is XMLs.
4. We have created a Java program to create XMLs (which is taking more time), just to make the process more understandable.
5. We did not use any XML parser to make the Substitution fast. We converted XMLn from XML with the help of regular expressions. So the given code will only run for the special types of XML.
6. We have another code to run on every type of XML, but it takes longer.
