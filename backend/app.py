# Autora: Cleviane Neves
# Fazer os seguintes comandos para funcionar
# No Windows: set FLASK_APP=app.py
# flask run
# Depois executar no terminal (Com o ambiente virtual ativado): flask run

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api, Resource, fields
from sqlalchemy import ForeignKey
from flask_cors import CORS, cross_origin

app = Flask(__name__)
#conexão com o meu banco do postgresql
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/sistema_imovel'
app.debug = True
CORS(app)
cross_origin(app = app, methods=['GET', 'POST', 'PUT', 'DELETE'])
appi = Api(app=app, version="1.0", title="Sistema de Imóveis CTT--Enforce",
           description="Sistema para Compra e Venda de Imóveis")
db = SQLAlchemy(app)


#clientes
nomes_cliente = appi.namespace('clientes', description="Operações com clientes")
model_cliente = appi.model('Cliente Model',
                           {'nm_cliente':fields.String(required=True,
                            description="Nome do Cliente"),
                            'cpf_cliente':fields.String(required=True,
                            description="CPF do Cliente"),
                            'rg_cliente':fields.String(required=True,
                            description="RG do Cliente"),
                            'endereco':fields.String(required=True,
                            description="Endereço do Cliente"),
                            'cep':fields.String(required=True,
                            description="CEP do endereço do Cliente"),
                            'uf':fields.String(required=True,
                            description="UF do endereço do Cliente"),
                            'data_nascimento':fields.Date(required=True,
                            description="Data de nascimento do Cliente"),
                            'estado_civil':fields.String(required=True,
                            description="Estado Civil atual do Cliente"),
                            'profissao':fields.String(required=True,
                            description="Profissão do Cliente")})
model_get_cliente = appi.model('Cliente Model', {'Id': fields.Integer(description="Id do cliente")})
model_put_cliente = appi.model('Cliente Model',
                            {'nm_cliente':fields.String(description="Nome do Cliente"),
                            'cpf_cliente':fields.String(description="CPF do Cliente"),
                            'rg_cliente':fields.String(description="RG do Cliente"),
                            'endereco':fields.String(description="Endereço do Cliente"),
                            'cep':fields.String(description="CEP do endereço do Cliente"),
                            'uf':fields.String(description="UF do endereço do Cliente"),
                            'data_nascimento':fields.Date(description="Data de nascimento do Cliente"),
                            'estado_civil':fields.String(description="Estado Civil atual do Cliente"),
                            'profissao':fields.String(description="Profissão do Cliente")})
#proprietario
nomes_proprietario = appi.namespace('proprietarios', description="Operações com proprietarios")
model_proprietario = appi.model('Proprietario Model', 
                                {'nm_proprietario':fields.String(required=True,
                                description="Nome do Proprietario"),
                                'cpf_proprietario':fields.String(required=True,
                                description="CPF do Proprietario"),
                                'rg_proprietario':fields.String(required=True,
                                description="RG do Proprietario"),
                                'data_nascimento':fields.String(required=True,
                                description="Data de Nascimento do Proprietario"),
                                'estado_civil':fields.String(required=True,
                                description="Estado Civil do Proprietario"),
                                'profissao':fields.String(required=True,
                                description="Profissão do Proprietario")})
model_put_proprietario = appi.model('Proprietario Model',
                                    {'nm_proprietario':fields.String(description="Nome do Proprietario"),
                                     'cpf_proprietario':fields.String(description="CPF do Proprietario"),
                                     'rg_proprietario':fields.String(description="RG do Proprietario"),
                                     'data_nascimento':fields.String(description="Data de Nascimento do Proprietario"),
                                     'estado_civil':fields.String(description="Estado Civil do Proprietario"),
                                     'profissao':fields.String(description="Profissão do Proprietario")})
