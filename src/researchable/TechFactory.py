from researchable.Tech import Tech


class TechFactory:
    @staticmethod
    def pottery():
        return Tech('Pottery', 35)

    @staticmethod
    def writing():
        return Tech('Writing', 55)
    
