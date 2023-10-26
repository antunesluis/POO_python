"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

class Conta:
    def __init__(self, agencia, num_conta, saldo):
         self._agencia = agencia 
         self._num_conta = num_conta
         self._saldo = saldo

    @property
    def agencia(self):
         return self._agencia 

    @agencia.setter
    def agencia(self, val):
         self._agencia = val 

    @property
    def num_conta(self):
         return self._num_conta 

    @agencia.setter
    def num_conta(self, val):
         self._num_conta = val 

    @property
    def saldo(self):
         return self._saldo

    @agencia.setter
    def saldo(self, val):
         self._saldo = val 

    def depositar():
         ...

    #deve ser implementada na conta corrente ou poupança. 
    def saque():
         ...