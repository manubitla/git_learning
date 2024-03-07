package stepDefinition;

import org.junit.runner.RunWith;

import io.cucumber.junit.CucumberOptions;
import io.cucumber.junit.Cucumber;

@RunWith(Cucumber.class)
@CucumberOptions(features="src/test/resources/Features", glue= {"stepDefinition"}, monochrome = true,
plugin = {"pretty", "html:target/HtmlReports.html"}
)
//tags = "@smoketest"
//plugin = {"pretty", "json:target/JsonReports"
//plugin = {"pretty", "html:target/HtmlReports.html"}
public class TestRunner {

}
	