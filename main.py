def gate_and(input1, input2):
  ''' an AND gate (input1 ^ input2)'''
  gate1 = input1 and input2
  return bool(gate1)

def gate_or(input1, input2):
  '''an OR gate (input1 v input2)'''
  gate1 = input1 or input2
  return bool(gate1)

def gate_xor(input1, input2):
  '''a XOR gate ( (input1 ^ -input2) v (-input1 ^ input2))'''
  gate1 = input1 and not input2
  gate2 = input2 and not input1
  return bool(gate1 or gate2)

def gate_nand(input1, input2):
  '''a NAND gate (-(input1 ^ input2)) '''
  gate1 = not(input1 and input2)
  return bool(gate1)

def gate_nor(input1, input2):
  '''a NOR gate (-(input1 v input2)) '''
  gate1 = not(input1 or input2)
  return bool(gate1)

def gate_not(input1):
  '''a NOT gate (-input1)'''
  return bool(not input1)

print("Truth Table for (A ∧ ¬(B ∧ C)")
print("By Mitchell Kealy\n")
print("A\t B\t C\t OUTPUT") #header
print("F\t F\t F\t", False and gate_nand(False, False)) #gate_nand returns false with inputs (f, f, f)
print("F\t F\t T\t", False and gate_nand(False, True)) #gate_nand returns false with inputs (f, f, t)
print("F\t T\t F\t", False and gate_nand(True, False)) #gate_nand returns false with inputs (f, t, f)
print("F\t T\t T\t", False and gate_nand(True, True)) #gate_nand returns false with inputs (f, t, t)
print("T\t F\t F\t", True and gate_nand(False, False)) #gate_nand returns true with inputs (t, f, f)
print("T\t F\t T\t", True and gate_nand(False, True)) #gate_nand returns true with inputs (t, f, t)
print("T\t T\t F\t", True and gate_nand(True, False)) #gate_nand returns true with inputs (t, t, f)
print("T\t T\t T\t", True and gate_nand(True, True)) #gate_nand returns false with inputs (f, f, f)