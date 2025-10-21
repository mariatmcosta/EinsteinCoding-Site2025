# Site Einstein Coding - 2025
Site institucional da Empresa Júnior Einstein Coding - 2025

Repositório oficial para o desenvolvimento do site da **Empresa Júnior Einstein Coding**, voltada para soluções de tecnologia e programação na área da saúde.

## Objetivo
Criar um site institucional funcional e responsivo para apresentar:
- A gestão atual e o hall da fama das gestões passadas;
- Nossos projetos e parcerias;
- Notícias, avisos e código social;
- Sobre nós;
- Contato;
- Área de login para membros e visitantes (a longo prazo).

---

## Estrutura do Projeto

```
EinsteinCoding-Site2025/
│
├── app.py
├── requirements.txt
├── /static/
│   ├── /css/
│   │   └── style.css
│   ├── /js/
│   │   └── script.js
│   └── /imgs/
│       ├── logo.png
│       └── equipe2025.jpg
└── /templates/
    ├── base.html
    ├── home.html
    └── gestao.html
```

---

## Equipe
**Scrum Master:** Maria Eduarda Taveiros Martins Costa

**Product Owner:** Henrique Machiaveli Martins

**Desenvolvedores:** Ana Beatriz Mamede Pampalon, Antonio Elias Faiçal Junior, Carolina Scilingo, Maria Vitória de Moura Coutinho e Bruna Sanches Paloni

---

## Mapa mental do Projeto
![Mapa mental do site Einstein Coding 2025](https://github.com/mariatmcosta/EinsteinCoding-Site2025/blob/main/static/imgs/mapa-mental-site.png)

---

## Especificações Técnicas do Projeto
## Projeto: Site da Entidade Einstein Coding

arquitetura:
  modelo: "Cliente-Servidor em 3 camadas"
  camadas:
    - Presentation (Frontend): "Interface com o usuário (HTML5, CSS3, JS ou NextJS futuramente)"
    - Application (Backend): "Camada de lógica e comunicação com o banco de dados (Django)"
    - Database: "Camada de armazenamento de dados (PostgreSQL)"
  justificativa: >
    A arquitetura de três camadas garante modularidade, segurança e
    escalabilidade, permitindo que novas funcionalidades sejam adicionadas
    sem reestruturar o sistema.

frameworks:
  frontend:
    nome: "HTML5, CSS3 e JavaScript"
    opcional_futuro: "NextJS"
    motivo: >
      Fornece uma base simples para o desenvolvimento inicial e permite
      migração futura para frameworks mais robustos, caso necessário.
  backend:
    nome: "Django (Python)"
    motivo: >
      Framework completo e seguro, com suporte nativo a banco de dados,
      autenticação e escalabilidade.
  observação: >
    O Django foi escolhido por sua robustez e facilidade de integração com o PostgreSQL.
    O Flask foi descartado devido à necessidade de montagem manual de componentes.

banco_de_dados:
  tipo: "Relacional (SQL)"
  nome: "PostgreSQL"
  justificativa: >
    Banco relacional maduro, compatível com Django, ideal para aprendizado
    e projetos escaláveis. Oferece integridade referencial e suporte a consultas complexas.
  alternativas_consideradas:
    - "MySQL"
    - "MongoDB (não relacional, mas descartado neste momento)"
  status: "Escolhido e adotado para o desenvolvimento"

ferramentas:
  versionamento: "Git + GitHub (Pull Requests, branches e commits controlados)"
  documentação: "README.md e issues no GitHub"
  gerenciamento_de_projeto: "GitHub Projects / Scrum (Sprints organizadas)"
  design_e_planejamento: "Miro (mapas mentais, fluxos e wireframes)"
  ambiente_de_desenvolvimento: "Visual Studio Code"
  controle_de_dependências: "pip / virtualenv (Python)"
  sistema_operacional: "macOS e Windows (configurações padronizadas via requirements.txt)"

levantamento_de_requisitos:
  funcionais:
    - "O sistema deve apresentar informações institucionais sobre o grupo Einstein Coding."
    - "O sistema deve permitir navegação entre páginas (ex.: Sobre, Projetos, Equipe, Contato)."
    - "O sistema deve possuir layout responsivo (mobile e desktop)."
    - "O sistema deve permitir exibição de imagens e ícones da entidade."
    - "O sistema deve permitir atualização manual de conteúdos estáticos (textos e imagens)."
    - "O sistema deve permitir integração futura com módulo de login autenticado."
    - "O sistema deve permitir inclusão futura de páginas dinâmicas (projetos, artigos, eventos)."
    - "O sistema deve aceitar expansão para formulários de contato com coleta de dados de visitantes."

  nao_funcionais:
    - "O sistema deve ser desenvolvido em Django, garantindo modularidade e segurança."
    - "O banco de dados deve ser PostgreSQL, assegurando integridade e compatibilidade com o backend."
    - "O código deve seguir boas práticas de versionamento no GitHub, com commits e revisões via Pull Request."
    - "O sistema deve manter separação clara entre frontend, backend e banco de dados."
    - "O sistema deve apresentar desempenho estável e tempo de resposta adequado."
    - "O sistema deve ter documentação completa e clara no README.md."
    - "O sistema deve permitir autenticação segura em versões futuras."
    - "A arquitetura deve ser escalável e flexível para futuras integrações (APIs e módulos)."

possibilidades_futuras:
  - "Implementar sistema de login e autenticação de usuários (com tokens)."
  - "Adicionar painel administrativo para gerenciamento de conteúdo."
  - "Integrar APIs externas para atualização dinâmica de informações."
  - "Realizar deploy em serviços de nuvem (AWS, Render, etc.)."
  - "Adicionar blog interno e área logada para membros."

status_atual:
  fase: "Levantamento de requisitos e definição de arquitetura"
  sprint: "Sprint 1 - Estruturação inicial do repositório e escolha das tecnologias"
  proximo_passo: "Iniciar prototipagem e implementação da camada Presentation"
