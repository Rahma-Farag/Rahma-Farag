import java.util.List;
import java.util.Set;
import java.util.ArrayList;
class Country
{
	private String code;
	private String name;
	private String continent;
	private double surfaceArea;
	private int population;
	private double gnp;
	private int capital;
	private List<City> cities = new ArrayList<City>();
	
	Country(String code, String name, String continent, int population, double surfaceArea, double gnp, int capital)
	{
		this.code = code;
		this.name = name;
		this.continent = continent;	
		this.population = population;
		this.surfaceArea = surfaceArea;
		this.gnp = gnp;
		this.capital = capital;
	}
	String getName()
	{
		return name;
	}
	String getCode()
	{
		return code;
	}
	List<City> getCities()
	{
		return cities;
	}
	String getContinent()
	{
		return continent;
	}
	int getCapital()
	{
		return capital;
	}
}
