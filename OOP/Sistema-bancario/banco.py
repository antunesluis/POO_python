import contas
import pessoas


class Banco:
    def __init__(
        self,
        agencia: list[int] | None = None,
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None
    ):
        self.agencias = agencia or []
        self.clientes = clientes or []
        self.contas = contas or []

    def adiciona_clientes(self, cliente):
        self.clientes.append(cliente)

    def adiciona_conta(self, conta):
        self.contas.append(conta)

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_cliente_possui_conta(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False

    def autenticar(self, cliente: pessoas.Cliente, conta: contas.Conta):
        return (
            self._checa_agencia(conta) and
            self._checa_cliente(cliente) and
            self._checa_conta(conta)
        )

    def __repr__(self):
        banco_nome = type(self).__name__
        banco_dados = f'({self.agencias!r}, {self.clientes!r},{self.contas!r})'
        return f'{banco_nome}{banco_dados}'


if __name__ == '__main__':
    c1 = pessoas.Cliente('Luiz', 30)
    c1.conta = contas.ContaCorrente(111, 222, 0, 0)
    print(c1)
    print(c1.conta)
    c2 = pessoas.Cliente('Maria', 18)
    c2.conta = contas.ContaPoupanca(112, 223, 100)
    print(c2)
    print(c2.conta)
