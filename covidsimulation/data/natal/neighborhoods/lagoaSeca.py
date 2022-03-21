# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

lagoaSeca = {
	# =============================================================
	# Dados Demográficos
	'regiao': 'leste',					# Zona ao qual o bairro pertence
	'tamPop': 4871,					# Tamanho da população
	'tamFisico': 61.09,					# Área do bairro em Hectare
	'densidadeDemografica': 81.13,		# Densidade demografica (Hab/km²)
	'numDomicilio': 1731,				# Numero de domicilios
	'domicilio': {'casa': 72.21, 'apartamento': 18.54, 'comodo': 0.06, 'casa de vila ou condominio': 9.2,  'outro': 0},
	'idade': [318, 553, 981, 576, 761, 624, 443, 341, 273],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [0.23, 1.96, 8.43, 26.46, 24.96, 11.27, 12.31, 8.9, 2.48, 2.89, 0.12], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 12.25, 'naoExiste': 87.75},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':0, 'estadual': 2, 'federal': 0,'particular': 1},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':0, 'estadual': 1069, 'federal': 0,'particular': 37},	# Número de escolas	# Média de Alunos por escolas
}
