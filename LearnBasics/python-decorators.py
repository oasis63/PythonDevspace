def upper(f):
  def w():
    return f().upper()
  return w

def exclaim(f):
  def w():
    return f() + "!"
  return w

@upper
@exclaim
def say():
  return "hi"

print(say())