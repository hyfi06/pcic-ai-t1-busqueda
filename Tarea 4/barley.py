import os
import gzip
import requests
from pgmpy.readwrite.BIF import BIFReader
from pgmpy.inference import VariableElimination


def download_and_decompress(url, dest_filename):
    print('Descargando...')
    response = requests.get(url, stream=True)
    with open(dest_filename, 'wb') as f_out:
        for chunk in response.iter_content(chunk_size=8192):
            f_out.write(chunk)

    print('Decomprimiendo...')
    if dest_filename.endswith('.gz'):
        with gzip.open(dest_filename, 'rb') as f_in:
            decompressed_file_content = f_in.read()
            with open(dest_filename[:-3], 'wb') as f_out:
                f_out.write(decompressed_file_content)  # type: ignore
        return dest_filename[:-3]
    print('Éxito!')
    return dest_filename


def load_barley():
    file_name = 'barley.bif'
    if not os.path.exists(f"./{file_name}"):
        url = 'https://www.bnlearn.com/bnrepository/barley/barley.bif.gz'
        file_name = download_and_decompress(url, f"{file_name}.gz")
    barley = BIFReader(file_name)
    return barley.get_model()


def main():
    model = load_barley()
    print("Nodos:")
    print(model.nodes(), end='\n\n')
    print('Aristas:')
    print(model.edges(), end='\n\n')

    infer = VariableElimination(model)

    print('P(keraks| slt22=x0_1, protein=x10_5_11_0)')
    query_result = infer.query(
        variables=['keraks'],
        evidence={
            'slt22': 'x0_1',
            'protein': 'x10_5_11_0'
        }
    )
    print(query_result, end='\n\n')

    print('P(nprot| aks_m2=x450_550, dgv5980=x15_25)')
    query_result = infer.query(
        variables=['nprot'],
        evidence={
            'aks_m2': 'x450_550',
            'dgv5980': 'x15_25'
        }
    )
    print(query_result, end='\n\n')

    print('P(protein| spndx=x_7)')
    query_result = infer.query(
        variables=['protein'],
        evidence={
            'spndx': 'x_7',
        }
    )
    print(query_result, end='\n\n')

    print(f"Están D-separados de 'nprot' al observar 'protein': ", end='')
    print(model.active_trail_nodes('nprot', observed='protein'))


if __name__ == "__main__":
    main()
