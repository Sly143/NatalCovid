# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

cidadeAlta = {
	# =============================================================
	# Dados Demográficos 2010 - 2017
	'regiao': 'leste',					# Zona ao qual o bairro pertence
	'tamPop': 7542,						# Tamanho da população
	'tamFisico': 116.41,				# Área do bairro em Hectare
	'densidadeDemografica': 64.46,		# Densidade demografica (Hab/km²)
	'numDomicilio': 2259,				# Numero de domicilios
	'domicilio': {'casa': 73.31, 'apartamento': 22.13, 'comodo': 2.17, 'casa de vila ou condominio': 2.17,  'outro': 0},
	'idade': [572, 1103, 1628, 1071, 1031, 864, 654, 322, 297],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [2.04, 4.52, 14.7, 20.63, 22, 10.4, 10.23, 8.9, 3.23, 3.1, 0.27], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 32.93, 'naoExiste': 67.07},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',		# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':0, 'estadual': 2, 'federal': 1,'particular': 8},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':0, 'estadual': 622, 'federal': 591,'particular': 4156},	# Número de escolas	# Média de Alunos por escolas
}
