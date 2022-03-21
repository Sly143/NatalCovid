
# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

lagoaNova = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'sul',				# Zona ao qual o bairro pertence
	'tamPop': 39727,					# Tamanho da população
	'tamFisico': 767.7,				# Área do bairro em Hectare
	'densidadeDemografica': 51.75,		# Densidade demografica (Hab/km²)
	'numDomicilio': 11500,				# Numero de domicilios
	'domicilio': {'casa': 53.13, 'apartamento': 41.46, 'comodo': 0.29, 'casa de vila ou condominio': 5.12,  'outro': 0},
	'idade': [2912, 3779, 8047, 5966, 5822, 5143, 4142, 2186, 1731],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [0.3, 1.46, 5.59, 12.83, 18, 12.75, 18.26, 20.03, 8.43, 2.3, 0.05], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 16.38, 'naoExiste': 83.62},	# Porcentagem de esgoto a céu aberto
	 
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':1, 'estadual': 12, 'federal': 1,'particular': 23},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':65, 'estadual': 3841, 'federal': 376,'particular': 9854},	# Número de escolas	# Média de Alunos por escolas
}
