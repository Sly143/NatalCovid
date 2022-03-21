# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

rocas = {
	# =============================================================
	# Dados Demográficos
	'regiao': 'leste',					# Zona ao qual o bairro pertence
	'tamPop': 10322,					# Tamanho da população
	'tamFisico': 66.01,					# Área do bairro em Hectare
	'densidadeDemografica': 156.55,		# Densidade demografica (Hab/km²)
	'numDomicilio': 3067,				# Numero de domicilios
	'domicilio': {'casa': 91.72, 'apartamento': 4.86, 'comodo': 0, 'casa de vila ou condominio': 3.4,  'outro': 0},
	'idade': [948, 1412, 1729, 1402, 1906, 1370, 693, 527, 336],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [1.14, 5.12, 17.93, 32.25, 26.12, 7.89, 4.4, 1.63, 0.36, 3.16, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 39.1, 'naoExiste': 60.9},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':0, 'estadual': 1, 'federal': 0,'particular': 3},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':0, 'estadual': 71, 'federal': 0,'particular': 299},	# Número de escolas	# Média de Alunos por escolas
}
