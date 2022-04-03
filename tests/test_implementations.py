from foldering.implementations import JsonValidator, Configuration
from foldering import Reader
from pathlib import Path


class TestConfiguration:
    def test_init_configuration(self):
        alpha = Configuration({})
        result = {}
        assert alpha == {}

        alpha = Configuration({"alpha": 1})
        result = {"alpha": 1}
        assert alpha == result

    def test_get_configuration(self):
        alpha = Configuration({"alpha": 1, "beta": Configuration({"beta": 2})})
        assert alpha["alpha"] == 1
        assert alpha["beta", "beta"] == 2
        assert alpha.alpha == 1
        assert alpha.beta.beta == 2

    def test_set_configuration(self):
        alpha = Configuration({"alpha": 1, "beta": Configuration({"beta": 1})})
        alpha["alpha"] = 2
        assert alpha["alpha"] == 2

        alpha.alpha = 1
        assert alpha.alpha == 1

        alpha["beta", "beta"] = 2
        assert alpha["beta", "beta"] == 2

        alpha.beta.beta = 1
        assert alpha.beta.beta == 1

        alpha.beta.beta = Configuration({"beta": 1})
        assert alpha.beta.beta == {"beta": 1}


class TestValidator:
    def test_init_validator(self):
        reader = Reader()
        schema = reader.openFile(Path("./conf/schemas/schema.json"))
        validator = JsonValidator(schema)
        test = reader.openFile(Path("./conf/parameters/a.txt"))
        assert validator.validate(test)

    def test_set_validator(self):
        validator = JsonValidator()
        reader = Reader()
        validator.schema = reader.openFile(Path("./conf/schemas/schema.json"))
        test = reader.openFile(Path("./conf/parameters/a.txt"))
        assert validator.validate(test)

    def test_get_validator(self):
        reader = Reader()
        schema = reader.openFile(Path("./conf/schemas/schema.json"))
        validator = JsonValidator(schema)
        test = reader.openFile(Path("./conf/schemas/schema.json"))
        assert validator.schema == test
