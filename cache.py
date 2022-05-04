import math
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib as mpl
from matplotlib.ticker import FormatStrFormatter, StrMethodFormatter
import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog
import pandas as pd

def Log2(x):
    return (math.log10(x) /
            math.log10(2))

# if cache read miss, then cycles taken to bring that memory location in cache 
miss_penalty=5 # 5 cycle penalty
clock_rate=1e-9 # 1 GHz

total_cache_accesses={}
total_cache_misses={}
program_execution_time={}

total_alu_instructions=0
total_load_instructions=0
total_store_instructions=0

new_dict={'Direct, WT':{}, 'Direct, WB':{}, 'FA, WT, LRU':{}, 'FA, WT, FIFO':{}, 'FA, WB, LRU':{}, 'FA, WB, FIFO':{}, 'SA, WT, LRU':{}, 'SA, WT, FIFO':{}, 'SA, WB, LRU':{}, 'SA, WB, FIFO':{}}

def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

def HexToBin(hexdec):   
    string=''  
    for i in hexdec:       
        if i == '0':
            string=string+'0000'
        elif i == '1':
            string=string+'0001'
        elif i == '2':
            string=string+'0010'
        elif i == '3':
            string=string+'0011'
        elif i == '4':
            string=string+'0100'
        elif i == '5':
            string=string+'0101'
        elif i == '6':
            string=string+'0110'
        elif i == '7':
            string=string+'0111'
        elif i == '8':
            string=string+'1000'
        elif i == '9':
            string=string+'1001'
        elif i == 'A' or i == 'a':
            string=string+'1010'
        elif i == 'B' or i == 'b':
            string=string+'1011'
        elif i == 'C' or i == 'c':
            string=string+'1100'
        elif i == 'D' or i == 'd':
            string=string+'1101'
        elif i == 'E' or i == 'e':
            string=string+'1110'
        elif i == 'F' or i == 'f':
            string=string+'1111'
        else:
            print("\nInvalid hexadecimal digit " +
                    str(hexdec[i]), end = '')
            return
    return string        


ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog

filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select The Trace File",
                                          filetypes = (("Trace files",
                                                        ".Trace"),
                                                       ("all files",
                                                        ".")))


USER_INP_1 = simpledialog.askstring(title="Cache Configuration",
                                  prompt="Enter Cache Size in Powers of 2:")
while (isPowerOfTwo(int(USER_INP_1))==0 or int(USER_INP_1)==1 ):
    USER_INP_1 = simpledialog.askstring(title="Cache Configuration",
                                  prompt="Invalid Cache Size! Enter Again:")

USER_INP_2 = simpledialog.askstring(title="Cache Configuration",
                                  prompt="Enter Block Size in Powers of 2:")
while (isPowerOfTwo(int(USER_INP_2))==0 ):
    USER_INP_2 = simpledialog.askstring(title="Cache Configuration",
                                  prompt="Invalid Block Size! Enter Again:")


USER_INP_3 = simpledialog.askstring(title="Cache Configuration",
                                  prompt="Enter Associativity for set associative Cache:")
while (isPowerOfTwo(int(USER_INP_3))==0  or float(USER_INP_3) >= float(int(USER_INP_1)/int(USER_INP_2))):
    USER_INP_3 = simpledialog.askstring(title="Cache Configuration",
                                  prompt="Invalid Associativity! Enter Again:")

cache_size=int(USER_INP_1) 
block_size=int(USER_INP_2) 
common_associativity=int(USER_INP_3)             

f = open(filename,'r')
master_file=f.readlines()


# Direct Mapped Cache, Write Through
if (True):
    offset_bits=int(Log2(block_size))
    blocks=int(cache_size/block_size)
    index_bits=int(Log2(blocks))
    tag_bits=int(32-index_bits-offset_bits)
    tag_array=[]
    tag_array = [' ' for x in range(int(blocks))]
    read_hit=0
    write_hit=0
    cycles=0
    compulsary_read_miss=0
    compulsary_write_miss=0
    conflict_read_miss=0
    conflict_write_miss=0
    capacity_read_misses=0
    capacity_write_misses=0
    Dirty_blocks=0
    alu_instructions=0

    for i in range(len(master_file)):
        alu_instructions+= int(master_file[i][13])
        if master_file[i][0]=='l':
            hex= (master_file[i][4:12])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            index = binary_string[int(tag_bits):int(tag_bits)+int(index_bits)]
            if tag_array[int(index,2)] == ' ' :
                tag_array[int(index,2)] = tag
                compulsary_read_miss+=1
                cycles+=miss_penalty
            elif (tag_array[int(index,2)] != tag):
                tag_array[int(index,2)] = tag
                conflict_read_miss+=1
                cycles+=miss_penalty
            else:
                read_hit+=1
                cycles+=1
        else:
            hex= (master_file[i][4:12])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            index = binary_string[int(tag_bits):int(tag_bits)+int(index_bits)]

            if tag_array[int(index,2)] == ' ' :
                tag_array[int(index,2)] = tag
                compulsary_write_miss+=1
                cycles+=2*miss_penalty
            elif (tag_array[int(index,2)] != tag):
                tag_array[int(index,2)] = tag
                conflict_write_miss+=1
                cycles+=2*miss_penalty
            else:
                write_hit+=1
                cycles+=miss_penalty

    read_misses=capacity_read_misses+compulsary_read_miss+conflict_read_miss
    write_misses=capacity_write_misses+compulsary_write_miss+conflict_write_miss
    total_cache_accesses['Direct, WT']=read_hit+write_hit
    total_cache_misses['Direct, WT']=read_misses+write_misses
    program_execution_time['Direct, WT']=1000*((cycles + alu_instructions)*clock_rate)
    cache_accesses=read_hit+write_hit
    cache_misses=read_misses+write_misses
    total_hit_rate=(cache_accesses)/(cache_accesses+cache_misses)
    load_hit_rate=read_hit/(read_hit+read_misses)
    store_hit_rate=write_hit/(write_hit+write_misses)
    nand_gates= 2+ 4*tag_bits

    new_dict.update({'Direct, WT':{'tag bits':tag_bits, 'index bits':index_bits, 'offset bits':offset_bits, 'blocks':blocks, 'cache accesses':cache_accesses, 'cache misses': cache_misses, 'read accesses': read_hit, 'write accesses':write_hit, 'read misses':read_misses, 'write misses': write_misses, 'compulsary read miss': compulsary_read_miss, 'compulsary write miss': compulsary_write_miss, 'Total compulsary misses':compulsary_write_miss+compulsary_read_miss, 'conflict read miss':conflict_read_miss, 'conflict write miss': conflict_write_miss, 'Total conflict misses': conflict_read_miss+conflict_write_miss, 'capacity read misses':capacity_read_misses, 'capacity write misses':capacity_write_misses, 'Total capacity misses': capacity_read_misses+capacity_write_misses, 'Dirty blocks evicted':Dirty_blocks, 'Program Execution Time':1000*((cycles + alu_instructions)*clock_rate), 'total hit rate':total_hit_rate,'load_hit_rate':load_hit_rate, 'store hit rate':store_hit_rate, 'Number of NAND gates':nand_gates }})

