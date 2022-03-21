# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

santosReis = {
	# =============================================================
	# Dados Demográficos
	'regiao': 'leste',					# Zona ao qual o bairro pertence
	'tamPop': 4745,					# Tamanho da população
	'tamFisico': 222.09,					# Área do bairro em Hectare
	'densidadeDemografica': 21.37,		# Densidade demografica (Hab/km²)
	'numDomicilio': 1531,				# Numero de domicilios
	'domicilio': {'casa': 97.39, 'apartamento': 1.44, 'comodo': 0, 'casa de vila ou condominio': 1.2,  'outro': 0.57},
	'idade': [486, 615, 833, 727, 782, 501, 421, 235, 143],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [2.29, 7.05, 23.25, 31.68, 19.33, 6.73, 4.18, 1.89, 0.85, 2.74, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 43.09, 'naoExiste': 56.91},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':2, 'estadual': 2, 'federal': 0,'particular': 0},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':1019, 'estadual': 612, 'federal': 0,'particular': 0},	# Número de escolas	# Média de Alunos por escolas
}
