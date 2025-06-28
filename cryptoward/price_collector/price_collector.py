from pydantic import BaseModel


class PriceCollector(BaseModel):
    @staticmethod
    def start() -> None:
        print("Consuming Kafka events")
