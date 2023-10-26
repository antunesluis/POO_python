import contas


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, val: str):
        self._nome = val

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, val: int):
        self._idade = val

    def __repr__(self):
        pessoa_nome = type(self).__name__
        pessoa_dados = f'({self.nome!r}), {self.idade!r}'
        return f'{pessoa_nome}{pessoa_dados}'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None


if __name__ == '__main__':
    c1 = Cliente('Luiz', 30)
    c1.conta = contas.ContaCorrente(111, 222, 0, 0)
    print(c1)
    print(c1.conta)
    c2 = Cliente('Maria', 18)
    c2.conta = contas.ContaPoupanca(112, 223, 100)
    print(c2)
    print(c2.conta)
