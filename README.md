# Rumo_ao_Hexa_API


API REST desenvolvida em **Django** + **Django REST Framework** para modelar e gerenciar dados de seleções, times, jogadores e comissão técnica rumo à Copa do Mundo.

> 📚 **Repositório de estudos**: este projeto foi criado para treinar e aprender os conceitos base do Django (models, migrations, admin, serializers e views do Django REST Framework), servindo como prática hands-on da framework.

## 🛠️ Tecnologias

- [Python](https://www.python.org/)
- [Django 6.0](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- SQLite (banco de dados padrão em desenvolvimento)

## 📦 Estrutura do Projeto

```
Rumo_ao_Hexa_API/
├── core/                   # App principal
│   ├── models.py           # Modelos: Player, Team, TeamGroup, Coach
│   ├── serializers.py      # Serializers do DRF
│   ├── admin.py            # Registro dos modelos no Django Admin
│   ├── views.py            # Views da API
│   └── migrations/         # Migrações do banco de dados
├── setup/                  # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
├── manage.py
└── requirements.txt
```

## 🗂️ Modelos de Dados

| Modelo | Descrição |
|---|---|
| `TeamGroup` | Grupo/chave de times (ex: grupos de uma competição) |
| `Team` | Time/seleção, vinculado a um `TeamGroup` |
| `Player` | Jogador, com posição, pé preferido, número e vínculo com um `Team` |
| `Coach` | Membro da comissão técnica, vinculado a um `TeamGroup` |

Todos os modelos herdam campos padrão de `ModelBase` (`id`, `is_active`, `created_at`, `updated_at`), e `Player`/`Coach` compartilham dados pessoais via o modelo abstrato `Person` (nome, data de nascimento, altura, peso, tamanho do pé, tamanho de camisa).

## 🚀 Como rodar o projeto

### Pré-requisitos
- Python 3.10+
- pip

### Passo a passo

```bash
# Clone o repositório
git clone https://github.com/LucasDantas2701/Rumo_ao_Hexa_API.git
cd Rumo_ao_Hexa_API

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrações
python manage.py migrate

# Crie um superusuário (para acessar o admin)
python manage.py createsuperuser

# Rode o servidor
python manage.py runserver
```

A aplicação estará disponível em `http://127.0.0.1:8000/`, e o painel administrativo em `http://127.0.0.1:8000/admin/`.

## 📌 Status do Projeto

🚧 Em desenvolvimento. Atualmente implementados:

- [x] Modelagem de dados (`Team`, `Player`, `TeamGroup`, `Coach`)
- [x] Serializers do DRF
- [x] Registro dos modelos no Django Admin
- [ ] Endpoints REST (views/rotas da API)
- [ ] Autenticação e permissões
- [ ] Testes automatizados

## 📄 Licença

Este projeto está sob livre uso para fins de estudo. Defina uma licença (MIT, por exemplo) caso deseje formalizar o uso.

## 👤 Autor

Desenvolvido por [Lucas Dantas](https://github.com/LucasDantas2701).
