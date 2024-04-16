import kivymd
import sqlite3
from kivymd.app import MDApp
from kivy.lang import Builder
import random
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, NumericProperty, BooleanProperty, StringProperty, ListProperty
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDRoundFlatButton
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.properties import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.label import MDLabel
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.chip import MDChip
from kivymd.uix.pickers import MDColorPicker, MDDatePicker, MDTimePicker
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivy.properties import Clock
from kivymd.uix.list import MDList, OneLineListItem, ThreeLineListItem


class Mimi(StackLayout, Screen):
	div = "yabulu"
	subon = StringProperty("")
	
	def sub(self, it):
		self.manager.ids.quiz.subject.text = it.text
		
	
	
	
class Sec(BoxLayout, Screen):
	difficulty = StringProperty("")
	
	def thing(self, time, qu):
		if time != "":
			if time.isnumeric() == False:
				return False
			self.manager.ids.quiz.qstop = False
			self.manager.ids.quiz.through = False
			self.manager.ids.quiz.tcount.value = 0
		
			self.manager.ids.quiz.tcount.max = eval(time)*60
			
			self.manager.ids.quiz.begin()
			self.manager.ids.quiz.dilog(None)
			self.manager.transition.direction = "left"
			self.manager.current = "quiz"
			
			
		
	def difficulty(self, diff):
		self.manager.ids.quiz.culty.text = diff


class Quiz(BoxLayout, Screen):
	tlet = False
	qnum = 0
	qstop = BooleanProperty(False)
	endrange = 3
	questions = []
	chooselet = False
	ansnum = NumericProperty(0)
	mainq = ListProperty()
	ansgroup = ListProperty()
	mainans = ListProperty()
	diffi = NumericProperty(0)
	through = False
	asterik = ListProperty()
	gans = []
	hold = []
	
	def begin(self):
		self.tlet = False
		
		self.forend = Clock.schedule_once(self.end, self.ids.tcount.max)
		if self.tlet == False:
			if self.ids.culty.text == "Easy":
				self.diffi = 1
			elif self.ids.culty.text == "Medium":
				self.diffi = .7
			elif self.ids.culty.text == "Hard":
				self.diffi = .5
			else:
				self.diffi = 1
			self.fortchange = Clock.schedule_interval(self.tchange, self.diffi)
		
			
	def end(self, dt):
		self.tlet = True
		
		
	def tchange(self, dt):
		if "Sorry, you don't have" in self.ids.quest.text or "You've ended the session" in self.ids.quest.text:
			self.forend.cancel()
			self.fortchange.cancel()
			return False
		if self.qstop == True:
			self.forend.cancel()
			self.fortchange.cancel()
			return False
		self.ids.tcount.value += 1
		
		

	
	def dilog(self, prev):
		for_qs = []
		for_sol = []
		b = []
		dic = {}
		mio = []
		
		
		if self.ids.tcount.value == self.ids.tcount.max:
			self.through = True
		
		if self.through == True:
			return False
			
		qu = self.ids.quest.text
		a1 = self.ids.ans1.text
		a2 = self.ids.ans2.text
		a3 = self.ids.ans3.text
		a4 = self.ids.ans4.text
		
		self.ids.ans1.text_color = 0, 0, 0, 1
		self.ids.ans2.text_color = 0, 0, 0, 1
		self.ids.ans3.text_color = 0, 0, 0, 1
		self.ids.ans4.text_color = 0, 0, 0, 1
		
		
		
		
		
		if self.chooselet == False:
			giv_answers = []
			
			mycon = sqlite3.connect("exam_base.db")
			c = mycon.cursor()
			with mycon:
				c.execute("SELECT question FROM dquiz2 WHERE subject = (?)", (self.ids.subject.text,))
				self.reply = c.fetchall()
				
				c.execute("SELECT answers FROM dquiz2 WHERE subject = (?)", (self.ids.subject.text,))
				self.puply = c.fetchall()
				
				
			for see in self.reply:
				for crux in see:
					self.questions.append(crux)
			
			for wee in self.puply:
				for brux in wee:
					giv_answers.append(brux)
			
			mycon.close()
			
			#print(self.questions)
#			print(giv_answers)
#			return False
			
			#for c in self.questions:
