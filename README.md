# fastapi-template
Um template de FastAPI com SQLAlchemy, Alembic e autenticação

## Como usar

### Instalar as dependências

```bash
uv sync
```

### Executar a API

```bash
uv run uvicorn apps.main:app --reload
```

### Comandos via Makefile

```bash
make install
make run
make migration msg="Add exams model"
make upgrade
make downgrade
make history
make current
```

#### Descrição de cada comando

- `make install` — instala as dependências do projeto com `uv sync`.
- `make run` — inicia a API localmente com recarregamento automático.
- `make migration msg="..."` — gera uma nova migration com base nas alterações dos modelos usando `alembic revision --autogenerate`.
- `make upgrade` — aplica todas as migrations pendentes no banco local.
- `make downgrade` — reverte uma migration, voltando um passo atrás.
- `make history` — exibe o histórico de migrations geradas.
- `make current` — mostra a revisão atual aplicada no banco.

