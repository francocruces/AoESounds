import os

FILES = {'01 yes.ogg': 'CQADAQADXQADH9CYR5aJYOj6W5uRAg', '02 no.ogg': 'CQADAQADXgADH9CYR8dGm30rabE-Ag', '03 food, please.ogg': 'CQADAQADXwADH9CYR58deMeZy5UrAg', '04 wood, please.ogg': 'CQADAQADYAADH9CYR5h6jsJMN7-jAg', '05 gold, please.ogg': 'CQADAQADYQADH9CYR8cfaf1Rr5j3Ag', '06 stone, please.ogg': 'CQADAQADYgADH9CYRyjzorQYMS6_Ag', '07 ahh.ogg': 'CQADAQADYwADH9CYRzsAASwpOj_L6gI', '08 all hail.ogg': 'CQADAQADZAADH9CYR9RCRffJJXoRAg', '09 oooh.ogg': 'CQADAQADZQADH9CYR0_F4n1mkhl7Ag', '10 back to age 1.ogg': 'CQADAQADZgADH9CYR8Bf51mB25PwAg', '11 herb laugh.ogg': 'CQADAQADZwADH9CYR00iucE1zCuBAg', '12 being rushed.ogg': 'CQADAQADaAADH9CYR4Qa7_iprRMAAQI', '13 blame your isp.ogg': 'CQADAQADaQADH9CYR_dVzaOSmyhHAg', '14 start the game.ogg': 'CQADAQADagADH9CYR7SfvTwkf4-WAg', "15 don't point that thing.ogg": 'CQADAQADawADH9CYRzYS2g3B3PK3Ag', '16 enemy sighted.ogg': 'CQADAQADbAADH9CYR2uszDoAAQHwjAI', '17 it is good.ogg': 'CQADAQADbQADH9CYR4ifGswtrM9GAg', '18 i need a monk.ogg': 'CQADAQADbgADH9CYRyFL4R8JcttxAg', '19 long time no siege.ogg': 'CQADAQADbwADH9CYR8Muk04T2A_jAg', '20 my granny.ogg': 'CQADAQADcAADH9CYRyMcwNKkiIJnAg', "21 nice town i'll take it.ogg": 'CQADAQADcQADH9CYR_oYawdiXkzsAg', '22 quit touchin.ogg': 'CQADAQADcgADH9CYR8f4DB-kNrNIAg', '23 raiding party.ogg': 'CQADAQADcwADH9CYR8W47d0jbANpAg', '24 dadgum.ogg': 'CQADAQADdAADH9CYR5yQZfCuE1rDAg', '25 smite me.ogg': 'CQADAQADdQADH9CYR9n2fNbA5O89Ag', '26 the wonder.ogg': 'CQADAQADdgADH9CYR4zUe2VnuP-aAg', '27 you play 2 hours.ogg': 'CQADAQADdwADH9CYRy7xxYU-1w5QAg', '28 you should see the other guy.ogg': 'CQADAQADeAADH9CYR5DRCRmcZWBHAg', '29 roggan.ogg': 'CQADAQADeQADH9CYR3aHarLO4R_cAg', '30 wololo.ogg': 'CQADAQADegADH9CYRyrC3MnPKKuMAg', '31 attack an enemy now.ogg': 'CQADAQADewADH9CYR8tHm6dVN5ClAg', '32 cease creating extra villagers.ogg': 'CQADAQADfAADH9CYR77N0pg8DrCQAg', '33 create extra villagers.ogg': 'CQADAQADfQADH9CYR5pNa8AvRoh_Ag', '34 build a navy.ogg': 'CQADAQADfgADH9CYRyhtabVGLlWXAg', '35 stop building a navy.ogg': 'CQADAQADfwADH9CYR5befHBXf_uYAg', '36 wait for my signal to attack.ogg': 'CQADAQADgAADH9CYR9qQ7h86WQIVAg', '37 build a wonder.ogg': 'CQADAQADgQADH9CYR5lr9js7mdSRAg', '38 give me your extra resources.ogg': 'CQADAQADggADH9CYR2Id8waFd3D7Ag', '39 ally.ogg': 'CQADAQADgwADH9CYR49GVdY3EP9mAg', '40 enemy.ogg': 'CQADAQADhAADH9CYR5fxcZ3ZKTmoAg', '41 neutral.ogg': 'CQADAQADhQADH9CYR7FHBh7b6oqTAg', '42 what age are you in.ogg': 'CQADAQADhgADH9CYR_T8wls4xcYrAg'}
FILE_ARRAY = ['CQADAQADXQADH9CYR5aJYOj6W5uRAg', 'CQADAQADXgADH9CYR8dGm30rabE-Ag', 'CQADAQADXwADH9CYR58deMeZy5UrAg', 'CQADAQADYAADH9CYR5h6jsJMN7-jAg', 'CQADAQADYQADH9CYR8cfaf1Rr5j3Ag', 'CQADAQADYgADH9CYRyjzorQYMS6_Ag', 'CQADAQADYwADH9CYRzsAASwpOj_L6gI', 'CQADAQADZAADH9CYR9RCRffJJXoRAg', 'CQADAQADZQADH9CYR0_F4n1mkhl7Ag', 'CQADAQADZgADH9CYR8Bf51mB25PwAg', 'CQADAQADZwADH9CYR00iucE1zCuBAg', 'CQADAQADaAADH9CYR4Qa7_iprRMAAQI', 'CQADAQADaQADH9CYR_dVzaOSmyhHAg', 'CQADAQADagADH9CYR7SfvTwkf4-WAg', 'CQADAQADawADH9CYRzYS2g3B3PK3Ag', 'CQADAQADbAADH9CYR2uszDoAAQHwjAI', 'CQADAQADbQADH9CYR4ifGswtrM9GAg', 'CQADAQADbgADH9CYRyFL4R8JcttxAg', 'CQADAQADbwADH9CYR8Muk04T2A_jAg', 'CQADAQADcAADH9CYRyMcwNKkiIJnAg', 'CQADAQADcQADH9CYR_oYawdiXkzsAg', 'CQADAQADcgADH9CYR8f4DB-kNrNIAg', 'CQADAQADcwADH9CYR8W47d0jbANpAg', 'CQADAQADdAADH9CYR5yQZfCuE1rDAg', 'CQADAQADdQADH9CYR9n2fNbA5O89Ag', 'CQADAQADdgADH9CYR4zUe2VnuP-aAg', 'CQADAQADdwADH9CYRy7xxYU-1w5QAg', 'CQADAQADeAADH9CYR5DRCRmcZWBHAg', 'CQADAQADeQADH9CYR3aHarLO4R_cAg', 'CQADAQADegADH9CYRyrC3MnPKKuMAg', 'CQADAQADewADH9CYR8tHm6dVN5ClAg', 'CQADAQADfAADH9CYR77N0pg8DrCQAg', 'CQADAQADfQADH9CYR5pNa8AvRoh_Ag', 'CQADAQADfgADH9CYRyhtabVGLlWXAg', 'CQADAQADfwADH9CYR5befHBXf_uYAg', 'CQADAQADgAADH9CYR9qQ7h86WQIVAg', 'CQADAQADgQADH9CYR5lr9js7mdSRAg', 'CQADAQADggADH9CYR2Id8waFd3D7Ag', 'CQADAQADgwADH9CYR49GVdY3EP9mAg', 'CQADAQADhAADH9CYR5fxcZ3ZKTmoAg', 'CQADAQADhQADH9CYR7FHBh7b6oqTAg', 'CQADAQADhgADH9CYR_T8wls4xcYrAg']
NAMES = ['01 yes', '02 no', '03 food, please', '04 wood, please', '05 gold, please', '06 stone, please', '07 ahh', '08 all hail', '09 oooh', '10 back to age 1', '11 herb laugh', '12 being rushed', '13 blame your isp', '14 start the game', "15 don't point that thing", '16 enemy sighted', '17 it is good', '18 i need a monk', '19 long time no siege', '20 my granny', "21 nice town i'll take it", '22 quit touchin', '23 raiding party', '24 dadgum', '25 smite me', '26 the wonder', '27 you play 2 hours', '28 you should see the other guy', '29 roggan', '30 wololo', '31 attack an enemy now', '32 cease creating extra villagers', '33 create extra villagers', '34 build a navy', '35 stop building a navy', '36 wait for my signal to attack', '37 build a wonder', '38 give me your extra resources', '39 ally', '40 enemy', '41 neutral', '42 what age are you in']

