from django.core.exceptions import ValidationError


def rfc_validator(value):
    value = value.upper()
    if len(value) != 12 and len(value) != 13:
        raise ValidationError('Se requieren 12 o 13 caracteres')
    if value[0].isdigit() or value[1].isdigit() or value[2].isdigit() or value[3].isdigit():
        raise ValidationError('Del primer al cuarto caracter debe ser una letra')
    if not value[4].isdigit() or not value[5].isdigit() or not value[6].isdigit() or not value[7].isdigit() or \
            not value[8].isdigit() or not value[9].isdigit():
        raise ValidationError('Del quinto al décimo caracter debe ser un número ')
    return value
