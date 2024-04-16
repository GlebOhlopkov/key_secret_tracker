# import re
#
# from rest_framework import serializers
#
#
# class KeySymbolsValidator:
#     """
#     Validator for checking symbols in secret KEY
#     Available symbols:
#     all letters - from a to z (A - Z),
#     all numbers - from 1 to 9,
#     symbols '-' and '_'.
#     """
#     def __call__(self, value):
#         key = value.get('key')
#         reg = re.compile('^[a-zA-Z0-9\-\s\_\s\=\s\*\s\+\s\/\s\<\s\>]+$')
#         if not bool(reg.match(key)):
#             raise serializers.ValidationError(
#                 'Sorry, your secret key must have only numbers and letters (and some symbols: "-", "_")')
