import pandas as pd


def get_Digits(value):
    tknno = int(float(value))
    tknno = str(tknno)
    tknno = tknno.zfill(4)

    return tknno


def get_minted():
    df = pd.read_excel('minted.xlsx')
    df = df.astype({"Mint": "int"})
    minted = df.values
    return minted


def get_data_final(changing=False):
    data = []
    if changing:
        df = pd.read_excel('Dabbu Metadata single.xlsx')
        df = df.dropna(how='all')
        df = df.astype({"PNG File No": 'str', })
        df_ones = df.loc[df['PNG File No'].str.contains(".", case=False)]
        df_ones = df_ones.drop_duplicates(subset=["PNG File No"])
        df_ones['Folder'] = df_ones['PNG File No'].str.split('.', expand=True)[0]
        df_ones['path'] = "https://dabbu.mypinata.cloud/ipfs/QmcwRKVjNEV24ReFjXVzBJvqFm7q9MfR5gk4QGRgmybmQk/" + df_ones[
            ['Folder', 'PNG File No']].agg('/'.join, axis=1) + ".png"
        df_ones = df_ones.astype({"PNG File No": 'float64', "Folder": 'int64', })
        data = df_ones.values
    return data


def get_data_ForStandar(changing=False, image_version=".1"):
    data = []
    if changing:
        df = pd.read_excel('Dabbu Metadata single.xlsx')
        df = df.dropna(how='all')
        df = df.astype({"PNG File No": 'str', })
        df_ones = df.loc[df['PNG File No'].str.contains(image_version, case=True, regex=False)]
        df_ones = df_ones.drop_duplicates(subset=["PNG File No"])
        df_ones['Folder'] = df_ones['PNG File No'].str.split('.', expand=True)[0]
        df_ones['path'] = "https://dabbu.mypinata.cloud/ipfs/QmcwRKVjNEV24ReFjXVzBJvqFm7q9MfR5gk4QGRgmybmQk/" + df_ones[
            ['Folder', 'PNG File No']].agg('/'.join, axis=1) + ".png"
        df_ones = df_ones.astype({"PNG File No": 'float64', "Folder": 'int64', })
        data = df_ones.values
    return data


def check_Christmas(pageno='1.1', path=''):
    if path.find('Christmassy') >= 0 and pageno.find('.1') >= 0:
        return True
    return False


def get_data_ForSimilar(changing=False, version_code="1.1", path=''):
    if changing:
        if path.find('Christmassy') >= 0 and version_code.find('.1') >= 0:
            return get_Christmas(changing=True)
        elif path.find('Metaverse') >= 0 and version_code.find('.2') >= 0:
            return get_coloured(changing=True)
        elif path.find('CharacterToken') >= 0:
            return get_Character(changing=True)
        df = pd.read_excel('Dabbu Metadata single.xlsx')
        df = df.dropna(how='all')
        df = df.astype({"PNG File No": 'str', })
        df_ones = df.loc[df['PNG File No'].str.contains(str(version_code), case=False)]
        df_ones = df_ones.drop_duplicates(subset=["PNG File No"])
        df_ones['Folder'] = df_ones['PNG File No'].str.split('.', expand=True)[0]
        df_ones['path'] = "https://dabbu.mypinata.cloud/ipfs/QmcwRKVjNEV24ReFjXVzBJvqFm7q9MfR5gk4QGRgmybmQk/" + df_ones[
            ['Folder', 'PNG File No']].agg('/'.join, axis=1) + ".png"
        df_ones = df_ones.astype({"PNG File No": 'float64', "Folder": 'int64', })
    return df_ones.values[:7]


def get_Orignial(changing=False):
    orgdata = []
    if changing:
        df = pd.read_excel('Dabbu Metadata single.xlsx')
        df = df.dropna(how='all')
        df = df.astype({"PNG File No": 'str', })
        df_ones = df.loc[df['PNG File No'].str.contains('.1', case=True)]
        df_ones = df_ones.drop_duplicates(subset=["Token Name"])
        df_ones['Folder'] = df_ones['PNG File No'].str.split('.', expand=True)[0]
        df_ones['path'] = "https://dabbu.mypinata.cloud/ipfs/QmcwRKVjNEV24ReFjXVzBJvqFm7q9MfR5gk4QGRgmybmQk/" + df_ones[
            ['Folder', 'PNG File No']].agg('/'.join, axis=1) + ".png"
        df_ones = df_ones.astype({"PNG File No": 'float64', "Folder": 'int64', })
        orgdata = df_ones.values
    return orgdata


