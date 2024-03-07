/*package stepDefinition;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;



import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class Login_Steps {
	WebDriver driver;
	@Given("user has given the login page")
	public void user_has_given_the_login_page() {
	    // Write code here that turns the phrase above into concrete actions
	    //throw new io.cucumber.java.PendingException();
		System.out.println("inside logindemo");
		driver= new ChromeDriver();
		driver.get("https://practice.expandtesting.com/login");
		driver.manage().window().maximize();
		driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(20));
		
	}

	@When("^user gives valid (.*) (.*)$")
	public void user_gives_valid_username_and_password(String username, String password) throws InterruptedException {
	    // Write code here that turns the phrase above into concrete actions
	    //throw new io.cucumber.java.PendingException();
		driver.findElement(By.id("username")).sendKeys(username);
		Thread.sleep(2500);
		driver.findElement(By.id("password")).sendKeys(password);
		Thread.sleep(2000);
		
	}

	@And("clicks login")
	public void clicks_login() {
	    // Write code here that turns the phrase above into concrete actions
	    //throw new io.cucumber.java.PendingException();
		driver.findElement(By.xpath("//button[@type='submit']")).click();
	}

	@Then("user should be navigated to home page")
	public void user_should_be_navigated_to_home_page() {
	    // Write code here that turns the phrase above into concrete actions
	    //throw new io.cucumber.java.PendingException();
		System.out.println(driver.findElement(By.xpath("//h4[@class='subheader']")).isDisplayed());
		driver.close();
		driver.quit();
	}

}
*/