#imovel
nomes_imovel = appi.namespace('imoveis', description="Operações com imoveis")
model_imovel = appi.model('Imovel Model', 
                        {'tipo_imovel':fields.String(required=True,
                        description="Tipo do Imovel"),
                        'endereco':fields.String(required=True,
                        description="Endereço do Imovel"),
                        'complemento':fields.String(required=True,
                        description="Complemento do Endereço do Imovel"),
                        'cep':fields.String(required=True,
                        description="Cep da localizaçao do Imovel"),
                        'uf':fields.String(required=True,
                        description="UF do Imovel"),
                        'id_proprietario':fields.Integer(required=True,
                        description="ID do Proprietario do Imovel"),
                        'adquirido_em':fields.String(required=True,
                        description="Quando o imovel foi adquirido"),
                        'valor_imovel':fields.String(required=True,
                        description="Valor de Venda do Imovel")})
model_put_imovel = appi.model('Imovel Model', 
                            {'tipo_imovel':fields.String(description="Tipo do Imovel"),
                            'endereco':fields.String(description="Endereço do Imovel"),
                            'complemento':fields.String(description="Complemento do Endereço do Imovel"),
                            'cep':fields.String(description="Cep da localizaçao do Imovel"),
                            'uf':fields.String(description="UF do Imovel"),
                            'id_proprietario':fields.Integer(description="ID do Proprietario do Imovel"),
                            'adquirido_em':fields.String(description="Quando o imovel foi adquirido"),
                            'valor_imovel':fields.String(description="Valor de Venda do Imovel")})
#gasto_imovel
nomes_gasto_imovel = appi.namespace('imovel/gasto', description="Operações de registro de despesas de um Imovel")
model_gasto_imovel = appi.model('Despesa Imovel Model',
                                {'id_imovel':fields.Integer(required=True,
                                description="Id do Imovel"),
                                'tipo_gasto':fields.Integer(required=True,
                                description="Tipo de gasto/despesa"),
                                'valor_gasto':fields.Integer(required=True,
                                description="Valor gasto com as despesas do Imovel")})
model_put_gasto_imovel = appi.model('Despesa Imovel Model',
                                    {'id_imovel':fields.Integer(description="Id do Imovel"),
                                    'tipo_gasto':fields.Integer(description="Tipo de gasto/despesa"),
                                    'valor_gasto':fields.Integer(description="Valor gasto com as despesas do Imovel")})
#compra
nomes_compra = appi.namespace('compras', description="Operações de compra de imoveis")
model_compra = appi.model('Compra Model',
                        {'id_imovel':fields.Integer(required=True,
                        description="ID do Imovel que esta sendo comprado"),
                        'id_cliente':fields.Integer(required=True,
                        description="ID do Imovel que esta sendo comprado"),
                        'tipo_pagamento':fields.String(required=True,
                        description="ID do Imovel que esta sendo comprado"),
                        'id_banco':fields.Integer(required=True,
                        description="ID do Imovel que esta sendo comprado"),
                        'valor_pagamento':fields.Integer(required=True,
                        description="ID do Imovel que esta sendo comprado")})
model_put_compra = appi.model('Compra Model',
                              {'id_imovel':fields.Integer(description="ID do Imovel que esta sendo comprado"),
                               'id_cliente':fields.Integer(description="ID do Imovel que esta sendo comprado"),
                               'tipo_pagamento':fields.String(description="ID do Imovel que esta sendo comprado"),
                               'id_banco': fields.Integer(description="ID do Imovel que esta sendo comprado"),
                               'valor_pagamento':fields.Integer(description="ID do Imovel que esta sendo comprado")})
#banco
nomes_banco = appi.namespace('banco', description="Operações com banco")
model_banco = appi.model('Banco Model',
                        {'nm_banco':fields.String(required=True,
                        description="Nome do Banco")})

# criação das tabelas/OBJETOS
#proprietario
class table_proprietario(db.Model):
    id_proprietario = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    nm_proprietario = db.Column(db.String)
    cpf_proprietario = db.Column(db.String)
    rg_proprietario = db.Column(db.String)
    data_nascimento = db.Column(db.Date)
    estado_civil = db.Column(db.String)
    profissao = db.Column(db.String)
    def __init__(self, nm_proprietario, cpf_proprietario, rg_proprietario, data_nascimento, estado_civil, profissao):
        self.nm_proprietario = nm_proprietario
        self.cpf_proprietario = cpf_proprietario
        self.rg_proprietario = rg_proprietario
        self.data_nascimento = data_nascimento
        self.estado_civil = estado_civil
        self.profissao = profissao
