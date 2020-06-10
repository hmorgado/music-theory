class Notes:

	notes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
	
	patterns = {
		'maj'      : [0, 2, 4, 5, 7, 9, 11, 12],
		'min'      : [0, 2, 3, 5, 7, 8, 10, 12],
		'maj_pent' : [0, 2, 4, 7, 9],
		'min_pent' : [0, 3, 5, 7, 10],
	}

	# https://www.pythonanywhere.com/

	# needs self cuz its a class method, not a function
	def custom_notes(self, n):
		n_idx = self.notes.index(n.upper())
		return self.notes[n_idx:len(self.notes)] + self.notes[0:n_idx]

	def get_scale(self, n, kind='maj'):
		if kind not in self.patterns:
			raise Exception(f'scale [{kind}] not found.')

		scale_pattern = self.patterns[kind]
		return list(self.custom_notes(n)[i % 12] for i in scale_pattern)

	def __init__(self):
		pass