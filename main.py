from src.utils.conversion import Conversion

conversion = Conversion()

message = "Bonjour le FLC lab"
dna = conversion.str_to_dna(message)
print("The secret message: " + message)
print("is encoded in the DNA sequence: " + dna)
decoded_message = conversion.dna_to_str(dna)
print("The decoded message is: " + decoded_message)


print("--------------------")
dna = "CCATCCCACAACCCAGCCCACACGCTCCCGTGAGAACGCGCGACCGATCTCAAGATATGGAGCGCTATCCCCCGGCCCCACGCCGGCTTGAACCTTCTCCCATGAGGTCGCACGTTCGTGAGTACCTGCGTAAGCTCAGCCATGCCATCTCACAGCCCCACCCCCTCAAGAACCAACAACCTATCCCACACCCTCCCTAGAGATCTAACATTCCATCTATTGGACACACGCCAGCGCCCCCGTGGGCTCTCGCGGCCGCTCATGCGTTCGAGCATACACCCCTTCTACCTCCAGCTCAGCCGTAAGGTCATACGCCCCCCCCAGCCTGCACCCCATCTCAAGAACGGCCGTCCCAACATTCTATCCATCAGCCAAGCGTACGCCAGATCGCACACCAGCGCTAGCGCCCCCGCACCCGTGCACACCAGCGCCGGCTAGACCCATCCCACATTCCAA"
print("The secret message: " + dna)
decoded_message = conversion.dna_to_str(dna)
print("The decoded message is: " + decoded_message)