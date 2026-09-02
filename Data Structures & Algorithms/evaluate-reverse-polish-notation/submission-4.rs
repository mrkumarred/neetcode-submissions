impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        // Set of operators; every other token is an operand to push.
        let operators: HashSet<&str> = ["+", "-", "*", "/"].into();
        let mut stack: Vec<i32> = Vec::new();

        for token in tokens {
            if operators.contains(token.as_str()) {
                // Operator: the two most recent operands are combined.
                let right = stack.pop().unwrap(); // later token → right operand
                let left = stack.pop().unwrap();  // earlier token → left operand

                let result: i32 = match token.as_str() {
                    "+" => left + right,
                    "-" => left - right,
                    "*" => left * right,
                    _ => left / right,  // Rust truncates toward zero natively
                };

                stack.push(result);
            } else {
                // Operand: convert to i32 and push.
                stack.push(token.parse::<i32>().unwrap());
            }
        }

        stack[0]  // exactly one value remains
    }
}