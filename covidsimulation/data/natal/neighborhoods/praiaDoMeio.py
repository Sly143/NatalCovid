# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

praiaDoMeio = {
	# =============================================================
	# Dados Demográficos
	'regiao': 'leste',					# Zona ao qual o bairro pertence
	'tamPop': 5390,					# Tamanho da população
	'tamFisico': 48.92,					# Área do bairro em Hectare
	'densidadeDemografica': 109.01,		# Densidade demografica (Hab/km²)
	'numDomicilio': 1620,				# Numero de domicilios
	'domicilio': {'casa': 63.02, 'apartamento': 34.88, 'comodo': 0, 'casa de vila ou condominio': 2.1,  'outro': 0},
	'idade': [419, 696, 886, 938, 1196, 607, 363, 157, 132],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [0.68, 4.57, 13.46, 25.49, 17.35, 7.28, 10.12, 11.98, 6.42, 2.65, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 1.06, 'naoExiste': 98.94},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':2, 'estadual': 0, 'federal': 0,'particular': 0},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':398, 'estadual': 0, 'federal': 0,'particular': 0},	# Número de escolas	# Média de Alunos por escolas
}
