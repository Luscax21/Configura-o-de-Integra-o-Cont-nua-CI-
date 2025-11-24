# test_validacao.py
import pytest
from funcoes_validacao import validar_senha

# 1. Uma senha válida que atende a todos os critérios.
def test_senha_valida():
    # Exemplo: 8 chars, tem maiúscula (S), tem número (1)
    assert validar_senha("SenhaForte1") == True

# 2. Uma senha com menos de 8 caracteres (inválida).
def test_senha_curta():
    # Exemplo: Tem maiúscula e número, mas só 5 chars
    assert validar_senha("Sen1") == False

# 3. Uma senha sem números (inválida).
def test_senha_sem_numeros():
    # Exemplo: 8 chars, tem maiúscula, mas sem número
    assert validar_senha("SenhaSemNumero") == False

# 4. Uma senha sem letras maiúsculas (inválida).
def test_senha_sem_maiuscula():
    # Exemplo: 8 chars, tem número, mas tudo minúsculo
    assert validar_senha("senhaminuscula1") == False