#imovel
class table_imovel(db.Model):
    id_imovel = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    tipo_imovel = db.Column(db.String)
    endereco = db.Column(db.String)
    complemento = db.Column(db.String)
    cep = db.Column(db.String)
    uf = db.Column(db.String)
    id_proprietario = db.Column(db.Integer, ForeignKey('table_proprietario.id_proprietario'))
    adquirido_em = db.Column(db.Date)
    valor_imovel = db.Column(db.Integer, unique=True)
    def __init__(self, tipo_imovel, endereco, complemento, cep, uf, id_proprietario, adquirido_em, valor_imovel):
        self.tipo_imovel = tipo_imovel
        self.endereco = endereco
        self.complemento = complemento
        self.cep = cep
        self.uf = uf
        self.id_proprietario = id_proprietario
        self.adquirido_em = adquirido_em
        self.valor_imovel = valor_imovel
#gastos_imovel
class table_gastos_imovel(db.Model):
    id_gasto = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    id_imovel = db.Column(db.Integer, ForeignKey('table_imovel.id_imovel'))
    tipo_gasto = db.Column(db.String)
    valor_gasto = db.Column(db.Integer)
    def __init__(self, id_imovel, tipo_gasto, valor_gasto):
        self.id_imovel = id_imovel
        self.tipo_gasto = tipo_gasto
        self.valor_gasto = valor_gasto
#cliente
class table_cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    nm_cliente = db.Column(db.String)
    cpf_cliente = db.Column(db.String)
    rg_cliente = db.Column(db.String)
    endereco = db.Column(db.String)
    cep = db.Column(db.String)
    uf = db.Column(db.String)
    data_nascimento = db.Column(db.Date)
    estado_civil = db.Column(db.String)
    profissao = db.Column(db.String)
    def __init__(self, nm_cliente, cpf_cliente, rg_cliente, endereco, cep, uf, data_nascimento, estado_civil,profissao):
        self.nm_cliente = nm_cliente
        self.cpf_cliente = cpf_cliente
        self.rg_cliente = rg_cliente
        self.endereco = endereco
        self.cep = cep
        self.uf = uf
        self.data_nascimento = data_nascimento
        self.estado_civil = estado_civil
        self.profissao = profissao
#banco
class table_banco(db.Model):
    id_banco = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    nm_banco = db.Column(db.String)
#compra
class table_compra(db.Model):
    id_compra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_imovel = db.Column(db.Integer, ForeignKey('table_imovel.id_imovel'), unique=True)
    id_cliente = db.Column(db.Integer, ForeignKey('table_cliente.id_cliente'), unique=True)
    tipo_pagamento = db.Column(db.String)
    id_banco = db.Column(db.Integer, ForeignKey('table_banco.id_banco'), unique=True)
    valor_pagamento = db.Column(db.Integer)
    def __init__(self, id_imovel, id_cliente, tipo_pagamento, id_banco, valor_pagamento):
        self.id_imovel = id_imovel
        self.id_cliente = id_cliente
        self.tipo_pagamento = tipo_pagamento
        self.id_banco = id_banco
        self.valor_pagamento = valor_pagamento
        
#CRIANDO TABELAS NO BANCO 
db.create_all()

