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


Arquitetura:

  Modelo: "Cliente-Servidor em 3 camadas"
  
  Camadas:
    - Presentation (Frontend): "Interface com o usuário (HTML5, CSS3, JS ou NextJS futuramente)"
    
    - Application (Backend): "Camada de lógica e comunicação com o banco de dados (Django)"
    
    - Database: "Camada de armazenamento de dados (PostgreSQL)"
    
  Justificativa:
    A arquitetura de três camadas garante modularidade, segurança e
    escalabilidade, permitindo que novas funcionalidades sejam adicionadas
    sem reestruturar o sistema.


Frameworks:

  Frontend:
  
    nome: "HTML5, CSS3 e JavaScript"
    
    opcional_futuro: "NextJS"
    
    motivo: 
      Fornece uma base simples para o desenvolvimento inicial e permite
      migração futura para frameworks mais robustos, caso necessário.
      
  Backend:
  
    nome: "Django (Python)"
    
    motivo: 
      Framework completo e seguro, com suporte nativo a banco de dados,
      autenticação e escalabilidade.
      
  Observação: 
    O Django foi escolhido por sua robustez e facilidade de integração com o PostgreSQL.
    O Flask foi descartado devido à necessidade de montagem manual de componentes.


Banco_de_Dados:

  tipo: "Relacional (SQL)"
  
  nome: "PostgreSQL"
  
  justificativa: 
    Banco relacional maduro, compatível com Django, ideal para aprendizado
    e projetos escaláveis. Oferece integridade referencial e suporte a consultas complexas.
    
  alternativas_consideradas:
    - "MySQL"
    - "MongoDB (não relacional, descartado neste momento)"
  status: "Escolhido e adotado para o desenvolvimento"


Ferramentas:

  versionamento: "Git + GitHub (pull Requests, branches e commits controlados)"
  
  documentação: "README.md e issues no GitHub"
  
  gerenciamento_de_projeto: "GitHub Projects / Scrum (Sprints organizadas)"
  
  design_e_planejamento: "Miro (mapas mentais, fluxos e wireframes) e Canva"
  
  ambiente_de_desenvolvimento: "Visual Studio Code"
  
  controle_de_dependências: "pip / virtualenv (Python)"
  
  sistema_operacional: "macOS e Windows (configurações padronizadas via requirements.txt)"


Levantamento_de_requisitos:

  Funcionais:
    - "O sistema deve apresentar informações institucionais sobre a entidade Einstein Coding."
    - "O sistema deve permitir navegação entre páginas."
    - "O sistema deve possuir layout responsivo."
    - "O sistema deve permitir exibição de imagens e ícones da entidade."
    - "O sistema deve permitir atualização manual de conteúdos estáticos."
    - "O sistema deve permitir integração futura com módulo de login autenticado."
    - "O sistema deve permitir inclusão futura de páginas dinâmicas."

  Nao_funcionais:
    - "O sistema deve ser desenvolvido em Django, garantindo modularidade e segurança."
    - "O banco de dados deve ser PostgreSQL, assegurando integridade e compatibilidade com o backend."
    - "O código deve seguir boas práticas de versionamento no GitHub, com commits e revisões via Pull Request."
    - "O sistema deve manter separação clara entre frontend, backend e banco de dados."
    - "O sistema deve apresentar desempenho estável e tempo de resposta adequado."
    - "O sistema deve ter documentação completa e clara no README.md."
    - "O sistema deve permitir autenticação segura em versões futuras."
    - "A arquitetura deve ser escalável e flexível para futuras integrações (APIs e módulos)."

Possibilidades_futuras:
  - "Implementar sistema de login e autenticação de usuários (com tokens)."
  - "Adicionar painel administrativo para gerenciamento de conteúdo."
  - "Integrar APIs externas para atualização dinâmica de informações."
  - "Realizar deploy em serviços de nuvem (AWS, Render, etc.)."
  - "Adicionar blog interno e área logada para membros."


Status_atual:

  fase: "Levantamento de requisitos e definição de arquitetura, frameworks e layout"
  
  sprint: "Sprint 1 - Estruturação inicial do repositório e escolha das tecnologias e design"
  
  proximo_passo: "Iniciar prototipagem e implementação da camada Presentation"
