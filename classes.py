class Pessoa:
    def __init__(self, nome, genero, mail, passaporte, cpf, nascimento, nacionalidade, pessoa_id):
        self.nome = nome
        self.genero = genero
        self.mail = mail
        self.passaporte = passaporte
        self.cpf = cpf
        self.nascimento = nascimento
        self.nacionalidade = nacionalidade
        self.pessoa_id = pessoa_id


class Aluno(Pessoa):
    def __init__(self, classe, categoria, semestres, instmail, matricula):
        self.categoria = categoria
        self.semestres = semestres
        self.instmail = instmail
        self.matricula = matricula
        Pessoa.__init__(self, classe["nome"], classe["genero"],
                        classe["mail"], classe["passaporte"], classe["cpf"],
                        classe["nascimento"], classe["nacionalidade"], classe["pessoa_id"])


class Mobi:
    def __init__(self, m_csf, m_in, m_out, m_total, _id):
        self.m_csf = m_csf
        self.m_in = m_in
        self.m_out = m_out
        self.m_total = m_total
        self._id = _id


class Instituicao(Mobi):
    def __init__(self, classe, nome, origem, sigla, pais, telefone,
                 telefone2, mail, mail2, mail3, responsavel, endereco, site):
        self.nome = nome
        self.origem = origem
        self.sigla = sigla
        self.pais = pais
        self.telefone = telefone
        self.telefone2 = telefone2
        self.mail = mail
        self.mail2 = mail2
        self.mail3 = mail3
        self.responsavel = responsavel
        self.endereco = endereco
        self.site = site
        Mobi.__init__(self, classe["m_csf"], classe["m_in"], classe["m_out"],
                      classe["m_total"], classe["_id"])


class Convenio(Mobi):
    def __init__(self, classe, nome, inst, site, pais, sigla_pais, latitude, data_inicial, data_final,
                 data_primeira, deadline1, deadline2, taxa, idioma, preve_mobilidade, obs, convenio_pdf):
        self.nome = nome
        self.inst = inst
        self.site = site
        self.pais = pais
        self.sigla_pais = sigla_pais
        self.latitude = latitude
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.data_primeira = data_primeira
        self.deadline1 = deadline1
        self.deadline2 = deadline2
        self.taxa = taxa
        self.idioma = idioma
        self.preve_mobilidade = preve_mobilidade
        self.obs = obs
        self.convenio_pdf = convenio_pdf
        Mobi.__init__(self, classe["m_csf"], classe["m_in"], classe["m_out"],
                      classe["m_total"], classe["_id"])


class Mobilidade(Aluno):

    def __init__(self, classe, duracao, convenio, edital, type_mobi, status, pais_fk, inst, curso_ufop, unidade, campus,
                 inicio, termino, afastamento, sem_afastado, ano_retorno, sem_retorno, data_afastamento,
                 data_assinatura_ret, programa, modalidade, bolsa, obs):
        self.duracao = duracao
        self.convenio = convenio
        self.edital = edital
        self.type_mobi = type_mobi
        self.status = status
        self.pais_fk = pais_fk
        self.inst = inst
        self.curso_ufop = curso_ufop
        self.unidade = unidade
        self.campus = campus
        self.inicio = inicio
        self.termino = termino
        self.afastamento = afastamento
        self.sem_afastado = sem_afastado
        self.ano_retorno = ano_retorno
        self.sem_retorno = sem_retorno
        self.data_afastamento = data_afastamento
        self.data_assinatura_ret = data_assinatura_ret
        self.programa = programa
        self.modalidade = modalidade
        self.bolsa = bolsa
        self.obs = obs

        Aluno.__init__(self, classe["categoria"], classe["semestres"], classe["instmail"],
                       classe["matricula"], classe["Aluno"])
