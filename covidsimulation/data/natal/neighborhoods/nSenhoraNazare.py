# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

nSenhoraNazare = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'oeste',					# Zona ao qual o bairro pertence
	'tamPop': 16516,					# Tamanho da população
	'tamFisico': 144.01,					# Área do bairro em Hectare
	'densidadeDemografica': 11468.65,		# Densidade demografica (Hab/km²)
	'numDomicilio': 4768,				# Numero de domicilios
	'domicilio': {'casa': 80.31, 'apartamento': 7.74, 'comodo': 0.96, 'casa de vila ou condominio': 10.99,  'outro': 0},
	'idade': [1695, 2192, 3262, 2724, 2542, 1536, 1487, 680, 399],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [1.17, 5.12, 18.96, 33.68, 22.36, 7.21, 5.22, 3.42, 1.05, 1.8, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 35.82, 'naoExiste': 64.18},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':4, 'estadual': 2, 'federal': 0,'particular': 2},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':1470, 'estadual':877, 'federal': 0,'particular': 210},	# Número de escolas	# Média de Alunos por escolas
}
