#به نام خدا
import psutil


class cpu_info():


    def cpu_times():
        cpu_time_percent= psutil.cpu_times_percent(interval=None, percpu=False)
        return cpu_time_percent

    def cpu_counter():
        cpu_count=psutil.cpu_count()
        return cpu_count

    def cpu_stats_boot():
       state = psutil.cpu_stats()
       
    

    

