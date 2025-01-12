m_s = int(input('m_s: '))
m_u = int(input('m_u: '))

while True:
    if m_s > 21:
        result = 'Win !'
        break
    elif m_u > m_s:
        result = 'Win !!'
        break
    elif m_s > m_u:
        result = 'Lose !'
        break
    elif m_s == m_u:
        result = 'Draw !'
        break
print(result)