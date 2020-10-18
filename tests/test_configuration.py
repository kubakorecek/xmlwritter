# ============ Testing the config_setter ========================#

from src.configuration.web_areal.config_setter import SetWebAreal
import pytest


@pytest.mark.parametrize("input_cnf,output_cnf", [('tests/test_config.ini', 'config.ini')])
def test_inti_WA(input_cnf, output_cnf):
    wb = SetWebAreal()
    wb.output_cnf, wb.input_cnf = output_cnf, input_cnf
    assert (wb.input_cnf, wb.output_cnf) == (input_cnf, output_cnf)
