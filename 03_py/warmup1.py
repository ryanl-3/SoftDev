def sleep_in(weekday, vacation):
  return not weekday or vacation

'''
Expected	Run		
sleep_in(False, False) → True	True	OK	
sleep_in(True, False) → False	False	OK	
sleep_in(False, True) → True	True	OK	
sleep_in(True, True) → True	True	OK
'''


def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

'''
Expected	Run		
monkey_trouble(True, True) → True	True	OK	
monkey_trouble(False, False) → True	True	OK	
monkey_trouble(True, False) → False	False	OK	
monkey_trouble(False, True) → False	False	OK
'''


def sum_double(a, b):
  if a == b:
    return 2 * (a + b)
  return a + b

'''
Expected	Run		
sum_double(1, 2) → 3	3	OK	
sum_double(3, 2) → 5	5	OK	
sum_double(2, 2) → 8	8	OK	
sum_double(-1, 0) → -1	-1	OK	
sum_double(3, 3) → 12	12	OK	
sum_double(0, 0) → 0	0	OK	
sum_double(0, 1) → 1	1	OK	
sum_double(3, 4) → 7	7	OK
'''

def diff21(n):
  if n >= 21:
    return 2 * (n - 21)
  return 21 - n

'''
Expected	Run		
diff21(19) → 2	2	OK	
diff21(10) → 11	11	OK	
diff21(21) → 0	0	OK	
diff21(22) → 2	2	OK	
diff21(25) → 8	8	OK	
diff21(30) → 18	18	OK	
diff21(0) → 21	21	OK	
diff21(1) → 20	20	OK	
diff21(2) → 19	19	OK	
diff21(-1) → 22	22	OK	
diff21(-2) → 23	23	OK	
diff21(50) → 58	58	OK
'''


def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

'''
Expected	Run		
parrot_trouble(True, 6) → True	True	OK	
parrot_trouble(True, 7) → False	False	OK	
parrot_trouble(False, 6) → False	False	OK	
parrot_trouble(True, 21) → True	True	OK	
parrot_trouble(False, 21) → False	False	OK	
parrot_trouble(False, 20) → False	False	OK	
parrot_trouble(True, 23) → True	True	OK	
parrot_trouble(False, 23) → False	False	OK	
parrot_trouble(True, 20) → False	False	OK	
parrot_trouble(False, 12) → False	False	OK
'''


def makes10(a, b):
  if a + b == 10:
    return True
  if a == 10 or b == 10:
    return True;
  return False;

'''
Expected	Run		
makes10(9, 10) → True	True	OK	
makes10(9, 9) → False	False	OK	
makes10(1, 9) → True	True	OK	
makes10(10, 1) → True	True	OK	
makes10(10, 10) → True	True	OK	
makes10(8, 2) → True	True	OK	
makes10(8, 3) → False	False	OK	
makes10(10, 42) → True	True	OK	
makes10(12, -2) → True	True	OK
'''


def near_hundred(n):
  return abs(100 - n) <= 10 or abs(200-n) <= 10

'''
Expected	Run		
near_hundred(93) → True	True	OK	
near_hundred(90) → True	True	OK	
near_hundred(89) → False	False	OK	
near_hundred(110) → True	True	OK	
near_hundred(111) → False	False	OK	
near_hundred(121) → False	False	OK	
near_hundred(-101) → False	False	OK	
near_hundred(-209) → False	False	OK	
near_hundred(190) → True	True	OK	
near_hundred(209) → True	True	OK	
near_hundred(0) → False	False	OK	
near_hundred(5) → False	False	OK	
near_hundred(-50) → False	False	OK	
near_hundred(191) → True	True	OK	
near_hundred(189) → False	False	OK	
near_hundred(200) → True	True	OK	
near_hundred(210) → True	True	OK	
near_hundred(211) → False	False	OK	
near_hundred(290) → False	False	OK
'''



def pos_neg(a, b, negative):
  if not negative and a * b < 0:
    return True
  if negative and a < 0 and b < 0:
    return True
  return False

'''
Expected	Run		
pos_neg(1, -1, False) → True	True	OK	
pos_neg(-1, 1, False) → True	True	OK	
pos_neg(-4, -5, True) → True	True	OK	
pos_neg(-4, -5, False) → False	False	OK	
pos_neg(-4, 5, False) → True	True	OK	
pos_neg(-4, 5, True) → False	False	OK	
pos_neg(1, 1, False) → False	False	OK	
pos_neg(-1, -1, False) → False	False	OK	
pos_neg(1, -1, True) → False	False	OK	
pos_neg(-1, 1, True) → False	False	OK	
pos_neg(1, 1, True) → False	False	OK	
pos_neg(-1, -1, True) → True	True	OK	
pos_neg(5, -5, False) → True	True	OK	
pos_neg(-6, 6, False) → True	True	OK	
pos_neg(-5, -6, False) → False	False	OK	
pos_neg(-2, -1, False) → False	False	OK	
pos_neg(1, 2, False) → False	False	OK	
pos_neg(-5, 6, True) → False	False	OK	
pos_neg(-5, -5, True) → True	True	OK	
'''

def not_string(str):
  if str[:3] == "not":
    return str
  return "not " + str


'''
Expected	Run		
not_string('candy') → 'not candy'	'not candy'	OK	
not_string('x') → 'not x'	'not x'	OK	
not_string('not bad') → 'not bad'	'not bad'	OK	
not_string('bad') → 'not bad'	'not bad'	OK	
not_string('not') → 'not'	'not'	OK	
not_string('is not') → 'not is not'	'not is not'	OK	
not_string('no') → 'not no'	'not no'	OK
'''

def front_back(str):
  if (len(str) > 1):
    new_str = str[-1:] + str[1:len(str) - 1] + str[0:1]
    return new_str
  return str




def front3(str):
  return str[:3]*3
