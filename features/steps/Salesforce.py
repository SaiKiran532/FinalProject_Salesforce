import os

from behave import given, when, then
from selenium import webdriver

from PageObjects.Converts import Converts
from PageObjects.CreateAccount import CreateAccount
from PageObjects.CreateContact import CreateContact
from PageObjects.CreateEvent import CreateEvent
from PageObjects.CreateLead import CreateLead
from PageObjects.CreateOpportunity import CreateOpportunity
from PageObjects.LoginPage import LoginPage
from PageObjects.RemoveAccount import RemoveAccount
from utilities.readProperties import ReadConfig
import time


class Testcase001:
    username = ReadConfig.get_user_name()
    password = ReadConfig.get_password()

    def __init__(self):
        self.logger = None
        self.driver = None

    @given('Open Salesforce page and verify title')
    def open_salesforce_page_and_verify_title(context):
        context.logger.info("Verifying homepage title")
        context.driver.get(ReadConfig.get_Application_url())
        time.sleep(2)
        actual_title = context.driver.title
        if actual_title != "Login | Salesforce":
            context.logger.error("Homepage title test failed")
            assert False, "Homepage title is incorrect"

    @when(u'Login with username and password')
    def login_to_page(context):
        context.lp = LoginPage(context.driver)
        context.lp.set_user_name(Testcase001.username)
        context.lp.set_password(Testcase001.password)
        context.lp.click_login()
        context.logger.info("Logged in successfully")

    @when(u'Create a lead with details: "{salutation}", "{first_name}", "{last_name}", "{company}"')
    def create_lead(context, salutation, first_name, last_name, company):
        context.cl = CreateLead(context.driver)
        context.cl.create_lead(salutation, first_name, last_name, company)
        context.logger.info(f"Lead created: {first_name} {last_name}, {company}")

    @then(u'Verify lead has created')
    def verify_lead_has_created(context):
        context.cl = CreateLead(context.driver)
        text = context.cl.verify_lead_has_created()
        if text == "Mr. Robert Twin" or "Mr. Nova Klan":
            assert True
            context.logger.info("********** Lead has successfully created and verified **********")
        else:
            context.logger.error("********** Failed in verifying lead **********")
            assert False

    @when(u'Create a account with details: "{account_name}"')
    def create_account(context, account_name):
        context.cl = CreateAccount(context.driver)
        context.cl.create_account(account_name)
        context.logger.info(f"Account created: {account_name}")

    @then(u'Verify account: "{account_name}" has created')
    def verify_account_has_created(context, account_name):
        context.cl = CreateAccount(context.driver)
        text = context.cl.verify_account_has_created(account_name)
        if text == "Acme":
            assert True
            context.logger.info("********** Account has successfully created and verified **********")
        else:
            context.logger.error("********** Failed in verifying Account **********")
            assert False

    @when(u'Convert the lead to account by creating new account from lead to account convert page')
    def convert_lead(context):
        context.rl = Converts(context.driver)
        context.rl.convert_lead()
        context.logger.info(f"Lead Converted")

    @then(u'Verify lead has converted successfully')
    def convert_lead(context):
        context.rl = Converts(context.driver)
        text = context.rl.verify_lead_has_converted()
        if text == "Your lead has been converted":
            assert True
            context.logger.info("********** Lead has successfully created and verified **********")
        else:
            context.logger.error("********** Failed in verifying lead **********")
            assert False
        context.rl.go_to_leads_page()


    @when(u'Convert the lead to account and use existing account: "{account_name}"')
    def convert_lead_using_existing_account(context, account_name):
        context.rl = Converts(context.driver)
        context.rl.convert_lead_using_existing_account(account_name)
        context.logger.info(f"Lead Converted")

    @then(u'Remove or Delete the account')
    def remove_lead(context):
        context.rl = RemoveAccount(context.driver)
        context.rl.remove_account()
        context.logger.info(f"Removed account")

    @when(u'Create a contact with details: "{salutation}", "{first_name}", "{last_name}" and attach "{account_name}"')
    def create_contact_and_attach_account(context,salutation, first_name, last_name,account_name):
        context.cc = CreateContact(context.driver)
        context.cc.create_contact(salutation, first_name, last_name,account_name)
        context.logger.info(f"Contact created and attached account")

    @then(u'Verify contact: "{contact_name}" has saved successfully with "{account_name}"')
    def verify_contact_has_saved(context,contact_name,account_name):
        context.rl = CreateContact(context.driver)
        text = context.rl.verify_contact_has_saved(contact_name,account_name)
        if text == "Zoya B":
            assert True
            context.logger.info("********** Contact has successfully created and verified **********")
        else:
            context.logger.error("********** Failed in verifying Contact **********")
            assert False

    @when(u'Create a opportunity with details: "{opportunity_name}", "{close_date}", "{stage}", "{forecast_category}" and attach "{account_name}"')
    def create_opportunity_and_attach_account(context, opportunity_name,close_date,stage,forecast_category,account_name):
        context.co = CreateOpportunity(context.driver)
        context.co.create_opportunity(opportunity_name,close_date,stage,forecast_category,account_name)
        context.logger.info(f"Opportunity created and attached account")

    @then(u'Verify opportunity: "{opportunity_name}" has saved successfully with "{account_name}"')
    def verify_opportunity_has_saved(context, opportunity_name, account_name):
        context.co = CreateOpportunity(context.driver)
        text = context.co.verify_opportunity_has_saved(opportunity_name, account_name)
        if text == "Zaya Opp":
            assert True
            context.logger.info("********** Opportunity has successfully created and verified **********")
        else:
            context.logger.error("********** Failed in verifying Opportunity **********")
            assert False

    @when(u'Create new event with subject: "{event_name}"')
    def create_lead(context,event_name):
        context.ce = CreateEvent(context.driver)
        context.ce.create_event(event_name)
        context.logger.info(f"Event created: {event_name}")

    @then(u'Verify event: "{event_name}" has added')
    def create_lead(context, event_name):
        context.ce = CreateEvent(context.driver)
        text = context.ce.verify_event_has_added(event_name)
        if text == "Call":
            assert True
            context.logger.info("********** Event has successfully added and verified **********")
        else:
            context.logger.error("********** Failed in verifying Event **********")
            assert False

    @then(u'click on logout')
    def clickOnLogout(context):
        context.lp = LoginPage(context.driver)
        context.lp.click_logout()
        time.sleep(5)
        context.logger.info("Logged out successfully")

