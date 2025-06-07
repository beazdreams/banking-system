# Banking System

Banking system developed using Python, for DIO's Python Developer Bootcamp.

## Challenge #1:

<details>
    <summary>Portuguese description</summary>
    <p>Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e, para isso, escolheu a linguagem Python.</p>
    <p>Para a primeira versão do sistema, iremos trabalhar com apenas um usuário, e devemos implementar três operações:</p>
    <h3>Depósito (<code>deposit_money</code>)</h3>
    <ul>
        <li>O sistema deve permitir o usuário depositar valores positivos para a conta bancária;</li>
        <li>O sistema deve armazenar o depósito em uma variável para exibição na operação de extrato.</li>
    </ul>
    <h3>Saque (<code>withdraw_money</code>)</h3>
    <ul>
        <li>O sistema deve permitir realizar <b>3 saques diários</b>;</li>
        <li>O sistema deve permitir que o usuário saque valores acima de 500 reais por saque;</li>
        <li>O sistema deve verificar se o saldo na conta é maior ou igual ao valor sacado;</li>
        <li>O sistema deve armazenar o saque em uma variável para exibição na operação de extrato.</li>
    </ul>
    <h3>Extrato (<code>print_statement</code>)</h3>
    <ul>
        <li>O sistema deve permitir o usuário exibir seu extrato bancário;</li>
        <li>O sistema deve exibir o saldo atual do usuário logo após o extrato, formatado sempre com duas casas decimais e com "R$" na frente.</li>
    </ul>
</details>
<br>

We were hired by a major bank to develop its new system. This bank aims to modernize its operations and, for that, has chosen Python as its programming language.

For the first version of the system, we will work with only one user and must implement three operations:

### Deposit (`deposit_money`)
- The system must allow the user to deposit positive amounts into their bank account.
- The system must store the deposit in a variable for display in the statement operation.

### Withdrawal (`withdraw_money`)
- The system must allow **three daily withdrawals**.
- The system must allow the user to withdraw amounts above 500 BRL per transaction.
- The system must verify if the account balance is greater than or equal to the withdrawn amount.
- The system must store the withdrawal in a variable for display in the statement operation.

### Statement (`print_statement`)
- The system must allow the user to view their bank statement.
- The system must display the user's current balance right after the statement, always formatted with two decimal places and preceded by "R$".

[Original description, given in the bootcamp](https://academiapme-my.sharepoint.com/:p:/g/personal/kawan_dio_me/Ef-dMEJYq9BPotZQso7LUCwBJd7gDqCC2SYlUYx0ayrGNQ?rtime=MDLUO0B13Ug).

## Challenge #2:

<details>
    <summary>Portuguese description</summary>
    <p>Devem ser implementadas novas funcionalidades:</p>
    <h3>Cadastrar conta corrente</h3>
    <ul>
        <li>O programa deve armazenar contas em uma lista;</li>
        <li>Uma conta é composta por agência, número da conta e usuário;</li>
        <li>O número da conta é sequencial, iniciando em 1;</li>
        <li>O número da agência é fixo: "0001";</li>
        <li>Um usuário pode ter mais de uma conta, mas uma conta pertence a apenas um usuário.</li>
    </ul>
    <h3>Criar usuário (cliente)</h3>
    <ul>
        <li>O programa deve armazenar usuários em uma lista;</li>
        <li>Um usuário é composto por nome, data de nascimento, CPF e endereço;</li>
        <li>O endereço é uma <code>string</code> com o formato: logradouro - nº - bairro - cidade/UF;</li>
        <li>Deve ser armazenado somente os números do CPF;</li>
        <li>Não podemos cadastrar 2 usuários com o mesmo CPF.</li>
    </ul>
</details>
<br>