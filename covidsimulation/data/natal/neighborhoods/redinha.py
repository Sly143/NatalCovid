
# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

redinha = {
	# =============================================================
	# Dados Demográficos
	'regiao': 'norte',					# Zona ao qual o bairro pertence
	'tamPop': 21499,					# Tamanho da população
	'tamFisico': 878.9,					# Área do bairro em Hectare
	'densidadeDemografica': 24.46,		# Densidade demografica (Hab/km²)
	'numDomicilio': 4647,				# Numero de domicilios
	'domicilio': {'casa': 94.21, 'apartamento': 2.54, 'comodo': 0.41, 'casa de vila ou condominio': 2.84,  'outro': 0},
	'idade': [2811, 3807, 4231, 3786, 3498, 1651, 1079, 410, 223],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [4.95, 10.63, 24.47, 27.11, 17.09, 4.2, 2.47, 0.58, 0.22, 8.26, 0.02], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 35.74, 'naoExiste': 64.26},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 3,				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':4, 'estadual': 2, 'particular': 2},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':1024, 'estadual': 625, 'particular': 161},	# Número de escolas	# Média de Alunos por escolas
}
