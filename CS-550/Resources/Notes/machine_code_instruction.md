# Machine Code Instruction

Machine code instruction usually consists of operation code and operand. All operation codes and operand written in binary. Machine code program consists of sequence of Op Codes and operands stored in the computers memory (RAM).
- Operation Code: (Op Code)
- Operand:

```assembly
LD A, 01H
```
LD - Load
A - Register A (inside CPU)
01 - Number loaded into A
H - Hexadecimal 

Assembler: Converts assembly into machine code

```machine code
00111110 00000001
// {Op Code}{Operand}
3E 01 
// Hexadecimal
``` 

Immediate Addressing: Data to be manipulated byt he instruction comes immediately after the Op Code.

Inc: increment 

Implied Addressing: implied the data to be manipulated by instruction is already in place. No operand needed. 