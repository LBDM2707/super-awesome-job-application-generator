class Experience:
    def __init__(self, data={}):
        self.name = data.get("name", "New experience")
        self.description = data.get("description", "")
        self.job_title = data.get("job_title", "")
        self.job_startdate = data.get("job_startdate", "")
        self.job_enddate = data.get("company_name", "")
        self.company_name = data.get("company_name", "")
        self.company_location = data.get("company_location", "")

    def update_detail(self, data={}):
        for key in data.keys():
            if key in self.__dict__:
                self.__dict__[key] = data[key]
