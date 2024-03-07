package Pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class LoginPage {
	
	WebDriver driver;
	By txt_username = By.id("username");
	By txt_psw = By.id("password");
	By button_login = By.xpath("//button[@type='submit']");
	By button_logout = By.xpath("//i[@class='icon-2x icon-signout']");
	
	
	public LoginPage(WebDriver driver)
	{
		this.driver = driver;
	}
	public void enterUsername(String uname)
	{
		driver.findElement(txt_username).sendKeys(uname);
	}
	public void enterPSW(String psw)
	{
		driver.findElement(txt_psw).sendKeys(psw);
	}
	public void clickLogin()
	{
		driver.findElement(button_login).click();
	}
	public void validateLogin(String uname, String psw)
	{
		driver.findElement(txt_username).sendKeys(uname);
		driver.findElement(txt_psw).sendKeys(psw);
		driver.findElement(button_login).click();
	}
	public void verify_Valid_Login()
	{
		driver.findElement(button_logout).isDisplayed();
	}
}
