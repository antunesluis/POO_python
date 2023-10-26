import abc


class Conta(abc.ABC):
    def __init__(self, agencia: int, num_conta: int, saldo: float = 0):
        self._agencia = agencia
        self._conta = num_conta
        self._saldo = saldo

    # deve ser implementada na conta corrente ou poupança.
    @abc.abstractmethod
    def sacar(self, val: float) -> float:
        ...

    @property
    def agencia(self) -> int:
        return self._agencia

    @agencia.setter
    def agencia(self, val: int):
        self._agencia = val

    @property
    def conta(self) -> int:
        return self._conta

    @conta.setter
    def conta(self, val: int):
        self._conta = val

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, val: float):
        self._saldo = val

    def depositar(self, val: float) -> float:
        self.saldo += val
        self.mostra_saldo(f'(DEPOSITO {val})')
        return self.saldo

    def mostra_saldo(self, msg: str = "") -> None:
        print(f'Saldo atual: {self.saldo:.2f} {msg}')

    def __repr__(self):
        nome_conta = type(self).__name__
        dados_conta = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{nome_conta}{dados_conta}'


class ContaPoupanca(Conta):
    def sacar(self, val: float) -> float:
        saldo_pos_saque = self.saldo - val

        if saldo_pos_saque >= 0:
            self.saldo = saldo_pos_saque
            self.mostra_saldo(f'(SAQUE {val})')
            return self.saldo

        print('Saldo insuficiente para saque')
        self.mostra_saldo(f'(SAQUE NEGADO {val})')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia: int, num_conta: int, saldo: float = 0,
                 limite: int = 0):
        super().__init__(agencia, num_conta, saldo)
        self._limite = limite

    @property
    def limite(self) -> int:
        return self._limite

    @limite.setter
    def limite(self, val: int):
        self._limite = val

    def sacar(self, val: float) -> float:
        saldo_pos_saque = self.saldo - val

        if saldo_pos_saque + self.limite >= 0:
            self.saldo = saldo_pos_saque
            self.mostra_saldo(f'(SAQUE {val})')
            return self.saldo

        print('Saldo insuficiente para saque')
        print(f'Seu limite é {-self.limite:.2f}')
        self.mostra_saldo(f'(SAQUE NEGADO {val})')
        return self.saldo


if __name__ == '__main__':
    cc1 = ContaPoupanca(111, 222, 0)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
