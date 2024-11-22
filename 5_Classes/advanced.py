import fire

# Here's an example of how you might  make a command line interface with grouped
# commands.


class IngestionStage():

    def run(self):
        return 'Ingesting! Nom nom nom...'


class DigestionStage():

    def run(self, volume=1):
        return ' '.join(['Burp!'] * volume)

    def status(self):
        return 'Satiated.'


class Pipeline():

    def __init__(self):
        self.ingestion = IngestionStage()
        self.digestion = DigestionStage()

    def run(self):
        ingestion_output = self.ingestion.run()
        digestion_output = self.digestion.run()
        return [ingestion_output, digestion_output]


if __name__ == '__main__':
    fire.Fire(Pipeline)