#MÉTODOS POST, GET, PUT E DELETE - cliente
@nomes_cliente.route('/clientes')
class ClienteClass(Resource):
    @appi.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def get(self):
        try:
            clientes = table_cliente.query.all()
            cli = []
            for cliente in clientes:
                currCliente = {}
                currCliente['id_cliente'] = cliente.id_cliente
                currCliente['nm_cliente'] = cliente.nm_cliente
                currCliente['cpf_cliente'] = cliente.cpf_cliente
                currCliente['rg_cliente'] = cliente.rg_cliente
                currCliente['endereco'] = cliente.endereco
                currCliente['cep'] = cliente.cep
                currCliente['uf'] = cliente.uf
                currCliente['data_nascimento'] = cliente.data_nascimento
                currCliente['estado_civil'] = cliente.estado_civil
                currCliente['profissao'] = cliente.profissao
                cli.append(currCliente)
            return jsonify(cli)
        except KeyError as error:
            nomes_cliente.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nomes_cliente.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")
    @appi.expect(model_cliente)
    def post(self):
        try:
            clienteData = request.get_json()
            cliente = table_cliente(
                nm_cliente=clienteData['nm_cliente'],
                cpf_cliente=clienteData['cpf_cliente'],
                rg_cliente=clienteData['rg_cliente'],
                endereco=clienteData['endereco'],
                cep=clienteData['cep'],
                uf=clienteData['uf'],
                data_nascimento=clienteData['data_nascimento'],
                estado_civil=clienteData['estado_civil'],
                profissao=clienteData['profissao'])
            db.session.add(cliente)
            db.session.commit()
            return jsonify(clienteData)
        except KeyError as error:
            nomes_cliente.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nomes_cliente.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")

@nomes_cliente.route('/clientes/<int:id_cliente>')
class ClienteClass(Resource):
    def get(self, id_cliente):
        try:
            clientes = tb_cliente.query.filter(tb_cliente.id_cliente == id_cliente)
            saida = []
            for cliente in clientes:
                dados_cliente = {}
                dados_cliente['id_cliente'] = cliente.id_cliente
                dados_cliente['nm_cliente'] = cliente.nm_cliente
                dados_cliente['cpf_cliente'] = cliente.cpf_cliente
                dados_cliente['rg_cliente'] = cliente.rg_cliente
                dados_cliente['endereco'] = cliente.endereco
                dados_cliente['cep'] = cliente.cep
                dados_cliente['uf'] = cliente.uf
                dados_cliente['data_nascimento'] = cliente.data_nascimento
                dados_cliente['estado_civil'] = cliente.estado_civil
                dados_cliente['profissao'] = cliente.profissao
                saida.append(dados_cliente)
            return jsonify(saida)
        except KeyError as error:
            nomes_cliente.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nomes_cliente.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")

    def delete(self, id_cliente):
        try:
            cliente_deletado = table_cliente.query.filter(
                table_cliente.id_cliente == id_cliente).delete()
            db.session.commit()
            return jsonify(cliente_deletado)
        except KeyError as error:
            nomes_cliente.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nomes_cliente.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")
@nomes_cliente.route('/clientes/<int:id>')
class ClienteClass(Resource):
    @appi.expect(model_put_cliente)
    def put(self, id):
        try:
            cliente_put = table_cliente.query.get(id)
            cliente_put.nm_cliente = request.json.get('nm_cliente', cliente_put.nm_cliente)
            cliente_put.cpf_cliente = request.json.get('cpf_cliente', cliente_put.cpf_cliente)
            cliente_put.rg_cliente = request.json.get('rg_cliente', cliente_put.rg_cliente)
            cliente_put.endereco = request.json.get('endereco', cliente_put.endereco)
            cliente_put.cep = request.json.get('cep', cliente_put.cep)
            cliente_put.uf = request.json.get('uf', cliente_put.uf)
            cliente_put.data_nascimento = request.json.get('data_nascimento', cliente_put.data_nascimento)
            cliente_put.estado_civil = request.json.get('estado_civil', cliente_put.estado_civil)
            cliente_put.profissao = request.json.get('profissao', cliente_put.profissao)
            db.session.commit()
            return jsonify({
                'nm_cliente': cliente_put.nm_cliente,
                'cpf_cliente': cliente_put.cpf_cliente,
                'rg_cliente': cliente_put.rg_cliente,
                'endereco': cliente_put.endereco,
                'cep': cliente_put.cep,
                'uf': cliente_put.uf,
                'data_nascimento': cliente_put.data_nascimento,
                'estado_civil': cliente_put.estado_civil,
                'profissao': cliente_put.profissao
            })
        except KeyError as error:
            nomes_cliente.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nomes_cliente.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")

