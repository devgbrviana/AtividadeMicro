# 📚 API de Atividades

Este repositório contém a API de Atividades, desenvolvida com Flask e SQLAlchemy, como parte de uma arquitetura baseada em microsserviços.

## 🧩 Arquitetura

A API de Atividades é um microsserviço que faz parte de um sistema maior chamado **School System**, sendo responsável exclusivamente pelo gerenciamento das atividades que o professor passa para seus alunos.

> ⚠️ Esta API **depende** da API de Gerenciamento Escolar (School System), que deve estar em execução e acessível localmente.

### 📡 Comunicação entre Microsserviços

A validação do professor ocorre via requisição HTTP REST:
- GET /professor/<id>` – Utilizada para verificar se o professor existe na API externa.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x  
- Flask  
- SQLAlchemy  
- SQLite (como banco de dados local)  
- Requests (para consumo da API externa)

---

## ▶️ Como Executar a API

1. **Clone o repositório**

bash
git clone https://github.com/beatrizbramont/AtividadeMicros.git
cd AtividadeMicros
Crie um ambiente virtual (opcional, mas recomendado)

bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Instale as dependências

bash
Copiar
Editar
pip install -r requirements.txt
Execute a API

bash
Copiar
Editar
python app.py
A aplicação estará disponível em: http://127.0.0.1:5000

📝 O banco de dados é criado automaticamente na primeira execução.

📡 Endpoints Principais
GET /atividades – Lista todas as atividades

POST /atividades – Cria uma nova atividade

GET /atividades/<id> – Detalha uma atividade

📥 Exemplo de corpo JSON para criação
json
Copiar
Editar
{
  "professor_id": 2,
  "tipo": "Trabalho em Grupo",
  "data_entrega": "2025-11-15",
  "titulo": "Projeto Integrador de APIs",
  "descricao": "Desenvolver um sistema completo com microsserviços"
}
🔗 Dependência Externa
Certifique-se de que a API de Gerenciamento Escolar esteja rodando em:

http://127.0.0.1:8001

E que o endpoint GET /professor/<id> esteja funcionando corretamente para que a validação seja realizada com sucesso.

📦 Estrutura do Projeto
arduino
Copiar
Editar
AtividadeMicros/
│
├── controller/
│   └── ativ_controller.py      
│
├── instance/
│   └── atividades.db           
│
├── models/
│   └── ativ_model.py      
│
├── app.py                    
├── config.py                 
├── database.py               
├── Dockerfile 
├── README.md               
└── requirements.txt
🛠️ Futuras Melhorias
Integração via fila (RabbitMQ) com outros microsserviços

Autenticação de usuários

Inserção das rotas PUT e DELETE

PUT /atividades/<id> – Atualiza uma atividade

DELETE /atividades/<id> – Remove uma atividade

🧑‍💻 Autores
Gabriel de Souza Viana

Arthur Mattos

Pablo Barros
