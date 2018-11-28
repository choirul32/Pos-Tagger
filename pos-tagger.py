from nltk.tag import CRFTagger

jumSample = 500000
namaFile = 'indonesia-train-tagged-corpus.tsv'
with open(namaFile, 'r', encoding='utf-8') as f:
	lines = f.read().split('\n')

pasangan = []
AllPassangan = []

for line in lines[: min(jumSample, len(lines))]:
	if line == '':
		AllPassangan.append(pasangan)
		pasangan = []
	else:
		kata, tag = line.split('\t')
		p = (kata, tag)
		pasangan.append(p)

ct = CRFTagger()
ct.train(AllPassangan, 'pos-tagger-indonesia-model.tagger')

