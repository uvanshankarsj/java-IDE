import os
class java:
    def __init__(self):
        self.file=open("text.java","w")
        
    def run(self):
        self.file.close()
        os.system("""java text.java""")
        
    def usercode(self):
        lines=""
        con=True
        while con:
            inp=input()
            if inp=="":
                con=False
            else:
                lines+=inp+"\n"
        self.file.write(lines)
        
    def predefinedcode(self):
        lines="""class HelloWorld { 
        	public static void main(String args[]) 
        	{ 
        		System.out.println("Hello, World"); 
        	} 
        }"""
        self.file.write(lines)


j=java()
print("""1-check if java is installed
2-IDE for java""")
repeat=True
while repeat:
    choice=input()
    match int(choice):
            case 1:
                j.predefinedcode()                            
                j.run()
                repeat=False
            case 2:
                j.usercode()
                j.run()
                repeat=False
            case default:
                print("invalid choice")
    
