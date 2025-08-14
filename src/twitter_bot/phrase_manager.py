import random
from redis import Redis
class PhraseManager:

    def __init__(self, redis_store: Redis, key_phrases: str = 'phrases_database', key_used: str = 'used_phrases', key_forced_phrases: str = 'forced_phrases'):
        self.store = redis_store
        self.phrases_db_key = key_phrases
        self.used_phrases_db_key = key_used
        self.forced_phrases_db_key = key_forced_phrases
        self.hashtag: str = self.store.get('hashtags_to_append')
        self.forced_phrases_placeholder: str = 'PLACEHOLDER'
        self.used_phrases_placeholder: str = 'PLACEHOLDER'

        # Add placeholders if they don't exist
        self.store.sadd(self.used_phrases_db_key,self.used_phrases_placeholder)
        self.store.sadd(self.forced_phrases_db_key,self.forced_phrases_placeholder)

        self.get_phrases_databases()
    
    def get_phrases_databases(self) -> None:
        """Updates all phrases databases from redis:
        - General phrases
        - Used phrases
        - Forced phrases
        """
        self.phrases_db = self.store.smembers(self.phrases_db_key)
        self.used_phrases_db = self.store.smembers(self.used_phrases_db_key)
        self.forced_phrases_db = self.store.smembers(self.forced_phrases_db_key)

    def get_forced_phrase(self, remove_forced_phrase: bool = True) -> str:
        phrase = self.forced_phrases_placeholder
        if self.forced_phrase_available():
            # Keep selecting until phrase is different from placeholder
            while phrase == self.forced_phrases_placeholder:
                phrase = random.choice(list(self.forced_phrases_db))
            if remove_forced_phrase:
                self.store.srem(self.forced_phrases_db_key, phrase)
        return phrase
    
    def get_phrase(self, add_phrase_to_used: bool = True) -> str:
        available_phrases = self.get_available_phrases()
        if not available_phrases:
            self.store.delete(self.used_phrases_db_key)
            self.store.sadd(self.used_phrases_db_key,self.used_phrases_placeholder) # Restores used phrases db with placeholder
            available_phrases = self.phrases_db
            
        return random.choice(available_phrases)

    def get_available_phrases(self) -> list:
        return list(self.phrases_db - self.used_phrases_db)
    
    def forced_phrase_available(self) -> bool:
        """Checks if any forced phrase is available by checking if forced_phrases_db has more than 1 member (placeholder)

        Returns:
            bool: True if a forced phrase is availabe, False otherwise
        """
        return self.store.scard(self.forced_phrases_db_key) != 1

    def generate_raw_phrase(self) -> str:
        self.get_phrases_databases()
        use_forced_phrase: bool = self.forced_phrase_available()
        return self.get_forced_phrase() if use_forced_phrase else self.get_phrase()            

    def format_raw_phrase(self, phrase: str, days: int) -> str:
        return phrase.format(dias=days)
    
    def add_raw_phrase_to_used(self, phrase: str):
        self.store.sadd(self.used_phrases_db_key, phrase)


    def add_phrases_to_database(self, phrases: list):
        for phrase in phrases:
            self.store.sadd(self.phrases_db_key, phrase)
    
    def add_forced_phrases(self, phrases: list):
        for phrase in phrases:
            self.store.sadd(self.forced_phrases_db_key, phrase)

