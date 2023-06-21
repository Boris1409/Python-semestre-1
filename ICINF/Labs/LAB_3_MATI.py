dic_regiones = {
    14: {
        'Los Rios':{
            'Superficie':18429, 
            'Habitantes':404432
            },
    },
    12: {
        'Magallanes':{
            'Superficie':1382291,
            'Habitantes':166533
        }
        }
}
print(dic_regiones)
print("\n")

dic_regiones[14]['Los Rios']['Densidad'] = round((dic_regiones[14]['Los Rios']['Habitantes'] / dic_regiones[14]['Los Rios']['Superficie']),1)
dic_regiones[12]['Magallanes']['Densidad'] = round((dic_regiones[12]['Magallanes']['Habitantes'] / dic_regiones[12]['Magallanes']['Superficie']),1)
print(dic_regiones)
print("\n")

dic_regiones[14]['Capital'] = ['Valdivia']
dic_regiones[12]['Capital'] = ['Punta Arenas']
print(dic_regiones)
print("\n")

dic_regiones[14]['Comunas'] = ['Rio Bueno', 'La Unión', 'Paillaco']
dic_regiones[12]['Comunas'] = ['Cabo de hornos', 'Puerto Williams', 'Porvenir']
print(dic_regiones)
print("\n")

dic_regiones[14]['Provincia'] = ['Ranco', 'Valdivia']
dic_regiones[12]['Provincia'] = ['Antartica Chilena','Magallanes', 'Tierra del fuego', 'Última Esperanza']
print(dic_regiones)