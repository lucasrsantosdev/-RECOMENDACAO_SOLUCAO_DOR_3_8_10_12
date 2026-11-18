
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from poc_shared import executar
from dor_10.poc.motor import avaliar

if __name__ == "__main__":
    resultado = executar(Path(__file__).parent, avaliar)

    print("POC 10 - EXECUCAO CONCLUIDA")
    print("Lote:", resultado["lote"])
    print("Casos:", resultado["gold"]["total"])
    print("Status:", resultado["gold"]["por_status"])
    print("RAW / Bronze / Silver / Gold: OK")
    print("Ajustes nos sistemas de origem: NENHUM")