# Direct Mapped Cache, Write Back
if (True):
    offset_bits=int(Log2(block_size))
    blocks=int(cache_size/block_size)
    index_bits=int(Log2(blocks))
    tag_bits=int(32-index_bits-offset_bits)
    tag_array=[]
    tag_array = [' ' for x in range(int(blocks))]
    dirty_bit=[0 for y in range(int(blocks))]
    read_hit=0
    write_hit=0
    cycles=0
    compulsary_read_miss=0
    compulsary_write_miss=0
    conflict_read_miss=0
    conflict_write_miss=0
    capacity_read_misses=0
    capacity_write_misses=0
    Dirty_blocks=0
    
    for i in range(len(master_file)):
        total_alu_instructions+= int(master_file[i][13])
        if master_file[i][0]=='l':
            total_load_instructions+=1
            hex= (master_file[i][4:12])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            index = binary_string[int(tag_bits):int(tag_bits)+int(index_bits)]
            if tag_array[int(index,2)] == ' ' :
                tag_array[int(index,2)] = tag
                compulsary_read_miss+=1
                cycles+=miss_penalty
            elif (tag_array[int(index,2)] != tag):
                tag_array[int(index,2)] = tag
                conflict_read_miss+=1
                cycles+=miss_penalty
                if dirty_bit[int(index,2)]==1:
                    Dirty_blocks+=1
            else:
                read_hit+=1
                cycles+=1
        else:
            total_store_instructions+=1
            hex= (master_file[i][4:12])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            index = binary_string[int(tag_bits):int(tag_bits)+int(index_bits)]
            if tag_array[int(index,2)] == ' ' :
                tag_array[int(index,2)] = tag
                dirty_bit[int(index,2)]=1
                compulsary_write_miss+=1
                cycles+=miss_penalty
            elif (tag_array[int(index,2)] != tag):
                tag_array[int(index,2)] = tag
                conflict_write_miss+=1
                cycles+=miss_penalty
                if dirty_bit[int(index,2)]==1:
                    Dirty_blocks+=1
            else:
                write_hit+=1
                cycles+=1


    read_misses=capacity_read_misses+compulsary_read_miss+conflict_read_miss
    write_misses=capacity_write_misses+compulsary_write_miss+conflict_write_miss
    total_cache_accesses['Direct, WB']=read_hit+write_hit
    total_cache_misses['Direct, WB']=read_misses+write_misses
    program_execution_time['Direct, WB']=1000*((cycles + alu_instructions)*clock_rate)
    cache_accesses=read_hit+write_hit
    cache_misses=read_misses+write_misses
    total_hit_rate=(cache_accesses)/(cache_accesses+cache_misses)
    load_hit_rate=read_hit/(read_hit+read_misses)
    store_hit_rate=write_hit/(write_hit+write_misses)
    nand_gates= 2+ 4*tag_bits

    new_dict.update({'Direct, WB':{'tag bits':tag_bits, 'index bits':index_bits, 'offset bits':offset_bits, 'blocks':blocks, 'cache accesses':cache_accesses, 'cache misses': cache_misses, 'read accesses': read_hit, 'write accesses':write_hit, 'read misses':read_misses, 'write misses': write_misses, 'compulsary read miss': compulsary_read_miss, 'compulsary write miss': compulsary_write_miss, 'Total compulsary misses':compulsary_write_miss+compulsary_read_miss, 'conflict read miss':conflict_read_miss, 'conflict write miss': conflict_write_miss, 'Total conflict misses': conflict_read_miss+conflict_write_miss, 'capacity read misses':capacity_read_misses, 'capacity write misses':capacity_write_misses, 'Total capacity misses': capacity_read_misses+capacity_write_misses, 'Dirty blocks evicted':Dirty_blocks, 'Program Execution Time':1000*((cycles + alu_instructions)*clock_rate), 'total hit rate':total_hit_rate,'load_hit_rate':load_hit_rate, 'store hit rate':store_hit_rate, 'Number of NAND gates':nand_gates }})