# MÉTODOS POST, GET E DELETE - banco
@nomes_banco.route('/banco')
class BancoClass(Resource):
    @appi.expect(model_get_cliente)
    def get(self):
        try:
            bancos = table_banco.query.all()
            ban = []
            for banco in bancos:
                currBanco = {}
                currBanco['id_banco'] = banco.id_banco
                currBanco['nm_banco'] = banco.nm_banco
                ban.append(currBanco)
            return jsonify(ban)
        except KeyError as error:
            nomes_banco.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nomes_banco.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")
    @appi.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @appi.expect(model_banco)
    def post(self):
        try:
            bancoData = request.get_json()
            banco = table_banco(
                nm_banco=bancoData['nm_banco'])
            db.session.add(banco)
            db.session.commit()
            return jsonify(bancoData)
        except KeyError as error:
            nomes_banco.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nomes_banco.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")
@nomes_banco.route('/banco/<int:id_banco>')
class BancoClass(Resource):
    def delete(self, id_banco):
        banco_deletado = table_banco.query.filter(tb_banco.id_banco == id_banco).delete()
        db.session.commit()
        return jsonify(banco_deletado)
    
# MÉTODOS POST, GET, PUT E DELETE - proprietario
@nomes_proprietario.route("/proprietario")
class ProprietarioClass(Resource):
    @appi.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def get(self):
        try:
            # if request.method == 'GET':
            proprietarios = table_proprietario.query.all()
            prop = []
            for proprietario in proprietarios:
                currProprietario = {}
                currProprietario['id_proprietario'] = proprietario.id_proprietario
                currProprietario['nm_proprietario'] = proprietario.nm_proprietario
                currProprietario['cpf_proprietario'] = proprietario.cpf_proprietario
                currProprietario['rg_proprietario'] = proprietario.rg_proprietario
                currProprietario['data_nascimento'] = proprietario.data_nascimento
                currProprietario['estado_civil'] = proprietario.estado_civil
                currProprietario['profissao'] = proprietario.profissao
                prop.append(currProprietario)
            return jsonify(prop)
        except KeyError as error:
            nomes_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nomes_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")
    @appi.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @appi.expect(model_proprietario)
    def post(self):
        try:
            proprietarioData = request.get_json()
            proprietario = tb_proprietario(
                nm_proprietario=proprietarioData['nm_proprietario'],
                cpf_proprietario=proprietarioData['cpf_proprietario'],
                rg_proprietario=proprietarioData['rg_proprietario'],
                data_nascimento=proprietarioData['data_nascimento'],
                estado_civil=proprietarioData['estado_civil'],
                profissao=proprietarioData['profissao'])
            db.session.add(proprietario)
            db.session.commit()
            return jsonify(proprietarioData)
        except KeyError as error:
            nomes_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nomes_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")
@nomes_proprietario.route("/proprietario/<int:id_proprietario>")
class ProprietarioClass(Resource):
    def delete(self, id_proprietario):
        try:
            proprietario_deletado = tb_proprietario.query.filter(
                table_proprietario.id_proprietario == id_proprietario).delete()
            db.session.commit()
            return jsonify(proprietario_deletado)
        except KeyError as error:
            nomes_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nomes_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")
@nomes_proprietario.route("/proprietario/<int:id>")
class ProprietarioClass(Resource):
    @appi.expect(model_put_proprietario)
    def put(self, id):
        try:
            put_proprietario = table_proprietario.query.get(id)
            put_proprietario.nm_proprietario = request.json.get('nm_proprietario', put_proprietario.nm_proprietario)
            put_proprietario.cpf_proprietario = request.json.get('cpf_proprietario', put_proprietario.cpf_proprietario)
            put_proprietario.rg_proprietario = request.json.get('rg_proprietario', put_proprietario.rg_proprietario)
            put_proprietario.data_nascimento = request.json.get('data_nascimento', put_proprietario.data_nascimento)
            put_proprietario.estado_civil = request.json.get('estado_civil', put_proprietario.estado_civil)
            put_proprietario.profissao = request.json.get('profissao', put_proprietario.profissao)
            db.session.commit()
            return jsonify({
                'nm_proprietario': put_proprietario.nm_proprietario,
                'cpf_proprietario': put_proprietario.cpf_proprietario,
                'rg_proprietario': put_proprietario.rg_proprietario,
                'data_nascimento': put_proprietario.data_nascimento,
                'estado_civil': put_proprietario.estado_civil,
                'profissao': put_proprietario.profissao
            })
        except KeyError as error:
            nomes_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nomes_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")

