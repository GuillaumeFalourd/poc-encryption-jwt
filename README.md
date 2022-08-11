# POC JWT encryption
<!-- markdownlint-disable -->
[![Security Pipeline](https://github.com/GuillaumeFalourd/poc-encryption-jwt/actions/workflows/security-pipeline.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-encryption-jwt/actions/workflows/security-pipeline.yml) [![Super Linter](https://github.com/GuillaumeFalourd/poc-encryption-jwt/actions/workflows/super-linter.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-encryption-jwt/actions/workflows/super-linter.yml) [![Gitleaks](https://github.com/GuillaumeFalourd/poc-encryption-jwt/actions/workflows/gitleaks.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-encryption-jwt/actions/workflows/gitleaks.yml)
<!-- markdownlint-restore -->


## 📋 Index

- [Setup](https://github.com/GuillaumeFalourd/poc-encryption-jwt#-setup)
- [Usage](https://github.com/GuillaumeFalourd/poc-encryption-jwt#-usage)
- [Generate new Key Pair](https://github.com/GuillaumeFalourd/poc-encryption-jwt#%EF%B8%8F-generate-new-key-pair)
- [TODOs](https://github.com/GuillaumeFalourd/poc-encryption-jwt#todos)
- [JWT Concept](https://github.com/GuillaumeFalourd/poc-encryption-jwt#-jwt-concept)
- [Contributing](https://github.com/GuillaumeFalourd/poc-encryption-jwt#-contributing)
- [License](https://github.com/GuillaumeFalourd/poc-encryption-jwt#-licensed)


## 🏗 Setup

To install the dependencies, run the following command at the repository `root`:

```sh
pip install -r requirements.txt
```


## 🚦 Usage

To execute the program, run the following command at thre repository `root`:

```sh
python3 main.py
```

It should display:

```txt
- The program started!
? What do you want to do? (Use arrow keys)
 » Encrypt
   Decrypt
```

1. You will need to create an `.encrypted_file` first at the repository `root` choosing the **Encrypt** option.
   1. This `.encrypted_file` will contains a JWT containing an cryptographed data (the user **machine_id**).

2. To decrypt the `.encrypted_file` generated at the repository `root`, choose the **Decrypt** option.
   1. The program will compare the JWT decoded **machine_id** with the user machine_id to check if the token is valid (**Valid** in that case means it has been generated on the same machine)

_Note: It's also possible to check the JWT present in the `.encrypted_file` content on [jwt.io](https://jwt.io/)._


## ⚙️ Generate new key pair

```markdown
ssh-keygen -t rsa -b 4096 -m PEM -f jwtRS256.key
openssl rsa -in jwtRS256.key -pubout -outform PEM -out jwtRS256.key.pub

cat jwtRS256.key # private key
cat jwtRS256.key.pub # public key
```

The `jwtRS256.key` and the `jwtRS256.key.pub` files need to be located on the `./encryption` folder.


## TODOs

- [ ] Add Unit tests.
- [ ] Add Unit tests pipelines.


## 🧐 JWT Concept

![jwt](/jwt.jpeg)


### Referências

_[Alexandre Fidélis Vieira Bitencourt](https://github.com/alexandrefvb): O JWS garante através de uma assinatura digital (que usa algoritmos criptográficos) a integridade da informação que está no token, mas não garante a confidencialidade das informações. Vale lembrar que quando lidamos com tokens JWT é muito importante que a assinatura seja verificada para garantir que o conteúdo do token não tenha sido alterado. O objetivo principal do token JWT no formato JWS é justamente permitir que os claims sejam inspecionados a fim de obter informações importantes para identificar o usuário, suas permissões e outras informações relevantes para o processo de autenticação/autorização de forma que sua sua integridade esteja garantida. O algoritmo usado para assinar o token vai variar dependendo de como será o processo de verificação podendo ser um algoritmo simétrico (uma chave apenas) ou assimétrico (usando uma chave privada para gerar o token e uma chave pública para verificar a assinatura). [Post que resume bem alguns conceitos](https://www.brunobrito.net.br/jose-jwt-jws-jwe-jwa-jwk-jwks/)_


## 🏅 Licensed

☞ This repository uses the [Apache License 2.0](https://github.com/GuillaumeFalourd/poc-encryption-jwt/blob/main/LICENSE)


## 🤝 Contributing

☞ If you're interested in contributing to this repository, please follow the [guidelines](https://github.com/GuillaumeFalourd/poc-encryption-jwt/blob/main/CONTRIBUTING.md)

### Contribuidores

<a href="https://github.com/GuillaumeFalourd/poc-encryption-jwt/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=GuillaumeFalourd/poc-encryption-jwt" />
</a>

(Criado com [contributors-img](https://contrib.rocks))