#Fully Associative Cache, Write Through, LRU replacement
if (True):
    offset_bits=int(Log2(block_size))
    blocks=int(cache_size/block_size)
    tag_bits=int(32-offset_bits)

    tag_array=[]
    tag_array = [' ' for x in range(int(blocks))]
    tag_array_index=[' ' for x in range(int(blocks))]

    read_hit=0
    write_hit=0
    cycles=0
    compulsary_read_miss=0
    compulsary_write_miss=0
    conflict_read_miss=0
    conflict_write_miss=0
    capacity_read_misses=0
    capacity_write_misses=0
    Dirty_blocks=0
    alu_instructions=0
    r=0

    for k in range(len(master_file)):
        alu_instructions+= int(master_file[k][13])
        if master_file[k][0]=='l':
            hex=(master_file[k][4:12])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            if tag in tag_array:
                m=tag_array.index(tag)
                tag_array_index.remove(m)
                tag_array_index.insert(0,m)
                cycles+=1
                read_hit+=1

            elif ' ' in tag_array:
                for i in range(len(tag_array)):
                    if tag_array[i]== ' ':
                        tag_array[i]=tag
                        tag_array_index.remove(tag_array_index[-1])
                        tag_array_index.insert(0,i)
                        compulsary_read_miss+=1
                        cycles+=miss_penalty

                        break
            else:
                tag_array[tag_array_index[-1]]=tag
                m=tag_array_index[-1]
                tag_array_index.remove(tag_array_index[-1])
                tag_array_index.insert(0,m)  
                r+=1 
                capacity_read_misses+=1
                cycles+=miss_penalty  
        else:
            hex=(master_file[k][4:12])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            if tag in tag_array:
                m=tag_array.index(tag)
                tag_array_index.remove(m)
                tag_array_index.insert(0,m)
                cycles+=miss_penalty
                write_hit+=1
            elif ' ' in tag_array:
                for i in range(len(tag_array)):
                    if tag_array[i]== ' ':
                        tag_array[i]=tag
                        tag_array_index.remove(tag_array_index[-1])
                        tag_array_index.insert(0,i)
                        compulsary_write_miss+=1
                        cycles+=2*miss_penalty
                        break
            else:
                tag_array[tag_array_index[-1]]=tag
                m=tag_array_index[-1]
                tag_array_index.remove(tag_array_index[-1])
                tag_array_index.insert(0,m)  
                r+=1 
                capacity_write_misses+=1
                cycles+=2*miss_penalty   

    read_misses=capacity_read_misses+compulsary_read_miss+conflict_read_miss
    write_misses=capacity_write_misses+compulsary_write_miss+conflict_write_miss
    
    total_cache_accesses['FA, WT, LRU']=read_hit+write_hit
    total_cache_misses['FA, WT, LRU']=read_misses+write_misses
    program_execution_time['FA, WT, LRU']=1000*((cycles + alu_instructions)*clock_rate)
    cache_accesses=read_hit+write_hit
    cache_misses=read_misses+write_misses
    total_hit_rate=(cache_accesses)/(cache_accesses+cache_misses)
    load_hit_rate=read_hit/(read_hit+read_misses)
    store_hit_rate=write_hit/(write_hit+write_misses)
    nand_gates= 2*blocks + blocks*tag_bits*4

    new_dict.update({'FA, WT, LRU':{'tag bits':tag_bits, 'index bits':0, 'offset bits':offset_bits, 'blocks':blocks, 'cache accesses':cache_accesses, 'cache misses': cache_misses, 'read accesses': read_hit, 'write accesses':write_hit, 'read misses':read_misses, 'write misses': write_misses, 'compulsary read miss': compulsary_read_miss, 'compulsary write miss': compulsary_write_miss, 'Total compulsary misses':compulsary_write_miss+compulsary_read_miss, 'conflict read miss':conflict_read_miss, 'conflict write miss': conflict_write_miss, 'Total conflict misses': conflict_read_miss+conflict_write_miss, 'capacity read misses':capacity_read_misses, 'capacity write misses':capacity_write_misses, 'Total capacity misses': capacity_read_misses+capacity_write_misses, 'Dirty blocks evicted':Dirty_blocks, 'Program Execution Time':1000*((cycles + alu_instructions)*clock_rate), 'total hit rate':total_hit_rate,'load_hit_rate':load_hit_rate, 'store hit rate':store_hit_rate, 'Number of NAND gates':nand_gates }})

#Fully Associative Cache, Write Through, FIFO
if ( True ):
    offset_bits=int(Log2(block_size))
    blocks=int(cache_size/block_size)
    tag_bits=int(32-offset_bits)
    tag_array=[]
    tag_array = [' ' for x in range(int(blocks))]
    read_hit=0
    write_hit=0
    cycles=0
    compulsary_read_miss=0
    compulsary_write_miss=0
    conflict_read_miss=0
    conflict_write_miss=0
    capacity_read_misses=0
    capacity_write_misses=0
    Dirty_blocks=0
    alu_instructions=0
    r=0

    for k in range(len(master_file)):
        alu_instructions+= int(master_file[k][13])
        if master_file[k][0]=='l':
            hex=(master_file[k][4:12])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            if tag in tag_array:
                read_hit+=1
                cycles+=1
            elif ' ' in tag_array:
                for i in range(len(tag_array)):
                    if tag_array[i]== ' ':
                        tag_array[i]=tag
                        compulsary_read_miss+=1
                        cycles+=miss_penalty
                        break
            else:
                tag_array[r%len(tag_array)]=tag
                r+=1
                capacity_read_misses+=1
                cycles+=miss_penalty
        else:
            hex=(master_file[k][4:12])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            if tag in tag_array:
                write_hit+=1
                cycles+=miss_penalty
            elif ' ' in tag_array:
                for i in range(len(tag_array)):
                    if tag_array[i]== ' ':
                        tag_array[i]=tag
                        compulsary_write_miss+=1
                        cycles+=2*miss_penalty
                        break 
                    
            else:
                tag_array[r%len(tag_array)]=tag
                r+=1
                capacity_write_misses+=1
                cycles+=2*miss_penalty
    read_misses=capacity_read_misses+compulsary_read_miss+conflict_read_miss
    write_misses=capacity_write_misses+compulsary_write_miss+conflict_write_miss
    total_cache_accesses['FA, WT, FIFO']=read_hit+write_hit
    total_cache_misses['FA, WT, FIFO']=read_misses+write_misses
    program_execution_time['FA, WT, FIFO']=1000*((cycles + alu_instructions)*clock_rate)
    cache_accesses=read_hit+write_hit
    cache_misses=read_misses+write_misses
    total_hit_rate=(cache_accesses)/(cache_accesses+cache_misses)
    load_hit_rate=read_hit/(read_hit+read_misses)
    store_hit_rate=write_hit/(write_hit+write_misses)
    nand_gates= 2*blocks + blocks*tag_bits*4

    new_dict.update({'FA, WT, FIFO':{'tag bits':tag_bits, 'index bits':0, 'offset bits':offset_bits, 'blocks':blocks, 'cache accesses':cache_accesses, 'cache misses': cache_misses, 'read accesses': read_hit, 'write accesses':write_hit, 'read misses':read_misses, 'write misses': write_misses, 'compulsary read miss': compulsary_read_miss, 'compulsary write miss': compulsary_write_miss, 'Total compulsary misses':compulsary_write_miss+compulsary_read_miss, 'conflict read miss':conflict_read_miss, 'conflict write miss': conflict_write_miss, 'Total conflict misses': conflict_read_miss+conflict_write_miss, 'capacity read misses':capacity_read_misses, 'capacity write misses':capacity_write_misses, 'Total capacity misses': capacity_read_misses+capacity_write_misses, 'Dirty blocks evicted':Dirty_blocks, 'Program Execution Time':1000*((cycles + alu_instructions)*clock_rate), 'total hit rate':total_hit_rate,'load_hit_rate':load_hit_rate, 'store hit rate':store_hit_rate, 'Number of NAND gates':nand_gates }})

