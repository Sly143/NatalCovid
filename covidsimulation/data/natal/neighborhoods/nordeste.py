# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

nordeste = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'oeste',					# Zona ao qual o bairro pertence
	'tamPop': 11792,					# Tamanho da população
	'tamFisico': 294.44,					# Área do bairro em Hectare
	'densidadeDemografica': 3951.21,		# Densidade demografica (Hab/km²)
	'numDomicilio': 3339,				# Numero de domicilios
	'domicilio': {'casa': 85.18, 'apartamento': 0.33, 'comodo': 0.36, 'casa de vila ou condominio': 14.14,  'outro': 0},
	'idade': [1275, 1778, 2322, 1787, 1869, 1138, 717, 541, 363],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [2.96, 8.3, 20.63, 32.32, 21.35, 5.9, 3.53, 1.65, 0.15, 3.17, 0.03], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 5.93, 'naoExiste': 94.07},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':2, 'estadual':1, 'federal': 0,'particular': 1},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':556, 'estadual': 355, 'federal': 0,'particular': 88},	# Número de escolas	# Média de Alunos por escolas
}
