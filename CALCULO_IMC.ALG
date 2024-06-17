Algoritmo "CalculoIMC"

Var

  peso, altura, imc : real

Inicio

    escreva("Insira seu peso: ")
    leia(peso)
    escreva("Insira sua altura: ")
    leia(altura)
    
    imc <- peso / (altura * altura)
    
      se imc < 18.5 entao
          escreva("Abaixo do peso.")
      senao
          se imc >= 18.5 entao
          se imc < 25 entao
              escreva("Peso ideal. Parabéns!")
          senao
              se imc >= 25 entao
              se imc < 30 entao
                  escreva("Sobrepeso.")
              senao
                  escreva("Obesidade.")
              fimse
          fimse
      fimse
    fimse
fimse

Fimalgoritmo
