import tkinter as tk
from tkinter import ttk, messagebox

# =====================================================================
# BANCO DE DADOS DOS CURSOS E DISCIPLINAS
# =====================================================================
# Aqui você define todos os cursos, disciplinas e suas dependências
# Para adicionar novos cursos, copie a estrutura abaixo e preencha com suas disciplinas
# =====================================================================

# --- Definição dos Cursos, Disciplinas e Pré-requisitos ---
CURSOS = {


    # CURSO 1: Engenharia de Energias - Foco em fontes renováveis e eficiência energética
    "Engenharia de Energias": {
        # NÍVEL 1 - Disciplinas básicas de formação
        "Introdução à Engenharia de Energias": {"requisitos": [], "nivel": 1, "carga_horaria": 68},
        # Disciplina introdutória
        "Cálculo Diferencial e Integral I": {"requisitos": [], "nivel": 1, "carga_horaria": 85},  # Base matemática
        "Física Geral e Experimental I": {"requisitos": [], "nivel": 1, "carga_horaria": 68},  # Base física
        "Química Geral": {"requisitos": [], "nivel": 1, "carga_horaria": 68},  # Base química

        # NÍVEL 2 - Disciplinas que desenvolvem as bases do nível 1
        "Termodinâmica Aplicada": {"requisitos": ["Cálculo Diferencial e Integral I", "Física Geral e Experimental I"],
                                   "nivel": 2, "carga_horaria": 68},  # Requer bases matemática e física
        "Cálculo Diferencial e Integral II": {"requisitos": ["Cálculo Diferencial e Integral I"], "nivel": 2,
                                              "carga_horaria": 85},  # Continuação da matemática
        "Mecânica dos Fluidos": {"requisitos": ["Cálculo Diferencial e Integral I"], "nivel": 2, "carga_horaria": 68},
        # Base para energias
        "Desenho Técnico e CAD": {"requisitos": [], "nivel": 2, "carga_horaria": 68},  # Ferramentas de projeto

        # NÍVEL 3 - Especialização em áreas específicas de energia
        "Energias Renováveis I": {"requisitos": ["Termodinâmica Aplicada"], "nivel": 3, "carga_horaria": 68},
        # Foco em fontes renováveis
        "Conversão de Energia": {"requisitos": ["Termodinâmica Aplicada", "Mecânica dos Fluidos"], "nivel": 3,
                                 "carga_horaria": 68},  # Processos de conversão
        "Sistemas Térmicos": {"requisitos": ["Termodinâmica Aplicada"], "nivel": 3, "carga_horaria": 68},
        # Sistemas de aquecimento
        "Eletricidade e Magnetismo": {"requisitos": ["Física Geral e Experimental I"], "nivel": 3, "carga_horaria": 68},
        # Base elétrica

        # NÍVEL 4 - Tecnologias avançadas e aplicações
        "Energia Solar Fotovoltaica": {"requisitos": ["Energias Renováveis I", "Eletricidade e Magnetismo"], "nivel": 4,
                                       "carga_horaria": 68},  # Especialização solar
        "Energia Eólica": {"requisitos": ["Energias Renováveis I", "Mecânica dos Fluidos"], "nivel": 4,
                           "carga_horaria": 68},  # Especialização eólica
        "Armazenamento de Energia": {"requisitos": ["Conversão de Energia"], "nivel": 4, "carga_horaria": 68},
        # Tecnologias de armazenamento
        "Eficiência Energética": {"requisitos": ["Sistemas Térmicos"], "nivel": 4, "carga_horaria": 68},
        # Otimização energética

        # NÍVEL 5 - Projetos e gestão em energia
        "Gestão de Projetos em Energia": {"requisitos": ["Energia Solar Fotovoltaica", "Energia Eólica"], "nivel": 5,
                                          "carga_horaria": 68},  # Gestão de projetos
        "Energias Renováveis II": {"requisitos": ["Energias Renováveis I"], "nivel": 5, "carga_horaria": 68},
        # Tópicos avançados
        "Sistemas de Potência": {"requisitos": ["Eletricidade e Magnetismo"], "nivel": 5, "carga_horaria": 68},
        # Sistemas elétricos de potência
        "Economia da Energia": {"requisitos": ["Introdução à Engenharia de Energias"], "nivel": 5, "carga_horaria": 68},
        # Aspectos econômicos

        # NÍVEL 6 - Disciplinas finais e integração
        "Projeto Final em Energias": {"requisitos": ["Gestão de Projetos em Energia", "Energias Renováveis II"],
                                      "nivel": 6, "carga_horaria": 102},  # Projeto de conclusão
        "Políticas Energéticas": {"requisitos": ["Economia da Energia"], "nivel": 6, "carga_horaria": 68},
        # Políticas públicas
        "Sistemas Híbridos de Energia": {
            "requisitos": ["Energia Solar Fotovoltaica", "Energia Eólica", "Armazenamento de Energia"], "nivel": 6,
            "carga_horaria": 68},  # Integração de sistemas
        "Tópicos Especiais em Energia": {"requisitos": ["Sistemas de Potência"], "nivel": 6, "carga_horaria": 68},
        # Temas emergentes
    },

    # CURSO 2: Engenharia de Tecnologia Assistiva - Foco em acessibilidade e inclusão
    "Engenharia de Tecnologia Assistiva": {
        # NÍVEL 1 - Fundamentos da tecnologia assistiva
        "Introdução à Tecnologia Assistiva": {"requisitos": [], "nivel": 1, "carga_horaria": 68},  # Conceitos básicos
        "Anatomia e Fisiologia Humana": {"requisitos": [], "nivel": 1, "carga_horaria": 68},  # Base biológica
        "Matemática Aplicada": {"requisitos": [], "nivel": 1, "carga_horaria": 68},  # Ferramentas matemáticas
        "Ética e Direitos Humanos": {"requisitos": [], "nivel": 1, "carga_horaria": 68},  # Aspectos éticos

        # NÍVEL 2 - Desenvolvimento de habilidades técnicas
        "Biomecânica Aplicada": {"requisitos": ["Anatomia e Fisiologia Humana", "Matemática Aplicada"], "nivel": 2,
                                 "carga_horaria": 68},  # Análise do movimento
        "Eletrônica Básica": {"requisitos": ["Matemática Aplicada"], "nivel": 2, "carga_horaria": 68},
        # Circuitos eletrônicos
        "Programação para Dispositivos": {"requisitos": [], "nivel": 2, "carga_horaria": 68},  # Programação aplicada
        "Ergonomia e Acessibilidade": {"requisitos": ["Introdução à Tecnologia Assistiva"], "nivel": 2,
                                       "carga_horaria": 68},  # Design inclusivo

        # NÍVEL 3 - Tecnologias específicas de assistiva
        "Próteses e Órteses": {"requisitos": ["Biomecânica Aplicada"], "nivel": 3, "carga_horaria": 68},
        # Dispositivos corporais
        "Sistemas de Comunicação Aumentativa": {"requisitos": ["Programação para Dispositivos"], "nivel": 3,
                                                "carga_horaria": 68},  # Comunicação alternativa
        "Sensores e Atuadores": {"requisitos": ["Eletrônica Básica"], "nivel": 3, "carga_horaria": 68},
        # Componentes eletrônicos
        "Reabilitação Tecnológica": {"requisitos": ["Ergonomia e Acessibilidade"], "nivel": 3, "carga_horaria": 68},
        # Processos de reabilitação

        # NÍVEL 4 - Desenvolvimento de sistemas complexos
        "Robótica Assistiva": {"requisitos": ["Sensores e Atuadores", "Programação para Dispositivos"], "nivel": 4,
                               "carga_horaria": 68},  # Robótica aplicada
        "Sistemas de Mobilidade": {"requisitos": ["Próteses e Órteses"], "nivel": 4, "carga_horaria": 68},
        # Tecnologias de locomoção
        "Interface Cérebro-Máquina": {"requisitos": ["Eletrônica Básica", "Anatomia e Fisiologia Humana"], "nivel": 4,
                                      "carga_horaria": 68},  # Interfaces neurais
        "Avaliação de Tecnologias Assistivas": {"requisitos": ["Reabilitação Tecnológica"], "nivel": 4,
                                                "carga_horaria": 68},  # Métodos de avaliação

        # NÍVEL 5 - Gestão e inovação em TA
        "Gestão de Projetos em TA": {"requisitos": ["Avaliação de Tecnologias Assistivas"], "nivel": 5,
                                     "carga_horaria": 68},  # Administração de projetos
        "Inovação em Tecnologia Assistiva": {"requisitos": ["Robótica Assistiva", "Sistemas de Mobilidade"], "nivel": 5,
                                             "carga_horaria": 68},  # Desenvolvimento criativo
        "Legislação e Acessibilidade": {"requisitos": ["Ética e Direitos Humanos"], "nivel": 5, "carga_horaria": 68},
        # Marco legal
        "Tecnologias para Deficiência Visual": {"requisitos": ["Sistemas de Comunicação Aumentativa"], "nivel": 5,
                                                "carga_horaria": 68},  # Especialização visual

        # NÍVEL 6 - Integração e projeto final
        "Projeto Final em TA": {"requisitos": ["Gestão de Projetos em TA", "Inovação em Tecnologia Assistiva"],
                                "nivel": 6, "carga_horaria": 102},  # Trabalho de conclusão
        "Tecnologias para Deficiência Auditiva": {"requisitos": ["Sensores e Atuadores"], "nivel": 6,
                                                  "carga_horaria": 68},  # Especialização auditiva
        "Sistemas Inteligentes de Apoio": {"requisitos": ["Interface Cérebro-Máquina"], "nivel": 6,
                                           "carga_horaria": 68},  # IA aplicada
        "Estágio Supervisionado em TA": {"requisitos": ["Legislação e Acessibilidade"], "nivel": 6,
                                         "carga_horaria": 68},  # Experiência prática
    },

    # CURSO 3: Engenharia de Materiais - Foco em desenvolvimento e aplicação de materiais
    "Engenharia de Materiais": {
        # NÍVEL 1 - Fundamentos da ciência dos materiais
        "Introdução à Engenharia de Materiais": {"requisitos": [], "nivel": 1, "carga_horaria": 68},
        # Visão geral da área
        "Química dos Materiais": {"requisitos": [], "nivel": 1, "carga_horaria": 68},  # Base química
        "Cálculo para Materiais": {"requisitos": [], "nivel": 1, "carga_horaria": 85},  # Matemática aplicada
        "Física dos Sólidos": {"requisitos": [], "nivel": 1, "carga_horaria": 68},  # Propriedades físicas

        # NÍVEL 2 - Caracterização e propriedades
        "Estrutura dos Materiais": {"requisitos": ["Química dos Materiais", "Física dos Sólidos"], "nivel": 2,
                                    "carga_horaria": 68},  # Estrutura atômica
        "Termodinâmica dos Materiais": {"requisitos": ["Cálculo para Materiais"], "nivel": 2, "carga_horaria": 68},
        # Comportamento térmico
        "Mecânica dos Materiais": {"requisitos": ["Cálculo para Materiais"], "nivel": 2, "carga_horaria": 68},
        # Resistência mecânica
        "Laboratório de Materiais I": {"requisitos": ["Introdução à Engenharia de Materiais"], "nivel": 2,
                                       "carga_horaria": 68},  # Prática laboratorial

        # NÍVEL 3 - Classes de materiais
        "Materiais Metálicos": {"requisitos": ["Estrutura dos Materiais", "Termodinâmica dos Materiais"], "nivel": 3,
                                "carga_horaria": 68},  # Metais e ligas
        "Materiais Poliméricos": {"requisitos": ["Química dos Materiais"], "nivel": 3, "carga_horaria": 68},
        # Plásticos e polímeros
        "Materiais Cerâmicos": {"requisitos": ["Estrutura dos Materiais"], "nivel": 3, "carga_horaria": 68},
        # Cerâmicas e vidros
        "Ensaios Mecânicos": {"requisitos": ["Mecânica dos Materiais"], "nivel": 3, "carga_horaria": 68},
        # Testes de propriedades

        # NÍVEL 4 - Processos e transformação
        "Processos de Fabricação": {"requisitos": ["Materiais Metálicos", "Materiais Poliméricos"], "nivel": 4,
                                    "carga_horaria": 68},  # Métodos de produção
        "Tratamentos Térmicos": {"requisitos": ["Termodinâmica dos Materiais"], "nivel": 4, "carga_horaria": 68},
        # Modificação de propriedades
        "Materiais Compósitos": {"requisitos": ["Materiais Metálicos", "Materiais Cerâmicos", "Materiais Poliméricos"],
                                 "nivel": 4, "carga_horaria": 68},  # Materiais híbridos
        "Laboratório de Materiais II": {"requisitos": ["Laboratório de Materiais I"], "nivel": 4, "carga_horaria": 68},
        # Prática avançada

        # NÍVEL 5 - Materiais avançados e aplicações
        "Materiais para Eletrônica": {"requisitos": ["Física dos Sólidos"], "nivel": 5, "carga_horaria": 68},
        # Semicondutores e outros
        "Nanomateriais": {"requisitos": ["Estrutura dos Materiais"], "nivel": 5, "carga_horaria": 68},
        # Materiais em escala nanométrica
        "Corrosão e Proteção": {"requisitos": ["Química dos Materiais", "Materiais Metálicos"], "nivel": 5,
                                "carga_horaria": 68},  # Degradação e prevenção
        "Seleção de Materiais": {"requisitos": ["Ensaios Mecânicos", "Processos de Fabricação"], "nivel": 5,
                                 "carga_horaria": 68},  # Critérios de escolha

        # NÍVEL 6 - Projeto e sustentabilidade
        "Projeto Final em Materiais": {"requisitos": ["Seleção de Materiais", "Laboratório de Materiais II"],
                                       "nivel": 6, "carga_horaria": 102},  # Trabalho de conclusão
        "Materiais Sustentáveis": {"requisitos": ["Materiais Poliméricos", "Materiais Cerámicos"], "nivel": 6,
                                   "carga_horaria": 68},  # Aspectos ambientais
        "Tecnologia de Superfícies": {"requisitos": ["Corrosão e Proteção"], "nivel": 6, "carga_horaria": 68},
        # Modificação superficial
        "Gestão da Qualidade em Materiais": {"requisitos": ["Ensaios Mecânicos"], "nivel": 6, "carga_horaria": 68},
        # Controle de qualidade
    },

    # CURSO 4: Engenharia de Produção - Foco em otimização de processos produtivos
    "Engenharia de Produção": {
        # NÍVEL 1 - Fundamentos da engenharia de produção
        "Introdução à Engenharia de Produção": {"requisitos": [], "nivel": 1, "carga_horaria": 68},
        # Visão geral da área
        "Cálculo Aplicado à Produção": {"requisitos": [], "nivel": 1, "carga_horaria": 85},  # Matemática industrial
        "Estatística Básica": {"requisitos": [], "nivel": 1, "carga_horaria": 68},  # Análise de dados
        "Gestão de Negócios": {"requisitos": [], "nivel": 1, "carga_horaria": 68},  # Administração empresarial

        # NÍVEL 2 - Ferramentas de gestão e controle
        "Pesquisa Operacional I": {"requisitos": ["Cálculo Aplicado à Produção", "Estatística Básica"], "nivel": 2,
                                   "carga_horaria": 68},  # Otimização matemática
        "Gestão da Qualidade": {"requisitos": ["Estatística Básica"], "nivel": 2, "carga_horaria": 68},
        # Controle estatístico
        "Economia Empresarial": {"requisitos": ["Gestão de Negócios"], "nivel": 2, "carga_horaria": 68},
        # Aspectos econômicos
        "Ergonomia e Segurança": {"requisitos": ["Introdução à Engenharia de Produção"], "nivel": 2,
                                  "carga_horaria": 68},  # Condições de trabalho

        # NÍVEL 3 - Processos produtivos
        "Planejamento e Controle da Produção": {"requisitos": ["Pesquisa Operacional I"], "nivel": 3,
                                                "carga_horaria": 68},  # Programação da produção
        "Gestão de Custos": {"requisitos": ["Economia Empresarial"], "nivel": 3, "carga_horaria": 68},
        # Análise de custos
        "Processos de Fabricação": {"requisitos": [], "nivel": 3, "carga_horaria": 68},  # Tecnologias de manufatura
        "Logística Empresarial": {"requisitos": ["Pesquisa Operacional I"], "nivel": 3, "carga_horaria": 68},
        # Gestão da cadeia

        # NÍVEL 4 - Sistemas integrados
        "Sistemas de Produção": {"requisitos": ["Planejamento e Controle da Produção", "Processos de Fabricação"],
                                 "nivel": 4, "carga_horaria": 68},  # Integração de sistemas
        "Gestão de Projetos": {"requisitos": ["Gestão de Custos"], "nivel": 4, "carga_horaria": 68},
        # Metodologias de projeto
        "Simulação de Sistemas": {"requisitos": ["Pesquisa Operacional I"], "nivel": 4, "carga_horaria": 68},
        # Modelagem computacional
        "Gestão Ambiental": {"requisitos": ["Gestão da Qualidade"], "nivel": 4, "carga_horaria": 68},
        # Sustentabilidade

        # NÍVEL 5 - Otimização e melhoria
        "Pesquisa Operacional II": {"requisitos": ["Pesquisa Operacional I"], "nivel": 5, "carga_horaria": 68},
        # Métodos avançados
        "Gestão da Manutenção": {"requisitos": ["Sistemas de Produção"], "nivel": 5, "carga_horaria": 68},
        # Manutenção industrial
        "Engenharia do Produto": {"requisitos": ["Gestão de Projetos"], "nivel": 5, "carga_horaria": 68},
        # Desenvolvimento de produtos
        "Gestão Estratégica": {"requisitos": ["Economia Empresarial"], "nivel": 5, "carga_horaria": 68},
        # Planejamento estratégico

        # NÍVEL 6 - Integração e projeto final
        "Projeto Final em Produção": {"requisitos": ["Gestão de Projetos", "Pesquisa Operacional II"], "nivel": 6,
                                      "carga_horaria": 102},  # Trabalho de conclusão
        "Sistemas de Informação": {"requisitos": ["Simulação de Sistemas"], "nivel": 6, "carga_horaria": 68},
        # TI aplicada à produção
        "Gestão da Inovação": {"requisitos": ["Engenharia do Produto"], "nivel": 6, "carga_horaria": 68},
        # Processos inovadores
        "Estágio Supervisionado": {"requisitos": ["Gestão Estratégica"], "nivel": 6, "carga_horaria": 68},
        # Experiência profissional
    },

    # =====================================================================
    # NOVO CURSO: Bacharelado Interdisciplinar em Energia e Sustentabilidade
    # =====================================================================
    "Bacharelado Interdisciplinar em Energia e Sustentabilidade": {
        # NÍVEL 1 - Primeiro Período (Total CH: 442h)
        "METODOLOGIA DA PESQUISA": {"requisitos": [], "nivel": 1, "carga_horaria": 34},
        # Disciplina introdutória à pesquisa
        "FUNDAMENTOS DA MATEMÁTICA": {"requisitos": [], "nivel": 1, "carga_horaria": 68},
        # Base matemática fundamental (SEM PRÉ-REQUISITOS PARA OUTRAS)
        "DIVERSIDADE, CULTURA E RELAÇÕES ÉTNICAS": {"requisitos": [], "nivel": 1, "carga_horaria": 68},
        # Aspectos sociais e culturais
        "OFICINA DE LEITURA E PRODUÇÃO DE TEXTOS": {"requisitos": [], "nivel": 1, "carga_horaria": 68},
        # Comunicação e expressão
        "FUNDAMENTOS DE QUÍMICA I": {"requisitos": [], "nivel": 1, "carga_horaria": 68},  # Base química inicial
        "PROGRAMAÇÃO DE COMPUTADORES I": {"requisitos": [], "nivel": 1, "carga_horaria": 68},
        # Introdução à programação
        "INTRODUÇÃO ÀS TECNOLOGIAS": {"requisitos": [], "nivel": 1, "carga_horaria": 68},  # Tecnologias aplicadas

        # NÍVEL 2 - Segundo Período (Total CH: 493h)
        "ADMINISTRAÇÃO": {"requisitos": ["METODOLOGIA DA PESQUISA"], "nivel": 2, "carga_horaria": 68},
        # Gestão organizacional
        "CIÊNCIAS DO AMBIENTE": {"requisitos": ["FUNDAMENTOS DE QUÍMICA I"], "nivel": 2, "carga_horaria": 68},
        # Estudos ambientais
        "GEOMETRIA ANALÍTICA": {"requisitos": [], "nivel": 2, "carga_horaria": 68},
        # Matemática avançada (SEM PRÉ-REQUISITO DE FUNDAMENTOS DA MATEMÁTICA)
        "PROJETO INTERDISCIPLINAR I": {"requisitos": ["METODOLOGIA DA PESQUISA"], "nivel": 2, "carga_horaria": 34},
        # Primeiro projeto integrador
        "LABORATÓRIO DE LÍNGUA INGLESA I": {"requisitos": ["OFICINA DE LEITURA E PRODUÇÃO DE TEXTOS"], "nivel": 2,
                                            "carga_horaria": 34},  # Inglês técnico
        "BASES TEÓRICAS E EXPERIMENTAIS DA FÍSICA": {"requisitos": [], "nivel": 2, "carga_horaria": 68},
        # Fundamentos físicos (SEM PRÉ-REQUISITO DE FUNDAMENTOS DA MATEMÁTICA)
        "CÁLCULO DIFERENCIAL E INTEGRAL I": {"requisitos": [], "nivel": 2, "carga_horaria": 85},
        # Cálculo básico (SEM PRÉ-REQUISITO DE FUNDAMENTOS DA MATEMÁTICA)
        "FUNDAMENTOS DE QUÍMICA II": {"requisitos": ["FUNDAMENTOS DE QUÍMICA I"], "nivel": 2, "carga_horaria": 68},
        # Química avançada

        # NÍVEL 3 - Terceiro Período (Total CH: 510h)
        "GEOPOLÍTICA DA ENERGIA": {"requisitos": ["CIÊNCIAS DO AMBIENTE"], "nivel": 3, "carga_horaria": 51},
        # Aspectos geopolíticos da energia
        "PROJETO INTERDISCIPLINAR II": {"requisitos": ["PROJETO INTERDISCIPLINAR I"], "nivel": 3, "carga_horaria": 34},
        # Segundo projeto integrador
        "PROBABILIDADE E ESTATÍSTICA": {"requisitos": ["CÁLCULO DIFERENCIAL E INTEGRAL I"], "nivel": 3,
                                        "carga_horaria": 51},  # Análise estatística
        "FENÔMENOS MECÂNICOS": {"requisitos": ["BASES TEÓRICAS E EXPERIMENTAIS DA FÍSICA"], "nivel": 3,
                                "carga_horaria": 102},  # Mecânica aplicada
        "CÁLCULO DIFERENCIAL E INTEGRAL II": {"requisitos": ["CÁLCULO DIFERENCIAL E INTEGRAL I"], "nivel": 3,
                                              "carga_horaria": 85},  # Cálculo intermediário
        "ÁLGEBRA LINEAR I": {"requisitos": ["GEOMETRIA ANALÍTICA"], "nivel": 3, "carga_horaria": 51},
        # Álgebra avançada
        "LIBRAS": {"requisitos": [], "nivel": 3, "carga_horaria": 68},  # Língua Brasileira de Sinais
        "DESENHO TÉCNICO I": {"requisitos": ["INTRODUÇÃO ÀS TECNOLOGIAS"], "nivel": 3, "carga_horaria": 68},
        # Representação técnica

        # NÍVEL 4 - Quarto Período (Total CH: 527h)
        "ECONOMIA": {"requisitos": ["ADMINISTRAÇÃO"], "nivel": 4, "carga_horaria": 68},  # Princípios econômicos
        "ENERGIA, DESENVOLVIMENTO E SUSTENTABILIDADE": {"requisitos": ["GEOPOLÍTICA DA ENERGIA"], "nivel": 4,
                                                        "carga_horaria": 51},  # Sustentabilidade energética
        "UNIVERSIDADE, SOCIEDADE E AMBIENTE": {"requisitos": ["DIVERSIDADE, CULTURA E RELAÇÕES ÉTNICAS"], "nivel": 4,
                                               "carga_horaria": 68},  # Relações universidade-sociedade
        "PROJETO INTERDISCIPLINAR III": {"requisitos": ["PROJETO INTERDISCIPLINAR II"], "nivel": 4,
                                         "carga_horaria": 34},  # Terceiro projeto integrador
        "OSCILAÇÕES, FLUIDOS E TERMODINÂMICA": {"requisitos": ["FENÔMENOS MECÂNICOS"], "nivel": 4,
                                                "carga_horaria": 102},  # Fenômenos físicos avançados
        "CÁLCULO DIFERENCIAL E INTEGRAL III": {"requisitos": ["CÁLCULO DIFERENCIAL E INTEGRAL II"], "nivel": 4,
                                               "carga_horaria": 68},  # Cálculo avançado
        "CIÊNCIA DOS MATERIAIS": {"requisitos": ["FUNDAMENTOS DE QUÍMICA II"], "nivel": 4, "carga_horaria": 68},
        # Estudo dos materiais
        "MECÂNICA DOS SÓLIDOS I": {"requisitos": ["FENÔMENOS MECÂNICOS"], "nivel": 4, "carga_horaria": 68},
        # Resistência dos materiais

        # NÍVEL 5 - Quinto Período (Total CH: 272h - período parcial)
        "PROJETO INTERDISCIPLINAR IV": {"requisitos": ["PROJETO INTERDISCIPLINAR III"], "nivel": 5,
                                        "carga_horaria": 34},  # Quarto projeto integrador
        "FENÔMENOS ELETROMAGNÉTICOS": {"requisitos": ["OSCILAÇÕES, FLUIDOS E TERMODINÂMICA"], "nivel": 5,
                                       "carga_horaria": 102},  # Eletromagnetismo
        "CÁLCULO NUMÉRICO": {"requisitos": ["CÁLCULO DIFERENCIAL E INTEGRAL III", "ÁLGEBRA LINEAR I"], "nivel": 5,
                             "carga_horaria": 68},  # Métodos numéricos
        "FENÔMENOS DE TRANSPORTE": {"requisitos": ["OSCILAÇÕES, FLUIDOS E TERMODINÂMICA"], "nivel": 5,
                                    "carga_horaria": 68},  # Transporte de massa e energia

        # NÍVEL 6 - Sexto Período (Total CH: 187h)
        "ELETRICIDADE APLICADA": {"requisitos": ["FENÔMENOS ELETROMAGNÉTICOS"], "nivel": 6, "carga_horaria": 68},
        # Aplicações elétricas
        "TRABALHO DE CONCLUSÃO DE CURSO": {"requisitos": ["PROJETO INTERDISCIPLINAR IV"], "nivel": 6,
                                           "carga_horaria": 51},  # Projeto final
        "TERMODINÂMICA": {"requisitos": ["OSCILAÇÕES, FLUIDOS E TERMODINÂMICA"], "nivel": 6, "carga_horaria": 68},
        # Termodinâmica avançada
    }

    # =====================================================================
    # PARA ADICIONAR MAIS CURSOS:
    # 1. Copie a estrutura acima (cole após a última chave } e adicione uma vírgula)
    # 2. Altere o nome do curso (ex: "Medicina", "Direito", etc.)
    # 3. Defina as disciplinas seguindo o padrão:
    #    "Nome da Disciplina": {"requisitos": ["lista", "de", "pré-requisitos"], "nivel": número, "carga_horaria": número}
    # =====================================================================
}


