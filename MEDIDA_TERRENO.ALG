Algoritmo "Medida_Terreno"

Var

  largura, comprimento, valorMetro, area, preco : real

Inicio

  escreva("Digite a largura do terreno: ")
  leia(largura)
  escreva("Digite o comprimento do terreno: ")
  leia(comprimento)
  escreva("Digite o valor do metro quadrado: ")
  leia(valorMetro)
  escreval()
  
  area <- largura * comprimento
  preco <- area * valorMetro
  
  escreval("A área do terreno é de: ", area:3:2)
  escreval()
  escreval("A área do terreno tem o valor de: ", preco:5:2)

Fimalgoritmo