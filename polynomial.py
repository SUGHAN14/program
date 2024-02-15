def add_polynomials(poly1, poly2):
    max_degree = max(len(poly1), len(poly2))
    result = [0] * max_degree

    for i in range(len(poly1)):
        result[i] += poly1[i]

    for i in range(len(poly2)):
        result[i] += poly2[i]

    return result

def multiply_polynomials(poly1, poly2):
    max_degree = len(poly1) + len(poly2) - 1
    result = [0] * max_degree

    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += poly1[i] * poly2[j]

    return result

def display_polynomial(poly):
    terms = []
    for degree, coefficient in enumerate(poly):
        if coefficient != 0:
            terms.append(f"{coefficient}x^{degree}")

    if not terms:
        return "0"
    return " + ".join(terms)

# Example usage
poly1 = [2, 0, 1]  # Represents 2x^2 + 1
poly2 = [1, 3]     # Represents x + 3

sum_result = add_polynomials(poly1, poly2)
product_result = multiply_polynomials(poly1, poly2)

print("Polynomial 1:", display_polynomial(poly1))
print("Polynomial 2:", display_polynomial(poly2))
print("Sum:", display_polynomial(sum_result))
print("Product:", display_polynomial(product_result))