# Fully Associative Cache, Write Back, LRU
if ( True):
    offset_bits=int(Log2(block_size))
    # print("Number of offset bits:" , offset_bits)
    blocks=int(cache_size/block_size)
    # print("Number of blocks:", blocks)
    tag_bits=int(32-offset_bits)
    # print("Number of tag bits:" ,tag_bits)
    # print("Tag bits are: " , tag)
    # print("Index bits are: " , index)
    # print("Offset bits are: " , offset)

    tag_array=[]
    tag_array = [' ' for x in range(int(blocks))]
    # print(len(tag_array))
    tag_array_index=[' ' for x in range(int(blocks))]

    read_hit=0
    write_hit=0
    cycles=0
    compulsary_read_miss=0
    compulsary_write_miss=0
    conflict_read_miss=0
    conflict_write_miss=0
    capacity_read_misses=0
    capacity_write_misses=0
    Dirty_blocks=0
    alu_instructions=0
    r=0
    dirty_bit=[0 for y in range(int(blocks))]

    for k in range(len(master_file)):
        alu_instructions+= int(master_file[k][13])
        if master_file[k][0]=='l':
            hex=(master_file[k][4:12])
            binary_string=HexToBin(hex)
            # print("Corresponding binary number is: ", binary_string)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            # print("Tag bits are: " , tag)
            # print("Offset bits are: " , offset)
            if tag in tag_array:
                m=tag_array.index(tag)
                tag_array_index.remove(m)
                tag_array_index.insert(0,m)
                # print("Cache Hit")
                # print(tag_array)
                # print(tag_array_index)
                read_hit+=1
                cycles+=1
            elif ' ' in tag_array:
                for i in range(len(tag_array)):
                    if tag_array[i]== ' ':
                        tag_array[i]=tag
                        tag_array_index.remove(tag_array_index[-1])
                        tag_array_index.insert(0,i)
                        # print("Compulsary Miss")
                        # print(tag_array)
                        # print(tag_array_index)
                        cycles+=miss_penalty
                        compulsary_read_miss+=1
                        break
            else:
                tag_array[tag_array_index[-1]]=tag
                m=tag_array_index[-1]
                tag_array_index.remove(tag_array_index[-1])
                tag_array_index.insert(0,m)  
                # print("Capacity Miss")
                cycles+=miss_penalty
                capacity_read_misses+=1
                r+=1 
                if dirty_bit[m]==1:
                    Dirty_blocks+=1
                # print(tag_array)
                # print(tag_array_index) 
        else:
            hex=(master_file[k][4:12])
            binary_string=HexToBin(hex)
            # print("Corresponding binary number is: ", binary_string)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            # print("Tag bits are: " , tag)
            # print("Offset bits are: " , offset)
            if tag in tag_array:
                m=tag_array.index(tag)
                tag_array_index.remove(m)
                tag_array_index.insert(0,m)
                # print("Cache Hit")
                # print(tag_array)
                # print(tag_array_index)
                write_hit+=1
                cycles+=1
            elif ' ' in tag_array:
                for i in range(len(tag_array)):
                    if tag_array[i]== ' ':
                        tag_array[i]=tag
                        tag_array_index.remove(tag_array_index[-1])
                        tag_array_index.insert(0,i)
                        # print("Compulsary Miss")
                        # print(tag_array)
                        # print(tag_array_index)
                        dirty_bit[i]=1
                        cycles+=miss_penalty
                        compulsary_write_miss+=1
                        break
            else:
                tag_array[tag_array_index[-1]]=tag
                m=tag_array_index[-1]
                tag_array_index.remove(tag_array_index[-1])
                tag_array_index.insert(0,m)  
                # print("Capacity Miss")
                cycles+=miss_penalty
                capacity_write_misses+=1
                r+=1 
                if dirty_bit[m]==1:
                    Dirty_blocks+=1  
    read_misses=capacity_read_misses+compulsary_read_miss+conflict_read_miss
    write_misses=capacity_write_misses+compulsary_write_miss+conflict_write_miss
    # print(read_hit+write_hit)
    # print(read_misses+write_misses)
    # print(read_hit)
    # print(write_hit)
    # print(read_misses)
    # print(write_misses)
    # print(compulsary_read_miss)
    # print(compulsary_write_miss)
    # print(compulsary_read_miss+compulsary_write_miss)
    # print(conflict_read_miss)
    # print(conflict_write_miss)
    # print(conflict_read_miss+conflict_write_miss)
    # print(capacity_read_misses)
    # print(capacity_write_misses)
    # print(capacity_read_misses+capacity_write_misses)
    # print(Dirty_blocks)
    # print( (cycles + alu_instructions)*clock_rate )
    total_cache_accesses['FA, WB, LRU']=read_hit+write_hit
    total_cache_misses['FA, WB, LRU']=read_misses+write_misses
    program_execution_time['FA, WB, LRU']=1000*((cycles + alu_instructions)*clock_rate)
    cache_accesses=read_hit+write_hit
    cache_misses=read_misses+write_misses
    total_hit_rate=(cache_accesses)/(cache_accesses+cache_misses)
    load_hit_rate=read_hit/(read_hit+read_misses)
    store_hit_rate=write_hit/(write_hit+write_misses)
    nand_gates= 2*blocks + blocks*tag_bits*4

    new_dict.update({'FA, WB, LRU':{'tag bits':tag_bits, 'index bits':0, 'offset bits':offset_bits, 'blocks':blocks, 'cache accesses':cache_accesses, 'cache misses': cache_misses, 'read accesses': read_hit, 'write accesses':write_hit, 'read misses':read_misses, 'write misses': write_misses, 'compulsary read miss': compulsary_read_miss, 'compulsary write miss': compulsary_write_miss, 'Total compulsary misses':compulsary_write_miss+compulsary_read_miss, 'conflict read miss':conflict_read_miss, 'conflict write miss': conflict_write_miss, 'Total conflict misses': conflict_read_miss+conflict_write_miss, 'capacity read misses':capacity_read_misses, 'capacity write misses':capacity_write_misses, 'Total capacity misses': capacity_read_misses+capacity_write_misses, 'Dirty blocks evicted':Dirty_blocks, 'Program Execution Time':1000*((cycles + alu_instructions)*clock_rate), 'total hit rate':total_hit_rate,'load_hit_rate':load_hit_rate, 'store hit rate':store_hit_rate, 'Number of NAND gates':nand_gates }})

