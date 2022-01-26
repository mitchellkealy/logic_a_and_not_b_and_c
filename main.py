def gate_nand(input1, input2):
  '''a NAND gate (-(input1 ^ input2)) '''
  gate1 = not(input1 and input2)
  return bool(gate1)

def gate_and(input1, input2):
  '''an AND gate(input 1 ^ input2)'''
  gate1 = (input1 and input2)
  return bool(gate1)

def gate_and_nand(input1, input2, input3):
  '''an AND gate with NAND gate'''
  gate1 = gate_nand(input2, input3)
  gate2 = gate_and(input1, gate1)
  return bool(gate2)

print("Truth Table for (A ∧ ¬(B ∧ C)")
print("By Mitchell Kealy\n")
print("A\t B\t C\t OUTPUT") #header
print("F\t F\t F\t", gate_and_nand(False, False, False)) #gate_and_nand returns false with inputs (f, f, f)
print("F\t F\t T\t", gate_and_nand(False, False, True)) #gate_and_nand returns false with inputs (f, f, t)
print("F\t T\t F\t", gate_and_nand(False, True, False)) #gate_and_nand returns false with inputs (f, t, f)
print("F\t T\t T\t", gate_and_nand(False, True, True)) #gate_and_nand returns false with inputs (f, t, t)
print("T\t F\t F\t", gate_and_nand(True, False, False)) #gate_and_nand returns true with inputs (t, f, f)
print("T\t F\t T\t", gate_and_nand(True, False, True)) #gate_and_nand returns true with inputs (t, f, t)
print("T\t T\t F\t", gate_and_nand(True, True, False)) #gate_and_nand returns true with inputs (t, t, f)
print("T\t T\t T\t", gate_and_nand(True, True, True)) #gate_and_nand returns false with inputs (f, f, f)