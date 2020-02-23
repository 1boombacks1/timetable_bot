from datetime import time
from datetime import datetime
from datetime import timedelta
from datetime import date
import os

Token = "900761267:AAFBoA-PyT7TE6OyOWsllqI5zaLSQju7uMw"
FMonday = [{"time": '10:40',"lesson": "Физра, кроме 3,5,13 н", "cabinet": "ФОК"},
           {"time": '13:10',"lesson": "Физра, кроме 3,5,13 н", "cabinet": "ФОК"},
           {"time": '14:50',"lesson": "ПР Дискретка, кроме 3,5,13 н", "cabinet": "399б"},
           {"time": '16:20',"lesson": "ПР Дискретка, кроме 3,5,13 н", "cabinet": "399б"}]

SMonday = [{"time": '09:00',"lesson": "ЛР Физика 4, 8, 12, 16 н", "cabinet": "В-411"},
           {"time": '10:40',"lesson": "ЛР Физика 4, 8, 12, 16 н", "cabinet": "В-411"},
           {"time": '13:10',"lesson": "ПР Физика", "cabinet": "В-401"},
           {"time": '14:50',"lesson": "ПР Физика", "cabinet": "В-401"}]

FTuesday = [{"time": '09:00',"lesson": "ЛЕК Тех Прога", "cabinet": "265"},
            {"time": '10:40',"lesson": "Физра, кроме 13, 15 н", "cabinet": "ФОК"},
            {"time": '13:10',"lesson": "ПР Лин Ал, кроме 13 н", "cabinet": "359"},
            {"time": '14:50',"lesson": "ПР Лин Ал, кроме 13 н", "cabinet": "359"}]

STuesday = [{"time": '09:00',"lesson": "ПР Тех Прога", "cabinet": "251а"},
            {"time": '10:40',"lesson": "ПР Тех Прога", "cabinet": "251а"},
            {"time": '13:10',"lesson": "ПР Архетиктура Инф Сис 4,8,12,16 н", "cabinet": "367"},
            {"time": '14:50',"lesson": "ПР Архетиктура Инф Сис 4,8,12,16 н", "cabinet": "367"}]

FWednesday= [{"time": '09:00',"lesson": "ЛЕК Архетиктура Инф Сис", "cabinet": "330"},
            {"time": '10:40',"lesson": "ЛЕК Архетиктура Инф Сис", "cabinet": "330"}]

SWednesday= [{"time": '09:00',"lesson": "Физра", "cabinet": "ФОК"},
            {"time": '10:40',"lesson": "Физра", "cabinet": "ФОК"}]

FThursday = [{"time": '09:00',"lesson": "ПР Экономика", "cabinet": "409"},
            {"time": '10:40',"lesson": "ПР Инглиш", "cabinet": "КАФ"},
            {"time": '13:10',"lesson": "ЛЕК Экономика", "cabinet": "350"},
            {"time": '14:50',"lesson": "ПР Дискретка", "cabinet": "399б"}]

SThursday = [{"time": '10:40',"lesson": "ПР Инглиш", "cabinet": "КАФ"},
            {"time": '13:10',"lesson": "ЛЕК Правовединение 4 н", "cabinet": "348"},
            {"time": '14:50',"lesson": "ПР Дискретка", "cabinet": "399б"}]

FFriday = [{"time": '09:00',"lesson": "ЛЕК Мат Анал)", "cabinet": "347"},
            {"time": '10:40',"lesson": "ЛЕК Лин Ал", "cabinet": "347"},
            {"time": '13:10',"lesson": "ЛЕК Дискретка", "cabinet": "379"},
            {"time": '14:50',"lesson": "ПР Мат Анал)", "cabinet": "266б"}]

SFriday = [{"time": '09:00',"lesson": "ЛЕК Мат Анал), кроме 12 н", "cabinet": "347"},
            {"time": '10:40',"lesson": "ЛЕК Лин Ал кроме 12 н", "cabinet": "347"},
            {"time": '13:10',"lesson": "ПР Правовединие 2,6,10,14 н", "cabinet": "379"},
            {"time": '14:50',"lesson": "ПР Мат Анал) кроме 12 н", "cabinet": "266б"}]

FSaturday = [{"time": '09:00',"lesson": "ЛЕК Физика 3,7,9,15 н", "cabinet": "A-10"},
            {"time": '10:40',"lesson": "ЛЕК Физика 3,7,9,15 н", "cabinet": "A-10"},
            {"time": '13:10',"lesson": "ПР Лин Алло 5,9 н", "cabinet": "369"},
            {"time": '14:50',"lesson": "ЛЕК Мат Анал 9н или ПР Мат Анал 15н", "cabinet": "347 или 266б"},
            {"time": '16:30',"lesson": "ПР Лин Алло 9 н", "cabinet": "347"}]

SSaturday = [{"time": '13:10',"lesson": "ПР Дискретка 2,4,12 н", "cabinet": "369"}]

FTimetable = {1: FMonday, 2: FTuesday, 3: FWednesday, 4:FThursday, 5: FFriday, 6: FSaturday}
STimetable = {1: SMonday, 2: STuesday, 3: SWednesday, 4:SThursday, 5: SFriday, 6: SSaturday}
