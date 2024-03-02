class Myediter :
	def execute(self):
		print("Compiling")
		print("Running")

class Vscode:
	def execute(self):
		print("spell check")
		print("convention check")
		print("Compiling")
		print("Running")




class laptop:
	def code(self , ide):
		ide.execute()


ide = Myediter()
ide2 = Vscode()
lap1 = laptop()
lap1.code(ide2)


# This is what the polymorphism is