# MÉTODOS POST, GET E DELETE - imovel
@nomes_imovel.route('/imoveis')
class ImovelClass(Resource):
    def get(self):
        try:
            imoveis = table_imovel.query.all()
            imo = []
            for imovel in imoveis:
                currImovel = {}
                currImovel['id_imovel'] = imovel.id_imovel
                currImovel['tipo_imovel'] = imovel.tipo_imovel
                currImovel['endereco'] = imovel.endereco
                currImovel['complemento'] = imovel.complemento
                currImovel['cep'] = imovel.cep
                currImovel['uf'] = imovel.uf
                currImovel['id_proprietario'] = imovel.id_proprietario
                currImovel['adquirido_em'] = imovel.adquirido_em
                currImovel['valor_imovel'] = imovel.valor_imovel
                imo.append(currImovel)
            return jsonify(imo)
        except KeyError as error:
            nomes_imovel.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nomes_imovel.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")
    @appi.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @appi.expect(model_imovel)
    def post(self):
        imovelData = request.get_json()
        imovel = table_imovel(
            tipo_imovel=imovelData['tipo_imovel'],
            endereco=imovelData['endereco'],
            complemento=imovelData['complemento'],
            cep=imovelData['cep'],
            uf=imovelData['uf'],
            id_proprietario=imovelData['id_proprietario'],
            adquirido_em=imovelData['adquirido_em'],
            valor_imovel=imovelData['valor_imovel'])
        db.session.add(imovel)
        db.session.commit()
        return jsonify(imovelData)
@nomes_imovel.route('/imoveis/<int:id_imovel>')
class ImovelClass(Resource):
    def delete(self, id_imovel):
        imovel_deletado = table_imovel.query.filter(table_imovel.id_imovel == id_imovel).delete()
        db.session.commit()
        return jsonify(imovel_deletado)
@nomes_imovel.route('/imoveis/<int:id>')
class ImovelClass(Resource):
    @appi.expect(model_put_imovel)
    def put(self, id):
        try:
            put_imovel = table_imovel.query.get(id)
            put_imovel.tipo_imovel = request.json.get('tipo_imovel', put_imovel.tipo_imovel)
            put_imovel.endereco = request.json.get('endereco', put_imovel.endereco)
            put_imovel.complemento = request.json.get('complemento', put_imovel.complemento)
            put_imovel.cep = request.json.get('cep', put_imovel.cep)
            put_imovel.uf = request.json.get('uf', put_imovel.uf)
            put_imovel.id_proprietario = request.json.get('id_proprietario', put_imovel.id_proprietario)
            put_imovel.adquirido_em = request.json.get('adquirido_em', put_imovel.adquirido_em)
            put_imovel.valor_imovel = request.json.get('valor_imovel', put_imovel.valor_imovel)
            db.session.commit()
            return jsonify({
                'tipo_imovel': put_imovel.tipo_imovel,
                'endereco': put_imovel.endereco,
                'complemento': put_imovel.complemento,
                'cep': put_imovel.cep,
                'uf': put_imovel.uf,
                'id_proprietario': put_imovel.id_proprietario,
                'adquirido_em': put_imovel.adquirido_em,
                'valor_imovel': put_imovel.valor_imovel
            })
        except KeyError as error:
            nomes_imovel.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nomes_imovel.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")

