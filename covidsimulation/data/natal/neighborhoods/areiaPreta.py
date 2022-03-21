# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

areiaPreta = {
	# =============================================================
	# Dados Demográficos
	'regiao': 'leste',					# Zona ao qual o bairro pertence
	'tamPop': 5013,					# Tamanho da população
	'tamFisico': 32.17,					# Área do bairro em Hectare
	'densidadeDemografica': 152.56,		# Densidade demografica (Hab/km²)
	'numDomicilio': 1160,				# Numero de domicilios
	'domicilio': {'casa': 62.41, 'apartamento': 35.69, 'comodo': 0, 'casa de vila ou condominio': 1.9,  'outro': 0},
	'idade': [433, 604, 920, 681, 892, 734, 410, 189, 149],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [0.17, 2.69, 6.39, 19.33, 23.7, 9.24, 10.76, 13.11, 13.78, 0.84, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 11.94, 'naoExiste': 88.06},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':0, 'estadual': 1, 'federal': 0,'particular': 0},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':0, 'estadual': 192, 'federal': 0,'particular': 0},	# Número de escolas	# Média de Alunos por escolas
}
