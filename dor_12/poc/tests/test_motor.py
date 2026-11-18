
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from dor_12.poc.motor import avaliar
from poc_shared import executar, gravar_imutavel

BASE = Path(__file__).resolve().parents[1]


class PocTests(unittest.TestCase):

    def test_cenarios_sinteticos(self):
        casos = json.loads(
            (BASE / "fixtures" / "cenarios.json")
            .read_text(encoding="utf-8")
        )

        for caso in casos:
            with self.subTest(caso=caso["caso"]):
                resultado = avaliar(caso)
                self.assertEqual(
                    resultado["status"], caso["esperado"]
                )
                self.assertFalse(
                    resultado["ajuste_automatico"]
                )

    def test_reexecucao_idempotente(self):
        primeira = executar(BASE, avaliar, salvar=True)
        segunda = executar(BASE, avaliar, salvar=True)

        self.assertEqual(primeira, segunda)

    def test_integridade_resultados(self):
        resultado = executar(BASE, avaliar, salvar=True)
        lote = resultado["lote"]

        destino = BASE / "output" / f"gold_{lote}.json"

        with self.assertRaises(RuntimeError):
            gravar_imutavel(
                destino,
                {"conteudo": "ALTERADO"}
            )


if __name__ == "__main__":
    unittest.main()
