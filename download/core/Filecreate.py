# coding = utf-8
import os, sys
import xlwt
from app.models import User
import app.models as models
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
download_url = os.path.join(BASE_DIR, 'file\\')
print(download_url)
import datetime
import xlwt

def BulidNewExcel(Column_list):
    db_dict = {
        'User': User,
    }
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
    #column_name_list = []
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet', cell_overwrite_ok=True)
    for i in range(len(Column_list)):
        ws.write(0, i, Column_list[i], style0)

    list_data = get_Userdata()
    if list_data == None:
        print('not data show')
    for i in range(len(list_data)):
        for j in range(len(list_data[0])):
            ws.write(i+1, j, list_data[i][j], style1)

    timestr = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    wb.save(download_url + 'New-' + timestr + '.xls')
    return 'New-' + timestr + '.xls'


def get_Userdata():
    list_data = []
    for user in User.query.all():
        list_tmp = []
        list_tmp = [user.id, user.name, user.password_hash, user.email]
        list_data.append(list_tmp)
    if list_data is not None:
        return list_data
    return None

if __name__ == '__main__':
    Column_list = ['id', 'name', 'password_hash', 'email']
    BulidNewExcel(Column_list)
