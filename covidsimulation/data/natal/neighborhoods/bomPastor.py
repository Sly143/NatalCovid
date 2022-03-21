# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

bomPastor = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'oeste',					# Zona ao qual o bairro pertence
	'tamPop': 18653,					# Tamanho da população
	'tamFisico': 346.09,					# Área do bairro em Hectare
	'densidadeDemografica': 5389.64,		# Densidade demografica (Hab/km²)
	'numDomicilio': 5191,				# Numero de domicilios
	'domicilio': {'casa': 85.67, 'apartamento': 0.75, 'comodo': 1.19, 'casa de vila ou condominio': 12.39,  'outro': 0},
	'idade': [2409, 3083, 3680, 2828, 3044, 1589, 1102, 609, 308],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [3.58, 11.17, 28.92, 35.31, 14.06, 2, 1.06, 0.17, 0.04, 3.68, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 84.06, 'naoExiste': 15.94},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':2, 'estadual': 3, 'federal': 0,'particular': 6},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':1168, 'estadual': 1228, 'federal': 0,'particular': 1336},	# Número de escolas	# Média de Alunos por escolas
}
