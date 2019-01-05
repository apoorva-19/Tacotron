'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run
through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
'''
from text import cmudict

_pad        = '_'
_eos        = '~'
# Character set for English
#_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\'(),-.:;? '
# Character set for Devnagri
_characters = 'ँंःऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऺऻ़ऽािीुूृॄॅॆेैॉॊोौ्ॎॏॐ॒॑॓॔ॕॖॗक़ख़ग़ज़ड़ढ़फ़य़ॠॡॢॣ '

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters): FOR ENGLISH ENUNCIATION
# Hence not required here
#_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Export all symbols: FOR ENGLISH
# symbols = [_pad, _eos] + list(_characters) + _arpabet

# For Devangri
symbols = [_pad, _eos] + list(_characters)