#				j = c.split("   ")
#				for k in j:
#					self.ansgroup = []
#					k = k.split("(")
#					for l in k:
#						k = l.replace("a)", "a. ")
#						k = k.replace("b)", "b. ")
#						k = k.replace("c)", "c. ")
#						k = k.replace("d)", "d. ")
#						
#						if "?" in k:
#							self.mainq.append(k)
#						if "*" in k:
#							k = k.replace("*", "")
#							self.asterik.append(k)
#						if "a. " in k or "b. " in k or "c. " in k or "d. " in k:
#								
#							self.ansgroup.append(k)
#					self.mainans.append(self.ansgroup)
			
			## MAKE A PERSON TO BE ABLE TO PUT  Qs and As IN ONE INPUT
			
			#print(self.questions)
#			qu = ""
#			
#			for ji in self.questions:
#				qu += ji
#			
#			qu = qu.split("ANSW")
#			
#			selfuestions = []
#			
#			for jy in qu:
#				qum = jy.split("END")
#				for poo in qum:
#					selfuestions.append(poo)
#			
#			
#			giv_answers = []
#			
#			for cum in selfuestions:
#				if cum == "":
#					selfuestions.remove(cum)
#			
#			
#			for cool in selfuestions:
#				if "ERS" in cool:
#					bim = cool.replace("ERS", "")
#					giv_answers.append(bim)
#					selfuestions.remove(cool)
					
			
			
			m = ""
			mi = ""
			
			
			for pru in giv_answers:
				m += pru
			
			for pra in self.questions:
				mi += pra+"   "
			
			m = m.lower()
			
			k = mi.replace("A.", "(a)")
			k = k.replace("B.", "(b)")
			k = k.replace("C.", "(c)")
			k = k.replace("D.", "(d)")
			
			stop = 1000
			step = 1000
					
			for n in range(1000):
				try:
					if f"{step}." in m:
						m = m.replace(f"{step}.", ".++")
						for_sol.append(str(step))
						
					step-=1
				except:
					pass
					
			m = m.split("++")
			m = m[1:]
			
			
			try:
				m[-1] = m[-1]+"."
			except:
				pass
			
			for_sol.reverse()
					
			
			for i in range(len(m)):
				try:
					dic[for_sol[i]] = m[i]
				except:
					pass
			
			
			for i in range(1600):
				try:
					#try:
	#					if int(k[0]):
	#						k = k.replace(k[0], "", 1)
	#				except:
	#					pass
					if f"{stop}." in k:
						for_qs.append(str(stop))
					k = k.replace(f"{stop}.", "   ", 1)
					stop -= 1
				except:
					break
			
			k = k.replace("INSTRUCTION", "   ¶")
			k = k.replace("Instruction", "   ¶")
			k = k.replace("instruction", "   ¶")
			
			j = k.split("   ")
			
			try:
				if j[-1] == "":
					j = j[:-1]
				if j[0] == "":
					j = j[1:]
			except IndexError as ie:
				pass
					
					
			for_qs.reverse()
	
			letit = False
					
			if 20>2:
				for m in j:
					self.ansgroup = []
							#try:
					#			rej = m.index("(")
					#			if m[rej+1].isalpha():
					#				m = m.split("(")
					#		except:
					#			pass
					m = m.split("(")
					self.mainq.append(m[0])
							
					for l in m:
						u = l.replace("a)", "a. ")
						u = u.replace("b)", "b. ")
						u = u.replace("c)", "c. ")
						u = u.replace("d)", "d. ")
								
						if letit == False:
							for ok in for_qs:
								if for_qs == []:
									break
								try:
									if dic[ok]:
										cor = dic[ok]
										cor = cor.strip()
										if cor in u and u[-1] != "*":
											u = u.replace(u, u+"*", 1)
											for_qs.remove(ok)
											letit = True
											break
										break
								except KeyError as ke:
									pass
						
						if "*" in u:
							u = u.replace("*", "")
							self.asterik.append(u)
						if "a. " in u or "b. " in u or "c. " in u or "d. " in u:
												
							self.ansgroup.append(u)
					self.mainans.append(self.ansgroup)
					letit = False
			
			
			#print(self.mainq)
