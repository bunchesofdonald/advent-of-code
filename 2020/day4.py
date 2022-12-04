import re


hair_color_re = re.compile(r'^#[0-9a-f]{6}$')


def valid_passport(passport):
    requried_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    if len(requried_fields.intersection(set(passport.keys()))) != len(requried_fields):
        return False

    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        return False

    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        return False

    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        return False

    if passport['hgt'].endswith('cm'):
        height = int(passport['hgt'].replace('cm', ''))
        if height < 150 or height > 193:
            return False
    elif passport['hgt'].endswith('in'):
        height = int(passport['hgt'].replace('in', ''))
        if height < 59 or height > 76:
            return False
    else:
        return False

    if not hair_color_re.match(passport['hcl']):
        return False

    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if len(passport['pid']) != 9:
        return False

    return True


if __name__ == "__main__":
    with open('day4.txt') as infile:
        passports = []
        passport = {}
        for line in infile.readlines():
            if not(line.strip()):
                passports.append(passport)
                passport = {}

            pairs = line.strip().split(' ')
            for pair in pairs:
                if pair:
                    key, value = pair.split(':')
                    passport[key] = value

        passports.append(passport)

    requried_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    valid_passports = []
    valid_count = 0
    for passport in passports:
        if valid_passport(passport):
            valid_passports.append(passport)

    import pdb; pdb.set_trace()

    print(len(valid_passports))
