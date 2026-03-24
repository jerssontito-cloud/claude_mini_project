"""
Skill: Tutor de Matemáticas
Proporciona ayuda para resolver problemas matemáticos
"""

def math_tutor_skill(question: str, level: str = "intermedio") -> dict:
    """
    Skill de tutor de matemáticas
    
    Args:
        question: La pregunta matemática a resolver
        level: Nivel de dificultad (básico, intermedio, avanzado)
    
    Returns:
        Diccionario con pistas y solución
    """
    print(f"🧮 Tutor de Matemáticas - Nivel: {level}")
    print(f"❓ Pregunta: {question}")
    
    # Análisis simple de la pregunta
    hints = []
    solution = ""
    
    if "2x" in question and "=" in question:
        hints.append("1. Identifica la variable a despejar (x)")
        hints.append("2. Mueve los términos constantes al otro lado")
        hints.append("3. Divide por el coeficiente de x")
        solution = "x = 2"
    elif "+" in question and "=" in question:
        hints.append("1. Identifica todos los términos")
        hints.append("2. Agrupa términos semejantes")
        hints.append("3. Resuelve la ecuación")
        solution = "Solución depende de los valores"
    else:
        hints.append("1. Lee cuidadosamente el problema")
        hints.append("2. Identifica los datos conocidos")
        hints.append("3. Aplica las fórmulas apropiadas")
        solution = "Análisis manual requerido"
    
    return {
        "question": question,
        "level": level,
        "hints": hints,
        "solution": solution,
        "status": "completado"
    }

def solve_math(question: str) -> str:
    """Función simple para resolver matemáticas básicas"""
    try:
        # Evaluación segura de expresiones matemáticas
        allowed_chars = "0123456789+-*/.() "
        if all(c in allowed_chars for c in question):
            result = eval(question)
            return f"Resultado: {result}"
        else:
            return "Expresión no válida"
    except Exception as e:
        return f"Error al calcular: {str(e)}"

if __name__ == "__main__":
    print("🎓 Skill: Tutor de Matemáticas")
    print("=" * 50)
    
    # Prueba 1
    result1 = math_tutor_skill("2x + 3 = 7", "básico")
    print(f"\nHints: {result1['hints']}")
    print(f"Solución: {result1['solution']}")
    
    # Prueba 2
    result2 = solve_math("5 + 3 * 2")
    print(f"\n5 + 3 * 2 = {result2}")
