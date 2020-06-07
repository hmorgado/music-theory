import random

class Chord:

	notes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
	
	major_scale = [0, 2, 4, 5, 7, 9, 11, 12]
	minor_scale = [0, 2, 3, 5, 7, 8, 10, 12]
	minor_pent  = [0, 3, 5, 7, 10]
	major_pent  = [0, 2, 4, 7, 9]

	# needs self cuz its a class method, not a function
	def custom_notes(self, n):
		n_idx = self.notes.index(n.upper())
		return self.notes[n_idx:len(self.notes)] + self.notes[0:n_idx]

	def get_scale(self, n, kind='maj'):
		if kind == 'maj':
			scale_pattern = self.major_scale
		elif kind == 'min':
			scale_pattern = self.minor_scale
		elif kind == 'min_pent':
			scale_pattern = self.minor_pent
		elif kind == 'maj_pent':
			scale_pattern = self.major_pent
		
		return list(self.custom_notes(n)[i % 12] for i in scale_pattern)

	def __init__(self):
		pass


chord = Chord()

print(chord.get_scale('D', 'min'))
print(chord.get_scale('C', 'maj'))
print(chord.get_scale('F', 'min_pent'))
print(chord.get_scale('A', 'min_pent'))

exit()