def get_Eatrth(changing=False):
    orgdata = []
    if changing:
        df = pd.read_excel('Dabbu Metadata single.xlsx')
        df = df.dropna(how='all')
        df = df.astype({"PNG File No": 'str', })
        df_ones = df.loc[df['PNG File No'].str.contains(".2", case=True, regex=False)]
        df_ones = df_ones.drop_duplicates(subset=["Token Name"])
        df_ones['Folder'] = df_ones['PNG File No'].str.split('.', expand=True)[0]
        df_ones['path'] = "https://dabbu.mypinata.cloud/ipfs/QmcwRKVjNEV24ReFjXVzBJvqFm7q9MfR5gk4QGRgmybmQk/" + df_ones[
            ['Folder', 'PNG File No']].agg('/'.join, axis=1) + ".png"
        df_ones = df_ones.astype({"PNG File No": 'float64', "Folder": 'int64', })
        orgdata = df_ones.values
    return orgdata


def get_Water(changing=False):
    orgdata = []
    if changing:
        df = pd.read_excel('Dabbu Metadata single.xlsx')
        df = df.dropna(how='all')
        df = df.astype({"PNG File No": 'str', })
        df_ones = df.loc[df['PNG File No'].str.contains(".3", case=True, regex=False)]
        df_ones = df_ones.drop_duplicates(subset=["Token Name"])
        df_ones['Folder'] = df_ones['PNG File No'].str.split('.', expand=True)[0]
        df_ones['path'] = "https://dabbu.mypinata.cloud/ipfs/QmcwRKVjNEV24ReFjXVzBJvqFm7q9MfR5gk4QGRgmybmQk/" + df_ones[
            ['Folder', 'PNG File No']].agg('/'.join, axis=1) + ".png"
        df_ones = df_ones.astype({"PNG File No": 'float64', "Folder": 'int64', })
        orgdata = df_ones.values
    return orgdata


def get_Fire(changing=False):
    orgdata = []
    if changing:
        df = pd.read_excel('Dabbu Metadata single.xlsx')
        df = df.dropna(how='all')
        df = df.astype({"PNG File No": 'str', })
        df_ones = df.loc[df['PNG File No'].str.contains(".4", case=True, regex=False)]
        df_ones = df_ones.drop_duplicates(subset=["Token Name"])
        df_ones['Folder'] = df_ones['PNG File No'].str.split('.', expand=True)[0]
        df_ones['path'] = "https://dabbu.mypinata.cloud/ipfs/QmcwRKVjNEV24ReFjXVzBJvqFm7q9MfR5gk4QGRgmybmQk/" + df_ones[
            ['Folder', 'PNG File No']].agg('/'.join, axis=1) + ".png"
        df_ones = df_ones.astype({"PNG File No": 'float64', "Folder": 'int64', })
        orgdata = df_ones.values
    return orgdata


def get_Air(changing=False):
    orgdata = []
    if changing:
        df = pd.read_excel('Dabbu Metadata single.xlsx')
        df = df.dropna(how='all')
        df = df.astype({"PNG File No": 'str', })
        df_ones = df.loc[df['PNG File No'].str.contains(".5", case=True, regex=False)]
        df_ones = df_ones.drop_duplicates(subset=["Token Name"])
        df_ones['Folder'] = df_ones['PNG File No'].str.split('.', expand=True)[0]
        df_ones['path'] = "https://dabbu.mypinata.cloud/ipfs/QmcwRKVjNEV24ReFjXVzBJvqFm7q9MfR5gk4QGRgmybmQk/" + df_ones[
            ['Folder', 'PNG File No']].agg('/'.join, axis=1) + ".png"
        df_ones = df_ones.astype({"PNG File No": 'float64', "Folder": 'int64', })
        orgdata = df_ones.values
    return orgdata


def get_Space(changing=False):
    orgdata = []
    if changing:
        df = pd.read_excel('Dabbu Metadata single.xlsx')
        df = df.dropna(how='all')
        df = df.astype({"PNG File No": 'str', })
        df_ones = df.loc[df['PNG File No'].str.contains(".6", case=True, regex=False)]
        df_ones = df_ones.drop_duplicates(subset=["Token Name"])
        df_ones['Folder'] = df_ones['PNG File No'].str.split('.', expand=True)[0]
        df_ones['path'] = "https://dabbu.mypinata.cloud/ipfs/QmcwRKVjNEV24ReFjXVzBJvqFm7q9MfR5gk4QGRgmybmQk/" + df_ones[
            ['Folder', 'PNG File No']].agg('/'.join, axis=1) + ".png"
        df_ones = df_ones.astype({"PNG File No": 'float64', "Folder": 'int64', })
        orgdata = df_ones.values
    return orgdata


