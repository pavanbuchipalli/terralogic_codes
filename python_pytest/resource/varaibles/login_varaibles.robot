*** Variables ***
${url_hros}     https://terralogic.paxanimi.ai/login
${click_terralogic}     xpath://button[@type="button"]
${email_hros}       //input[@type="email"]
${next_email_hros}      xpath://span[text()='Next']//parent::button
${passwords_hros}        //input[@type="password"]
${next_password_hros}    xpath://span[text()='Next']/..
${dashboard}        (//span[@class="ant-menu-title-content"]/a)[3]


${manager_xapath}       (//span[@class="ant-menu-title-content"]/a)[3]


${manager_name}     (//div[@id="625764aececaa30012bed3ee"]/div)[1]/div/div[2]


${employee_name}        (//div[@id="6433d492f27e0315d9a73106"]/div)[1]/div/div[2]

${timesheet_xpath}      (//span[@class="ant-menu-title-content"]/a)[2]

${data_filled_xpath}        //img[contains(@src, '/static/timesheetCheck.bf9bab90.svg')]

${emilid_hros}      pavan.buchipalli@terralogic.com
${password_hros}        Yugesh@05