# Name: Chris Edwards
# Evergreen Login: edwchr30
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of specific nucleotides seen so far.
g_count = 0
c_count = 0
a_count = 0
t_count = 0
extra_count = 0
# Number of specific nucleotides combinations seen so far.
gc_count = 0
at_count = 0
sum_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # Count specific nucleotides
    if bp == 'G':
        g_count = g_count + 1
        
    if bp == 'C':
        c_count = c_count + 1
        
    if bp == 'A':
        a_count = a_count + 1
        
    if bp == 'T':
        t_count = t_count + 1
        
#Calculate nucleotide combinations

gc_count = float(g_count) + float(c_count)
at_count = float(a_count) + float(t_count)
at_gc_ratio = (float(a_count) + float(t_count)) / (float(g_count) + float(c_count))
sum_count = float(g_count) + float(c_count) + float(a_count) + float(t_count)

# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count

at_content = float(at_count) / total_count

# Print the answer
print 'Number of G nucleotides:', g_count
print 'Number of C nucleotides:', c_count
print 'Number of A nucleotides:', a_count
print 'Number of T nucleotides:', t_count
print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'AT/GC ratio:', at_gc_ratio
print 'Sum of individual counts:', sum_count
print 'The total number of bps:', total_count
print 'Length of the Sequence:', len(seq)

if gc_content>0.6:
    print 'This sample is considered to have a high GC content'
elif gc_content<0.4:
    print 'This sample is considered to have a low GC content'
else:
    print 'This sample is considered to have a moderate GC content'
