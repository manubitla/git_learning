package stepDefinition;

import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

import java.time.Duration;

import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;


public class GoogleSearch_Steps {
	WebDriver driver;

	@Given("user is in google landing page")
	public void user_is_in_google_landing_page() {
	    driver = new FirefoxDriver();
	    driver.get("https://www.google.com");
	    driver.manage().window().maximize();
	    driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
	}

	@When("user enters a search keyword in search text box")
	public void user_enters_a_search_keyword_in_search_text_box() {
	    // Write code here that turns the phrase above into concrete actions
	    //throw new io.cucumber.java.PendingException();
		WebElement w=driver.findElement(By.name("q"));
		w.sendKeys("Amore Home bakers");
	}

	@When("clicks on search button")
	public void clicks_on_search_button() {
	    // Write code here that turns the phrase above into concrete actions
	    //throw new io.cucumber.java.PendingException();
		//Actions a = new
		driver.findElement(By.name("q")).sendKeys(Keys.ENTER);
	}

	@Then("user should get the search results")
	public void user_should_get_the_search_results(){
	    // Write code here that turns the phrase above into concrete actions
	    //throw new io.cucumber.java.PendingException();
		System.out.println(driver.findElement(By.xpath("//h2[@class='qrShPb pXs6bb PZPZlf q8U8x aTI8gc hNKfZe']//span[contains(text(),'Amore Home Bakers_Homemade Cakes & Donuts')]")).isDisplayed());
		
	}

}
