import hmac
import secrets

def generate_random_num_str(length=6):
    # Calculate the number of bytes needed for the desired length of decimal digits
    # Each byte can represent 2 decimal digits, so we divide by 2 and add 1 if the length is odd
    num_bytes = (length + 1) // 2
    
    # Generate a random byte string of the calculated length
    rand_bytes = secrets.token_bytes(num_bytes)
    
    # Convert the random bytes to an integer using 'big' byte order
    rand_num = int.from_bytes(rand_bytes, byteorder='big')
    
    # Convert the integer to a string and trim to the desired length
    return str(rand_num)[:length]


def constant_time_comparison_str(s1, s2):
    """
        Constant time comparison to prevent timing attack.
        a timing attack is a side-channel attack in which
        the attacker attempts to compromise a cryptosystem
        by analyzing the time taken to execute cryptographic algorithms

    """
    return hmac.compare_digest(bytes(s1), bytes(s2))