# MÉTODOS POST, GET E DELETE - gastos com imovel
@nomes_gasto_imovel.route('/gastos_imovel')
class GastosClass(Resource):
    def get(self):
        try:
            gastos = table_gastos_imovel.query.all()
            gas = []
            for gasto in gastos:
                currGasto = {}
                currGasto['id_imovel'] = gasto.id_imovel
                currGasto['tipo_gasto'] = gasto.tipo_gasto
                currGasto['valor_gasto'] = gasto.valor_gasto
                gas.append(currGasto)
            return jsonify(gas)
        except KeyError as error:
            nomes_gasto_imovel.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nomes_gasto_imovel.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")
    @appi.expect(model_gasto_imovel)
    def post(self):
        gastoData = request.get_json()
        gasto = tb_gastos_imovel(
            id_imovel=gastoData['id_imovel'],
            tipo_gasto=gastoData['tipo_gasto'],
            valor_gasto=gastoData['valor_gasto'])
        db.session.add(gasto)
        db.session.commit()
        return jsonify(gastoData)
@nomes_gasto_imovel.route('/gastos_imovel/<int:id>')
class GastosClass(Resource):
    @appi.expect(model_put_gasto_imovel)
    def put(self, id):
        try:
            put_gasto = table_gastos_imovel.query.get(id)
            put_gasto.id_imovel = request.json.get('id_imovel', put_gasto.id_imovel)
            put_gasto.tipo_gasto = request.json.get('tipo_gasto', put_gasto.tipo_gasto)
            put_gasto.valor_gasto = request.json.get('valor_gasto', put_gasto.valor_gasto)
            db.session.commit()
            return jsonify({
                'id_imovel': put_gasto.id_imovel,
                'tipo_gasto': put_gasto.tipo_gasto,
                'valor_gasto': put_gasto.valor_gasto
            })
        except KeyError as error:
            nomes_gasto_imovel.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nomes_gasto_imovel.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")

# MÉTODOS POST , PUT e GET - compra
@nomes_compra.route('/compra')
class CompraClass(Resource):
    @appi.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def get(self):
        try:
            compras = table_compra.query.all()
            comp = []
            for compra in compras:
                currCompra = {}
                currCompra['id_compra'] = compra.id_compra
                currCompra['id_imovel '] = compra.id_imovel
                currCompra['id_cliente '] = compra.id_cliente
                currCompra['tipo_pagamento'] = compra.tipo_pagamento
                currCompra['id_banco'] = compra.id_banco
                currCompra['valor_pagamento'] = compra.valor_pagamento
                comp.append(currCompra)
            return jsonify(comp)
        except KeyError as error:
            nomes_compra.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nomes_compra.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")
    @appi.expect(model_compra)
    def post(self):
        compra_data = request.get_json()
        compra = table_compra(
            id_imovel=compra_data['id_imovel'],
            id_cliente=compra_data['id_cliente'],
            tipo_pagamento=compra_data['tipo_pagamento'],
            id_banco=compra_data['id_banco'],
            valor_pagamento=compra_data['valor_pagamento'])
        db.session.add(compra)
        db.session.commit()
        return jsonify(compra_data)
@nomes_compra.route('/compra/<int:id>')
class CompraClass(Resource):
    @appi.expect(model_put_compra)
    def put(self, id):
        try:
            put_compra = table_compra.query.get(id)
            put_compra.id_imovel = request.json.get('id_imovel', put_compra.id_imovel)
            put_compra.id_cliente = request.json.get('id_cliente', put_compra.id_cliente)
            put_compra.tipo_pagamento = request.json.get('tipo_pagamento', put_compra.tipo_pagamento)
            put_compra.id_banco = request.json.get('id_banco', put_compra.id_banco)
            put_compra.valor_pagamento = request.json.get('valor_pagamento', put_compra.valor_pagamento)
            db.session.commit()
            return jsonify({
                'id_imovel': put_compra.id_imovel,
                'id_cliente': put_compra.id_cliente,
                'tipo_pagamento': put_compra.tipo_pagamento,
                'id_banco': put_compra.id_banco,
                'valor_pagamento': put_compra.valor_pagamento
            })
        except KeyError as error:
            nomes_compra.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nomes_compra.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")