# Fully Associative Cache, Write Back, FIFO
if ( True ):
    offset_bits=int(Log2(block_size))
    blocks=int(cache_size/block_size)
    tag_bits=int(32-offset_bits)
    tag_array=[]
    tag_array = [' ' for x in range(int(blocks))]
    read_hit=0
    write_hit=0
    cycles=0
    compulsary_read_miss=0
    compulsary_write_miss=0
    conflict_read_miss=0
    conflict_write_miss=0
    capacity_read_misses=0
    capacity_write_misses=0
    Dirty_blocks=0
    alu_instructions=0
    r=0
    dirty_bit=[0 for y in range(int(blocks))]
    for k in range(len(master_file)):
        alu_instructions+= int(master_file[k][13])
        if master_file[k][0]=='l':
            hex=(master_file[k][4:12])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            if tag in tag_array:
                read_hit+=1
                cycles+=1
            elif ' ' in tag_array:
                for i in range(len(tag_array)):
                    if tag_array[i]== ' ':
                        tag_array[i]=tag
                        compulsary_read_miss+=1
                        cycles+=miss_penalty
                        break
            else:
                tag_array[r%len(tag_array)]=tag
                r+=1
                capacity_read_misses+=1
                cycles+=miss_penalty
                if dirty_bit[r%len(tag_array)]==1:
                    Dirty_blocks+=1
        else:
            hex=(master_file[k][4:12])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            if tag in tag_array:
                write_hit+=1
                cycles+=1
            elif ' ' in tag_array:
                for i in range(len(tag_array)):
                    if tag_array[i]== ' ':
                        tag_array[i]=tag
                        dirty_bit[i]=1
                        compulsary_write_miss+=1
                        cycles+=miss_penalty
                        break 
                    
            else:
                tag_array[r%len(tag_array)]=tag
                r+=1
                if dirty_bit[r%len(tag_array)]==1:
                    Dirty_blocks+=1
                capacity_write_misses+=1
                cycles+=miss_penalty
    read_misses=capacity_read_misses+compulsary_read_miss+conflict_read_miss
    write_misses=capacity_write_misses+compulsary_write_miss+conflict_write_miss
    total_cache_accesses['FA, WB, FIFO']=read_hit+write_hit
    total_cache_misses['FA, WB, FIFO']=read_misses+write_misses
    program_execution_time['FA, WB, FIFO']=1000*((cycles + alu_instructions)*clock_rate)
    cache_accesses=read_hit+write_hit
    cache_misses=read_misses+write_misses
    total_hit_rate=(cache_accesses)/(cache_accesses+cache_misses)
    load_hit_rate=read_hit/(read_hit+read_misses)
    store_hit_rate=write_hit/(write_hit+write_misses)
    nand_gates= 2*blocks + blocks*tag_bits*4

    new_dict.update({'FA, WB, FIFO':{'tag bits':tag_bits, 'index bits':0, 'offset bits':offset_bits, 'blocks':blocks, 'cache accesses':cache_accesses, 'cache misses': cache_misses, 'read accesses': read_hit, 'write accesses':write_hit, 'read misses':read_misses, 'write misses': write_misses, 'compulsary read miss': compulsary_read_miss, 'compulsary write miss': compulsary_write_miss, 'Total compulsary misses':compulsary_write_miss+compulsary_read_miss, 'conflict read miss':conflict_read_miss, 'conflict write miss': conflict_write_miss, 'Total conflict misses': conflict_read_miss+conflict_write_miss, 'capacity read misses':capacity_read_misses, 'capacity write misses':capacity_write_misses, 'Total capacity misses': capacity_read_misses+capacity_write_misses, 'Dirty blocks evicted':Dirty_blocks, 'Program Execution Time':1000*((cycles + alu_instructions)*clock_rate), 'total hit rate':total_hit_rate,'load_hit_rate':load_hit_rate, 'store hit rate':store_hit_rate, 'Number of NAND gates':nand_gates }})

#Set Associative Cache, Write Through, LRU replacement
if ( True ):
    associativity= common_associativity
    offset_bits=int(Log2(block_size))
    blocks=int(cache_size/block_size)
    no_of_sets = int(blocks/associativity)
    index_bits=int(Log2(no_of_sets))
    tag_bits=int(32-offset_bits-index_bits)
    tag_array=[[' ' for i in range(associativity)] for j in range(no_of_sets)]
    index_array_all=[[' ' for y in range(associativity)] for x in range(int(no_of_sets))]
    read_hit=0
    write_hit=0
    cycles=0
    compulsary_read_miss=0
    compulsary_write_miss=0
    conflict_read_miss=0
    conflict_write_miss=0
    capacity_read_misses=0
    capacity_write_misses=0
    Dirty_blocks=0
    alu_instructions=0
    for k in range(len(master_file)):
        alu_instructions+= int(master_file[k][13])
        if master_file[k][0]=='l':
            hex=(master_file[k][4:12])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            index = binary_string[int(tag_bits):int(tag_bits)+int(index_bits)]
            array_new=tag_array[int(index,2)]
            if tag in array_new:
                m=array_new.index(tag)
                index_array_all[int(index,2)].remove(m)
                index_array_all[int(index,2)].insert(0,m)
                read_hit+=1
                cycles+=1
            elif ' ' in array_new:
                for i in range(len(array_new)):
                    if array_new[i]== ' ':
                        array_new[i]=tag
                        index_array_all[int(index,2)].remove(index_array_all[int(index,2)][-1])
                        index_array_all[int(index,2)].insert(0,i)
                        cycles+=miss_penalty
                        compulsary_read_miss+=1
                        break
            else:
                array_new[index_array_all[int(index,2)][-1]]=tag
                m=index_array_all[int(index,2)][-1]
                index_array_all[int(index,2)].remove(index_array_all[int(index,2)][-1])
                index_array_all[int(index,2)].insert(0,m)  
                capacity_read_misses+=1
                cycles+=miss_penalty
        else:
            hex=(master_file[k][4:12])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            index = binary_string[int(tag_bits):int(tag_bits)+int(index_bits)]
            array_new=tag_array[int(index,2)]
            if tag in array_new:
                m=array_new.index(tag)
                index_array_all[int(index,2)].remove(m)
                index_array_all[int(index,2)].insert(0,m)
                write_hit+=1
                cycles+=miss_penalty
            elif ' ' in array_new:
                for i in range(len(array_new)):
                    if array_new[i]== ' ':
                        array_new[i]=tag
                        index_array_all[int(index,2)].remove(index_array_all[int(index,2)][-1])
                        index_array_all[int(index,2)].insert(0,i)
                        cycles+=2*miss_penalty
                        compulsary_write_miss+=1
                        break
            else:
                array_new[index_array_all[int(index,2)][-1]]=tag
                m=index_array_all[int(index,2)][-1]
                index_array_all[int(index,2)].remove(index_array_all[int(index,2)][-1])
                index_array_all[int(index,2)].insert(0,m)  
                capacity_write_misses+=1
                cycles+=2*miss_penalty                       
    
    read_misses=capacity_read_misses+compulsary_read_miss+conflict_read_miss
    write_misses=capacity_write_misses+compulsary_write_miss+conflict_write_miss
    total_cache_accesses['SA, WT, LRU']=read_hit+write_hit
    total_cache_misses['SA, WT, LRU']=read_misses+write_misses
    program_execution_time['SA, WT, LRU']=1000*((cycles + alu_instructions)*clock_rate)
    cache_accesses=read_hit+write_hit
    cache_misses=read_misses+write_misses
    total_hit_rate=(cache_accesses)/(cache_accesses+cache_misses)
    load_hit_rate=read_hit/(read_hit+read_misses)
    store_hit_rate=write_hit/(write_hit+write_misses)
    nand_gates= 2*common_associativity + common_associativity*tag_bits*4

    new_dict.update({'SA, WT, LRU':{'tag bits':tag_bits, 'index bits':index_bits, 'offset bits':offset_bits, 'blocks':blocks, 'cache accesses':cache_accesses, 'cache misses': cache_misses, 'read accesses': read_hit, 'write accesses':write_hit, 'read misses':read_misses, 'write misses': write_misses, 'compulsary read miss': compulsary_read_miss, 'compulsary write miss': compulsary_write_miss, 'Total compulsary misses':compulsary_write_miss+compulsary_read_miss, 'conflict read miss':conflict_read_miss, 'conflict write miss': conflict_write_miss, 'Total conflict misses': conflict_read_miss+conflict_write_miss, 'capacity read misses':capacity_read_misses, 'capacity write misses':capacity_write_misses, 'Total capacity misses': capacity_read_misses+capacity_write_misses, 'Dirty blocks evicted':Dirty_blocks, 'Program Execution Time':1000*((cycles + alu_instructions)*clock_rate), 'total hit rate':total_hit_rate,'load_hit_rate':load_hit_rate, 'store hit rate':store_hit_rate, 'Number of NAND gates':nand_gates }})

