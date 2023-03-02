#orange HRM locators

class Orange_Locator:
   # Locators for Login
    username_locator = 'username'
    password_locator = 'password'
    submitButton_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
     #locator for pim
    PIM_CNT = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
    # locators for employee add
    Add_employee= '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a'
    first_input='firstName'
    second_input='middleName'
    last_input='lastName'
    save_details='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    #locators for employee add(existing)
    emplyoee_list='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]'
    edit_employee='/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[6]/div/div[9]/div/button[2]'
    name ='middleName'
    save='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
    delete='/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]/i'
    pop_up='/html/body/div/div[3]/div/div/div/div[3]/button[2]'