ABCD3 to Django models
========================


Requirements
-----------------

- generateDS -- Generate Data Structures from XML Schema 
  - doc: https://www.davekuhlman.org/generateDS.html
  - repo: https://bitbucket.org/dkuhlman/generateds
- ABCD: Access to Biological Collection Data (ABCD) 
  - doc: https://abcd.tdwg.org/
  - repo: https://github.com/tdwg/abcd/blob/master/xml/ABCD_3.0.xsd

Process
-------------------
1. download ABCD XSD
2. install generateDS
3. download generateDS source code
4. generate models.py

  - rename ABCD_3.xsd to ABCD3.xsd (underline character will cause error)
  - $ ./gends_run_gen_django.py -f -v ABCD3.xsd