#Set Associative Cache, Write Through, FIFO replacement
if ( True ):
    associativity= common_associativity
    offset_bits=int(Log2(block_size))
    blocks=int(cache_size/block_size)
    no_of_sets = int(blocks/associativity)
    index_bits=int(Log2(no_of_sets))
    tag_bits=int(32-offset_bits-index_bits)
    tag_array=[[' ' for i in range(associativity)] for j in range(no_of_sets)]
    r=[0 for i in range(no_of_sets)]
    read_hit=0
    write_hit=0
    cycles=0
    compulsary_read_miss=0
    compulsary_write_miss=0
    conflict_read_miss=0
    conflict_write_miss=0
    capacity_read_misses=0
    capacity_write_misses=0
    Dirty_blocks=0
    alu_instructions=0
    
    for k in range(len(master_file)):
        if master_file[k][0]=='l':
            hex=(master_file[k][4:12])
            alu_instructions+= int(master_file[k][13])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            index = binary_string[int(tag_bits):int(tag_bits)+int(index_bits)]
            array_new=tag_array[int(index,2)]
            if tag in array_new:
                read_hit+=1
                cycles+=1
            elif ' ' in array_new:
                for i in range(len(array_new)):
                    if array_new[i]== ' ':
                        array_new[i]=tag
                        compulsary_read_miss+=1
                        cycles+=miss_penalty
                        break
            else:
                array_new[r[int(index,2)]%len(array_new)]=tag
                r[int(index,2)]+=1
                capacity_read_misses+=1
                cycles+=miss_penalty
        else:
            hex=(master_file[k][4:12])
            alu_instructions+= int(master_file[k][13])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            index = binary_string[int(tag_bits):int(tag_bits)+int(index_bits)]
            array_new=tag_array[int(index,2)]
            if tag in array_new:
                write_hit+=1
                cycles+=miss_penalty
            elif ' ' in array_new:
                for i in range(len(array_new)):
                    if array_new[i]== ' ':
                        array_new[i]=tag
                        compulsary_write_miss+=1
                        cycles+=2*miss_penalty
                        break
            else:
                array_new[r[int(index,2)]%len(array_new)]=tag
                r[int(index,2)]+=1
                capacity_write_misses+=1
                cycles+=2*miss_penalty
    read_misses=capacity_read_misses+compulsary_read_miss+conflict_read_miss
    write_misses=capacity_write_misses+compulsary_write_miss+conflict_write_miss
    total_cache_accesses['SA, WT, FIFO']=read_hit+write_hit
    total_cache_misses['SA, WT, FIFO']=read_misses+write_misses
    program_execution_time['SA, WT, FIFO']=1000*((cycles + alu_instructions)*clock_rate)
    cache_accesses=read_hit+write_hit
    cache_misses=read_misses+write_misses
    total_hit_rate=(cache_accesses)/(cache_accesses+cache_misses)
    load_hit_rate=read_hit/(read_hit+read_misses)
    store_hit_rate=write_hit/(write_hit+write_misses)
    nand_gates= 2*common_associativity + common_associativity*tag_bits*4

    new_dict.update({'SA, WT, FIFO':{'tag bits':tag_bits, 'index bits':index_bits, 'offset bits':offset_bits, 'blocks':blocks, 'cache accesses':cache_accesses, 'cache misses': cache_misses, 'read accesses': read_hit, 'write accesses':write_hit, 'read misses':read_misses, 'write misses': write_misses, 'compulsary read miss': compulsary_read_miss, 'compulsary write miss': compulsary_write_miss, 'Total compulsary misses':compulsary_write_miss+compulsary_read_miss, 'conflict read miss':conflict_read_miss, 'conflict write miss': conflict_write_miss, 'Total conflict misses': conflict_read_miss+conflict_write_miss, 'capacity read misses':capacity_read_misses, 'capacity write misses':capacity_write_misses, 'Total capacity misses': capacity_read_misses+capacity_write_misses, 'Dirty blocks evicted':Dirty_blocks, 'Program Execution Time':1000*((cycles + alu_instructions)*clock_rate), 'total hit rate':total_hit_rate,'load_hit_rate':load_hit_rate, 'store hit rate':store_hit_rate, 'Number of NAND gates':nand_gates }})

