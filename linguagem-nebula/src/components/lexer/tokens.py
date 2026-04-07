"""
Definição de Tokens e Tipos de Token para a linguagem Nebula.
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import Any


class TipoToken(Enum):
    """Enumeração de todos os tipos de tokens da linguagem Nebula."""

    CRIAR = auto()
    SE = auto()
    ENTAO = auto()
    SENAO = auto()
    ENQUANTO = auto()
    DEFINIR = auto()
    RETORNAR = auto()
    EXIBIR = auto()
    LER = auto()

    NUMERO_INTEIRO = auto()
    NUMERO_REAL = auto()
    STRING = auto()
    BOOLEANO = auto()
    IDENTIFICADOR = auto()

    SOMA = auto()
    SUBTRACAO = auto()
    MULTIPLICACAO = auto()
    DIVISAO = auto()
    MODULO = auto()
    POTENCIA = auto()

    IGUAL = auto()
    DIFERENTE = auto()
    MENOR = auto()
    MENOR_IGUAL = auto()
    MAIOR = auto()
    MAIOR_IGUAL = auto()

    E_LOGICO = auto()
    OU_LOGICO = auto()
    NAO_LOGICO = auto()

    ATRIBUICAO = auto()
    PONTO_VIRGULA = auto()
    VIRGULA = auto()
    DOIS_PONTOS = auto()

    ABRE_PARENTESES = auto()
    FECHA_PARENTESES = auto()
    ABRE_CHAVE = auto()
    FECHA_CHAVE = auto()
    INICIO = auto()
    FIM = auto()

    NEBULA = auto()

    EOF = auto()

    def __repr__(self):
        return f"{self.name}"


@dataclass
class Token:
    """Representa um token na análise léxica."""
    tipo: TipoToken
    valor: Any = None
    linha: int = 0
    coluna: int = 0

    def __repr__(self):
        if self.valor is not None:
            return f"Token({self.tipo}, '{self.valor}', linha={self.linha}, col={self.coluna})"
        return f"Token({self.tipo}, linha={self.linha}, col={self.coluna})"
