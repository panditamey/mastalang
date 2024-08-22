# MastaLang

<a href="https://mastalang.vercel.app"><img alt="Build" src="https://img.shields.io/badge/website-mastalang.vercel.app-blue"/></a>

**Masta(मस्त)Lang** is a Marath-Moli, Easy Pseudo Language that interprets Marathi-English Code with ease made in Python.

## Overview

MastaLang is a fun project of Marath-Moli (मराठमोळी), Easy Pseudo Language that interprets Marathi-English Code with ease. Source code of interpreter is written in Python.

## Features

- **Simple Marathi-English Syntax**: Write code using Marathi-English constructs.
- **Code Interpretation**: The language interprets code with ease, making it straightforward to see results.
- **Interactive Playground**: Test and run your MastaLang code directly in a web-based playground.

## Key Constructs

- **Comments**: Use `Ignore Maar` to write comments in your code.
- **Print Statements**: Use `Bol` to output values.
- **Variable Initialization**: Initialize variables using `He Bagh <name> mhanje <value>`.
- **Arithmetic Operations**: Perform arithmetic using keywords like `adhik` (addition), `vaja` (subtraction), `guna` (multiplication), and `bhag` (division).
- **Conditional Statements**: Use `Jar` for if statements, `Nahi Tar` for else, and `Sod` to end the conditional block.
- **Loop Statements**: Loop with `Chal` and `Te`, and end loops with `Sod`.

## Examples

### Comments

```plaintext
Ignore Maar Comments can be written in the form of Ignore Maar
```

### Print Statement

```plaintext
Bol "Namaskar Mandali"
```

### Horizontal Line

```plaintext
Line Maar
```

### Variable Initialization

```plaintext
Ignore Maar Initialize the sum variable
He Bagh sum mhanje 10
```

### Arithmetic Operations

```plaintext
Ignore Maar Arithmetic operations

He Bagh a mhanje 20 adhik 10
Bol a

He Bagh b mhanje 20 vaja 10
Bol b

He Bagh c mhanje 20 guna 10
Bol c

He Bagh d mhanje 20 bhag 10
Bol d
```

### Conditional Statements

```plaintext
Ignore Maar Conditional Example

He Bagh x mhanje 7

Jar x > 5
    Bol "x motha ahe"
Nahi Tar
    Bol "x chota ahe"
Sod
```

### Loop Statements

```plaintext
Ignore Maar Initialize the sum variable
He Bagh sum mhanje 0

Line Maar
Line Maar

Ignore Maar Loop from 1 to 5
He Bagh i mhanje 1
Chal i 1 Te 5
    He Bagh sum mhanje sum adhik i
    Bol "Value i chi ahe :"
    Bol i
    He Bagh i mhanje i adhik 1
Sod

Ignore Maar Print the final result
Bol "Final Sum ahe :"
Bol sum
Line Maar
Line Maar

Ignore Maar End of program
Parat 0
```
