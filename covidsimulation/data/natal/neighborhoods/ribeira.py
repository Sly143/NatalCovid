# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

ribeira = {
	# =============================================================
	# Dados Demográficos
	'regiao': 'leste',					# Zona ao qual o bairro pertence
	'tamPop': 2274,					# Tamanho da população
	'tamFisico': 94.39,					# Área do bairro em Hectare
	'densidadeDemografica': 24.04,		# Densidade demografica (Hab/km²)
	'numDomicilio': 764,				# Numero de domicilios
	'domicilio': {'casa': 47.51, 'apartamento': 52.36, 'comodo': 0, 'casa de vila ou condominio': 0.1,  'outro': 0},
	'idade': [129, 229, 404, 473, 484, 236, 135, 85, 97],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [1.18, 2.75, 5.5, 16.49, 18.46, 12.04, 15.58, 16.1, 10.21, 1.7, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 16.88, 'naoExiste': 83.12},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':1, 'estadual': 1, 'federal': 0,'particular': 1},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':318, 'estadual': 288, 'federal': 0,'particular': 1177},	# Número de escolas	# Média de Alunos por escolas
}