#			print(self.mainans)
#			print(self.asterik)
			self.chooser = range(0, len(self.mainq))
			self.chooser = random.sample(self.chooser, len(self.chooser))
			self.manager.ids.result.Rasterik = self.asterik
			self.chooselet = True
		
		
		if self.manager.ids.sec.qu.text == "":
			num_q = len(self.mainq)
		else:
			num_q = int(self.manager.ids.sec.qu.text)
		
		
			
		if self.qnum >= num_q and prev != True or num_q > len(self.mainq) and prev != True:
			qu = "Sorry, you don't have the amount of questions you inputed"
			
			if self.qnum == num_q and len(self.mainq) != 0:
				qu = "You've ended the session\nWelldone!"
			self.ids.ans1.text = ""
			self.ids.ans2.text = ""
			self.ids.ans3.text = ""
			self.ids.ans4.text = ""
			self.ids.quest.text = qu
			self.through = True
			return False
		
		self.hold.append(self.qnum)

		if prev == True:
			
			if self.qnum > 0:
				self.qnum -= 2
			else:
				return False
			if self.qnum == -1:
				self.qnum = 0
				return False
		
		if self.manager.ids.sec.letshuffle.active == False:
			chooser = self.qnum
		else:
			chooser = self.chooser[self.qnum]
			
		qu = self.mainq[chooser]
		
		
		
		
		
		
		if max(self.hold) == self.qnum:
			self.manager.ids.result.Rmainq.append(qu)
		
		
		
		
		
		try:
			
			a1 = self.mainans[chooser][0]
		except:
			a1 = ""
		try:
			a2 = self.mainans[chooser][1]
		except:
			a2 = ""
		try:
			a3 = self.mainans[chooser][2]
		except:
			a3 = ""
		try:
			a4 = self.mainans[chooser][3]
		except:
			a4 = ""
			
		if "¶" in qu:
			a1 = ""
			a2 = ""
			a3 = ""
			a4 = ""
		
		#print(qu)
#		print(a1)
#		print(a2)
#		print(a3)
#		print(a4)
		
		
		try:
			if a1 == self.gans[self.qnum]:
				self.ids.ans1.text_color = 0, 1, 0, 1
			elif a2 == self.gans[self.qnum]:
				self.ids.ans2.text_color = 0, 1, 0, 1
			elif a3 == self.gans[self.qnum]:
				self.ids.ans3.text_color = 0, 1, 0, 1
			elif a4 == self.gans[self.qnum]:
				self.ids.ans4.text_color = 0, 1, 0, 1
		except:
			pass
		
		
	
		if max(self.hold) == self.qnum:
			send = [a1, a2, a3, a4]
			self.manager.ids.result.Rmainans.append(send)
			send = []
		
		self.qnum += 1
			
			
		
		
		self.ids.quest.text = qu
		self.ids.ans1.text = a1
		self.ids.ans2.text = a2
		self.ids.ans3.text = a3
		self.ids.ans4.text = a4
	
	def myinlog(self, tit, p, btext):
		self.dia1 = MDDialog(
		title = tit,
		text = p,
		size_hint = (.9, .4)
		)
		btn = MDFlatButton(
		text = btext,
		on_press = self.out
		)
		self.dia1.add_widget(btn)
		self.dia1.open()
		
	
	def cancelall(self):
		if self.ids.tcount.value == self.ids.tcount.max:
			self.manager.transition.direction = "right"
			self.manager.current = "sec"
			self.out2()
			return False
		if "Sorry, you don't have" in self.ids.quest.text or "You've ended the session" in self.ids.quest.text:
			self.manager.transition.direction = "right"
			self.manager.current = "sec"
			self.out2()
			return False
		tit = "Exit"
		p = "Click on                                   to exit\n\nYour current quiz won't be saved"
		btext = "leave"
		self.myinlog(tit, p, btext)
		

		
	def out(self, instance):
		self.manager.transition.direction = "right"
		self.manager.current = "sec"
		self.out2()
		self.dia1.dismiss()
	
	def out2(self):
		self.manager.ids.result.Rmainans = ()
		self.manager.ids.result.Rmainq = ()
		self.qstop = True
		self.chooselet = False
		self.qnum = 0
		self.questions = []
		self.mainq = []
		self.ansgroup = []
		self.mainans = []
		self.asterik = []
		self.gans = []
		self.hold = []
		self.manager.ids.result.Rasterik = []
		self.manager.ids.result.Rgans = []
		self.manager.ids.result.score = 0
		
		
	
	def corans(self, answer):
		self.ids.ans1.text_color = 0, 0, 0, 1
		self.ids.ans2.text_color = 0, 0, 0, 1
		self.ids.ans3.text_color = 0, 0, 0, 1
		self.ids.ans4.text_color = 0, 0, 0, 1
		
		if len(self.gans) != self.qnum-1: # and self.qnum != 0:
			for i in range((self.qnum-1)-(len(self.gans))):
				self.gans.append('')
		
		self.gans.append(answer.text)
		answer.text_color = 0, 1, 0, 1
	
			
		
		
		for p in self.gans:
			if p in self.mainans[self.chooser[self.qnum-1]] and p != self.gans[-1]:
				try:
					e = self.gans.index(p)
					self.gans.remove(p)
					
					
					self.gans.insert(e, self.gans[-1])
					self.gans.pop(-1)
					break
				except:
					pass
				
		
		
		
	def resultown(self):
		self.manager.ids.result.Rgans = self.gans
		self.manager.ids.result.startit()
	
		
