from Bio import SeqIO
startswithATG= []
for record in SeqIO.parse("UniqueMR.fasta.transdecoder.cds", "fasta"):
	if record.seq.startswith('ATG'):
		#Add to list
		startswithATG.append(record)
output = open("UniqueMR.fasta.transdecoder.cds.ATG", "w")
SeqIO.write(startswithATG, output, 'fasta')
output.close()
	