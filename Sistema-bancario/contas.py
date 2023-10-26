import abc


class Conta(abc.ABC):
    def __init__(self, agencia, num_conta, saldo=0):
        self._agencia = agencia
        self._conta = num_conta
        self._saldo = saldo

    # deve ser implementada na conta corrente ou poupança.
    @abc.abstractmethod
    def sacar(self, valor):
        ...

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, val):
        self._agencia = val

    @property
    def conta(self):
        return self._conta

    @agencia.setter
    def conta(self, val):
        self._conta = val

    @property
    def saldo(self):
        return self._saldo

    @agencia.setter
    def saldo(self, val):
        self._saldo = val

    def depositar(self, val):
        self.saldo += val
        self.mostra_saldo(f'(DEPOSITO {val})')

    def mostra_saldo(self, msg=""):
        print(f'Saldo atual: {self.saldo:.2f} {msg}')


class ContaPoupanca(Conta):
    def sacar(self, val):
        saldo_pos_saque = self.saldo - val

        if saldo_pos_saque >= 0:
            self.saldo = saldo_pos_saque
            self.mostra_saldo(f'(SAQUE {val})')
            return self.saldo

        print('Saldo insuficiente para saque')
        self.mostra_saldo(f'(SAQUE NEGADO {val})')


class ContaPoupanca(Conta):
    def sacar(self, val):
        saldo_pos_saque = self.saldo - val

        if saldo_pos_saque >= 0:
            self.saldo = saldo_pos_saque
            self.mostra_saldo(f'(SAQUE {val})')
            return self.saldo

        print('Saldo insuficiente para saque')
        self.mostra_saldo(f'(SAQUE NEGADO {val})')


class ContaOrrente(Conta):
    def __init__(self, agencia, num_conta, saldo=0, limite=0):
        super().__init__(agencia, num_conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, val):
        self._limite = val

    def sacar(self, val):
        saldo_pos_saque = self.saldo - val

        if saldo_pos_saque + self.limite >= 0:
            self.saldo = saldo_pos_saque
            self.mostra_saldo(f'(SAQUE {val})')
            return self.saldo

        print('Saldo insuficiente para saque')
        self.mostra_saldo(f'(SAQUE NEGADO {val})')


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222, 0)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    cp1.sacar(1)
