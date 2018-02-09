class Patient:

    def __init__(self, name):

      """

      :param name:
      """
      self.name = name
    def discharge(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """
        print(self.name)
        print(type(self))
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class EmergencyPatient(Patient):

    def __init__(self, name):
        """

        :param name:
        """
        Patient.__init__(self, name)
        self.name=name
    def discharge(self):
        """

        :return:
        """

        return (self.name,type(self))


class HospitalizedPatient(Patient):

    def __init__(self, name):
        """

        :param name:
        """
        Patient.__init__(self, name)
        self.cost = 1000
    def discharge(self):
        """

        :return:
        """
        return (self.name, type(self))



class Hospital:
    def __init__(self):
        """

        :param patients:
        :param cost:
        """

    def admit(self,patients):
        self.patients = patients
        self.patients.append(patients)
        for patient in self:
            patients = type(self)
        return patients

    def discharge_all(self):
        return self.discharge()
    def get_total_cost(self):
        cost = 0 # expected cost initialized with the cost of visiting the current node
        for patient in self:
            if type(patient) == EmergencyPatient:
                cost += 1000
            if type(patient) == HospitalizedPatient:
                    cost += 2000

        return cost





myhospital = Hospital()
Patient1 = HospitalizedPatient("Judy")
Patient2 = HospitalizedPatient("Kate")
Patient3 = EmergencyPatient("John")
Patient4 = EmergencyPatient("Rachel")
Patient5 = EmergencyPatient("Julie")
patientsum = [Patient1,Patient2,Patient3,Patient4,Patient5]

myhospital.admit(Patient1)

