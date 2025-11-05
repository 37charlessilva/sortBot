# 🧠 SortBot

O **SortBot** é um script em Python feito para **organizar automaticamente arquivos da faculdade**.  
Ele identifica arquivos em uma pasta de origem (como *Downloads*), analisa o nome de cada arquivo (que contém uma flag numérica indicando o tipo de conteúdo) e move os arquivos para as pastas corretas dentro de uma estrutura organizada.

---

## ⚙️ Funcionamento

1. O script lê o arquivo `config.txt` para saber:
   - Onde estão os arquivos que precisam ser organizados (`@source`);
   - Qual é a pasta raiz onde os arquivos serão guardados (`@root`);
   - Quais são as pastas principais (`@pastas`);
   - E, opcionalmente, as subpastas (`@subPastas`).

2. Depois, ele procura arquivos na pasta de origem (`@source`) com nomes que contenham uma **flag numérica**, por exemplo:
```

1_ListaCalculo.pdf
2_ExercicioAlgoritmos.py
3_ResumoFisica.txt

```

3. O SortBot:
- Lê o número da flag;
- Remove a flag do nome;
- Move o arquivo para a pasta correspondente no diretório definido em `@root`.

---

## 🧩 Estrutura do arquivo `config.txt`

Exemplo de configuração:

```

@source C:\Users\charles\Downloads
@root C:\Users\charles\Faculdade
@pastas Calculo, Algoritmos, Fisica
@subPastas Exercicios, Listas, Resumos

```

> 💡 O SortBot usa essas informações para criar (caso não existam) as pastas dentro de `@root`.

---

## 🧰 Exemplo de uso

### Antes:
Pasta `Downloads/` contém:
```

1Lista1Calculo.pdf
2ExercicioAlgoritmos.py
3ResumoFisica.txt

```

### Depois de rodar o SortBot:
```

Faculdade/
├── Calculo/
│   └── Lista1Calculo.pdf
├── Algoritmos/
│   └── ExercicioAlgoritmos.py
└── Fisica/
└── ResumoFisica.txt

````

---

## 🚀 Como executar

No terminal:

```bash
python sortbot.py
````

(Ou o nome que você deu pro seu script principal.)

O programa vai:

* Ler o `config.txt`;
* Criar as pastas se não existirem;
* Mover e renomear os arquivos automaticamente.

---

## 📦 Requisitos

- Python 3.8 ou superior
- Bibliotecas padrão:
  - `os`
  - `pathlib`

---

## 💡 Ideias futuras

* Interface gráfica;

---

## 🧑‍💻 Autor

**Charles Silva**
Estudante de Ciência da Computação UERJ
Desenvolvido para facilitar a organização de materiais da faculdade 🎓

```