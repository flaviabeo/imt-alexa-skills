# IMT Pesquisa Foundation Models para Alexa Skills

### Como rodar esse notebook

1. Instalar python virtualenvwrapper

```bash
pip install virtualenvwrapper
```
2. Incluir as variáveis no path

```bash
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```
3. Criar a virtualenv
Esse comando lista as virtualenvs já criadas, quando fazemos o setup inicial, ele não vai retornar nada.
```bash
workon
```
Para criar a primeira virtualenv:
```bash
mkvirtualenv nome-da-virtualenv
```

### O Modelo de exemplo

[SentenceTransformers](https://www.sbert.net/)
 é uma biblioteca em Python para incorporação de frases, textos e imagens de última geração. O trabalho inicial é descrito em nosso artigo Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. Isso pode ser útil para similar textual semântico, pesquisa semântica ou mineração de paráfrase.

**Instalar**
```bash
pip install sentence-transformers
```

