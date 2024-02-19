# Django Book Management System

Este é um sistema de gerenciamento de livros desenvolvido com Django. Permite aos usuários criar, visualizar, atualizar e excluir livros, bem como marcar livros como lidos.

## Modelo Book

O `Book` é um modelo Django que representa um livro.

### Campos

- `title`: O título do livro.
- `author`: O autor do livro.
- `year`: O ano de lançamento do livro.
- `page_numbers`: O número de páginas do livro.
- `read`: Indica se o livro foi lido ou não.

### Métodos

- `__str__()`: Retorna uma representação de string do objeto, neste caso, o título do livro.
- `book_read()`: Marca o livro como lido.

### Meta

- `verbose_name`: Define o nome singular para este modelo no admin do Django como "Livro".
- `verbose_name_plural`: Define o nome plural para este modelo no admin do Django como "Livros".
- `ordering`: Define a ordem padrão de classificação dos registros, neste caso, por `read`.

## Views

Este módulo contém várias classes de visualização baseadas em classes e funções de visualização para manipular a lógica de negócios relacionada aos livros.

### Funções de Visualização

- `home_page(request)`: Renderiza a página inicial do aplicativo de livros.

- `BookReadView(View)`: Marca um livro como lido.

### Classes de Visualização Baseadas em Classe

- `BookListView(ListView)`: Lista todos os livros cadastrados no sistema.
- `BookCreateView(CreateView)`: Cria um novo livro.
- `BookUpdateView(UpdateView)`: Atualiza um livro existente.
- `BookDeleteView(DeleteView)`: Exclui um livro existente.

### Atributos Comuns

- `model`: O modelo associado à visualização.
- `form_class`: A classe do formulário associada à visualização.
- `success_url`: A URL para redirecionamento após uma operação bem-sucedida.

## URLs

Este módulo contém definições de URLs que mapeiam as visualizações às URLs correspondentes para manipulação de solicitações HTTP.

### Rotas

- `"admin/"`: Mapeia para a interface de administração do Django.
- `"books/"`: Inclui as rotas definidas no aplicativo de livros (`books.urls`).

### Inclusão de Aplicativos

A função `include()` é usada para incluir as definições de URL de outros aplicativos Django. Isso permite que as URLs sejam organizadas modularmente em aplicativos separados.

## Configurações de URL Principal

Este módulo contém as definições de URL principal para o projeto Django, incluindo a inclusão de URLs específicas do aplicativo de livros.

- `"admin/"`: Mapeia para a interface de administração do Django.
- `"books/"`: Inclui as rotas definidas no aplicativo de livros (`books.urls`).

Essas configurações de URL permitem que o Django encaminhe solicitações HTTP para as visualizações correspondentes no aplicativo de livros e na interface de administração, conforme necessário.