BASE_PATH = os.getcwd()+"\\Update\\sounds"

MP3FILES = {'01 yes.ogg': 'CQADAQADjAADH9CYR1bGukP0MnshAg', '02 no.ogg': 'CQADAQADjQADH9CYR9LhGYqAp6Q4Ag', '03 food, please.ogg': 'CQADAQADjgADH9CYR2-enVBKTXTsAg', '04 wood, please.ogg': 'CQADAQADjwADH9CYR1L0Jznq6tyeAg', '05 gold, please.ogg': 'CQADAQADkAADH9CYR2eAsEWxJ66kAg', '06 stone, please.ogg': 'CQADAQADkQADH9CYR93FIL8r17YiAg', '07 ahh.ogg': 'CQADAQADkgADH9CYR8d8JRpd2YJCAg', '08 all hail.ogg': 'CQADAQADkwADH9CYRy7PrgZs2la7Ag', '09 oooh.ogg': 'CQADAQADlAADH9CYR3unbIfQh4g7Ag', '10 back to age 1.ogg': 'CQADAQADlQADH9CYR6Vs6hH8E9jaAg', '11 herb laugh.ogg': 'CQADAQADlgADH9CYR8gYcURXitz0Ag', '12 being rushed.ogg': 'CQADAQADlwADH9CYR7kpwdjBnIoqAg', '13 blame your isp.ogg': 'CQADAQADmAADH9CYR0khPrV2buC4Ag', '14 start the game.ogg': 'CQADAQADmQADH9CYRx3jFVM5zP_oAg', "15 don't point that thing.ogg": 'CQADAQADmgADH9CYR7RAaFvpIvRdAg', '16 enemy sighted.ogg': 'CQADAQADmwADH9CYR0UYt4-X-DTCAg', '17 it is good.ogg': 'CQADAQADnAADH9CYR4GuTLBvcQLnAg', '18 i need a monk.ogg': 'CQADAQADnQADH9CYRy9xNPvVoG44Ag', '19 long time no siege.ogg': 'CQADAQADngADH9CYR-Dbn32puwd3Ag', '20 my granny.ogg': 'CQADAQADnwADH9CYR3WAKnT6OqR4Ag', "21 nice town i'll take it.ogg": 'CQADAQADoAADH9CYR4WoeZjZdEI0Ag', '22 quit touchin.ogg': 'CQADAQADoQADH9CYR2eMyjF6OWA9Ag', '23 raiding party.ogg': 'CQADAQADogADH9CYR9q5Er3E--G4Ag', '24 dadgum.ogg': 'CQADAQADowADH9CYR6vqqQJTCMjqAg', '25 smite me.ogg': 'CQADAQADpAADH9CYR8R5QSgRsD6XAg', '26 the wonder.ogg': 'CQADAQADpQADH9CYR5LQl1NEpBypAg', '27 you play 2 hours.ogg': 'CQADAQADpgADH9CYR7jIIJnznc2jAg', '28 you should see the other guy.ogg': 'CQADAQADpwADH9CYR4U_7r3c-ROuAg', '29 roggan.ogg': 'CQADAQADqAADH9CYRx8-IsoVITrSAg', '30 wololo.ogg': 'CQADAQADqQADH9CYRzFO2GV4MqyJAg', '31 attack an enemy now.ogg': 'CQADAQADqgADH9CYR8XXjX0GXJTgAg', '32 cease creating extra villagers.ogg': 'CQADAQADqwADH9CYRyMMHAyrygoqAg', '33 create extra villagers.ogg': 'CQADAQADrAADH9CYR7nZfJqamh7NAg', '34 build a navy.ogg': 'CQADAQADrQADH9CYR7JhdyJTpCbLAg', '35 stop building a navy.ogg': 'CQADAQADrgADH9CYR0ehWy5Zfk5QAg', '36 wait for my signal to attack.ogg': 'CQADAQADrwADH9CYR6BtohnBLD-gAg', '37 build a wonder.ogg': 'CQADAQADsAADH9CYRxc3iZwUgI1zAg', '38 give me your extra resources.ogg': 'CQADAQADsQADH9CYRy1Aaaiocn3mAg', '39 ally.ogg': 'CQADAQADsgADH9CYR1pzCi4hGppQAg', '40 enemy.ogg': 'CQADAQADswADH9CYR_QdQJN2pjliAg', '41 neutral.ogg': 'CQADAQADtAADH9CYR5DrDis6CXl8Ag', '42 what age are you in.ogg': 'CQADAQADtQADH9CYR82lbsDBDsQKAg'}
MP3NAMES = NAMES
MP3FILE_ARRAY = ['CQADAQADjAADH9CYR1bGukP0MnshAg', 'CQADAQADjQADH9CYR9LhGYqAp6Q4Ag', 'CQADAQADjgADH9CYR2-enVBKTXTsAg', 'CQADAQADjwADH9CYR1L0Jznq6tyeAg', 'CQADAQADkAADH9CYR2eAsEWxJ66kAg', 'CQADAQADkQADH9CYR93FIL8r17YiAg', 'CQADAQADkgADH9CYR8d8JRpd2YJCAg', 'CQADAQADkwADH9CYRy7PrgZs2la7Ag', 'CQADAQADlAADH9CYR3unbIfQh4g7Ag', 'CQADAQADlQADH9CYR6Vs6hH8E9jaAg', 'CQADAQADlgADH9CYR8gYcURXitz0Ag', 'CQADAQADlwADH9CYR7kpwdjBnIoqAg', 'CQADAQADmAADH9CYR0khPrV2buC4Ag', 'CQADAQADmQADH9CYRx3jFVM5zP_oAg', 'CQADAQADmgADH9CYR7RAaFvpIvRdAg', 'CQADAQADmwADH9CYR0UYt4-X-DTCAg', 'CQADAQADnAADH9CYR4GuTLBvcQLnAg', 'CQADAQADnQADH9CYRy9xNPvVoG44Ag', 'CQADAQADngADH9CYR-Dbn32puwd3Ag', 'CQADAQADnwADH9CYR3WAKnT6OqR4Ag', 'CQADAQADoAADH9CYR4WoeZjZdEI0Ag', 'CQADAQADoQADH9CYR2eMyjF6OWA9Ag', 'CQADAQADogADH9CYR9q5Er3E--G4Ag', 'CQADAQADowADH9CYR6vqqQJTCMjqAg', 'CQADAQADpAADH9CYR8R5QSgRsD6XAg', 'CQADAQADpQADH9CYR5LQl1NEpBypAg', 'CQADAQADpgADH9CYR7jIIJnznc2jAg', 'CQADAQADpwADH9CYR4U_7r3c-ROuAg', 'CQADAQADqAADH9CYRx8-IsoVITrSAg', 'CQADAQADqQADH9CYRzFO2GV4MqyJAg', 'CQADAQADqgADH9CYR8XXjX0GXJTgAg', 'CQADAQADqwADH9CYRyMMHAyrygoqAg', 'CQADAQADrAADH9CYR7nZfJqamh7NAg', 'CQADAQADrQADH9CYR7JhdyJTpCbLAg', 'CQADAQADrgADH9CYR0ehWy5Zfk5QAg', 'CQADAQADrwADH9CYR6BtohnBLD-gAg', 'CQADAQADsAADH9CYRxc3iZwUgI1zAg', 'CQADAQADsQADH9CYRy1Aaaiocn3mAg', 'CQADAQADsgADH9CYR1pzCi4hGppQAg', 'CQADAQADswADH9CYR_QdQJN2pjliAg', 'CQADAQADtAADH9CYR5DrDis6CXl8Ag', 'CQADAQADtQADH9CYR82lbsDBDsQKAg']
