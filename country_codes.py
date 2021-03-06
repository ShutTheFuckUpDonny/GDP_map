'''Pygal использует систему с двухбуквенными кодами, а JSON-файл имеет 3-буквенный'''

from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        if country_name == "Yemen, Rep.": return 'ye'
        if country_name == "Iran, Islamic Rep.": return 'ir'
        if country_name == "Kyrgyz Republic": return 'kg'
        if country_name == 'Moldova': return 'md'
        if country_name == 'Slovak Republic': return 'sk'
        if country_name == 'Venezuela, RB': return 've'
        if country_name == 'Bolivia': return 'bo'
        if country_name == 'Libya': return 'ly'
        if country_name == 'Egypt, Arab Rep.': return 'eg'
        if country_name == 'Korea, Rep.': return 'kr'
        if country_name == 'Tanzania': return 'tz'
        if country_name == 'Congo, Dem. Rep.': return 'cd'
        if country_name == 'Congo, Rep.': return 'cg'
        if country_name == 'Cabo Verde': return 'cv'
        if country_name == 'Vietnam': return 'vn'
        if country_name == 'Lao PDR': return 'la'
        if country_name == 'West Bank and Gaza': return 'ps'
        if country_name == 'Gambia, The': return 'gm'
        if country_name == 'Macedonia, FYR': return 'mk'
        if country_name == 'Hong Kong SAR, China': return 'hk'
    # Если страна не найдена, вернуть None
    return None
