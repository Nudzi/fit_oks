from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.welcome_page_for_new_user import WelcomePafeForNewUser
from pages.welcome_page import WelcomePage
from pages.update_profile_page import UpdateProfilePage
from pages.profile_updated_page import ProfileUpdatedPage

def test_update_contact_info(driver):
    home_page = HomePage(driver)
    welcome_page = WelcomePage(driver)
    home_page.go_to()
    assert home_page.get_page_tile() == "ParaBank | Welcome | Online Banking"
    assert home_page.is_forgot_to_login_info_visible() == True
    assert home_page.is_register_visible() == True

    # clean data
    home_page.clean_data()
    
    home_page.go_to_register_page()
    register_page = RegisterPage(driver)

    assert register_page.header_message() == 'Signing up is easy!'

    username = "username-test"
    password = "password-test"
    firstName = "Test Name"
    lastName = "Test LastName"
    address = "Test Address"
    city = "Test City"
    state = "Test State"
    zipCode = "Test ZipCode"
    phoneNumber = "Test Phone Number"
    ssn = "Test SSN"
    register_page.register(firstName, lastName, address, city, state, zipCode, phoneNumber, ssn, username, password, password)
    
    welcome_page_for_new_user = WelcomePafeForNewUser(driver)
    assert welcome_page_for_new_user.header_message() == f"Welcome {username}"
    assert welcome_page_for_new_user.info_message() == "Your account was created successfully. You are now logged in."

    welcome_page = WelcomePage(driver)

    assert welcome_page.is_logout_link_visible() == True
    assert welcome_page.is_account_name_visible() == f"Welcome {firstName} {lastName}"
    assert welcome_page.is_login_link_invisible() == True
    assert welcome_page.is_register_invisible() == True

    # go to page to update info
    welcome_page.go_to_update_contact_info()

    # check old values
    update_profile_page = UpdateProfilePage(driver)

    firstNameId = 'customer.firstName'
    assert update_profile_page.is_input_field_available(firstNameId) == True
    assert update_profile_page.get_value_from_inputs(firstNameId) == firstName
    lastNameId = "customer.lastName"
    assert update_profile_page.get_value_from_inputs(lastNameId) == lastName
    streetId = "customer.address.street"
    assert update_profile_page.get_value_from_inputs(streetId) == address
    cityId = "customer.address.city"
    assert update_profile_page.get_value_from_inputs(cityId) == city
    stateId = "customer.address.state"
    assert update_profile_page.get_value_from_inputs(stateId) == state
    zipCodeId = "customer.address.zipCode"
    assert update_profile_page.get_value_from_inputs(zipCodeId) == zipCode
    phoneNumberId = "customer.phoneNumber"
    assert update_profile_page.get_value_from_inputs(phoneNumberId) == phoneNumber

    #update profile
    newfirstName = "Test Name2"
    newlastName = "Test LastName2"
    newaddress = "Test Address2"
    newcity = "Test City2"
    newstate = "Test State2"
    newzipCode = "Test ZipCode2"
    newphoneNumber = "Test Phone Number2"

    assert update_profile_page.header_message() == "Update Profile"
    update_profile_page.update_profile(newfirstName, newlastName, newaddress, newcity, newstate, newzipCode, newphoneNumber)

    profile_updated_page = ProfileUpdatedPage(driver)
    assert profile_updated_page.header_message() == "Profile Updated"

    #check profile
    welcome_page.go_to_update_contact_info()

    assert update_profile_page.get_value_from_inputs(firstNameId) == newfirstName
    assert update_profile_page.get_value_from_inputs(lastNameId) == newlastName
    assert update_profile_page.get_value_from_inputs(streetId) == newaddress
    assert update_profile_page.get_value_from_inputs(cityId) == newcity
    assert update_profile_page.get_value_from_inputs(stateId) == newstate
    assert update_profile_page.get_value_from_inputs(zipCodeId) == newzipCode
    assert update_profile_page.get_value_from_inputs(phoneNumberId) == newphoneNumber
