
# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

potengi = {
	# =============================================================
	# Dados Demográficos
	'regiao': 'norte',					# Zona ao qual o bairro pertence
	'tamPop': 59209,					# Tamanho da população
	'tamFisico': 799.9,					# Área do bairro em Hectare
	'densidadeDemografica': 74.02,		# Densidade demografica (Hab/km²)
	'numDomicilio': 16309,				# Numero de domicilios
	'domicilio': {'casa': 96.03, 'apartamento': 0.3, 'comodo':0.02, 'casa de vila ou condominio': 3.64,  'outro':0 },
	'idade': [5732, 6784, 12650, 8785, 7446, 8768, 5618, 2055, 1371],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [0.9, 3.94, 17.08, 34.77, 28.41, 7.65, 3.88, 1.11, 0.2, 2.07, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 36.83, 'naoExiste': 63.17},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 8,				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':16, 'estadual': 11, 'federal': 1, 'particular': 24},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':6432, 'estadual': 8051, 'federal': 812,'particular': 7612},	# Número de escolas	# Média de Alunos por escolas
}