def get_Manuscript(changing=False):
    orgdata = []
    if changing:
        df = pd.read_excel('Dabbu Metadata single.xlsx')
        df = df.dropna(how='all')
        df = df.astype({"PNG File No": 'str', })
        df_ones = df.loc[df['PNG File No'].str.contains(".7", case=True, regex=False)]
        df_ones = df_ones.drop_duplicates(subset=["Token Name"])
        df_ones['Folder'] = df_ones['PNG File No'].str.split('.', expand=True)[0]
        df_ones['path'] = "https://dabbu.mypinata.cloud/ipfs/QmcwRKVjNEV24ReFjXVzBJvqFm7q9MfR5gk4QGRgmybmQk/" + df_ones[
            ['Folder', 'PNG File No']].agg('/'.join, axis=1) + ".png"
        df_ones = df_ones.astype({"PNG File No": 'float64', "Folder": 'int64', })
        orgdata = df_ones.values
    return orgdata


def get_mataverse(changing=False):
    orgdata = []
    if changing:
        df = pd.read_excel('Dabbu Metadata single.xlsx')
        df = df.dropna(how='all')
        df = df.astype({"PNG File No": 'str', })
        df_ones = df.loc[df['PNG File No'].str.contains(".8", case=True, regex=False)]
        df_ones = df_ones.drop_duplicates(subset=["Token Name"])
        df_ones['Folder'] = df_ones['PNG File No'].str.split('.', expand=True)[0]
        df_ones['path'] = "https://dabbu.mypinata.cloud/ipfs/QmcwRKVjNEV24ReFjXVzBJvqFm7q9MfR5gk4QGRgmybmQk/" + df_ones[
            ['Folder', 'PNG File No']].agg('/'.join, axis=1) + ".png"
        df_ones = df_ones.astype({"PNG File No": 'float64', "Folder": 'int64', })
        orgdata = df_ones.values
    return orgdata


def get_Christmas(changing=False):
    chrdata = []
    if changing:
        xls = pd.ExcelFile('Dabbu Metadata single.xlsx')
        df = pd.read_excel(xls, '53 Christmas Special Token (FIN')
        df = df.dropna(how='all')
        df = df.astype({"PNG File No": 'str', })
        df_ones = df.loc[df['PNG File No'].str.contains(".1", case=True, regex=False)]
        df_ones = df_ones.drop_duplicates(subset=["PNG File No"])
        # df_ones['Folder'] = df_ones['53 Christmas Token'].str.split('.', expand=True)[0]
        df_ones['path'] = "https://dabbu.mypinata.cloud/ipfs/QmcwRKVjNEV24ReFjXVzBJvqFm7q9MfR5gk4QGRgmybmQk" \
                          "/ChristmasToken/Christmassy/" + df_ones[['PNG File No']].agg('/'.join, axis=1) + ".png "
        df_ones = df_ones.astype({"PNG File No": 'float64'})
        chrdata = df_ones.values
    return chrdata


def get_Character(changing=False, typea='random'):
    chrdata = []
    if changing:
        xls = pd.ExcelFile('Dabbu Metadata single.xlsx')
        df = pd.read_excel(xls, '34 Character Token (FINAL)')
        df = df.dropna(how='all')
        df = df.astype({"PNG File No": 'str', })
        df_ones = df.loc[df['PNG File No'].str.contains(".", case=False)]
        df_ones = df_ones.drop_duplicates(subset=["Token Name"])
        # df_ones['Folder'] = df_ones['53 Christmas Token'].str.split('.', expand=True)[0]
        df_ones['path'] = "https://dabbu.mypinata.cloud/ipfs/QmcwRKVjNEV24ReFjXVzBJvqFm7q9MfR5gk4QGRgmybmQk" \
                          "/CharacterToken/" + df_ones[['PNG File No']].agg('/'.join, axis=1) + ".png "
        df_ones = df_ones.astype({"PNG File No": 'float64'})
        chrdata = df_ones.values
        fancy = []
        for x in chrdata:
            if x[7] == typea:
                fancy.append(x)
        if typea != 'random' and typea is not None:
            return fancy
    return chrdata


def get_coloured(changing=False):
    chrdata = []
    if changing:
        xls = pd.ExcelFile('Dabbu Metadata single.xlsx')
        df = pd.read_excel(xls, '53 Christmas Special Token (FIN')
        df = df.dropna(how='all')
        df = df.astype({"PNG File No": 'str', })
        df_ones = df.loc[df['PNG File No'].str.contains(".2", case=True, regex=False)]
        df_ones = df_ones.drop_duplicates(subset=["PNG File No"])
        df_ones['path'] = "https://dabbu.mypinata.cloud/ipfs/QmcwRKVjNEV24ReFjXVzBJvqFm7q9MfR5gk4QGRgmybmQk" \
                          "/ChristmasToken/Metaverse/" + df_ones[['PNG File No']].agg('/'.join, axis=1) + ".png "
        df_ones = df_ones.astype({"PNG File No": 'float64'})
        chrdata = df_ones.values
    return chrdata