# =====================================================================
# CLASSE PRINCIPAL DA APLICAÇÃO
# =====================================================================
# Esta classe gerencia toda a interface e lógica do programa
# =====================================================================

class AplicacaoProgressoAcademico:
    def __init__(self, root):
        """
        Inicializa a aplicação principal
        root: janela principal do Tkinter
        """
        self.root = root
        self.root.title("🎓 Progresso Acadêmico Interativo")
        # Define tamanho inicial maior para melhor visualização
        self.root.geometry("1000x700")  # Aumentado para 1000x700 para caber mais conteúdo

        # =================================================================
        # ESTADO DA APLICAÇÃO - Variáveis que controlam o estado do programa
        # =================================================================
        self.selected_course = list(CURSOS.keys())[0]  # Curso selecionado (primeiro da lista por padrão)
        self.cursadas = set()  # Conjunto de disciplinas já cursadas
        self.disponiveis = set()  # Conjunto de disciplinas disponíveis para cursar
        self.initialized_course = {}  # Controla se um curso já foi inicializado

        # Cria a interface gráfica
        self.criar_interface()
        # Inicializa as disciplinas disponíveis para o curso selecionado
        self.inicializar_disponibilidade(self.selected_course)

    def criar_interface(self):
        """
        Cria todos os elementos da interface gráfica com scrollbars duplas
        """
        # =================================================================
        # CONFIGURAÇÃO DO SISTEMA DE SCROLLBARS DUPLAS
        # =================================================================
        # Cria um frame principal que contém tudo
        main_container = ttk.Frame(self.root)
        main_container.pack(fill="both", expand=True)

        # Adiciona scrollbar vertical
        v_scrollbar = ttk.Scrollbar(main_container, orient="vertical")
        v_scrollbar.pack(side="right", fill="y")

        # Adiciona scrollbar horizontal
        h_scrollbar = ttk.Scrollbar(main_container, orient="horizontal")
        h_scrollbar.pack(side="bottom", fill="x")

        # Cria um canvas que será rolável nas duas direções
        self.canvas_principal = tk.Canvas(
            main_container,
            yscrollcommand=v_scrollbar.set,
            xscrollcommand=h_scrollbar.set
        )
        self.canvas_principal.pack(side="left", fill="both", expand=True)

        # Configura as scrollbars para controlar o canvas
        v_scrollbar.config(command=self.canvas_principal.yview)
        h_scrollbar.config(command=self.canvas_principal.xview)

        # Cria um frame dentro do canvas que conterá todo o conteúdo
        self.main_frame = ttk.Frame(self.canvas_principal)

        # Adiciona o frame ao canvas
        self.canvas_principal.create_window((0, 0), window=self.main_frame, anchor="nw")

        # Configura o canvas para ajustar a área de scroll quando o frame interno mudar de tamanho
        self.main_frame.bind(
            "<Configure>",
            lambda e: self.canvas_principal.configure(scrollregion=self.canvas_principal.bbox("all"))
        )

        # =================================================================
        # CONFIGURAÇÃO DO SISTEMA DE GRID - Para layout responsivo
        # =================================================================
        # Configura expansão do frame principal
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(3, weight=1)

        # =================================================================
        # TÍTULO E INSTRUÇÕES
        # =================================================================
        titulo = ttk.Label(self.main_frame, text="🎓 Progresso Acadêmico Interativo",
                           font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=0, columnspan=3, pady=(10, 5), sticky="ew")

        instrucao = ttk.Label(self.main_frame,
                              text="Marque as disciplinas que você já cursou e veja as próximas liberadas!",
                              font=("Arial", 10))
        instrucao.grid(row=1, column=0, columnspan=3, pady=(0, 10), sticky="ew")

        # =================================================================
        # SELEÇÃO DE CURSO E BOTÃO DE LIMPAR
        # =================================================================
        # Frame para agrupar os controles superiores
        frame_controles = ttk.Frame(self.main_frame)
        frame_controles.grid(row=2, column=0, columnspan=3, sticky="ew", pady=5)
        frame_controles.columnconfigure(1, weight=1)  # Faz o combobox expandir

        # Label e combobox para seleção de curso
        ttk.Label(frame_controles, text="Selecione seu Curso:").grid(row=0, column=0, sticky="w", padx=(0, 10))

        self.combo_curso = ttk.Combobox(frame_controles, values=list(CURSOS.keys()),
                                        state="readonly")  # readonly impede digitação
        self.combo_curso.set(self.selected_course)  # Define o curso padrão
        self.combo_curso.grid(row=0, column=1, sticky="ew")
        # Vincula o evento de seleção à função on_curso_selecionado
        self.combo_curso.bind('<<ComboboxSelected>>', self.on_curso_selecionado)

        # =================================================================
        # BOTÃO PARA LIMPAR TODAS AS SELEÇÕES
        # =================================================================
        # Botão que permite limpar todas as disciplinas marcadas de uma vez
        btn_limpar_tudo = ttk.Button(
            frame_controles,
            text="🗑️ Limpar Tudo",
            command=self.limpar_todas_disciplinas
        )
        btn_limpar_tudo.grid(row=0, column=2, sticky="e", padx=(10, 0))

        # =================================================================
        # ÁREA DE DISCIPLINAS COM SCROLLBAR INTERNA
        # =================================================================
        # Frame para conter a área rolável das disciplinas
        frame_container_disciplinas = ttk.Frame(self.main_frame)
        frame_container_disciplinas.grid(row=3, column=0, columnspan=3, sticky="nsew", pady=10)

        # Configura expansão da área de disciplinas
        self.main_frame.rowconfigure(3, weight=1)
        frame_container_disciplinas.columnconfigure(0, weight=1)
        frame_container_disciplinas.rowconfigure(0, weight=1)

        # Cria um canvas interno específico para as disciplinas
        self.canvas_disciplinas = tk.Canvas(frame_container_disciplinas, highlightthickness=0)

        # Scrollbar vertical para o canvas das disciplinas
        scrollbar_disciplinas = ttk.Scrollbar(frame_container_disciplinas, orient="vertical",
                                              command=self.canvas_disciplinas.yview)

        # Frame que vai dentro do canvas (conterá as disciplinas)
        self.scrollable_frame = ttk.Frame(self.canvas_disciplinas)

        # Configura o canvas para ajustar a área de scroll quando o frame interno mudar de tamanho
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas_disciplinas.configure(scrollregion=self.canvas_disciplinas.bbox("all"))
        )

        # Coloca o frame dentro do canvas
        self.canvas_disciplinas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        # Conecta a scrollbar ao canvas
        self.canvas_disciplinas.configure(yscrollcommand=scrollbar_disciplinas.set)

        # Empacota o canvas e a scrollbar
        self.canvas_disciplinas.grid(row=0, column=0, sticky="nsew")
        scrollbar_disciplinas.grid(row=0, column=1, sticky="ns")

        # =================================================================
        # CONFIGURA SCROLL COM TOUCH/MOUSE WHEEL
        # =================================================================
        # Permite rolagem com a roda do mouse ou gestos de touch
        self.canvas_disciplinas.bind("<MouseWheel>", self._on_mousewheel)
        self.canvas_principal.bind("<MouseWheel>", self._on_mousewheel)

        # =================================================================
        # ÁREA DE RESUMO
        # =================================================================
        self.frame_resumo = ttk.LabelFrame(self.main_frame, text="Resumo do Progresso", padding=10)
        self.frame_resumo.grid(row=4, column=0, columnspan=3, sticky="ew", pady=(10, 0))

    def _on_mousewheel(self, event):
        """
        Manipula eventos de rolagem do mouse/touch
        event: evento do Tkinter com informações da rolagem
        """
        # Determina a direção e intensidade da rolagem
        scroll_amount = -1 * (event.delta // 120)  # Normaliza o valor do delta

        # Rola o canvas principal verticalmente
        self.canvas_principal.yview_scroll(scroll_amount, "units")

        # Rola o canvas das disciplinas verticalmente
        self.canvas_disciplinas.yview_scroll(scroll_amount, "units")

    def limpar_todas_disciplinas(self):
        """
        Limpa todas as disciplinas marcadas como cursadas
        Função acionada pelo botão 'Limpar Tudo'
        """
        # Verifica se há disciplinas para limpar
        if not self.cursadas:
            messagebox.showinfo("Informação", "Não há disciplinas para limpar!")
            return

        # Confirmação antes de limpar tudo
        resposta = messagebox.askyesno(
            "Confirmar Limpeza",
            "Tem certeza que deseja limpar TODAS as disciplinas marcadas?\n\n"
            f"Esta ação irá desmarcar {len(self.cursadas)} disciplina(s)."
        )

        # Se o usuário confirmou, limpa as disciplinas
        if resposta:
            self.cursadas.clear()  # Remove todas as disciplinas do conjunto
            messagebox.showinfo("Sucesso", "Todas as disciplinas foram desmarcadas!")
            # Recalcula a disponibilidade e atualiza a interface
            self.verificar_disponibilidade()

    def on_curso_selecionado(self, event):
        """
        Chamado quando o usuário seleciona um novo curso no combobox
        event: evento do Tkinter (não usado, mas necessário)
        """
        novo_curso = self.combo_curso.get()  # Pega o curso selecionado

        # Só faz algo se o curso realmente mudou
        if novo_curso != self.selected_course:
            self.selected_course = novo_curso  # Atualiza o curso selecionado
            # Reinicializa a disponibilidade para o novo curso
            self.inicializar_disponibilidade(novo_curso)

    def inicializar_disponibilidade(self, curso_selecionado):
        """
        Inicializa as disciplinas disponíveis para um curso
        curso_selecionado: nome do curso a ser inicializado
        """
        # Verifica se o curso já foi inicializado (para não resetar acidentalmente)
        if curso_selecionado not in self.initialized_course or not self.initialized_course.get(curso_selecionado,
                                                                                               False):
            # Limpa as disciplinas cursadas e disponíveis
            self.cursadas = set()
            self.disponiveis = set()

            # Pega as disciplinas do curso selecionado
            disciplinas_do_curso = CURSOS[curso_selecionado]

            # Para cada disciplina no curso...
            for disciplina, info in disciplinas_do_curso.items():
                # Se a disciplina não tem pré-requisitos, ela fica disponível inicialmente
                if not info["requisitos"]:
                    self.disponiveis.add(disciplina)

            # Marca o curso como inicializado
            self.initialized_course[curso_selecionado] = True

        # Verifica quais disciplinas ficaram disponíveis após a inicialização
        self.verificar_disponibilidade()

    def verificar_disponibilidade(self):
        """
        Verifica e atualiza quais disciplinas estão disponíveis
        baseado nas disciplinas já cursadas
        """
        disciplinas_do_curso = CURSOS[self.selected_course]
        novas_disponiveis = set()  # Conjunto para as novas disciplinas disponíveis

        # Para cada disciplina no curso atual...
        for disciplina, info in disciplinas_do_curso.items():
            # Se a disciplina ainda não foi cursada...
            if disciplina not in self.cursadas:
                # Verifica se TODOS os pré-requisitos foram cursados
                todos_requisitos_satisfeitos = all(
                    req in self.cursadas for req in info["requisitos"]
                )

                # Se todos os pré-requisitos estão satisfeitos, a disciplina fica disponível
                if todos_requisitos_satisfeitos:
                    novas_disponiveis.add(disciplina)

        # Atualiza as disciplinas disponíveis (remove as que já foram cursadas)
        self.disponiveis = novas_disponiveis - self.cursadas
        # Atualiza a interface para refletir as mudanças
        self.atualizar_interface()

    def on_disciplina_click(self, disciplina):
        """
        Chamado quando o usuário clica em uma disciplina
        disciplina: nome da disciplina clicada
        """
        # Se a disciplina já estava cursada...
        if disciplina in self.cursadas:
            # Remove das cursadas (desmarca)
            self.cursadas.remove(disciplina)
            messagebox.showinfo("Sucesso", f"A disciplina '{disciplina}' foi desmarcada.")

        # Se a disciplina estava disponível (não cursada)...
        elif disciplina in self.disponiveis:
            # Adiciona às cursadas
            self.cursadas.add(disciplina)
            messagebox.showinfo("Sucesso", f"A disciplina '{disciplina}' foi marcada como cursada.")

        # Se a disciplina não está disponível nem cursada (bloqueada)...
        else:
            messagebox.showerror("Erro", f"Você precisa cursar os pré-requisitos antes de '{disciplina}'.")
            return  # Para a execução aqui

        # Após qualquer mudança, verifica novamente a disponibilidade
        self.verificar_disponibilidade()

    def calcular_porcentagem_conclusao(self):
        """
        Calcula a porcentagem de conclusão do curso baseado nas disciplinas cursadas
        Retorna: porcentagem (0-100) e texto formatado
        """
        disciplinas_do_curso = CURSOS[self.selected_course]
        total_disciplinas = len(disciplinas_do_curso)

        # Conta quantas disciplinas do curso atual foram cursadas
        cursadas_no_curso = len([d for d in self.cursadas if d in disciplinas_do_curso])

        # Calcula a porcentagem
        if total_disciplinas > 0:
            porcentagem = (cursadas_no_curso / total_disciplinas) * 100
        else:
            porcentagem = 0

        return porcentagem, cursadas_no_curso, total_disciplinas

    def calcular_carga_horaria_total(self):
        """
        Calcula a carga horária total do curso e a carga horária cursada
        Retorna: (carga_horaria_cursada, carga_horaria_total)
        """
        disciplinas_do_curso = CURSOS[self.selected_course]

        # Calcula carga horária total do curso
        carga_horaria_total = sum(info["carga_horaria"] for info in disciplinas_do_curso.values())

        # Calcula carga horária cursada
        carga_horaria_cursada = sum(
            info["carga_horaria"]
            for disciplina, info in disciplinas_do_curso.items()
            if disciplina in self.cursadas
        )

        return carga_horaria_cursada, carga_horaria_total

    def atualizar_interface(self):
        """
        Atualiza toda a interface gráfica para refletir o estado atual
        """
        # =================================================================
        # LIMPEZA DOS ELEMENTOS ANTERIORES
        # =================================================================
        # Remove todas as disciplinas da área rolável
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Remove todas as informações do resumo
        for widget in self.frame_resumo.winfo_children():
            widget.destroy()

        # =================================================================
        # PREPARAÇÃO DAS DISCIPLINAS POR NÍVEL
        # =================================================================
        disciplinas_do_curso_atual = CURSOS[self.selected_course]

        # Dicionário para agrupar disciplinas por nível
        disciplinas_por_nivel = {}

        # Para cada disciplina no curso atual...
        for disciplina, info in disciplinas_do_curso_atual.items():
            nivel = info.get("nivel", 1)  # Pega o nível (padrão é 1 se não existir)

            # Se o nível ainda não existe no dicionário, cria uma lista vazia
            if nivel not in disciplinas_por_nivel:
                disciplinas_por_nivel[nivel] = []

            # Adiciona a disciplina à lista do seu nível
            disciplinas_por_nivel[nivel].append(disciplina)

        # =================================================================
        # EXIBIÇÃO DAS DISCIPLINAS POR NÍVEL
        # =================================================================
        # Ordena os níveis para exibir do 1 ao mais alto
        niveis_ordenados = sorted(disciplinas_por_nivel.keys())

        # Para cada nível...
        for nivel in niveis_ordenados:
            # Cria um frame para agrupar as disciplinas deste nível
            frame_nivel = ttk.LabelFrame(self.scrollable_frame, text=f"Nível {nivel}", padding="10")
            frame_nivel.pack(fill="x", padx=5, pady=5)  # Empacota com preenchimento horizontal

            # =============================================================
            # CONFIGURAÇÃO DO GRID PARA AS DISCIPLINAS DESTE NÍVEL
            # =============================================================
            num_cols = 3  # Número de colunas por linha
            row, col = 0, 0  # Posição inicial no grid

            # Para cada disciplina neste nível...
            for i, disciplina in enumerate(disciplinas_por_nivel[nivel]):
                # =========================================================
                # DETERMINA O STATUS E CORES DA DISCIPLINA
                # =========================================================
                if disciplina in self.cursadas:
                    bg_color = "#D4EDDA"  # Verde claro - já cursada
                    text_color = "#155724"  # Verde escuro
                    status = "CURSADA ✅"
                elif disciplina in self.disponiveis:
                    bg_color = "#CCE5FF"  # Azul claro - disponível para cursar
                    text_color = "#004085"  # Azul escuro
                    status = "DISPONÍVEL"
                else:
                    bg_color = "#F8D7DA"  # Vermelho claro - bloqueada (faltam pré-requisitos)
                    text_color = "#721C24"  # Vermelho escuro
                    status = "BLOQUEADA 🔒"

                # =========================================================
                # CRIA O FRAME INDIVIDUAL PARA CADA DISCIPLINA
                # =========================================================
                frame_disc = tk.Frame(frame_nivel, bg=bg_color, relief="raised", bd=1)
                frame_disc.grid(row=row, column=col, padx=5, pady=5, sticky="ew")

                # Configura a coluna para expandir igualmente
                frame_nivel.columnconfigure(col, weight=1)

                # =========================================================
                # LABEL COM O NOME DA DISCIPLINA E CARGA HORÁRIA
                # =========================================================
                carga_horaria = disciplinas_do_curso_atual[disciplina]["carga_horaria"]
                label_texto = f"{disciplina}\n({carga_horaria}h)"

                label_nome = tk.Label(frame_disc, text=label_texto, bg=bg_color,
                                      fg=text_color, font=("Arial", 8, "bold"),  # Fonte menor para caber mais texto
                                      wraplength=140, justify="center")  # wraplength quebra texto longo
                label_nome.pack(padx=3, pady=2)

                # =========================================================
                # LABEL COM O STATUS DA DISCIPLINA
                # =========================================================
                label_status = tk.Label(frame_disc, text=status, bg=bg_color,
                                        fg=text_color, font=("Arial", 7))  # Fonte menor
                label_status.pack(padx=3, pady=1)

                # =========================================================
                # BOTÃO PARA CLICAR NA DISCIPLINA
                # =========================================================
                # Se a disciplina está disponível ou já foi cursada...
                if disciplina in self.disponiveis or disciplina in self.cursadas:
                    # Cria botão clicável
                    btn = ttk.Button(frame_disc, text="Clique para alternar",
                                     command=lambda d=disciplina: self.on_disciplina_click(d))
                    btn.pack(padx=3, pady=3, fill="x")
                else:
                    # Cria botão desabilitado para disciplinas bloqueadas
                    btn = ttk.Button(frame_disc, text="Bloqueada", state="disabled")
                    btn.pack(padx=3, pady=3, fill="x")

                # =========================================================
                # ATUALIZA A POSIÇÃO NO GRID
                # =========================================================
                col += 1  # Vai para a próxima coluna
                if col >= num_cols:  # Se chegou ao final da linha
                    col = 0  # Volta para a primeira coluna
                    row += 1  # Vai para a próxima linha

        # =================================================================
        # ATUALIZA O RESUMO COM BARRA DE PROGRESSO E CARGA HORÁRIA
        # =================================================================
        self.atualizar_resumo()

        # =================================================================
        # ATUALIZA AS SCROLLBARS APÓS MUDANÇAS NO CONTEÚDO
        # =================================================================
        self.scrollable_frame.update_idletasks()
        self.canvas_disciplinas.configure(scrollregion=self.canvas_disciplinas.bbox("all"))
        self.main_frame.update_idletasks()
        self.canvas_principal.configure(scrollregion=self.canvas_principal.bbox("all"))

    def atualizar_resumo(self):
        """
        Atualiza a área de resumo com informações sobre o progresso incluindo porcentagem e carga horária
        """
        # =================================================================
        # CALCULA PORCENTAGEM DE CONCLUSÃO E CARGA HORÁRIA
        # =================================================================
        porcentagem, cursadas_no_curso, total_disciplinas = self.calcular_porcentagem_conclusao()
        carga_horaria_cursada, carga_horaria_total = self.calcular_carga_horaria_total()

        # =================================================================
        # BARRA DE PROGRESSO VISUAL
        # =================================================================
        # Frame para a barra de progresso
        frame_progresso = ttk.Frame(self.frame_resumo)
        frame_progresso.pack(fill="x", pady=5)

        # Label da porcentagem
        label_porcentagem = ttk.Label(
            frame_progresso,
            text=f"{porcentagem:.1f}%",
            font=("Arial", 12, "bold"),
            foreground="green" if porcentagem > 50 else "orange"
        )
        label_porcentagem.pack(side="right", padx=(10, 0))

        # Barra de progresso visual
        progress_bar = ttk.Progressbar(
            frame_progresso,
            orient="horizontal",
            length=200,
            mode='determinate'
        )
        progress_bar['value'] = porcentagem
        progress_bar.pack(side="left", fill="x", expand=True)

        # =================================================================
        # INFORMAÇÕES SOBRE DISCIPLINAS CURSADAS
        # =================================================================
        label_cursadas = ttk.Label(
            self.frame_resumo,
            text=f"Disciplinas Cursadas: {cursadas_no_curso} de {total_disciplinas}",
            font=("Arial", 10, "bold")
        )
        label_cursadas.pack(anchor="w", pady=2)

        # =================================================================
        # INFORMAÇÕES SOBRE CARGA HORÁRIA
        # =================================================================
        label_carga_horaria = ttk.Label(
            self.frame_resumo,
            text=f"Carga Horária: {carga_horaria_cursada}h de {carga_horaria_total}h ({carga_horaria_cursada / carga_horaria_total * 100:.1f}%)",
            font=("Arial", 9, "bold"),
            foreground="blue"
        )
        label_carga_horaria.pack(anchor="w", pady=2)

        # Se há disciplinas cursadas, mostra quais são
        if cursadas_no_curso > 0:
            disciplinas_cursadas = [d for d in self.cursadas if d in CURSOS[self.selected_course]]
            texto_cursadas = f"Você já cursou: {', '.join(sorted(disciplinas_cursadas))}"
            label_detalhe_cursadas = ttk.Label(
                self.frame_resumo,
                text=texto_cursadas,
                foreground="green",
                wraplength=800  # Permite quebra de linha para textos longos
            )
            label_detalhe_cursadas.pack(anchor="w", pady=2)
        else:
            label_detalhe_cursadas = ttk.Label(
                self.frame_resumo,
                text="Nenhuma disciplina cursada ainda neste curso.",
                foreground="blue"
            )
            label_detalhe_cursadas.pack(anchor="w", pady=2)

        # =================================================================
        # INFORMAÇÕES SOBRE DISCIPLINAS DISPONÍVEIS
        # =================================================================
        # Pega as disciplinas disponíveis que ainda não foram cursadas
        disponiveis_nao_cursadas = self.disponiveis - self.cursadas
        # Filtra apenas as do curso atual
        disponiveis_no_curso = [d for d in disponiveis_nao_cursadas if d in CURSOS[self.selected_course]]

        # Se há disciplinas disponíveis, mostra quais são
        if disponiveis_no_curso:
            texto_disponiveis = f"Disponíveis para cursar: {', '.join(sorted(disponiveis_no_curso))}"
            label_detalhe_disponiveis = ttk.Label(
                self.frame_resumo,
                text=texto_disponiveis,
                foreground="darkblue",
                wraplength=800  # Permite quebra de linha para textos longos
            )
            label_detalhe_disponiveis.pack(anchor="w", pady=2)
        else:
            label_detalhe_disponiveis = ttk.Label(
                self.frame_resumo,
                text="Nenhuma disciplina disponível para cursar no momento.",
                foreground="orange"
            )
            label_detalhe_disponiveis.pack(anchor="w", pady=2)


# =====================================================================
# EXECUÇÃO PRINCIPAL DO PROGRAMA
# =====================================================================
# Este código só roda quando o arquivo é executado diretamente
# =====================================================================

if __name__ == "__main__":
    # Cria a janela principal do Tkinter
    root = tk.Tk()
    # Cria a aplicação passando a janela principal
    app = AplicacaoProgressoAcademico(root)
    # Inicia o loop principal da interface gráfica
    root.mainloop()