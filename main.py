import argparse

from constants import REPORTS

def main():
    parser = argparse.ArgumentParser(description='Анализ журнала логирования')
    parser.add_argument('log_files', type=str, nargs='+',
                         help='пути к логам, файлов может быть несколько')
    parser.add_argument('--report', type=str, required=True,
                         help='название отчета который нужно сформировать')
    args = parser.parse_args()
    
    # validation
    for report_name, report_init, report_process, report_result in REPORTS:
        if args.report == report_name:
            break
    else:
        print('Неизвестный отчет', args.report)
        return
    
    # process
    data = report_init()
    for log_file in args.log_files:
        with open(log_file) as in_file:
            while in_str:=in_file.readline():
                report_process(data, in_str)

    # result
    result = report_result(data)
    print(result)


if __name__ == '__main__':
    main()
