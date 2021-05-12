from dataclasses import dataclass


@dataclass
class FileReader:
    context: str = ''
    fname: str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''

    @staticmethod
    def main():
        fr = FileReader()
        fr.context = 'context'
        print(f'context: {fr.context}')

if __name__ == '__main__':
    FileReader.main()