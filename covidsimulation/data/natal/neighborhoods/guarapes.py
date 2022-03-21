# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

guarapes = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'oeste',					# Zona ao qual o bairro pertence
	'tamPop': 11583,					# Tamanho da população
	'tamFisico': 865.95,					# Área do bairro em Hectare
	'densidadeDemografica': 1337.61,		# Densidade demografica (Hab/km²)
	'numDomicilio': 2822,				# Numero de domicilios
	'domicilio': {'casa': 97.2, 'apartamento': 0.39, 'comodo': 1.88, 'casa de vila ou condominio': 0.53,  'outro': 0},
	'idade': [1964, 2467, 2661, 1474, 1405, 902, 431, 204, 77],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [10.31, 17.43, 34.94, 25.12, 5.56, 0.78, 0.28, 0.04, 0.07, 5.42, 0.04], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 66.53, 'naoExiste': 33.47},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':5, 'estadual': 1, 'federal': 0,'particular': 0},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':2088, 'estadual': 222, 'federal': 0,'particular': 0},	# Número de escolas	# Média de Alunos por escolas
}
