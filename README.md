# caso-COH-PIAH
Pythom e IDLE Pycharm
Veja o desafio em:
<https://www.coursera.org/learn/ciencia-computacao-python-conceitos/programming/oUnlk/programa-completo-similaridades-entre-textos-caso-coh-piah>

# Descrição do Desafio
Atividade final proposta no curso de Python (parte 1) criado pela USP na plataforma Coursera.

John é monitor na matéria de Introdução à Produção Textual I na Penn State University (PSU). Durante esse período, John descobriu que uma epidemia de COH-PIAH estava se espalhando pela PSU. Esses doença rara e altamente contagiosa faz com que as pessoas contaminadas produzam textos extremamente semelhantes de forma involuntária. Após a entrega da primeira redação, John desconfiou que alguns alunos estavam sofrendo de COH-PIAH. John, se preocupando com a saúde da turma, resolveu buscar um método para identificar os casos de COH-PIAH. Para isso, ele necessita da sua ajuda para desenvolver um programa que o auxilie a identificar os alunos contaminados.

### Detecção de autoria

Utilizando diferentes estatísticas do texto, é possível identificar aspectos que funcionam como uma “assinatura” do autor. Diferentes pessoas possuem diferentes estilos de escrita, algumas preferindo sentenças mais curtas, outras preferindo sentenças mais longas. Essas “assinatura” pode ser utilizada para detecção de plágio, evidência forense, ou nesse caso, para detectar a grave doença COH-PIAH.

### Traços linguísticos

Nesse exercício utilizaremos as seguintes estatísticas para detectar a doença:

Tamanho médio de palavra: Média simples do número de caracteres por palavra.

Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.

Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo número total de palavras.

Tamanho médio de sentença: Média simples do número de caracteres por sentença.

Complexidade de sentença: Média simples do número de frases por sentença.

Tamanho médio de frase: Média simples do número de caracteres por frase.

### Funcionamento do programa

Diversos estudos foram compilados e hoje se conhece precisamente a assinatura de um portador de COH-PIAH. Seu programa deverá receber diversos textos e calcular os valores dos diferentes traços linguísticos da seguinte forma:

* Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.

* Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale $\frac{4}{5} = 0.8$.

* Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale $\frac{3}{5} = 0.6$

* Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).

* Complexidade de sentença é o número total de frases divido pelo número de sentenças.

* Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).

Após calcular esses valores para cada texto, você deve comparar com a assinatura fornecida para os infectados por COH-PIAH. O grau de similaridade entre dois textos, $a$ e $b$, é dado pela fórmula:

$S_{ab} = \frac{\sum_{i=1}^6 || f_{i,a} - f_{i,b} ||}{6}$

Onde: 
* $S_{ab}$ é o grau de similaridade entre os textos a e b; 
* $f_{i,a}$ é o valor de cada traço linguístico i no texto a; e
* $f_{i,b}$ é o valor de cada traço linguístico i no texto b. 

No nosso caso, o texto  $b$ não é conhecido, mas temos a assinatura correspondente: a assinatura de um aluno infectado com COH-PIAH. Ou seja, sabemos o valor de $f_{i,b}$
que é dado como valor de entrada do programa.

Para cada traço linguístico $i$ (tamanho médio da palavra, relação type-token etc.) se quer a diferença entre o valor obtido em cada texto dado $(a)$ e o valor típico do texto de uma pessoa infectada $(b): f_{i,a} - f_{i,b}$

Dessa diferença se toma o módulo $(||...||)$, lembre-se da função abs do python.

Somamos os resultados dos 6 trações linguísticos $(\sum_{i=1}^6)$

E por final dividimos por 6 $\frac{x}{6}$

Perceba que quanto mais similares $a$ e $b$ forem, menor $S_{ab}$ será. Para cada texto, você deve calcular o grau de similaridade com a assinatura do portador de COH-PIAH e, no final, exibir qual texto mais provavelmente foi escrito por algum aluno infectado (ou seja, o texto com assinatura mais similar à assinatura dada).

