
# Create a region
class Region:

    def __init__(self, regionName):
        self.regionName = regionName
        self.descendents = list()

    def checkIfItsEqual(self, region):
        
        region_to_check = [ [self, region] ]
        
        # Para cada descendente precisamos de verificar todos os seus descendentes
        # com a outra região, com isso temos muitas comparações e uma 
        # complexidade de tempo de O(n^2)

        while region_to_check:
            region_a, region_b = region_to_check.pop()

            if region_a.regionName != region_b.regionName:
                return False

            # Aqui, precisamos de comparar os descendentes
            # de cada uma das regiões
            if len(region_a.descendents) != len(region_b.descendents):
                return False

            # Existe uma melhor solução utilizando sets
            # ou alguma outra estrutura que a ordem dos elementos
            # não importe, pois assim não seria necessário utilizar
            # o sorted(), o que reduziria a complexidade de tempo
            for i in range(len(region_a.descendents)):
                region_to_check.append(
                    [region_a.descendents[i], region_b.descendents[i]]
                )

        return True

if __name__ == '__main__':

    br = Region('Brazil')

    rj = Region('RJ')
    rj.descendents.append(Region("buzios"))
    rj.descendents.append(Region("marica"))
    rj.descendents.append(Region("rio-de-janeiro"))

    br.descendents.append(rj)
    
    print(br.regionName)
    print(br.descendents[0].descendents[0].regionName)

# Create another region

    br2 = Region('Brazil')

    rj2 = Region('RJ')
    rj2.descendents.append(Region("buzios"))
    rj2.descendents.append(Region("marica"))
    rj2.descendents.append(Region("rio-de-janeiro"))

    br2.descendents.append(rj2)

    print(br2.regionName)
    print(br2.descendents[0].descendents[0].regionName)


    # Compare them
    areEqual = br.checkIfItsEqual(br2)

    print(areEqual)

    # {2, 5}
    # {5, 2}