class Newq(BoxLayout, Screen):
	def save1(self, info, subject, answers):
		mycon = sqlite3.connect("exam_base.db")
		c = mycon.cursor()
		with mycon:
			c.execute("INSERT INTO dquiz2 VALUES (?, ?, ?, ?, ?)", (subject.text, info.text, answers.text, None, None))
		mycon.close()
		
		tit = "Saved"
		p = "Your questions have been saved. Go to the subject sections to do them."
		mylog(tit, p)
	
	def warn(self):
		tit = "Warning"
		p = "Please fill in all inputs correctly and accurately so as to avoid mistakes in computer calculations and scoring."
		mylog(tit, p)
		

class Result(Screen):
	Rmainq = ListProperty()
	Rmainans = ListProperty()
	Rasterik = ListProperty()
	Rgans = ListProperty()
	score = NumericProperty(0)
	teller = 0
	questions_length = 0
	numbering = 0
	#def __init__(self, **kwargs):
#		super().__init__(**kwargs)
#		Clock.schedule_once(self.startit, 1)
	
	#def on_size(self, *args):
#		self.resultplace.size_hint_y = None
#		self.resultplace.height = self.minimum_height
		
		
	def startit(self):
		self.questions_length = len(self.Rmainq)
		for y in self.Rgans:
			if y in self.Rasterik:
				self.score += 1
		
		self.suu = BoxLayout(size_hint_y=.2)
		self.teller += 1
		self.tell = MDLabel(
		size_hint_x = 1,
		text = f"{self.manager.ids.quiz.subject.text} {self.teller}",
		font_size = dp(9),
		bold=True
		)
		
		for g in self.Rmainq:
			if "¶" in g:
				self.questions_length -= 1
		
		
		self.box = MDLabel(
		text = f"{self.score} out of {self.questions_length}",
		font_style = "H4",
		bold=True
		)
		
		self.suu.add_widget(self.tell)
		self.suu.add_widget(self.box)
		self.ids.resultplace.add_widget(self.suu)
		
		
		for i in range(len(self.Rmainq)):
			if not "¶" in self.Rmainq[i]:
				self.numbering += 1
			
			self.boxes = MDLabel(
			text = f"\n{self.numbering}.  {self.Rmainq[i]}" if not "¶" in self.Rmainq[i] else f"\n{self.Rmainq[i]}",
			size_hint_y=None,
			bold=True,
			font_style="Body1"
			
			)
			self.boxes1 = MDLabel(
			text = f"{self.Rmainans[i][0]}",
			size_hint_y=None,
			font_style="Body2")
			
			self.boxes2 = MDLabel(
			text = f"{self.Rmainans[i][1]}",
			size_hint_y=None,
			font_style="Body2"
			)
			self.boxes3 = MDLabel(
			text = f"{self.Rmainans[i][2]}",
			size_hint_y=None,
			font_style="Body2"
			)
			self.boxes4 = MDLabel(
			text = f"{self.Rmainans[i][3]}",
			size_hint_y=None,
			font_style="Body2"
			)
			
			
			for m in self.Rasterik:
				g = "blue"
				try:
					if m == self.Rmainans[i][0]:
						self.boxes1.theme_text_color = "Custom"
						self.boxes1.text_color = g	
				except:
					pass
				try:
					if m == self.Rmainans[i][1]:
						self.boxes2.theme_text_color = "Custom"
						self.boxes2.text_color = g	
				except:
					pass
				try:
					if m == self.Rmainans[i][2]:
						self.boxes3.theme_text_color = "Custom"
						self.boxes3.text_color = g
				except:
					pass
				try:
					if m == self.Rmainans[i][3]:
						self.boxes4.theme_text_color = "Custom"
						self.boxes4.text_color = g	
				except:
					pass
			
			for y in self.Rgans:
				if y in self.Rasterik:
					g = "green"
				elif not y in self.Rasterik:
					g = "red"
				if 10>2:
					try:
						if y == self.Rmainans[i][0]:
							self.boxes1.theme_text_color = "Custom"
							self.boxes1.text_color = g
					except:
						pass
					try:
						if y == self.Rmainans[i][1]:
							self.boxes2.theme_text_color = "Custom"
							self.boxes2.text_color = g
					except:
						pass
					try:
						if y == self.Rmainans[i][2]:
							self.boxes3.theme_text_color = "Custom"
							self.boxes3.text_color = g
					except:
						pass
					try:
						if y == self.Rmainans[i][3]:
							self.boxes4.theme_text_color = "Custom"
							self.boxes4.text_color = g
					except:
						pass	
		
			self.ids.resultplace.add_widget(self.boxes)
			self.ids.resultplace.add_widget(self.boxes1)
			self.ids.resultplace.add_widget(self.boxes2)
			self.ids.resultplace.add_widget(self.boxes3)
			self.ids.resultplace.add_widget(self.boxes4)
		
		
		
	def reset2(self):
		self.manager.ids.quiz.forend.cancel()
		self.manager.ids.quiz.fortchange.cancel()
		self.manager.ids.quiz.out2()
		self.questions_length = 0
		
