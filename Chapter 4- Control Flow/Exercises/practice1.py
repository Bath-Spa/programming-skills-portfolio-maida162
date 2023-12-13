
lang=input("what's the programming language you want to learn?")
match lang:
   case "java script":
      print("you can become a web developer")

   case "python":
      print("you can become data scientist")

   case "PHP":
      print("you can become a backened developer")
    
   case "solidity":
      print("you can become backchain developer")

   case "java":
      print("you can become a mobile app developer")

   case _:
      print("the language doesn't matter, what matters is solving problems")       