##Set Associative Cache, Write Back, LRU replacement
if ( True ):
    associativity= common_associativity
    offset_bits=int(Log2(block_size))
    blocks=int(cache_size/block_size)
    no_of_sets = int(blocks/associativity)
    index_bits=int(Log2(no_of_sets))
    tag_bits=int(32-offset_bits-index_bits)
    tag_array=[[' ' for i in range(associativity)] for j in range(no_of_sets)]
    index_array_all=[[' ' for y in range(associativity)] for x in range(int(no_of_sets))]
    read_hit=0
    write_hit=0
    cycles=0
    compulsary_read_miss=0
    compulsary_write_miss=0
    conflict_read_miss=0
    conflict_write_miss=0
    capacity_read_misses=0
    capacity_write_misses=0
    Dirty_blocks=0
    alu_instructions=0
    dirty_bit=[[0 for y in range(associativity)] for x in range(int(no_of_sets))]
    for k in range(len(master_file)):
        alu_instructions+= int(master_file[k][13])
        if master_file[k][0]=='l':
            hex=(master_file[k][4:12])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            index = binary_string[int(tag_bits):int(tag_bits)+int(index_bits)]
            array_new=tag_array[int(index,2)]
            if tag in array_new:
                m=array_new.index(tag)
                index_array_all[int(index,2)].remove(m)
                index_array_all[int(index,2)].insert(0,m)
                read_hit+=1
                cycles+=1
            elif ' ' in array_new:
                for i in range(len(array_new)):
                    if array_new[i]== ' ':
                        array_new[i]=tag
                        index_array_all[int(index,2)].remove(index_array_all[int(index,2)][-1])
                        index_array_all[int(index,2)].insert(0,i)
                        cycles+=miss_penalty
                        compulsary_read_miss+=1
                        break
            else:
                array_new[index_array_all[int(index,2)][-1]]=tag
                m=index_array_all[int(index,2)][-1]
                index_array_all[int(index,2)].remove(index_array_all[int(index,2)][-1])
                index_array_all[int(index,2)].insert(0,m)  
                capacity_read_misses+=1
                if dirty_bit[int(index,2)][i]==1:
                    Dirty_blocks+=1
                cycles+=miss_penalty
        else:
            hex=(master_file[k][4:12])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            index = binary_string[int(tag_bits):int(tag_bits)+int(index_bits)]
            array_new=tag_array[int(index,2)]
            if tag in array_new:
                m=array_new.index(tag)
                dirty_bit[int(index,2)][array_new.index(tag)]=1
                index_array_all[int(index,2)].remove(m)
                index_array_all[int(index,2)].insert(0,m)
                write_hit+=1
                cycles+=1
            elif ' ' in array_new:
                for i in range(len(array_new)):
                    if array_new[i]== ' ':
                        array_new[i]=tag
                        index_array_all[int(index,2)].remove(index_array_all[int(index,2)][-1])
                        index_array_all[int(index,2)].insert(0,i)
                        cycles+=miss_penalty
                        compulsary_write_miss+=1
                        dirty_bit[int(index,2)][i]=1
                        break
            else:
                array_new[index_array_all[int(index,2)][-1]]=tag
                m=index_array_all[int(index,2)][-1]
                index_array_all[int(index,2)].remove(index_array_all[int(index,2)][-1])
                index_array_all[int(index,2)].insert(0,m)  
                capacity_write_misses+=1
                if dirty_bit[int(index,2)][i]==1:
                    Dirty_blocks+=1
                cycles+=miss_penalty                       
    
    read_misses=capacity_read_misses+compulsary_read_miss+conflict_read_miss
    write_misses=capacity_write_misses+compulsary_write_miss+conflict_write_miss
    total_cache_accesses['SA, WB, LRU']=read_hit+write_hit
    total_cache_misses['SA, WB, LRU']=read_misses+write_misses
    program_execution_time['SA, WB, LRU']=1000*((cycles + alu_instructions)*clock_rate)
    cache_accesses=read_hit+write_hit
    cache_misses=read_misses+write_misses
    total_hit_rate=(cache_accesses)/(cache_accesses+cache_misses)
    load_hit_rate=read_hit/(read_hit+read_misses)
    store_hit_rate=write_hit/(write_hit+write_misses)
    nand_gates= 2*common_associativity + common_associativity*tag_bits*4

    new_dict.update({'SA, WB, LRU':{'tag bits':tag_bits, 'index bits':index_bits, 'offset bits':offset_bits, 'blocks':blocks, 'cache accesses':cache_accesses, 'cache misses': cache_misses, 'read accesses': read_hit, 'write accesses':write_hit, 'read misses':read_misses, 'write misses': write_misses, 'compulsary read miss': compulsary_read_miss, 'compulsary write miss': compulsary_write_miss, 'Total compulsary misses':compulsary_write_miss+compulsary_read_miss, 'conflict read miss':conflict_read_miss, 'conflict write miss': conflict_write_miss, 'Total conflict misses': conflict_read_miss+conflict_write_miss, 'capacity read misses':capacity_read_misses, 'capacity write misses':capacity_write_misses, 'Total capacity misses': capacity_read_misses+capacity_write_misses, 'Dirty blocks evicted':Dirty_blocks, 'Program Execution Time':1000*((cycles + alu_instructions)*clock_rate), 'total hit rate':total_hit_rate,'load_hit_rate':load_hit_rate, 'store hit rate':store_hit_rate, 'Number of NAND gates':nand_gates }})