## WHEN YOU ARE FREE, MAKE THE PAGE START FROM THE LAST QUIZ
## THAT THE PERSON DID
		
		
#subject text PRIMARY KEY,
#		subject, text
#		question text,
#		answer, text
#		score integer,
#		time integer


class Edit(BoxLayout, Screen):
	
	
	def requestion(self, tell):
		mycon = sqlite3.connect("exam_base.db")
		c = mycon.cursor()
			
		if tell == "request":
			with mycon:
				c.execute("SELECT * FROM dquiz2 WHERE subject = (?)", (self.ids.subb.text,))
				
				all = c.fetchall()
			mycon.close()
			
			try:
				for ip in range(len(all[0])):
					jjk = ip/2
					if ".0" in str(jjk):
						self.ids.ass.text += all[0][ip]+"\n\n\n"
					
					else:
						self.ids.qs.text += all[0][ip]+"\n\n\n"
			except:
				pass
				
			
		elif tell == "submit":
			questi = self.ids.qs.text.replace("\n", "")
			ans = self.ids.ass.text.replace("\n", "")
			
			with mycon:
				c.execute("DELETE FROM dquiz2 WHERE subject = (?)", (self.ids.subb.text,))
				
				c.execute("INSERT INTO dquiz2 VALUES (?, ?, ?, ?, ?)", (self.ids.subb.text, questi, ans, None, None))
			
			mycon.close()
			tit = "Saved"
			p = "Your edited questions have been saved."
			mylog(tit, p)


class Man(ScreenManager):
	pass


def mylog(tit, p):
	dia1 = MDDialog(
	title = tit,
	text = p,
	size_hint = (.9, .4)
	)
	#btn = MDFlatButton(
#	text = btext
#	)
	#dia1.add_widget(btn)
	dia1.open()
	

