from nltk.tag import CRFTagger

ct = CRFTagger()
ct.set_model_file('pos-tagger-indonesia-model.tagger')

hasil = ct.tag_sents([['Saya','bekerja','di','Bandung'],['Nama','saya','Yudi']])
print(hasil)