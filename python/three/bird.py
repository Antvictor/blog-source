class Bird:
      def __init__(self,  wings, feather):
          self.wings = wings
          self.feather = feather
      def fly(self):
          print(f"this bird use {self.wings} fly and it has {self.feather}")

class Penguin(Bird) :

  def run(self):
    print(f"yes, I`m run")

  def fly(self):   
    print(f"I`m Penguin, I`m can`t fly, I just glide")
    
  def fly(self, cry):
    print(f"I`m Penguin, {cry}, I`m gliding")