kv = ('''
#: import Factory kivy.factory.Factory


Man:
	Mimi:
		id: mimi
	Sec:
		id: sec
	Quiz:
		id: quiz
	Newq:
		id: newq
	Result:
		id: result
	Edit:
		id: edit
		
	
	
<Edit>:
	name: "edit"
	orientation: "vertical"
	padding: "10dp"
	
	MDIconButton:
		icon: "arrow-left"
		on_release:
			app.root.current = "main"
			app.root.transition.direction = "right"
	
	ScrollView:
		BoxLayout:
			orientation: "vertical"
			spacing: "20dp"
			size_hint_y: None
			height: self.minimum_height
			
			MDRoundFlatButton:
				text: "Get"
				pos_hint: {"center_x": .5}
				on_release:
					qs.text = ""
					ass.text = ""
					root.requestion("request")
					
			
			TextInput:
				id: subb
				size_hint_y: None
				height: "20dp"
				
				
			TextInput:
				id: qs
				size_hint_y: None
				height: "600dp"
				#text: "CRS"
				
			MDSeparator:
				color: "black"
				
			TextInput:
				id: ass
				size_hint_y: None
				height: "600dp"
			MDRoundFlatButton:
				text: "Submit"
				pos_hint: {"center_x": .5}
				on_release:
					root.requestion("submit")
	

<Result>:
	name: "result"
	
	
	ScrollView:
		id: scroll
		BoxLayout:
			id: resultplace
			orientation: "vertical"
			padding: "19dp", "44dp"
			size_hint_y: None
			height: self.minimum_height

	
	MDIconButton:
		id: btn
		pos_hint: {"top": 1}
		icon: "arrow-left"
		on_release:
			root.reset2()
			app.root.current = "main"
			app.root.transition.direction = "right"
	
			
			
			
			
	
	


<Sec>:
	name: "sec"
	orientation: "vertical"
	time: time
	qu: qu
	diff: diff
	letshuffle: letshuffle
	
	padding: "20dp"
	spacing: "30dp"
	
	MDIconButton:
		icon: "arrow-left"
		on_release:
			app.root.current = "main"
			app.root.transition.direction = "right"
			time.text = ""
			qu.text = ""
			
	MDLabel:
		text: "Hiya, there"
		bold: True
		halign: "center"
		size_hint_y: None
		height: self.texture_size[1]
	BoxLayout:
		spacing: "10dp"
		size_hint_y: .1
		MDLabel:
			text: "Time"
			size_hint_x: .4
		TextInput:
			id: time
			multiline: False
			
	BoxLayout:
		spacing: "10dp"
		size_hint_y: .1
		MDLabel:
			text: "Questions"
			size_hint_x: .4
		TextInput:
			id: qu
			multiline: False
	
	BoxLayout:
		spacing: "10dp"
		size_hint_y: .1
		MDLabel:
			text: "Difficulty:"
			size_hint_x: .4
		BoxLayout:
			id: diff
			spacing: "15dp"
			BoxLayout:
				size_hint_x: .25
				spacing: "-14dp"
				MDLabel:
					text: "Easy"
					#size_hint_x: .5
					font_size: "10dp"
				MDCheckbox:
					#size_hint_x: .5
					group: "cult"
					on_active:
						root.difficulty("Easy")
			BoxLayout:
				size_hint_x: .35
				spacing: "-10dp"
				MDLabel:
					text: "Medium"
					size_hint_x: .5
					font_size: "10dp"
				MDCheckbox:
					size_hint_x: .5
					group: "cult"
					on_active:
						root.difficulty("Medium")
			BoxLayout:
				size_hint_x: .25
				spacing: "-17dp"
				MDLabel:
					text: "Hard"
					size_hint_x: .5
					font_size: "10dp"
				MDCheckbox:
					size_hint_x: .5
					group: "cult"
					on_active:
						root.difficulty("Hard")
				
	BoxLayout:
		size_hint: .4, .08
		MDLabel:
			text: "Shuffle Off" if letshuffle.active == False else "Shuffle On"
			
		MDCheckbox:
			id: letshuffle
			opacity: 6
			size_hint_x: None
			
	MDFillRoundFlatButton:
		text: "Start Quiz"
		font_size: "35dp"
		pos_hint: {"center_x": .5, "center_y": .5}
		on_release:
			root.thing(time.text, qu.text)
			
	ScrollView:

	

<Quiz>:
	subject: subject
	tcount: tcount
	culty: culty
	orientation: "vertical"
	name: "quiz"
	padding: "20dp"
	spacing: "10dp"
	
	BoxLayout:
		size_hint_y: .2
		MDIconButton:
			icon: "arrow-left"
			on_release:
				root.cancelall()
				
	RelativeLayout:
		size_hint_y: .001
		MDLabel:
			pos_hint: {"x": .74, "y": 1}
			id: culty
			text: "David"
			bold: True
			font_style: "H5"
			size_hint_y: None
			height: self.texture_size[1]
		
	MDLabel:
		markup: True
		id: subject
		text: "[b][u][/b][/u]"
		font_style: "H6"
		font_size: "41dp"
		halign: "center"
		size_hint_y: None
		height: self.texture_size[1]
	BoxLayout:
		orientation: "vertical"
		size_hint_y: .1
		MDLabel:
			text: "Time left: " + str(tcount.max-tcount.value)
			halign: "center"
			size_hint_y: None
			height: self.texture_size[1]
		
			
		MDProgressBar:
			id: tcount
			size_hint_y: .1
			min: 0
			max: 0
			value: 0
			

		
	BoxLayout:
		size_hint_y: 5.3
		orientation: "vertical"
			
		spacing: "10dp"
		MDLabel:
			id: quest
			text: "Hello there"
			halign: "center"
			font_style: "H4"
			font_size: "30dp"
		
		BoxLayout:
			id: anspace
			orientation: "vertical"
			
			MDList:
				OneLineListItem:
				#MDFlatButton:
					id: ans1
					theme_text_color: "Custom"
					text: "a.   Select here if it is correct"
					on_press:
						root.corans(self)
						
					
				OneLineListItem:
				#MDFlatButton:
					id: ans2
					theme_text_color: "Custom"
					text: "b.   Select here if you think otherwise"
					on_press:
						root.corans(self)
						
				OneLineListItem:
				#MDFlatButton:
					id: ans3
					theme_text_color: "Custom"
					text: "c.   This might also be your choice"
					on_press:
						root.corans(self)
						
				OneLineListItem:
				#MDFlatButton:
					id: ans4
					theme_text_color: "Custom"
					text: "d.   Never forget the last"
					on_press:
						root.corans(self)
					
	BoxLayout:
		
		AnchorLayout:
			anchor_x: "left"
			
			MDFlatButton:
				text: "Previous Question"
				on_press:
					root.dilog(True)
		
		AnchorLayout:
			anchor_x: "right"
			MDFlatButton:
				text: "NextQuestion"
				on_press:
					root.dilog(False)
					
						
	ScrollView:
	
	BoxLayout:
		AnchorLayout:
			anchor_x: "right"
			MDTextButton:
				text: "Go to results>>"
				on_release:
					root.resultown()
					app.root.current = "result"
					app.root.transition.direction = "left"
		
		
		
		
		
		
<Newq>:
	name: "newq"
	orientation: "vertical"
	padding: "20dp"
	spacing: "5dp"
	
	MDIconButton:
		size_hint_y: None
		height: "5dp"
		icon: "arrow-left"
		on_release:
			app.root.current = "main"
			app.root.transition.direction = "right"
	
	#BoxLayout:
		#size_hint_y: .03
	#MDLabel:
#		text: "Subject: "
#		size_hint_x: .3
#		size_hint_y: None
#		height: self.texture_size[1]
	


	RelativeLayout:
		size_hint_y: .1
		pos_hint: {"x": .5, "y": 2}
		Widget:
			
			#size_hint_y: .1
		
		    # trick to not lost the Dropdown instance
		    # Dropdown itself is not really made to be used in kv.
		    __safe_id: [dropdown.__self__]
		
		    Button:
		        id: dsubject
		        background_normal: "white"
		        color: "black"
		        markup: True
		        text: "[b]Pick subject[/b]"
		        on_release: dropdown.open(self)
		        
		        size_hint: None, None
		        width: "190dp"
		        height: "30dp"
		
		    Widget:
		        on_parent: dropdown.dismiss()
		
		    DropDown:
		
		        id: dropdown
		        on_select: dsubject.text = '{}'.format(args[1])
				
		        
				MDFillRoundFlatButton:
					text: "Maths"
					on_release: dropdown.select(self.text)
					
				MDFillRoundFlatButton:
					text: "English"
					on_release: dropdown.select(self.text)
					
				MDFillRoundFlatButton:
					text: "Basic Science"
					on_release: dropdown.select(self.text)
					
				MDFillRoundFlatButton:
					text: "CRS"
					on_release: dropdown.select(self.text)
					
				MDFillRoundFlatButton:
					text: "Security Education"
					on_release: dropdown.select(self.text)
					
				MDFillRoundFlatButton:
					text: "Agric"
					on_release: dropdown.select(self.text)
					
				MDFillRoundFlatButton:
					text: "Yoruba"
					on_release: dropdown.select(self.text)
					
				MDFillRoundFlatButton:
					text: "Business Studies"
					on_release: dropdown.select(self.text)
					
				MDFillRoundFlatButton:
					text: "Computer Studies"
					on_release: dropdown.select(self.text)
					
				MDFillRoundFlatButton:
					text: "French"
					on_release: dropdown.select(self.text)
					
				MDFillRoundFlatButton:
					text: "IRS"
					on_release: dropdown.select(self.text)
					
				MDFillRoundFlatButton:
					text: "Civic education"
					on_release: dropdown.select(self.text)
					
				MDFillRoundFlatButton:
					text: "Home economics"
					on_release: dropdown.select(self.text)
					
				MDFillRoundFlatButton:
					text: "PHE"
					on_release: dropdown.select(self.text)
					
				MDFillRoundFlatButton:
					text: "social studies"
					on_release: dropdown.select(self.text)
					
				MDFillRoundFlatButton:
					text: "Basic Technology"
					on_release: dropdown.select(self.text)
					
				MDFillRoundFlatButton:
					text: "CCA"
					on_release: dropdown.select(self.text)
					
		
		
	
	MDLabel:
		text: "Input Questions here"
		size_hint_y: None
		height: self.texture_size[1]
		halign: "center"
		font_style: "Caption"
	MDSeparator:
		color: "black"
		
	TextInput:
		id: qq
	
	MDLabel:
		text: "Input Answers here"
		size_hint_y: None
		height: self.texture_size[1]
		halign: "center"
		font_style: "Caption"
	MDLabel:
		text: "Make sure to input the same number of questions and answers"
		size_hint_y: None
		height: self.texture_size[1]
		halign: "center"
		font_size: "10dp"
		theme_text_color: "Hint"
	
	MDSeparator:
		color: "black"
		
	TextInput:
		id: solsol
	
	MDFlatButton:
		text: "Submit question"
		pos_hint: {"center_x": .5}
		on_release:
			root.save1(qq, dsubject, solsol) if qq.text != "" and dsubject.text != "" and solsol.text != "" else root.warn()

	
	
<Mimi>:
	name: "main"
	orientation: "lr-tb"
	padding: "20dp"
	spacing: "20dp"
	
	
	MDRectangleFlatButton:
		id: mat
		text: "Maths"
		on_release:
			root.sub(self)
			app.root.current = "sec"
			app.root.transition.direction = "left"
			
		
	MDRectangleFlatButton:
		id: eng
		text: "English"
		on_release:
			root.sub(self)
			app.root.current = "sec"
			app.root.transition.direction = "left"
			
	MDRectangleFlatButton:
		id: sci
		text: "Basic Science"
		on_release:
			root.sub(self)
			app.root.current = "sec"
			app.root.transition.direction = "left"
			
	MDRectangleFlatButton:
		id: crs
		text: "CRS"
		on_release:
			root.sub(self)
			app.root.current = "sec"
			app.root.transition.direction = "left"
	
	MDRectangleFlatButton:
		id: security
		text: "Security Education"
		on_release:
			root.sub(self)
			app.root.current = "sec"
			app.root.transition.direction = "left"
			
	MDRectangleFlatButton:
		id: agric
		text: "Agric"
		on_release:
			root.sub(self)
			app.root.current = "sec"
			app.root.transition.direction = "left"
			
	MDRectangleFlatButton:
		id: yor
		text: "Yoruba"
		on_release:
			root.sub(self)
			app.root.current = "sec"
			app.root.transition.direction = "left"
			
	MDRectangleFlatButton:
		id: bus
		text: "Business Studies"
		on_release:
			root.sub(self)
			app.root.current = "sec"
			app.root.transition.direction = "left"
			
	MDRectangleFlatButton:
		id: comp
		text: "Computer Studies"
		on_release:
			root.sub(self)
			app.root.current = "sec"
			app.root.transition.direction = "left"
			
	MDRectangleFlatButton:
		id: french
		text: "French"
		on_release:
			root.sub(self)
			app.root.current = "sec"
			app.root.transition.direction = "left"
			
	MDRectangleFlatButton:
		id: irs
		text: "IRS"
		on_release:
			root.sub(self)
			app.root.current = "sec"
			app.root.transition.direction = "left"
	
	MDRectangleFlatButton:
		id: civic
		text: "Civic education"
		on_release:
			root.sub(self)
			app.root.current = "sec"
			app.root.transition.direction = "left"
	
	MDRectangleFlatButton:
		id: hom
		text: "Home economics"
		on_release:
			root.sub(self)
			app.root.current = "sec"
			app.root.transition.direction = "left"
	
	MDRectangleFlatButton:
		id: phe
		text: "PHE"
		on_release:
			root.sub(self)
			app.root.current = "sec"
			app.root.transition.direction = "left"
	
	MDRectangleFlatButton:
		id: soc
		text: "social studies"
		on_release:
			root.sub(self)
			app.root.current = "sec"
			app.root.transition.direction = "left"
	
	MDRectangleFlatButton:
		id: btech
		text: "Basic Technology"
		on_release:
			root.sub(self)
			app.root.current = "sec"
			app.root.transition.direction = "left"
			
	MDRectangleFlatButton:
		id: cca
		text: "CCA"
		on_release:
			root.sub(self)
			app.root.current = "sec"
			app.root.transition.direction = "left"
	
	
	StackLayout:
		orientation: "tb-rl"
		MDFlatButton:
			text: "Edit questions"
			on_release:
				app.root.current = "edit"
			
	Widget:
		MDFlatButton:
			text: "Enter exam questions"
			on_release:
				app.root.current = "newq"





''')





	

class myTiles(MDApp):
	def build(self):
		mycon = sqlite3.connect("exam_base.db")
		c = mycon.cursor()
		c.execute(''' CREATE TABLE IF NOT EXISTS dquiz2(
		subject text,
		question text,
		answers text,
		score text,
		time integer
		)
		''')
		mycon.commit()
		mycon.close()
		
		self.theme_cls.primary_palette = "Purple"
		pig = Builder.load_string(kv)
		return pig
	
	
	
	
myTiles().run()