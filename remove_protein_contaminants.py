##Script Name: remove_protein_contaminants.py
##Purpose: Removes protein seqs annotated as contaminants by job.py from the original FASTA protein file (*.transdecoder.pep)
##
##Author: Ethan Baker
## Computational Genomics Lab, University of Connecticut
##
##Last Update 7/11/14

print "Getting started..."
 
from Bio import SeqIO

#Part 0 - Get file paths
originalprotseq = raw_input("Enter the path of the contaminated protein FASTA file (relative is OK!): ")
contaminantsfile = raw_input("Enter the path of the contaminants job.py out file (relative is OK!): ")

#Part 1 - Simplifies FASTA header lines to just ID number. 
outputfile=(open('centroids.fasta.transdecoder.pep.mod','w'))
with open(originalprotseq,'r') as pepfile:
		print "Loading original FASTA protein file...."
		for line in pepfile:
			if line.startswith('>'):
				x = line.split('|', 1)[0]      #Splits the header line to minimal amount to be unique
				#print x
				outputfile.write(x)				#Writes header line. 
				outputfile.write('\n')
			else:
				#print line
				outputfile.write(line)			#Writes sequence
		print "FASTA modification complete!"
outputfile.close()

#Part 2 - Make list of contaminant ID numbers. 
nameslist=open('proteincontaminants.list','w')
with open(contaminantsfile,'r') as contaminants_table:
	print "Loading contaminants table..."
	for line in contaminants_table:
		firstcol = line.split('\t',1)[0]
		idnum = firstcol.split('|', 1)[0] 		#Gets minimal unique portion (same as in part 1)
		nameslist.write('cds.')					#Required to match format of FASTA headers. 
		nameslist.write(idnum)
		nameslist.write('\n')
print "Contaminant names list generated!"
nameslist.close()

#Part 3 - Load contaminant IDs to list.
headerlines=[]
with open('proteincontaminants.list', 'r') as namefile:
	headerlines = namefile.read().splitlines()

#Part 4 -  Remove contaminants from protein seq file
uncontaminated=[]
print 'Removing contaminants...'
for record in SeqIO.parse('centroids.fasta.transdecoder.pep.mod', "fasta"):
	if record.id not in headerlines:		#If file is not in the contaminants list, it must be clean, so append it to the uncontaminated list. 
		uncontaminated.append(record)
print "Generating clean sequence file..."
finaloutput=open("uncontaminatedseqs.pep","w")
SeqIO.write(uncontaminated, finaloutput, "fasta")	#Writes FASTA file
finaloutput.close()	
print "Done!"		