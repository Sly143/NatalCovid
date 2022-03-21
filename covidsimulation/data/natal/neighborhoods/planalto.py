# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

planalto = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'oeste',					# Zona ao qual o bairro pertence
	'tamPop': 40344,					# Tamanho da população
	'tamFisico': 463.83,					# Área do bairro em Hectare
	'densidadeDemografica': 8697.58,		# Densidade demografica (Hab/km²)
	'numDomicilio': 9305,				# Numero de domicilios
	'domicilio': {'casa': 89.94, 'apartamento': 2.94, 'comodo': 0, 'casa de vila ou condominio': 7.11,  'outro': 0},
	'idade': [4966, 6836, 7570, 7808, 7886, 2710, 1548, 647, 368],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [2.75, 9.23, 23.86, 33.63, 19.47, 4.32, 2.29, 0.67, 0.04, 3.7, 0.04], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 49.34, 'naoExiste': 50.66},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':4, 'estadual': 0, 'federal': 0,'particular': 6},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':1962, 'estadual': 0, 'federal': 0,'particular': 532},	# Número de escolas	# Média de Alunos por escolas
}
