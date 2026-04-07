# NEBULA Language Interpreter

Linguagem de programação didática para a disciplina de Construção de Interpretadores e Compiladores.

## 📁 Estrutura do Projeto

```
NEBULA-PROVA/
├── examples/
│   └── tests/
│       ├── consulta_planetas.neb
│       ├── teste_bloco_antigo_invalido.neb
│       ├── teste_condicional.neb
│       ├── teste_erros.neb
│       ├── teste_funcao.neb
│       ├── teste_invalido.neb
│       ├── teste_precedencia.neb
│       ├── teste_tipos_soma_invalida.neb
│       └── programa_exemplo.neb
│
├── src/
│   ├── components/
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   └── runner.py
│   │   │
│   │   ├── interpreter/
│   │   │   ├── __init__.py
│   │   │   └── interpreter.py
│   │   │
│   │   ├── lexer/
│   │   │   ├── __init__.py
│   │   │   ├── lexer.py
│   │   │   └── tokens.py
│   │   │
│   │   ├── nebula_ast/
│   │   │   ├── __init__.py
│   │   │   └── nodes.py
│   │   │
│   │   └── parser/
│   │       ├── __init__.py
│   │       └── parser.py
│   │
│   ├── nebula.py
│   └── run_tests.py
│
├── .gitignore
└── README.md
```

## 🚀 Como Usar

### Executar um programa

```bash
# Na raiz do projeto
python src/nebula.py examples/programa_exemplo.neb

# Com modo verbose (mostra tokens e AST)
python src/nebula.py examples/programa_exemplo.neb -v

# Ou usando caminho absoluto/relativo
python src/nebula.py /caminho/para/meu_programa.neb
```

### Executar todos os testes

```bash
python src/run_tests.py
```

## 📝 Características da Linguagem

- **Palavras-chave em português**: `criar`, `se`, `senao`, `enquanto`, `exibir`
- **Blocos**: delimitados por `inicio` ... `fim`
- **Terminador**: statements terminam com `;`
- **Operadores lógicos**: `&&` (E), `||` (OU), `!` (NÃO)
- **Comentários**: `//` linha única, `/* */` bloco
- **Tipos**: números inteiros, reais, strings, booleanos


## 🧪 Testes

Os testes estão em `examples/tests/`:

- `teste_condicional.neb` - Testa if/else
- `teste_precedencia.neb` - Testa precedência de operadores
- `teste_enquanto.neb` - Testa loops while

## 📚 Atualizações de Uso da Linguagem

As seções abaixo complementam a documentação existente com comportamentos que já estão implementados no código atual do projeto.

### Sintaxe atual de blocos e condicionais

Os blocos usados em condicionais são escritos com chaves e a palavra `entao`.

Formato válido:

```nebula
se (x > 10) entao {
    exibir("maior");
}
senao {
    exibir("menor");
}
```

Observações:
- `senao` continua opcional
- os statements dentro do bloco continuam terminando com `;`
- o comando de saída continua sendo `exibir(...)`
- o alias `saida(...)` também é aceito

Formato antigo que deve gerar erro:

```nebula
se (x > 10) inicio
    exibir("maior");
fim
```

### Validação de tipos na soma

A operação `+` continua válida entre números e também entre textos.

Casos válidos:

```nebula
criar a = 10 + 5;
criar nome = "Ola" + " Mundo";
```

Casos inválidos:

```nebula
criar texto = "ola";
criar numero = 10;

criar x = texto + numero;
criar y = numero + texto;
```

Nesses casos, a execução deve falhar com erro de incompatibilidade de tipos na operação de soma.

Resumo prático:
- `numero + numero` -> válido
- `string + string` -> válido
- `string + numero` -> erro
- `numero + string` -> erro

### Declaração e chamada de funções

O projeto agora aceita declaração de funções com parâmetros, retorno de valor e chamada como expressão.

Exemplo simples:

```nebula
funcao dobro(x) {
    devolve x * 2;
}

criar resultado = dobro(5);
saida(resultado);
```

Equivalências aceitas pelo lexer:
- `funcao` e `definir`
- `devolve` e `retornar`
- `saida` e `exibir`

Observações:
- os parâmetros são passados entre parênteses
- o corpo da função usa `{ }`
- o retorno usa `devolve <expressao>;`
- o ponto e vírgula continua obrigatório

### Função recebendo função como argumento

Também é possível passar uma função como argumento para outra função.

Exemplo válido:

```nebula
funcao dobro(x) {
    devolve x * 2;
}

funcao aplicar(valor, fn) {
    devolve fn(valor);
}

criar x = aplicar(5, dobro);
saida(x);
```

Nesse caso:
- `dobro` é passada como referência
- `fn(valor)` executa a função recebida
- o resultado final esperado é `10`

### Observações para teste e avaliação

Para verificar rapidamente os comportamentos mais recentes do projeto, os arquivos abaixo são úteis:

- `examples/tests/teste_condicional.neb` - uso de `se (...) entao { ... } senao { ... }`
- `examples/tests/teste_tipos_soma_invalida.neb` - rejeição de soma entre texto e número
- `examples/tests/teste_bloco_antigo_invalido.neb` - rejeição do formato antigo com `inicio/fim`
- `examples/tests/teste_funcao_como_argumento.neb` - função recebendo função como argumento

Ao executar `python src/run_tests.py`, esses cenários podem ser observados diretamente na saída do interpretador.

## 👥 Autores

- João Victor Rocha Santos - 600951313
- Denis Filho Cunha Godoi - 601005438

**Disciplina**: N477 - Construção de Interpretadores e Compiladores  
**Instituição**: Unitri