#Set Associative Cache, Write Back, FIFO replacement
if ( True ):
    associativity= common_associativity
    offset_bits=int(Log2(block_size))
    blocks=int(cache_size/block_size)
    no_of_sets = int(blocks/associativity)
    index_bits=int(Log2(no_of_sets))
    tag_bits=int(32-offset_bits-index_bits)
    tag_array=[[' ' for i in range(associativity)] for j in range(no_of_sets)]
    r=[0 for i in range(no_of_sets)]
    dirty_bit=[[0 for y in range(associativity)] for x in range(int(no_of_sets))]
    read_hit=0
    write_hit=0
    cycles=0
    compulsary_read_miss=0
    compulsary_write_miss=0
    conflict_read_miss=0
    conflict_write_miss=0
    capacity_read_misses=0
    capacity_write_misses=0
    Dirty_blocks=0
    alu_instructions=0
    for k in range(len(master_file)):
        if master_file[k][0]=='l':
            hex=(master_file[k][4:12])
            alu_instructions+= int(master_file[k][13])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            index = binary_string[int(tag_bits):int(tag_bits)+int(index_bits)]
            array_new=tag_array[int(index,2)]
            if tag in array_new:
                read_hit+=1
                cycles+=1
            elif ' ' in array_new:
                for i in range(len(array_new)):
                    if array_new[i]== ' ':
                        array_new[i]=tag
                        compulsary_read_miss+=1
                        cycles+=miss_penalty
                        break
            else:
                array_new[r[int(index,2)]%len(array_new)]=tag
                r[int(index,2)]+=1
                capacity_read_misses+=1
                cycles+=miss_penalty
                if dirty_bit[int(index,2)][i]==1:
                    Dirty_blocks+=1
        else:
            hex=(master_file[k][4:12])
            alu_instructions+= int(master_file[k][13])
            binary_string=HexToBin(hex)
            offset = binary_string[-int(offset_bits):]
            tag = binary_string[:int(tag_bits)]
            index = binary_string[int(tag_bits):int(tag_bits)+int(index_bits)]
            array_new=tag_array[int(index,2)]
            if tag in array_new:
                write_hit+=1
                cycles+=1
                dirty_bit[int(index,2)][array_new.index(tag)]=1
            elif ' ' in array_new:
                for i in range(len(array_new)):
                    if array_new[i]== ' ':
                        array_new[i]=tag
                        compulsary_write_miss+=1
                        cycles+=miss_penalty
                        dirty_bit[int(index,2)][i]=1
                        break
            else:
                array_new[r[int(index,2)]%len(array_new)]=tag
                r[int(index,2)]+=1
                capacity_write_misses+=1
                cycles+=miss_penalty
                if dirty_bit[int(index,2)][i]==1:
                    Dirty_blocks+=1 
    read_misses=capacity_read_misses+compulsary_read_miss+conflict_read_miss
    write_misses=capacity_write_misses+compulsary_write_miss+conflict_write_miss
    
    total_cache_accesses['SA, WB, FIFO']=read_hit+write_hit
    total_cache_misses['SA, WB, FIFO']=read_misses+write_misses
    program_execution_time['SA, WB, FIFO']=1000*((cycles + alu_instructions)*clock_rate)
    cache_accesses=read_hit+write_hit
    cache_misses=read_misses+write_misses
    total_hit_rate=(cache_accesses)/(cache_accesses+cache_misses)
    load_hit_rate=read_hit/(read_hit+read_misses)
    store_hit_rate=write_hit/(write_hit+write_misses)
    nand_gates= 2*common_associativity + common_associativity*tag_bits*4

    new_dict.update({'SA, WB, FIFO':{'tag bits':tag_bits, 'index bits':index_bits, 'offset bits':offset_bits, 'blocks':blocks, 'cache accesses':cache_accesses, 'cache misses': cache_misses, 'read accesses': read_hit, 'write accesses':write_hit, 'read misses':read_misses, 'write misses': write_misses, 'compulsary read miss': compulsary_read_miss, 'compulsary write miss': compulsary_write_miss, 'Total compulsary misses':compulsary_write_miss+compulsary_read_miss, 'conflict read miss':conflict_read_miss, 'conflict write miss': conflict_write_miss, 'Total conflict misses': conflict_read_miss+conflict_write_miss, 'capacity read misses':capacity_read_misses, 'capacity write misses':capacity_write_misses, 'Total capacity misses': capacity_read_misses+capacity_write_misses, 'Dirty blocks evicted':Dirty_blocks, 'Program Execution Time':1000*((cycles + alu_instructions)*clock_rate), 'total hit rate':total_hit_rate,'load_hit_rate':load_hit_rate, 'store hit rate':store_hit_rate, 'Number of NAND gates':nand_gates }})


#Generating CSV file for all outputs
keys=list(new_dict.keys())
parameters= list(new_dict['Direct, WT'].keys())
col = [[new_dict[c][r] for r in list(new_dict['Direct, WT'].keys()) ] for c in list(new_dict.keys())]
dict = {}
dict['Parameters'] =parameters
for i in range(len(col)):
    dict[keys[i]] = col[i]

df = pd.DataFrame(dict)
df.to_csv(r'D:\\cache_parameters.csv')


# Conclusive Statement
key_list_2 = list(program_execution_time.keys())
val_list_2 = list(program_execution_time.values())
position_2=position = val_list_2.index((min(list(program_execution_time.values()))))
print('Best Execution Time is ', (min(list(program_execution_time.values()))) , ' and it corresponds to ',key_list_2[position_2],' cache configutation.')

#Plotting the graphs
plt.subplot(2, 2, 1)
keys_1 = list(total_cache_misses.keys())
values_1 = list(total_cache_misses.values())
plt.barh(keys_1, values_1)
for index, value in enumerate(values_1):
    plt.text(value, index,
             str(value))
plt.ylabel("Cache Configuration")
plt.xlabel("Total Cache Misses")
a="Cache size: "+ str(cache_size) + ", Block size: " + str(block_size) + ", Associativity: " + str(common_associativity)
plt.title(a)
max_y_lim = 1.02*max(values_1)
min_y_lim = 0.98*min(values_1)
plt.xlim(min_y_lim, max_y_lim)


plt.subplot(2, 2, 3)
keys_2 = list(program_execution_time.keys())
values_2 = list(program_execution_time.values())
plt.barh(keys_2, values_2)
for index, value in enumerate(values_2):
    plt.text(value, index,
             str(value))
plt.ylabel("Cache Configuration")
plt.xlabel("Total Execution time")
max_y_lim =1.2*max(values_2)
min_y_lim = 0.8*min(values_2)
plt.xlim(min_y_lim, max_y_lim)


plt.subplot(2, 2, 2)
y=[total_alu_instructions, total_load_instructions, total_store_instructions]
a1="ALU instructions: "+str(total_alu_instructions)
a2="Load instructions: "+str(total_load_instructions)
a3="Store instructions: "+str(total_store_instructions)
mylabels = [a1,a2,a3]
plt.pie(y, labels = mylabels , autopct='%1.0f%%')

plt.show()

