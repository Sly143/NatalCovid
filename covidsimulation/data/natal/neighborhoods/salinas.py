
# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

salinas = {
	# =============================================================
	# Dados Demográficos
	'regiao': 'norte',					# Zona ao qual o bairro pertence
	'tamPop': 1522,						# Tamanho da população
	'tamFisico': 1031.2,				# Área do bairro em Hectare
	'densidadeDemografica': 1.48,		# Densidade demografica (Hab/km²)
	'numDomicilio': 331,				# Numero de domicilios
	'domicilio': {'casa': 100, 'apartamento':0 , 'comodo':0, 'casa de vila ou condominio':0 ,  'outro':0 },
	'idade': [232, 312, 309, 290, 141, 73, 95, 58, 11],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [10.27, 17.82, 35.05, 24.47, 2.11, 0.6, 0.6, 0.3, 0, 8.76, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 77.78, 'naoExiste': 22.22},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',			# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',				# Numero de leitos dos hospitais
	'uti': 'vazio',					# Número de UTIS do bairro
	'doencasCronicas': 'vazio',		# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':0, 'estadual': 0, 'particular': 0},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':0, 'estadual': 0, 'particular': 0},	# Número de escolas	# Média de Alunos por escolas
}
