class Carta:
    
    def __init__(self, valor='', palo=''):
        self.__valor = valor
        self.__palo = palo
        self.__visible:bool = False
        
    @property
    def visible(self):
        return self.__visible
        
    @visible.setter
    def visible(self, visible):
        self.__visible = visible
        
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
        
    @property
    def palo(self):
        return self.__palo
    
    @palo.setter
    def palo(self, palo):
        self.__palo = palo  
    
    def _valor_numerico(self):
        valores = ['J','Q','K','A']
        if self.valor in valores:
            idx = valores.index(self.valor)
            return (11 + idx)
        return int(self.valor)            
            
        
    def __gt__(self, otra):
        """2 cartas deben compararse por su valor numérico"""
        return self._valor_numerico() > otra._valor_numerico()
        
    def __str__(self):
        if self.visible == False:
            return "-X"
        else:
            return self.valor + self.palo
    
    def __repr__(self):
        return str(self)
    
    
if __name__ == "__main__":
    carta = Carta("♣", "3")
    print(carta)
    carta.visible = True
    print(carta)
    