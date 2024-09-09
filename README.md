# Tech News

## Contexto

O foco principal deste projeto é, com base nos ensinamentos da **Trybe**, desenvolver uma aplicação para realizar consultas de notícias sobre tecnologia. Essas notícias são obtidas por meio de raspagem de dados (web scraping) do [_blog da Trybe_](https://blog.betrybe.com), e os dados extraídos são armazenados em um banco de dados **MongoDB** para facilitar consultas futuras.

<details>
  <summary>O que é a Trybe?🤔</summary>
  A Trybe é uma escola de desenvolvimento web genuinamente comprometida com o sucesso profissional de seus estudantes. Com o Modelo de Sucesso Compartilhado (MSC) oferecido pela Trybe Fintech, uma instituição financeira autorizada pelo Banco Central do Brasil, os alunos têm a opção de pagar apenas quando estiverem trabalhando.
</details>

A aplicação permite buscar as últimas notícias publicadas, paginar os resultados, e realizar pesquisas por título, data e categoria das notícias. A raspagem dos dados é feita por meio da biblioteca **Parsel** para extrair o conteúdo HTML e identificar as informações relevantes. Além disso, a aplicação precisa respeitar um **Rate Limit** para evitar sobrecarga no servidor do blog, garantindo uma requisição por segundo.

### Funcionalidades e Tarefas Principais:

1. **Requisição e Obtenção de HTML**:
   - Implementação da função `fetch`, responsável por realizar a requisição HTTP e obter o conteúdo HTML das páginas de notícias do blog.

2. **Raspagem de URLs de Notícias**:
   - Criação da função `scrape_updates` para extrair as URLs das páginas de notícias a partir do HTML da página inicial do blog.

3. **Paginação**:
   - Desenvolvimento da função `scrape_next_page_link` para buscar o link da próxima página de notícias e possibilitar a paginação.

4. **Extração de Dados das Notícias**:
   - Implementação da função `scrape_news`, responsável por extrair os dados de cada notícia individual, como título, autor, tempo de leitura e resumo.

5. **Obtenção e Armazenamento de Notícias**:
   - Criação da função `get_tech_news`, que utiliza as funções anteriores para obter e armazenar no **MongoDB** as últimas notícias publicadas.

6. **Buscas no Banco de Dados**:
   - Implementação de funcionalidades que permitem buscar notícias no banco de dados por título (`search_by_title`), data (`search_by_date`) e categoria (`search_by_category`).

### Habilidades Desenvolvidas:
- **Web Scraping**: Aplicação de técnicas de raspagem de dados usando a biblioteca **Parsel** para extrair informações de páginas HTML.
- **Manipulação de Banco de Dados**: Utilização do **MongoDB** para armazenar e consultar dados extraídos.
- **Programação com Python**: Desenvolvimento de funções modulares e reutilizáveis para requisições HTTP, raspagem de dados, e manipulação de banco de dados.
- **Testes Automatizados**: Implementação de testes para garantir o funcionamento correto das funcionalidades desenvolvidas.
- **Rate Limiting**: Implementação de um controle de requisições para garantir que o servidor não seja sobrecarregado.

---

## Tecnologias Usadas

- [Python](https://www.python.org/) - Linguagem de programação utilizada para desenvolver a aplicação.
- [Parsel](https://parsel.readthedocs.io/) - Biblioteca para extração de dados de documentos HTML e XML.
- [Requests](https://docs.python-requests.org/en/latest/) - Biblioteca para realizar requisições HTTP.
- [MongoDB](https://www.mongodb.com/) - Banco de dados NoSQL utilizado para armazenar as notícias extraídas.
- [Pytest](https://docs.pytest.org/en/6.2.x/) - Framework de testes automatizados usado para validar as funcionalidades.
- [Docker](https://www.docker.com/) - Ferramenta usada para rodar o banco de dados **MongoDB** em ambiente controlado via **Docker Compose**.

## Entre em contato:
<a href="mailto:zazac3179@gmail.com" target="_blank">
  <img align="center" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail" height="40" width="auto" />
</a>
<a href="https://www.linkedin.com/in/isaque-s-oliveira/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="isaque oliveira" height="30" width="40" /></a>
<a href="https://wa.me/5574981510614" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/whatsapp.svg" alt="WhatsApp" height="30" width="40" /></a>
