

ES215 Computer Organization and Architecture

Project Report

Cache Simulator

Aryan Gupta

aryan.gupta@iitgn.ac.in

20110026

Ruchit Chudasama

ruchit.chudasama@iitgn.ac.in

20110172

Rahul Lalani

rahul.lalani@iitgn.ac.in

20110154

26 APRIL, 2022





Contents

[1](#br3)[ ](#br3)[Abstract](#br3)

2

[2](#br5)[ ](#br5)[Introduction](#br5)

4

4

4

4

5

[2.1](#br5)[ ](#br5)[The](#br5)[ ](#br5)[goal](#br5)[ ](#br5)[of](#br5)[ ](#br5)[this](#br5)[ ](#br5)[project](#br5)[ ](#br5). . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

[2.2](#br5)[ ](#br5)[The](#br5)[ ](#br5)[rationale](#br5)[ ](#br5)[of](#br5)[ ](#br5)[the](#br5)[ ](#br5)[project](#br5)[ ](#br5). . . . . . . . . . . . . . . . . . . . . . . . . . .

[2.3](#br5)[ ](#br5)[The](#br5)[ ](#br5)[importance](#br5)[ ](#br5)[of](#br5)[ ](#br5)[the](#br5)[ ](#br5)[project](#br5)[ ](#br5). . . . . . . . . . . . . . . . . . . . . . . . . .

[2.4](#br6)[ ](#br6)[Our](#br6)[ ](#br6)[contributions](#br6)[ ](#br6)[to](#br6)[ ](#br6)[the](#br6)[ ](#br6)[project](#br6)[ ](#br6). . . . . . . . . . . . . . . . . . . . . . . . .

[3](#br7)[ ](#br7)[Literature](#br7)[ ](#br7)[Review](#br7)

[4](#br8)[ ](#br8)[Project](#br8)[ ](#br8)[Idea](#br8)

6

7

8

[5](#br9)[ ](#br9)[Assumptions](#br9)

[6](#br10)[ ](#br10)[Project](#br10)[ ](#br10)[Implementation](#br10)

9

9

9

9

[6.1](#br10)[ ](#br10)[Programming](#br10)[ ](#br10)[Language](#br10)[ ](#br10)[and](#br10)[ ](#br10)[Libraries](#br10)[ ](#br10)[Used](#br10)[ ](#br10). . . . . . . . . . . . . . . . . .

[6.2](#br10)[ ](#br10)[Meat](#br10)[ ](#br10)[Portions](#br10)[ ](#br10)[of](#br10)[ ](#br10)[the](#br10)[ ](#br10)[Code](#br10)[ ](#br10). . . . . . . . . . . . . . . . . . . . . . . . . . . .

[6.2.1](#br10)[ ](#br10)[Implementing](#br10)[ ](#br10)[Direct](#br10)[ ](#br10)[Mapped](#br10)[ ](#br10)[Cache](#br10)[ ](#br10)[with](#br10)[ ](#br10)[Write](#br10)[ ](#br10)[Back](#br10)[ ](#br10). . . . . . . .

[6.2.2](#br11)[ ](#br11)[Implementing](#br11)[ ](#br11)[a](#br11)[ ](#br11)[Fully](#br11)[ ](#br11)[Associative](#br11)[ ](#br11)[Cache](#br11)[ ](#br11)[with](#br11)[ ](#br11)[Write](#br11)[ ](#br11)[Through](#br11)[ ](#br11)[and](#br11)[ ](#br11)[FIFO](#br11)

[Replacement](#br11)[ ](#br11)[Policy](#br11)[ ](#br11). . . . . . . . . . . . . . . . . . . . . . . . . . . 10

[6.2.3](#br13)[ ](#br13)[Implementing](#br13)[ ](#br13)[a](#br13)[ ](#br13)[Set](#br13)[ ](#br13)[Associative](#br13)[ ](#br13)[Cache](#br13)[ ](#br13)[with](#br13)[ ](#br13)[Write](#br13)[ ](#br13)[Back](#br13)[ ](#br13)[and](#br13)[ ](#br13)[LRU](#br13)[ ](#br13)[Re-](#br13)

[placement](#br13)[ ](#br13)[Policy](#br13)[ ](#br13). . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

[6.3](#br14)[ ](#br14)[Challenges](#br14)[ ](#br14). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

[7](#br16)[ ](#br16)[Testing](#br16)[ ](#br16)[and](#br16)[ ](#br16)[Experiments](#br16)

[8](#br17)[ ](#br17)[Data](#br17)[ ](#br17)[Analysis](#br17)

15

16

20

21

22

[9](#br21)[ ](#br21)[Future](#br21)[ ](#br21)[Scope](#br21)[ ](#br21)[of](#br21)[ ](#br21)[this](#br21)[ ](#br21)[Project](#br21)

[10](#br22)[ ](#br22)[Work](#br22)[ ](#br22)[Distribution](#br22)

[11](#br23)[ ](#br23)[Bibliography](#br23)

1





Abstract

We have implemented a cache simulator for a single level cache hierarchy from scratch in

python.

Inputs:

• Cache size (in Bytes)

• Block size (in Bytes)

• File containing memory traces (each entry containing 8-digit Hex-decimal number).

• Associativity

Outputs:

• A csv ﬁle A csv ﬁle containing 26 parameters for all kinds of cache conﬁguration out

of which some have been listed below:

– Number of tag bits

– Number of Cache Blocks

– Number of Cache Accesses

– Number of Read Accesses

– Number of Write Accesses

– Number of Cache Misses

– Number of Compulsory Misses

– Number of Capacity Misses

– Number of Conﬂict Misses

– Number of Read Misses

– Number of Write Misses

– Number of Dirty Blocks Evicted

– Program Execution Time

2





– Number of NAND Gates

– Total Hit Rate

• A separate window displaying the Total Cache Misses, Total Execution Time for various

cache conﬁgurations and breakdown of instruction types

3





Introduction

2.1 The goal of this project

The objective of this course project is to simulate the behaviour of a cache hardware. This

project aims to study a single-level cache hierarchy system where the user can conﬁgure the

parameters of the cache such as Cache Size, Block Size and Associativity as well as input the

program trace ﬁle and outputs the best cache mapping and cache policy for a given cache

conﬁguration and trace ﬁle. The output will be decided by analysing the program execution

time corresponding to diﬀerent cache mapping and policies. We also hope to visually plot

bar charts and pie graphs and a table containing all the parameters such as cache hits,

cache misses, read hits, write hits, read misses, write misses corresponding to diﬀerent cache

mappings and policies.

2.2 The rationale of the project

We were always mesmerised to see a web page taking lesser time to load if it had been

recently opened. We observed similar behaviour for proﬁle pictures on Whatsapp. This

made us keen to explore how an individual cache is managed, what data to bring, where it

gets placed and what happens if it is already present in the cache when we do future look

ups.

2.3 The importance of the project

Cache memory is important because it improves the eﬃciency of data retrieval. It stores

program instructions and data that are used repeatedly in the operation of programs or

information that the CPU is likely to need next. Via this project, we can analyse which

cache mapping and policy is suitable for a particular cache organization which overall will

increase the eﬃciency of the computer processor. We can also understand how the memory

accesses are made while running programs on the processor which ultimately will help us to

optimize the execution time of running a computer program.

4





2.4 Our contributions to the project

There are multiple cache mappings and cache policies which can give a variety of combina-

tions to choose from. We will be designing our cache simulator which will output various

performance metrics such as additional hardware used, program execution time, hit rate

etc. for all kinds of cache conﬁguration based on which the user can decide which kind of

cache is suitable. for a particular program corresponding to a ﬁxed cache conﬁguration and

a computer program.

5





Literature Review

• We started working on the project before the topic was covered in the class. So, we

took help from online lectures of CS3810 (University of Utah) to get understanding of

caches. We also refereed to the lecture slides to get insights into the topic.

• We faced some challenges while we were working on the code. We asked to Prof. Sameer

Kulkarni whenever we had trouble in understanding some concepts. For example, we

had doubts regarding the writing policies and also regarding the miss penalties for

diﬀerent policies. These doubts were regularly addressed and were cleared by the

faculty.

• We minutely studied "Paracache", an existing web-based simulator. Studying this

simulator made us understand how a cache simulator works and indeed laid a solid

foundation on which we could build our own cache simulator from scratch.

6





Pro ject Idea

The growing diﬀerence between processor and memory speeds makes the cache memory and

its eﬃcient utilization a crucial factor in determining program performance. With increasing

demand in computation and large set of data involved, understanding the memory mapping

techniques would be the baseline for student to further improve eﬃciency in resources uti-

lization.

Since there are multiple cache mappings and various writing and replacement policies, we

aim to design a cache simulator which outputs various performance metrics such as ad-

ditional hardware used, program execution time, hit rate etc. for all kinds of cache con-

ﬁguration based on which we can comprehend which kind of cache is optimal for a par-

ticular program corresponding to a ﬁxed cache conﬁguration and a computer program.

Figure 4.1: Cache Mapping and Cache Policies

7





Assumptions

After doing an intensive literature review, we felt that it would not be feasible to implement

each and every detail that we had studied. So, we make the following assumptions:

• We are not concerned with the type of data that we are writing or reading from

memory, we are only focusing on the memory LOCATION on which the data is being

read/wrote.

• As we are not dealing with the content of memory, so we don’t know memory bits.

And hence we don’t know overhead.

• The trace ﬁle that we have considered has a speciﬁc format. The trace ﬁle will specify

all the data memory accesses that occur in the sample program. Each line in the trace

ﬁle will specify a new memory reference.

Each line in the trace cache will therefore have the following three ﬁelds:

Access Type: A single character indicating a load (’l’) or a store (’s’) instruction.

Address: A 32-bit integer (in unsigned hexidecimal format) specifying the mem-

ory address that is being accessed. For example, "0xﬀ32e100" speciﬁes that memory

address 4281524480 is accessed.

Instructions since last memory access: Indicates the number of instructions of any

type that executed between since the last memory access (i.e. the one on the previous

line in the trace). For example, if the 5th and 10th instructions in the program’s

execution are loads, and there are no memory operations between them, then the trace

line for with the second load has "4" for this ﬁeld.

• We have assumed write allocate policy for cache write miss.

• If there is cache hit, then it happens in 1 cycle.

• If there is cache miss, then the miss-penalty is 5 cycles.

• All the ALU instructions are processed by a pipelined processor and hence they execute

in 1 cycle.

• The clock rate is 1 GHz.

8





Pro ject Implementation

6.1 Programming Language and Libraries Used

The entire code was written in python on Google Collab for seamless collaboration.

The entire code was brainstormed and implemented from scratch.

Matplotlib was used to visually plot program output parameters for clarity.

Tkinter was used to design a basic graphical user interface for taking inputs from the program.

6.2 Meat Portions of the Code

6.2.1 Implementing Direct Mapped Cache with Write Back

for i in range(len(master\_file)):

total\_alu\_instructions+= int(master\_file[i][13])

if master\_file[i][0]==’l’:

total\_load\_instructions+=1

hex= (master\_file[i][4:12])

binary\_string=HexToBin(hex)

offset = binary\_string[-int(offset\_bits):]

tag = binary\_string[:int(tag\_bits)]

index = binary\_string[int(tag\_bits):int(tag\_bits)+int(index\_bits)]

if tag\_array[int(index,2)] == ’ ’ :

tag\_array[int(index,2)] = tag

compulsary\_read\_miss+=1

cycles+=miss\_penalty

elif (tag\_array[int(index,2)] != tag):

tag\_array[int(index,2)] = tag

conflict\_read\_miss+=1

cycles+=miss\_penalty

if dirty\_bit[int(index,2)]==1:

Dirty\_blocks+=1

else:

read\_hit+=1

cycles+=1

else:

total\_store\_instructions+=1

9





hex= (master\_file[i][4:12])

binary\_string=HexToBin(hex)

offset = binary\_string[-int(offset\_bits):]

tag = binary\_string[:int(tag\_bits)]

index = binary\_string[int(tag\_bits):int(tag\_bits)+int(index\_bits)]

if tag\_array[int(index,2)] == ’ ’ :

tag\_array[int(index,2)] = tag

dirty\_bit[int(index,2)]=1

compulsary\_write\_miss+=1

cycles+=miss\_penalty

elif (tag\_array[int(index,2)] != tag):

tag\_array[int(index,2)] = tag

conflict\_write\_miss+=1

cycles+=miss\_penalty

if dirty\_bit[int(index,2)]==1:

Dirty\_blocks+=1

else:

write\_hit+=1

cycles+=1

This code has been implemented for a Direct Mapped Cache with Write Back Policy

• All the initial output parameters have been set to zero. They have been updated in

the for loop as and when required.

• The tag comparisons were made with one cache block only as this is a direct mapped

cache.

• For implementing the concept of write back policy, we updated only the cache and

updated the main memory at the stage when the block was going to e evicted, thus

reducing latency.

6.2.2 Implementing a Fully Associative Cache with Write Through

and FIFO Replacement Policy

r=0

for k in range(len(master\_file)):

alu\_instructions+= int(master\_file[k][13])

if master\_file[k][0]==’l’:

hex=(master\_file[k][4:12])

binary\_string=HexToBin(hex)

offset = binary\_string[-int(offset\_bits):]

tag = binary\_string[:int(tag\_bits)]

if tag in tag\_array:

read\_hit+=1

cycles+=1

10





elif ’ ’ in tag\_array:

for i in range(len(tag\_array)):

if tag\_array[i]== ’ ’:

tag\_array[i]=tag

compulsary\_read\_miss+=1

cycles+=miss\_penalty

break

else:

tag\_array[r%len(tag\_array)]=tag

r+=1

capacity\_read\_misses+=1

cycles+=miss\_penalty

else:

hex=(master\_file[k][4:12])

binary\_string=HexToBin(hex)

offset = binary\_string[-int(offset\_bits):]

tag = binary\_string[:int(tag\_bits)]

if tag in tag\_array:

write\_hit+=1

cycles+=miss\_penalty

elif ’ ’ in tag\_array:

for i in range(len(tag\_array)):

if tag\_array[i]== ’ ’:

tag\_array[i]=tag

compulsary\_write\_miss+=1

cycles+=2\*miss\_penalty

break

else:

tag\_array[r%len(tag\_array)]=tag

r+=1

capacity\_write\_misses+=1

cycles+=2\*miss\_penalty

This code has been implemented for a Fully Associative Cache with Write Through and

FIFO Replacement Policy

• All the initial output parameters have been set to zero. They have been updated in

the for loop as and when required.

• For implementing the concept of FIFO, we used a dummy variable r to keep track of

which cache block is ﬁrst ﬁlled with memory. It is updated by one if a cache miss

occurs

• The tag comparisons were made corresponding to each cache block as this is a fully

associative cache.

• For implementing the concept of write through policy, we updated the main memory

11





as soon as we write to a cache and this introduces extra latency, thus reducing the

total program execution time.

6.2.3 Implementing a Set Associative Cache with Write Back and

LRU Replacement Policy

for k in range(len(master\_file)):

alu\_instructions+= int(master\_file[k][13])

if master\_file[k][0]==’l’:

hex=(master\_file[k][4:12])

binary\_string=HexToBin(hex)

offset = binary\_string[-int(offset\_bits):]

tag = binary\_string[:int(tag\_bits)]

index = binary\_string[int(tag\_bits):int(tag\_bits)+int(index\_bits)]

array\_new=tag\_array[int(index,2)]

if tag in array\_new:

m=array\_new.index(tag)

index\_array\_all[int(index,2)].remove(m)

index\_array\_all[int(index,2)].insert(0,m)

read\_hit+=1

cycles+=1

elif ’ ’ in array\_new:

for i in range(len(array\_new)):

if array\_new[i]== ’ ’:

array\_new[i]=tag

index\_array\_all[int(index,2)].remove(index\_array\_all[int(index,2)][-1])

index\_array\_all[int(index,2)].insert(0,i)

cycles+=miss\_penalty

compulsary\_read\_miss+=1

break

else:

array\_new[index\_array\_all[int(index,2)][-1]]=tag

m=index\_array\_all[int(index,2)][-1]

index\_array\_all[int(index,2)].remove(index\_array\_all[int(index,2)][-1])

index\_array\_all[int(index,2)].insert(0,m)

capacity\_read\_misses+=1

if dirty\_bit[int(index,2)][i]==1:

Dirty\_blocks+=1

cycles+=miss\_penalty

else:

hex=(master\_file[k][4:12])

binary\_string=HexToBin(hex)

offset = binary\_string[-int(offset\_bits):]

tag = binary\_string[:int(tag\_bits)]

index = binary\_string[int(tag\_bits):int(tag\_bits)+int(index\_bits)]

array\_new=tag\_array[int(index,2)]

12





if tag in array\_new:

m=array\_new.index(tag)

dirty\_bit[int(index,2)][array\_new.index(tag)]=1

index\_array\_all[int(index,2)].remove(m)

index\_array\_all[int(index,2)].insert(0,m)

write\_hit+=1

cycles+=1

elif ’ ’ in array\_new:

for i in range(len(array\_new)):

if array\_new[i]== ’ ’:

array\_new[i]=tag

index\_array\_all[int(index,2)].remove(index\_array\_all[int(index,2)][-1])

index\_array\_all[int(index,2)].insert(0,i)

cycles+=miss\_penalty

compulsary\_write\_miss+=1

dirty\_bit[int(index,2)][i]=1

break

else:

array\_new[index\_array\_all[int(index,2)][-1]]=tag

m=index\_array\_all[int(index,2)][-1]

index\_array\_all[int(index,2)].remove(index\_array\_all[int(index,2)][-1])

index\_array\_all[int(index,2)].insert(0,m)

capacity\_write\_misses+=1

if dirty\_bit[int(index,2)][i]==1:

Dirty\_blocks+=1

cycles+=miss\_penalty

This code has been implemented for a Set Associative Cache with Write Back and Cache

Replacement Policy

• All the initial output parameters have been set to zero. They have been updated in

the for loop as and when required.

• For implementing the concept of LRU, we used a queue to keep track of the accesses

in which the cache blocks were accessed.

• The tag comparisons were made corresponding to each set as this is a set associative

cache.

• For implementing the concept of write back policy, we assigned each cache blocks an

initial dirty bit of zero and later updated it to 1 when the data was updated in the

cache but not in the main memory.

6.3 Challenges

• One of the major challenges we faced while implementing the project was the lack

of knowledge regarding the various aspects of Cache. Since, the topic was yet to be

13





covered in the class, we familiarized ourselves with the various aspects of a cache on

our own.

• Another challenge we faced was that since we were a group of only three members,

everyone had to did a little more work as compared to other group’s members in the

project.

• We also faced a challenge while implementing the LRU cache mapping. After a lot of

brainstorming and web search, we decided to use the concept of queue to implement

LRU.

• We tried to verify the results of our cache simulator using the online cache simulator

"Paracache", but it was crashing for mere 50,000 memory references. Just to compare

the coverage of the simulators, our code of cache simulator is running for at least 3

million memory references.

14





Testing and Experiments

• Open the ’cache.py’ ﬁle. On running this ﬁle a pop up window will appear which will

ask you to select a trace ﬁle.

• After selecting the trace ﬁle dialogue boxes will appear where we will have to enter

cache size,block size and associativity.

• Now wait for half a minute for simulator to run .

• After the program has been run , the plots showing execution time , cache misses and

the distribution of instructions type will appear in a separate window .

• Also a csv ﬁle named "cache\_parameters.csv" will be automatically generated in the

D drive.

• On the console, a conclusive statement will appear telling the best execution time and

to what cache organization it corresponds to.

• The ﬁle will have 25 parameters for 10 diﬀerent types of cache organization .

The written code was run several times and Matplotlib, a python library was used to

visually plot the data. The data trends were observed and were validated and they were in

accordance with what we have been taught in the course.

15





Data Analysis

An extensive and comprehensive analysis was performed on data which was visually stored

in the form of bar graphs and pie charts and additionally all the cache parameters were

stored in a csv ﬁle. The following observations were made:

• Higher associativity improves the hit-rate but negatively aﬀects the complexity of the

architecture in terms of number of NAND gates used.

• Higher associativity increases the miss-penalty, thus adversely aﬀecting average mem-

ory access time of the system.

• From this analysis we can predict that in computers that we use, higher associativity

is implemented in L1 Cache, which will have relatively small capacity.

• Direct map is implemented in L2 cache.

• An approximation overview of cost versus performance need to be simulated in order

to give deeper understanding on the trade-oﬀs of cache types.

From this analysis we can predict that in computers that we use nowadays:

• Higher associativity is implemented in L1 Cache, which will have relatively small ca-

pacity.

• Direct map is implemented in L2 cache.

• An approximation overview of cost versus performance need to be simulated in order

to give deeper understanding on the trade-oﬀs of cache types.

16





Figure 8.1: Observations for small cache size

Figure 8.2: Values of cache parameters for small cache size

17





Figure 8.3: Observations for moderate cache size

Figure 8.4: Values of cache parameters for moderate cache size

18





Figure 8.5: Observations for large cache size

Figure 8.6: Values of cache parameters for large cache size

19





Future Scope of this Pro ject

• We had thought to implement LFU (Least Frequently Used) replacement policy for all

cache mappings. Due to time constraint, we couldn’t implement it. If given a chance,

we will surely implement it so that this policy can be compared with other policies.

• We had also thought to compute the hardware latency that comes at an additional

cost while increasing the associativity of the cache. We will surely devise a way to do

so if given a chance.

20





Work Distribution

• The entire cache study as well as brainstorming for the project was done by Aryan and

Ruchit.

• The entire code was written by both Aryan and Ruchit by collaboritng on Google

Collab.

• All the timely reporting of the project to Professor Sameer Kulkarni was done by Aryan

and Ruchit.

• The numerical analysis as well the writing the report was done by Aryan and Ruchit.

• Rahul designed the graphical user interface for the program as well as made the pre-

sentation slides.

21





Bibliography

• A. Paramita and K. G. Smitha, "PARACACHE: Educational Simulator for Cache and

Virtual Memory," 2017 International Symposium on Educational Technology (ISET),

2017, pp. 234-238, doi: 10.1109/ISET.2017.60.

• https://www.cs.utah.edu/ rajeev/cs3810/

• https://cseweb.ucsd.edu/classes/fa07/cse240a/project1.html (Trace ﬁles)

22


