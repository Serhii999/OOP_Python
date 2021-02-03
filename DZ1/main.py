class Element(object):
    def agg_state(self, t):
        if t >= self.t_ispareniya:
            return "Sostoyanie ispareniya"
        elif self.t_ispareniya > t and self.t_plavleniya < t:
            return "Sostoyanie plavleniya"
        else:
            return "Tverdoe sostoyanie"

    def perevod_v_far(self, t):
        if t >= self.t_ispareniya:
            return "Temperatura v Zelsiyah - {} Temperatura v farengeitah - {}" \
                   "Sostoyanie ispareniya".format(t, ((t * 9 / 5) + 32))
        elif self.t_ispareniya > t and self.t_plavleniya < t:
            return "Temperatura v Zelsiyah - {} Temperatura v farengeitah - {}" \
                   "Sostoyanie plavleniya".format(t, ((t * 9 / 5) + 32))
        else:
            return "Temperatura v Zelsiyah - {} Temperatura v farengeitah - {}" \
                   "  Tverdoe sostoyanie".format(t, ((t * 9 / 5) + 32))

    def perevod_v_kel(self, t):
        if t >= self.t_ispareniya:
            return "Temperatura v Zelsiyah - {} Temperatura v farengeitah - {}" \
                   "Sostoyanie ispareniya".format(t, (t + 273.15))
        elif self.t_ispareniya > t and self.t_plavleniya < t:
            return "Temperatura v Zelsiyah - {} Temperatura v farengeitah - {}" \
                   "Sostoyanie plavleniya".format(t, (t + 273.15))
        else:
            return "Temperatura v Zelsiyah - {} Temperatura v farengeitah - {}" \
                   "  Tverdoe sostoyanie".format(t, (t + 273.15))

    def perevod_iz_far_v_kel(self, t):
        if t >= self.t_f_ispareniya:
            return "Temperatura v Farengeitah - {} Temperatura v Kelvinah - {}" \
                   " Sostoyanie ispareniya".format(t, ((t - 32) * 5 / 9 + 273.15))
        elif self.t_f_ispareniya > t and self.t_f_plavleniya < t:
            return "Temperatura v Farengeitah - {} Temperatura v Kelvinah - {}" \
                   " Sostoyanie plavleniya".format(t, ((t - 32) * 5 / 9 + 273.15))
        else:
            return "Temperatura v Farengeitah - {} Temperatura v Kelvinah - {}" \
                   " Tverdoe sostoyanie".format(t, ((t - 32) * 5 / 9 + 273.15))

    def perevod_iz_kel_v_far(self, t):
        if t >= self.t_k_ispareniya:
            return "Temperatura v Kelvinah - {} Temperatura v Farengeitah - {}" \
                   " Sostoyanie ispareniya".format(t, (1.8 * (t - 273) + 32))
        elif self.t_k_ispareniya > t and self.t_k_plavleniya < t:
            return "Temperatura v Kelvinah - {} Temperatura v Farengeitah - {}" \
                   " Sostoyanie plavleniya".format(t, (1.8 * (t - 273) + 32))
        else:
            return "Temperatura v Kelvinah - {} Temperatura v Farengeitah - {}" \
                   " Tverdoe sostoyanie".format(t, (1.8 * (t - 273) + 32))

    def perevod_iz_far_v_cel(self, t):
        if t >= self.t_f_ispareniya:
            return "Temperatura v Farengeitah - {} Temperatura v Celsiyah - {}" \
                   " Sostoyanie ispareniya".format(t, ((t - 32) * 5 / 9))
        elif self.t_f_ispareniya > t and self.t_f_plavleniya < t:
            return "Temperatura v Farengeitah - {} Temperatura v Celsiyah - {}" \
                   " Sostoyanie plavleniya".format(t, ((t - 32) * 5 / 9))
        else:
            return "Temperatura v Farengeitah - {} Temperatura v Celsiyah - {}" \
                   " Tverdoe sostoyanie".format(t, ((t - 32) * 5 / 9))

    def perevod_iz_kel_v_cel(self, t):
        if t >= self.t_k_ispareniya:
            return "Temperatura v Kelvinah - {} Temperatura v Celsiyah - {}" \
                   " Sostoyanie ispareniya".format(t, (t - 273.15))
        elif self.t_k_ispareniya > t and self.t_k_plavleniya < t:
            return "Temperatura v Kelvinah - {} Temperatura v Celsiyah - {}" \
                   " Sostoyanie plavleniya".format(t, (t - 273.15))
        else:
            return "Temperatura v Kelvinah - {} Temperatura v Celsiyah - {}" \
                   " Tverdoe sostoyanie".format(t, (t - 273.15))


class Iron (Element):
    t_zamerzaniya =0
    t_plavleniya = 0
    t_ispareniya = 0

    t_f_zamerzaniya =0
    t_f_plavleniya = 0
    t_f_ispareniya = 0

    t_k_zamerzaniya =0
    t_k_ispareniya =0
    t_k_plavleniya = 0


    


iron = Iron()

iron.t_ispareniya = 2862
iron.t_plavleniya = 1538
iron.t_zamerzaniya =1538

iron.t_f_ispareniya = (iron.t_ispareniya*9/5)+32
iron.t_f_plavleniya = (iron.t_plavleniya*9/5)+32
iron.t_f_zamerzaniya = (iron.t_zamerzaniya*9/5)+32

iron.t_k_ispareniya= (iron.t_ispareniya+273.15)
iron.t_k_plavleniya= (iron.t_k_plavleniya+273.15)
iron.t_k_zamerzaniya= (iron.t_k_zamerzaniya+273.15)

print(iron.agg_state(200))
print(iron.perevod_v_far(100))
print(iron.perevod_v_kel(250))
print(iron.perevod_iz_far_v_kel(5184))
print(iron.perevod_iz_kel_v_far(500))
print(iron.perevod_iz_far_v_cel(1000))
print(iron.perevod_iz_kel_v_cel(200))
