# HIGH SPEED LOW VOLTAGE CMOS FULL ADDER VLSI DESIGN
  * [Abstract](#abstract)
  * [Reference Circuit Details](#reference-circuit-details)
  * [Reference Circuit Diagram](#reference-circuit-diagram)
  * [Reference Circuit Waveform](#reference-circuit-waveform)
  * [Desirable Truth Table](#desirable-truth-table)
  * [Tools Used](#tools-used)
- [Simulation in Synopsys](#simulation-in-synopsys)
  * [Inverter_Block](#inverter_block)
  * [Carry_Block](#carry_block)
  * [Sum_Block](#sum_block)
  * [Parameters set for Voltage Sources](#parameters-set-for-voltage-sources)
  * [Transient Settings](#transient-settings)
  * [Schematic of Full_Adder using the above Blocks](#schematic-of-full_adder-using-the-above-blocks)
  * [Output Waveform](#output-waveform)
  * [Netlist](#netlist)
  * [Conclusion](#conclusion)
  * [Author](#author)
  * [Acknowledgements](#acknowledgements)
  * [References](#references)

## Abstract

We have implemented a cache simulator for a single level cache hierarchy from scratch in
python.
Inputs:
• Cache size (in Bytes)
• Block size (in Bytes)
• File containing memory traces (each entry containing 8-digit Hex-decimal number).
• Associativity
Outputs:
• A csv file A csv file containing 26 parameters for all kinds of cache configuration out
of which some have been listed below:
– Number of tag bits
– Number of Cache Blocks
– Number of Cache Accesses
– Number of Read Accesses
– Number of Write Accesses
– Number of Cache Misses
– Number of Compulsory Misses
– Number of Capacity Misses
– Number of Conflict Misses
– Number of Read Misses
– Number of Write Misses
– Number of Dirty Blocks Evicted
– Program Execution Time
– Number of NAND Gates
– Total Hit Rate

• A separate window displaying the Total Cache Misses, Total Execution Time for various
cache configurations and breakdown of instruction types

## Reference Circuit Details

Conventional CMOS Full Adder is the most basic full adder implementation techniques. Conventional CMOS Full Adder consists of 28 transistors. A, B and Cin are the inputs and Sum & Cout are the outputs. Static logic provides robustness against noise effects, so automatically provides a reliable operation. Pseudo NMOS pass-transistor logic and reduce the number of transistors required to implement a given logic function but these suffer from static power dissipation. On the other hand, dynamic logic requires less silicon area for implementation of complex function but charge leakage and charge refreshing are required which reduces the frequency of operation. This circuit uses both NMOS and PMOS transistors. In Conventional CMOS Full Adder, there are many leakage paths which lead to more sub threshold leakage.

## Reference Circuit Diagram
<img width="500" alt="Reference_Ckt" src="https://user-images.githubusercontent.com/93763657/155788874-5a8cec99-159a-4ec4-8b76-b69078528177.png">

## Reference Circuit Waveform
<img width="500" alt="Reference_Ckt" src="https://user-images.githubusercontent.com/93763657/155790480-3bc5d6fa-db32-40db-bcda-69d90ba2579c.png">

## Desirable Truth Table
![image](https://user-images.githubusercontent.com/93763657/155791837-fdcea58e-c368-4dd6-8358-c243f478283f.png)

## Tools Used:
• Synopsys Custom Compiler:
 The Synopsys Custom Compiler™ design environment is a modern solution for full-custom analog, custom digital, and mixed-signal IC design. As the heart of the Synopsys Custom Design Platform, Custom Compiler provides design entry, simulation management and analysis, and custom layout editing features. This tool was used to design the circuit on a transistor level.
 
 ![custom_compiler](https://user-images.githubusercontent.com/59500283/155473715-c6a1fd5b-71c7-4655-936a-5fe3befabfd8.png)


• Synopsys Primewave:
 PrimeWave™ Design Environment is a comprehensive and flexible environment for simulation setup and analysis of analog, RF, mixed-signal design, custom-digital and memory designs within the Synopsys Custom Design Platform. This tool helped in various types of simulations of the above designed circuit.

• Synopsys 28nm PDK:
 The Synopsys 28nm Process Design Kit(PDK) was used in creation and simulation of the above designed circuit.
 
# Simulation in Synopsys
## Inverter_Block
<p float="left">
  <img src="https://user-images.githubusercontent.com/93763657/155931622-78ce33af-f9da-4693-9cd1-f439f34cb33b.png" width="385" hspace="50" title="schmatic"/>
  <img src="https://user-images.githubusercontent.com/93763657/155931735-32386b44-eca5-4187-9944-df2fa242c795.png" width="400" /> 

## Carry_Block
<p float="left">
  <img src="https://user-images.githubusercontent.com/93763657/155933486-53aee664-1007-4414-9602-2b9b6992498c.png" height="500" width="720" hspace="30" title="schmatic"/>
  <img src="https://user-images.githubusercontent.com/93763657/155933601-3fa875ee-dd74-4d58-84aa-3dc69abc9ae1.png" width="200" /> 

## Sum_Block
<p float="left">
  <img src="https://user-images.githubusercontent.com/93763657/155934902-1c767439-6fcb-40ad-a2b6-70cb17bf428a.png" height="500" width="720" hspace="30" title="schmatic"/>
  <img src="https://user-images.githubusercontent.com/93763657/155934770-6e3cb89b-2dce-4329-863e-60f464af32d2.png" width="200" /> 
 
## Parameters set for Voltage Sources
<p float="left">
  <img src="https://user-images.githubusercontent.com/59500283/155388964-19e9a68d-e11c-4b39-8a08-1bdd65005658.png" width="270" hspace="20">
  <img src="https://user-images.githubusercontent.com/59500283/155388995-879f0e25-8a64-4e78-bd85-e79c15a113f4.png" width="270" hspace="20"> 
  <img src="https://user-images.githubusercontent.com/59500283/155389151-0461b3bf-d8d1-4464-a471-0056d355ffc4.png" width="270" hspace="20"/>

## Transient Settings
<img width="675" alt="Transient_Analysis" src="https://user-images.githubusercontent.com/93763657/155937385-5a26354e-937f-4582-b458-a32f2a43c006.png">

## Schematic of Full_Adder using the above Blocks
<img width="1400" alt="Final_Design" src="https://user-images.githubusercontent.com/93763657/155937580-fb0c4c97-1de6-4cd3-855f-379a969854ad.png">

## Output Waveform
<img width="1400" alt="Output" src="https://user-images.githubusercontent.com/93763657/155938066-48d2d74a-a268-40b5-9c61-dc9100b7a439.png">

 ## Netlist 
 ```
 *  Generated for: PrimeSim
*  Design library name: full_adder
*  Design cell name: full-adder
*  Design view name: schematic
.lib 'saed32nm.lib' TT

*Custom Compiler Version S-2021.09
*Fri Feb 25 19:28:27 2022

.global gnd!
********************************************************************************
* Library          : full_adder
* Cell             : carry_block
* View             : schematic
* View Search List : hspice hspiceD schematic spice veriloga
* View Stop List   : hspice hspiceD
********************************************************************************
.subckt carry_block a b c carry gnd_1 vdd
xm5 carry carry_bar vdd vdd p105 w=0.1u l=0.03u nf=1 m=1
xm4 net19 a vdd vdd p105 w=0.1u l=0.03u nf=1 m=1
xm3 carry_bar b net19 vdd p105 w=0.1u l=0.03u nf=1 m=1
xm2 carry_bar c net7 vdd p105 w=0.1u l=0.03u nf=1 m=1
xm1 net7 b vdd vdd p105 w=0.1u l=0.03u nf=1 m=1
xm0 net7 a vdd vdd p105 w=0.1u l=0.03u nf=1 m=1
xm11 carry carry_bar gnd_1 gnd_1 n105 w=0.1u l=0.03u nf=1 m=1
xm10 carry_bar b net43 gnd_1 n105 w=0.1u l=0.03u nf=1 m=1
xm9 net43 a gnd_1 gnd_1 n105 w=0.1u l=0.03u nf=1 m=1
xm8 net33 b gnd_1 gnd_1 n105 w=0.1u l=0.03u nf=1 m=1
xm7 net33 a gnd_1 gnd_1 n105 w=0.1u l=0.03u nf=1 m=1
xm6 carry_bar c net33 gnd_1 n105 w=0.1u l=0.03u nf=1 m=1
.ends carry_block

********************************************************************************
* Library          : full_adder
* Cell             : invertor
* View             : schematic
* View Search List : hspice hspiceD schematic spice veriloga
* View Stop List   : hspice hspiceD
********************************************************************************
.subckt invertor gnd_1 input not vdd
xm0 not input gnd_1 gnd_1 n105 w=0.1u l=0.03u nf=1 m=1
xm1 not input vdd vdd p105 w=0.1u l=0.03u nf=1 m=1
.ends invertor

********************************************************************************
* Library          : full_adder
* Cell             : sum_block
* View             : schematic
* View Search List : hspice hspiceD schematic spice veriloga
* View Stop List   : hspice hspiceD
********************************************************************************
.subckt sum_block a b c carry_bar gnd_1 sum_bar vdd
xm6 sum_bar carry_bar net7 vdd p105 w=0.1u l=0.03u nf=1 m=1
xm5 sum_bar c net21 vdd p105 w=0.1u l=0.03u nf=1 m=1
xm4 net21 b net17 vdd p105 w=0.1u l=0.03u nf=1 m=1
xm3 net17 a vdd vdd p105 w=0.1u l=0.03u nf=1 m=1
xm2 net7 c vdd vdd p105 w=0.1u l=0.03u nf=1 m=1
xm1 net7 b vdd vdd p105 w=0.1u l=0.03u nf=1 m=1
xm0 net7 a vdd vdd p105 w=0.1u l=0.03u nf=1 m=1
xm13 net53 a gnd_1 gnd_1 n105 w=0.1u l=0.03u nf=1 m=1
xm12 net49 b net53 gnd_1 n105 w=0.1u l=0.03u nf=1 m=1
xm11 sum_bar c net49 gnd_1 n105 w=0.1u l=0.03u nf=1 m=1
xm10 net37 c gnd_1 gnd_1 n105 w=0.1u l=0.03u nf=1 m=1
xm9 net37 b gnd_1 gnd_1 n105 w=0.1u l=0.03u nf=1 m=1
xm8 net37 a gnd_1 gnd_1 n105 w=0.1u l=0.03u nf=1 m=1
xm7 sum_bar carry_bar net37 gnd_1 n105 w=0.1u l=0.03u nf=1 m=1
.ends sum_block

********************************************************************************
* Library          : full_adder
* Cell             : full-adder
* View             : schematic
* View Search List : hspice hspiceD schematic spice veriloga
* View Stop List   : hspice hspiceD
********************************************************************************
xi0 a b c carry gnd! net38 carry_block
xi3 gnd! net37 sum net38 invertor
xi1 gnd! carry net39 net38 invertor
xi2 a b c net39 gnd! net37 net38 sum_block
vc c gnd! dc=0 pulse ( 0 '1.8V' 0 0.1u 0.1u 20u 40u )
vb b gnd! dc=0 pulse ( 0 '1.8V' 0 0.1u 0.1u 10u 20u )
va a gnd! dc=0 pulse ( 0 1.8 0 0.1u 0.1u 5u 10u )
v4 net38 gnd! dc=1.8
c7 sum gnd! c=1p
c5 carry gnd! c=1p








.tran '1u' '40u' name=tran

.option primesim_remove_probe_prefix = 0
.probe v(*) i(*) level=1
.probe tran v(a) v(b) v(c) v(carry) v(sum)

.temp 25



.option primesim_output=wdf


.option parhier = LOCAL






.end

 ```
 
## Simulation Log
 ```
 
                                   PrimeSim 

                 Version S-2021.09 for linux64 - Aug 26, 2021 

                    Copyright (c) 2003 - 2021 Synopsys, Inc.
   This software and the associated documentation are proprietary to Synopsys,
 Inc. This software may only be used in accordance with the terms and conditions
 of a written license agreement with Synopsys, Inc. All other use, reproduction,
   or distribution of this software is strictly prohibited.  Licensed Products
     communicate with Synopsys servers for the purpose of providing software
    updates, detecting software piracy and verifying that customers are using
    Licensed Products in conformity with the applicable License Key for such
  Licensed Products. Synopsys will use information gathered in connection with
    this process to deliver software updates and pursue software pirates and
                                   infringers.

 Inclusivity & Diversity - Visit SolvNetPlus to read the "Synopsys Statement on
            Inclusivity and Diversity" (Refer to article 000036315 at
                        https://solvnetplus.synopsys.com)
---------------------------------------------------------------------------------

PrimeSim SPICE S-2021.09 RHEL64  (Compiled on Aug 26 2021 at 14:29:28 (US-Pacific)) build id: 7232578

Hostname: snps-analog-group-03, Username: ruchit.chudasama
Tool Path: /Applications/Synopsys/Install/primesim/S-2021.09/primesim/platform/linux64/primesim_spice

PrimeSim SPICE S-2021.09 RHEL64  (Compiled on Aug 26 2021 at 14:29:28 (US-Pacific)) build id: 7232578

Hostname: snps-analog-group-03, Username: ruchit.chudasama, PID: 10306
Tool Path: /Applications/Synopsys/Install/primesim/S-2021.09/primesim/platform/linux64/primesim_spice

**** Environment Variables
(NAME)               (VALUE) 
LD_LIBRARY_PATH      /Applications/Synopsys/Install/primesim/S-2021.09/lib/linux64:/Applications/Synopsys/Install/primesim/S-2021.09/python/linux64/lib:/Applications/Synopsys/Install/customcompiler/S-2021.09/linux64/platform/lib/python-2.6:/Applications/Synopsys/Install/customcompiler/S-2021.09/linux
64/lib/freeType:/Applications/Synopsys/Install/customcompiler/S-2021.09/linux64/platform/lib:/Applications/Synopsys/Install/customcompiler/S-2021.09/linux64/lib:/Applications/Synopsys/Install/customcompiler/S-2021.09/linux64/OA/lib/linux_rhel60_64/opt:/Applications/Synopsys/Install/customcompiler/S-2
021.09/linux64/PyCellStudio/linux64/3rd/Python/lib:/Applications/Synopsys/Install/customcompiler/S-2021.09/linux64/PySide/2.6.2/lib:/Applications/Synopsys/Install/customcompiler/S-2021.09/linux64/PyCellStudio/linux64/lib:/Applications/Synopsys/Install/customcompiler/S-2021.09/linux64/PyCellStudio/lin
ux64/lib/python-38:/Applications/Synopsys/Install/customcompiler/S-2021.09/linux64/PyCellStudio/linux64/lib/python-26 
PRIMESIM             1 
PRIMESIM_HOME        /Applications/Synopsys/Install/primesim/S-2021.09 
****


FlexNet Licensing checkout error: No such feature exists.
Feature:       SYNOPSYS_ANOMALY
License path:  27020@178.128.123.110:
FlexNet Licensing error:-5,147.  System Error: 2 "No such file or directory"
license file(s):  27020@178.128.123.110
[SCL] 02/25/2022 19:28:30 PID:10306 Client:snps-analog-group-03 Server:27020@178.128.123.110 Authorization succeeded primesim 2021.09
Started at Fri Feb 25 19:28:30 2022
Command line: 	/Applications/Synopsys/Install/primesim/S-2021.09/bin/primesim /home/ruchit.chudasama/simulation/TestSuite3/history_1/simulation/Testbench1/PrimeSimSPICE/nominal/netlist/primesim.spi -o primesim -remove_backslash -spice -sae -inc /PDK/SAED_PDK32nm/hspice
Working Directory: /home/ruchit.chudasama/simulation/TestSuite3/history_1/simulation/Testbench1/PrimeSimSPICE/nominal/results

INFO! read global configuration file (/Applications/Synopsys/Install/primesim/S-2021.09/primesim.cfg)

                </PDK/SAED_PDK32nm/hspice/saed32nm.lib>

Resource Usage for Reading Netlist(self/total): 0.2/0.2 sec (cpu), 0.0/0.0 sec (elapsed), 767.4/767.4 MB

primesim_output_dc=wdf is used for .dc analysis.
primesim_output_op=wdf is used for .op analysis
primesim_output_ac=wdf is used for .ac analysis

**** Used Options:
   primesim_remove_probe_prefix = 0
   primesim_output = wdf
   parhier = local
****

**** Macro Options:
****
  Main Setting: runlvl
Resource Usage for Parsing(self/total): 0.0/0.2 sec (cpu), 0.0/0.0 sec (elapsed), 14.5/781.9 MB

Simulation mode: SPICE
Checkout succeeded: primesim/3FF452EEFC581681C6D8
	License file: 27020@178.128.123.110
	License Server: 27020@178.128.123.110
Checkout succeeded: primesim/3FF452EEFC581681C6D8
	License file: 27020@178.128.123.110
	License Server: 27020@178.128.123.110
[SCL] Checking status for feature primesim - 02/25/2022 19:28:30
[SCL] 02/25/2022 19:28:30 PID:10306 Client:snps-analog-group-03 Server:27020@178.128.123.110 Checkout succeeded primesim 2021.09
License: Checked out primesim(2) successfully from :27020@178.128.123.110 

Resource Usage for License(self/total): 0.0/0.2 sec (cpu), 0.0/0.0 sec (elapsed), 2.4/784.3 MB

Elapsed checking license time: 0.0 seconds

Title: *  Generated for: PrimeSim



**** expand probe
   probe pattern 'v(*)' (level=1) matches with 10 nodes on toplevel (primesim.spi:97)
   probe pattern 'i(*)' (level=1) matches with 4 devices on toplevel (primesim.spi:97)
****

WARNING! "risetime" set to 2.500000e-07 accoording to user-specified "tstep" value (25%).

  # MOSFET   : 30
  # Capacitor: 2 (Min/Max=1e-12/1e-12) 
  # V Source : 4 (Max/Min=1.8V/0V)

  TEMP=25
Resource Usage for Circuit Elaboration(self/total): 0.1/0.3 sec (cpu), 0.0/0.0 sec (elapsed), 44.7/829.0 MB

Generating MOS models ...
  Table value up to 1.8V
  Model 4/5
  Level=54 Version=4.5
Resource Usage for MOS Model(self/total): 0.0/0.3 sec (cpu), 0.0/0.0 sec (elapsed), 2.9/831.9 MB


Building Connectivity ...
Resource Usage for Connectivity Building(self/total): 0.0/0.3 sec (cpu), 0.0/0.0 sec (elapsed), -9.0/822.9 MB

Building DB ...
Resource Usage for DB Building(self/total): 0.0/0.3 sec (cpu), 0.0/0.0 sec (elapsed), 0.0/822.9 MB

Initializing ...
Resource Usage for Initialization(self/total): 0.0/0.3 sec (cpu), 0.0/0.0 sec (elapsed), 0.0/822.9 MB

Preparing Outputs ...
  # probed signals  : 14
Resource Usage for Output Preparation(self/total): 0.0/0.3 sec (cpu), 0.0/0.0 sec (elapsed), 0.0/823.0 MB


Building Matrices ...
Resource Usage for Matrix Building(self/total): 0.0/0.3 sec (cpu), 0.0/0.0 sec (elapsed), -12.0/811.0 MB

Starting DC Initialization ...
    ic file 'primesim.ic'
  DC converged at step 1

End of DC Initialization
Resource Usage for DC Initialization(self/total): 0.0/0.3 sec (cpu), 0.0/0.0 sec (elapsed), 3.0/814.0 MB

Starting Transient Analysis ...
  Important settings:
	runlvl = 4
	tolscale = 10
    finished at 40us
    output file 'primesim_wdf/tran.tran'
    # time points: 571
End of Transient Analysis                               
Resource Usage for Transient Analysis(self/total): 0.4/0.7 sec (cpu), 0.0/0.0 sec (elapsed), 13.6/827.5 MB

Simulation ended at Fri Feb 25 19:28:30 2022

Total CPU time: 0.7 seconds (0.00 hours)
Total memory usage: peak= 831.9 MB, avg= 698.3 MB

Total elapsed time: 0.0 seconds (0.00 hours)
PrimeSim Successfully Completed at Fri Feb 25 19:28:30 2022

[SCL] 02/25/2022 19:28:30 PID:10306 Client:snps-analog-group-03 checkin primesim 

 ```
 
 
## Conclusion
Thus, the addition for a single-bit is achieved using 28T CMOS full adder.

## Author

- [Ruchit Chudasama, B.Tech EE, IIT Gandhinagar](https://www.linkedin.com/in/ruchit-chudasama-a04465219/)

## Acknowledgements

- [Kunal Ghosh, Co-founder, VSD Corp. Pvt. Ltd.](https://www.linkedin.com/in/kunal-ghosh-vlsisystemdesign-com-28084836/)
- [Synopsys Inc](https://www.synopsys.com/)
- [IIT Hyderabad](https://iith.ac.in/)
- [Analog IC Design Hackathon](https://www.iith.ac.in/events/2022/02/15/Cloud-Based-Analog-IC-Design-Hackathon/)
- [Sameer Durgoji, NIT Karnataka](https://www.linkedin.com/in/sameer-s-durgoji-340b26180/)
- [Chinmay Panda, IIT Hyderabad](https://www.iith.ac.in/events/2022/02/15/Cloud-Based-Analog-IC-Design-Hackathon/)

## References

[1] Subodh Wairya, Rajendra Kumar Nagaria, Sudarshan Tiwari, "Performance Analysis of High Speed Hybrid CMOS Full Adder Circuits for Low Voltage VLSI Design", VLSI Design, vol. 2012, Article ID 173079, 18 pages, 2012. https://doi.org/10.1155/2012/173079 

[2] A. P. Chandrakasan, S. Sheng and R. W. Brodersen, "Low-power CMOS digital design," in IEEE Journal of Solid-State Circuits, vol. 27, no. 4, pp. 473-484, April 1992, doi: 10.1109/4.126534. 

[3] Akansha Bhargava, Gauri Salunkhe, Ashok Yadav, Jyoti Jeetendra Gurav, 2017, Analysis of Different CMOS Full Adder Circuits Based on Different Parameter for Low Voltage, INTERNATIONAL JOURNAL OF ENGINEERING RESEARCH & TECHNOLOGY (IJERT) ICIATE – 2017 (Volume 5 – Issue 01).

[4] Analysis and Performance Evaluation of 1-bit Full Adder Using Different Topologies http://pnrsolution.org/Datacenter/Vol5/Issue1/26.pdf

[5] Moradi, Farshad & Wisland, D.T. & Mahmoodi, Hamid & Aunet, Snorre & Cao, Tuan & Peiravi, Ali. (2009). Ultra Low Power Full Adder Topologies.. 3158-3161. 10.1109/ISCAS.2009.5118473. 

[6] Wikipedia contributors, 'Adder (electronics)', Wikipedia, The Free Encyclopedia, 26 February 2022, 11:45 UTC, <https://en.wikipedia.org/w/index.php?title=Adder_(electronics)&oldid=1074100022> 
