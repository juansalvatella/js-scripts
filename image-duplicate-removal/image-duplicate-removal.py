import os
import sys
import filecmp

from multiprocessing import Pool

N_THREADS  = 1
BATCH_SIZE = 100000000

def process_batch(listing):
	duplicated = 0
	r_list = listing[:]
	for path1 in listing:
	    for path2 in r_list:
	    	if path1 != path2:
	    		cond = filecmp.cmp(path1, path2)
	    		print path1 + ' ' + path2 + ': ' + str(cond)
	    		if cond:
	    			duplicated = duplicated + 1
	    			os.remove(path2)
	    			r_list.remove(path2)
	    			listing.remove(path2)
	    r_list.remove(path1)
	print 'Total duplicates: ' + str(duplicated) + ' True'

if __name__ == '__main__':
	directory = sys.argv[1]

	l = []
	for root, dirs, files in os.walk(directory):
		for name in files:
			l.extend([os.path.join(root, name)])
	sub_listings = [l[i:i+BATCH_SIZE] for i in range(0,len(l),BATCH_SIZE)]

	p = Pool(N_THREADS)
	total = p.map(process_batch, sub_listings)
	print 'Total files processed: ' + str(len(l)) + ' True'