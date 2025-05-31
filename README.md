# Treti_ukol
Zadány 3 testovací funkce, výsledek viz níže. Vzhledem k tomu, že mám verzi Phytonu 3.13.2, měl jsem jsem problémy s použitím vlastní page, proto ji v testu nepoužívám. Raději pro potlačení chybové hlášky PytestDeprecationWarning jsem vytvořil pytest.ini, který je součástí testu.
Využívám prohlížeč MS Edge.
Výsledek testů:
pytest test_wilsonka.py -v
=========================================== test session starts ===========================================
platform win32 -- Python 3.13.2, pytest-8.3.5, pluggy-1.5.0 -- C:\Users\Petr\AppData\Local\Programs\Python\P
                                                                                                          Python313\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.13.2', 'Platform': 'Windows-11-10.0.26100-SP0', 'Packages': {'pytest': '8.3.5', 'pluggy': '1.5.0'}, 'Plugins': {'anyio': '4.9.0', 'asyncio': '1.0.0', 'base-url': '2.1.0', 'cov': '6.1.1', 'html': '4.1.1', 'metadata': '3.1.1', 'playwright': '0.7.0'}, 'Base URL': ''}
rootdir: C:\Users\Petr\Documents\Testování\Projekt 3
configfile: pytest.ini
plugins: anyio-4.9.0, asyncio-1.0.0, base-url-2.1.0, cov-6.1.1, html-4.1.1, metadata-3.1.1, playwright-0.7.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=function, asyncio_default_test_loop_scope=function
collected 3 items                                                                                          

test_wilsonka.py::test_cookies[chromium] PASSED                                                      [ 33%]
test_wilsonka.py::test_hledat[chromium] PASSED                                                       [ 66%]
test_wilsonka.py::test_title[chromium] PASSED                                                        [100%]

