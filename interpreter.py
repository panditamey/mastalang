class MarathiScriptInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.output = []

    def execute(self, code):
        lines = code.splitlines()
        i = 0
        while i < len(lines):
            try:
                line = lines[i].strip()
                if not line or line.startswith('Ignore Maar'):
                    i += 1
                    continue

                if line.startswith('Kaam Kar'):
                    func_name = line.split(' ')[2]
                    body = self._extract_block(lines, i + 1)
                    self.functions[func_name] = body
                    i += len(body) + 2 #not sure
                elif line.startswith('He Bagh'):
                    var_name, expression = self._parse_assignment(line)
                    self.variables[var_name] = self._evaluate_expression(expression)
                elif line.startswith('Bol'):
                    message = line.split(' ', 1)[1].strip('"')
                    if message in self.variables:
                        self.output.append(str(self.variables[message]))
                    else:
                        self.output.append(message)
                elif line.startswith('Line Maar'):
                    self.output.append('--------------------------------------------')
                elif line.startswith('Jar'):
                    condition = self._parse_condition(line)
                    # print(f"Condition evaluated: {condition}")  # Debugging output
                    if condition:
                        i += 1
                        while i < len(lines) and not lines[i].strip().startswith('Nahi Tar') and not lines[i].strip().startswith('Sod'):
                            self.execute(lines[i])  # Execute each line in the true block
                            i += 1
                        # Skip lines until 'Sod' after executing the true block
                        while i < len(lines) and not lines[i].strip().startswith('Sod'):
                            i += 1
                    else:
                        # Skip lines until 'Nahi Tar' or 'Sod' if the condition is false
                        while i < len(lines) and not lines[i].strip().startswith('Nahi Tar') and not lines[i].strip().startswith('Sod'):
                            i += 1
                        if i < len(lines) and lines[i].strip().startswith('Nahi Tar'):
                            i += 1
                            while i < len(lines) and not lines[i].strip().startswith('Sod'):
                                self.execute(lines[i])   # Execute each line in the false block
                                i += 1
                    # Skip the 'Sod' line to continue execution correctly
                    if i < len(lines) and lines[i].strip().startswith('Sod'):
                        i += 1
                elif line.startswith('Chal'):
                    loop_vars = self._parse_loop(line)
                    block_lines = self._extract_block(lines, i + 1)
                    for j in range(loop_vars['start'], loop_vars['end'] + 1):
                        self.variables[loop_vars['var']] = j
                        self.execute_block(block_lines)
                    i += len(block_lines) + 1
                elif line.startswith('Loop Laav'):
                    # Handle while loop (if needed)
                    pass
                elif line.startswith('Karya Karo'):
                    func_name = line.split(' ')[2]
                    if func_name in self.functions:
                        for func_line in self.functions[func_name]:
                            self.execute_line(func_line.strip())
                elif line.startswith('Parat'):
                    return
                elif line.startswith('Sod'):
                    return

                i += 1
            except Exception :
                raise Exception("Baba chukicha kelais neat kar")

    def _extract_block(self, lines, start_index):
        block = []
        i = start_index
        while i < len(lines) and not lines[i].strip().startswith('Sod'):
            block.append(lines[i].strip())
            i += 1
        return block

    def _parse_assignment(self, line):
        # Expect format: He Bagh var mhanje expression
        parts = line.split(' ')
        var_name = parts[2]
        expression = ' '.join(parts[4:])
        return var_name, expression

    def _evaluate_expression(self, expression):
        # Replace Marathi operators with Python operators
        expression = expression.replace('adhik', '+')
        expression = expression.replace('vaja', '-')
        expression = expression.replace('guna', '*')
        expression = expression.replace('bhag', '/')
        
        # Debug: Print the expression being evaluated
        # print(f"Evaluating expression: {expression}")
        
        # Evaluate the expression
        try:
            return eval(expression, {}, self.variables)
        except Exception as e:
            raise Exception("Baba chukicha kelais neat kar ")
            return 0

    def _parse_condition(self, line):
        parts = line.split(' ')
        var_name = parts[1]
        operator = parts[2]
        value = int(parts[3])
        if var_name in self.variables:
            if operator == '>':
                return self.variables[var_name] > value
            elif operator == '<':
                return self.variables[var_name] < value
            elif operator == '==':
                return self.variables[var_name] == value
        return False

    def _parse_loop(self, line):
        # Correctly parse the loop line
        parts = line.split(' ')
        var_name = parts[1]
        start = int(parts[2])
        end = int(parts[4])  # Corrected to handle 'Te' keyword and extract end value
        return {'var': var_name, 'start': start, 'end': end}

    def execute_line(self, line):
        if line.startswith('Bol'):
            message = line.split(' ', 1)[1].strip('"')
            if message in self.variables:
                self.output.append(str(self.variables[message]))
            else:
                self.output.append(message)
        elif line.startswith('He Bagh'):
            var_name, expression = self._parse_assignment(line)
            self.variables[var_name] = self._evaluate_expression(expression)
        elif line.startswith('Chal'):
            loop_vars = self._parse_loop(line)
            block_lines = self._extract_block(lines, i + 1)
            for j in range(loop_vars['start'], loop_vars['end'] + 1):
                self.variables[loop_vars['var']] = j
                self.execute_block(block_lines)
        # Implement other line types as needed

    def execute_block(self, block_lines):
        for line in block_lines:
            self.execute_line(line.strip())

    def get_output(self):
        return self.output

def run_file(filename):
    try:
        with open(filename, 'r') as file:
            code = file.read()

        interpreter = MarathiScriptInterpreter()
        interpreter.execute(code)
        output = interpreter.get_output()
        print("\n".join(output))
        print("Barobar kelas")  # Print this if no exception occurs
    except Exception as e:
        print(e)  # This will print 'Baba chukicha kelais neat kar' if an exception occurs


# Running the interpreter on a file
if __name__ == "__main__":
    output = run_file("var_example.masta")
    print("\n".join(output))
