import random, sys, time, os

#take a look down here, there is an example should help.

class cprint():
	"""
	Some Color Codes to use: A: light blue, F:light white, D:light purple, C:light red, E:light yellow
			
	#i know it's crazy using oop this way, but i don't really care, this is the way i opertate xD
	"""
	def __init__(self,text , style='r', speed=1/99,cmd_color="A", newline=False, warningOn=False, robotOn=False, freeze=False, normal=False):
		if newline:print()            # newline
		os.system("color "+cmd_color) #cmd_color
		self.letters = [chr(i) for  i in range(65, 123)] + ["@", "#", "$", "%", "^", "&", "*", "~"] #Editable! 
		if robotOn and len(text)>75:
			warningOn = False
			text = text[:30]+ "..." + text[-30:] #robotOn : this force the the text to be under 75 letters so funcs work fine.
		if normal:
			print(text)
			return None
		if len(text) > 75 and warningOn: #Warning!
			self.dprint("WARNING: your text must be less than 75 letters! or shit happens.")
			print("\n")
			self.tprint("Press any key to continue...", speed=1/92)
			input()


		categories = { 
			"d": "self.dprint(text, speed)",     #Distortion printing
			"fo": "self.foprint(text, speed)",   #Fade out print
			"fow":"self.fowprint(text, speed)",  #Words #Fade out print
			"sd": "self.sdprint(text, speed)",   #Slow #Distortion printing
			"rsd": "self.rsdprint(text, speed)", #reverse #Slow #Distortion printing
			"t": "self.tprint(text, speed)",     #Train printing
			"rt": "self.rtprint(text, speed)",	 #Reverse #Train printing 
			"s": "self.sprint(text, speed)",	 #Slow printing   
			"rs": "self.rsprint(text, speed)",	 #Reverse #Slow printing
			"m": "self.mprint(text, speed)",     #Middle printing
			"rm": "self.rmprint(text, speed)",	 #reverse #Middle printing
			"u": "self.uprint(text, speed)",	 #upper casing slow printing
			"r": 'eval(categories[random.choice(["d", "fo", "fow", "sd", "rsd", "t", "rt", "s", "rs", "m", "rm", "u"])])'
		}
		self.memory = [999,999999]
		try:
			eval(categories[style])
		except:
			print("invalid Choice")
		if freeze: #this makes printing freezes for any input after printing!
			input()
	def dprint(self, text, speed=1/99): 
		#Full name: Distortion printing
		res = [text]
		text = list(text)
		for i in range(len(text)+5):
			for _ in range(random.randint(0, 6)):
				text[random.randint(0, len(text)-1)] = random.choice(self.letters)
			res.append("".join(text))
		self.Core(res[::-1], "i", speed, False)

	def foprint(self, text, speed=1/99):
		#Full name: fade out print
		res = [text]
		text = list(text)
		for i in range(len(text)+5):
			for _ in range(random.randint(0, 3)):
				text[random.randint(0, len(text)-1)] = " "
			res.append("".join(text))
		self.Core(res[::-1], "i", speed, False)
	def fowprint(self, text, speed=(1/99)):
		splited = text.split()
		if len(splited) < 4:
			self.foprint(text)
			return None
		seq = [text]
		
		def rando(s,e):
			while True:
				n = random.randint(s, e)
				if n != self.memory[-1] and n!= self.memory[-2]:
					self.memory.append(n)
					return n
		for i in range(0,len(splited)+30):
			copy = splited[:]
			for _ in range(i+1):
				rnd = rando(0, len(copy)-1)
				copy[rnd] = " "*len(copy[rnd])
			seq.append(" ".join(copy))
		seq= [" "*len(splited)] + seq[::-1]
		self.Core(seq, "i", speed, False) 


	def sdprint(self, text, speed=1/99):
		#Full name: Slow distortion printing
		res = [text]
		text = list(text)
		for i in range(len(text)):
			for _ in range(random.randint(0, 6)):
				text[random.randint(0, len(text)-1)] = random.choice(self.letters)
			res.append("".join(text)[:len(text)-i])
		self.Core(res[::-1], "i", speed, False)
	
	def rsdprint(self, text, speed=1/99):
		#Full name: Reverse slow distortion printing
		res = [(0, text)]
		text = list(text)
		for i in range(len(text)):
			for _ in range(random.randint(0, (len(text)-i)//10)):
				text[random.randint(0, len(text)-1)] = random.choice(self.letters)
			piece = "".join(text)[:len(text)-i]
			res.append( (len(text)-len(piece), piece) )
		
		self.Core(res[::-1], "' '*i+j", speed)

	def tprint(self, text, speed=1/99):
		#Full name: Train style print.
		seq = [text[i:] for i in range(len(text)+1,0,-1)] + [text]
		self.Core(seq, "i", speed, double=False)

	def rtprint(self, text, speed=1/99):
		#Full name: Reverse train style print.
		seq = [(len(text)-len(text[:i]), text[:i]) for i in range(0, len(text)+1)] + [(0, text)]
		self.Core(seq, "' '*i + j", speed)
	
	def sprint(self, text, speed=1/99): 
		#Full name: Slow printing.
		seq = [text[0:i] for i in range(1, len(text)+1)]
		self.Core(seq, "i", speed, double=False)

	def rsprint(self, text, speed=1/99): 
		#Full name: Reverse slow printing.
		re_seq = [(len(text)-i, text[-i:]) for i in range(1, len(text)+1)]
		pattern = "' '*i + j"
		self.Core(re_seq, pattern, speed)

	def mprint(self, text, speed=1/99): 
		##Full name: Middle slow printing.
		seq = [(len(text)-i, text[-i:i]) for i in range(1, len(text)+1) if text[-i:i] != ""]
		pattern = "' '*i + j + ' '*i"
		self.Core(seq, pattern, speed)

	def rmprint(self, text, speed=1/99): 
		#Full name: Reverse middle slow printing.
		if len(text)<6:
			print("ERROR: text must be at least 6 letters.")
			return None
		seq, re_seq = [text[0:i] for i in range(1, len(text)//2+1)], [text[-i:] for i in range(1, len(text)//2+1)]
		seq, pattern = zip(seq, re_seq), "i + ' '*(" + str(len(text)) + "-len(i)*2) + j"
		self.Core(seq, pattern, speed)
	def uprint(self, text, speed=1/99):
		seq = [text]
		text, last = list(text), text.upper()
		for i in range(len(text)+5):
			for _ in range(random.randint(0, 6)):
				index = random.randint(0, len(text)-1)
				text[index] = text[index].upper()
			seq.append("".join(text))
		seq.append(last)
		seq = seq+ seq[::-1]
		self.Core(seq, "i", speed, False)
	def Core(self, seq, pattern, speed, double=True):
		if double:
			for i, j in seq:
				sys.stdout.write("\r" + eval(pattern))
				sys.stdout.flush()
				time.sleep(speed)
		else:
			for i in seq:
				sys.stdout.write("\r" + eval(pattern))
				sys.stdout.flush()
				time.sleep(speed)



if __name__ == "__main__":
	
	########### Test ###########
	text = "Hello, Human!, this message should be printed in a cool way xD: "
	cprint(text)            #Random printing style  
	print("\n")             #Do work here instead
	styles=["d", "fo", "fow", "sd", "rsd", "t", "rt", "s", "rs", "m", "rm", "u"]
	for  i in styles:
		cprint(text, style=i)
		print("\n")         #Do work here instead
	input()
