# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

cidadeNova = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'oeste',					# Zona ao qual o bairro pertence
	'tamPop': 19946,					# Tamanho da população
	'tamFisico': 262.12,					# Área do bairro em Hectare
	'densidadeDemografica': 7609.49,		# Densidade demografica (Hab/km²)
	'numDomicilio': 5200,				# Numero de domicilios
	'domicilio': {'casa': 86.08, 'apartamento': 2.44, 'comodo': 0.65, 'casa de vila ou condominio': 10.83,  'outro': 0},
	'idade': [2423, 3574, 4105, 3270, 3283, 1597, 986, 435, 278],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [2.9, 9.29, 27.5, 34.67, 16.92, 2.92, 1.6, 0.42, 0.08, 3.69, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 93.31, 'naoExiste': 6.69},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':7, 'estadual': 1, 'federal': 0,'particular': 3},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':2578, 'estadual': 1221, 'federal': 0,'particular': 516},	# Número de escolas	# Média de Alunos por escolas
}
