import java.util.List;
import java.util.Set;
class City
{
	private int id;
	private String name;
	private int population;
	private String countryCode;
	
	
	City(int id, String name, String countryCode, int pop)
	{
		this.id = id;
		this.name = name;
		this.countryCode = countryCode;
		this.population = pop; 
	}
	String getCountryCode()
	{
		return countryCode;
	}
	int getId()
	{
		return id;
	}
	int getPop()
	{
		return population;
	}
	
	String getName()
	{
	
		return name;
	}
}
