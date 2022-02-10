@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        director_name = request.args.get('name')
        res = Director.query
        if director_name is not None:
            res = res.filter(Director.name == director_name)
        result = res.all()
        return direct_schema.dump(result, many=True), 200

    def post(self):
        r_json = request.json
        add_director = Director(**r_json)
        with db.session.begin():
            db.session.add(add_director)
        return "", 201


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid):
        director = Director.query.get(uid)
        if not director:
            return "", 404
        return direct_schema.dump(director)

    def put(self, uid):
        director = Director.query.get(uid)
        if not director:
            return "", 404

        director.name = request.json.get("name")
        db.session.add(director)
        db.session.commit()
        return "", 204

    def delete(self, uid):
        director = Director.query.get(uid)
        if not director:
            return "", 404
        db.session.delete(director)
        db.session.commit()
        return "", 204