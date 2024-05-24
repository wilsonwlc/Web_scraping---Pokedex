from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


def main():
    driver = webdriver.Firefox()
    try:
        links_pokemon = get_link_pokemon(driver)
        filename_data = "pokemon_demo.csv"
        fieldnames_data = generate_fieldnames_data()
        create_file(filename_data, fieldnames_data)
        filename_pokedex_entries = "pokemon_pokedox_entry.csv"
        fieldnames_pokedex_entries = ["national_number", "version", "description"]
        create_file(filename_pokedex_entries, fieldnames_pokedex_entries)
        for link in links_pokemon[0:151]:
            driver.get(link)
            name = find_name(driver)
            generation = find_generation(driver)
            national_number = find_national_number(driver)
            pokemon_type = find_type(driver)
            species = find_species(driver)
            height = find_height(driver)
            weight = find_weight(driver)
            base_stats = find_base_stat(driver)
            min_stats = find_min_stat(driver)
            max_stats = find_max_stat(driver)
            image_url = find_image_url(driver)
            records = ([name, generation, national_number] + pokemon_type
                       + [species, height, weight] + base_stats + min_stats
                       + max_stats + [image_url, link])
            records = dict(zip(fieldnames_data, records))
            append_record(filename_data, fieldnames_data, records)

            records = find_pokedex_entries(driver)
            records = [[national_number, item[0], item[1]] for item in records]
            append_multiple_records(filename_pokedex_entries, fieldnames_pokedex_entries, records)
    finally:
        driver.close()


def generate_fieldnames_data():
    pokemon_stats = ["hp", "attack", "defense", "sp_attack", "sp_defence", "speed"]
    prefixes = ["base_", "min_", "max_"]
    fieldnames_stats = [f"{prefix}{stat}" for prefix in prefixes for stat in pokemon_stats]
    fieldnames_data = (["name", "generation", "national_number", "type1", "type2", "species", "height", "weight"] + fieldnames_stats + ["image_url", "url"])
    return fieldnames_data


def create_file(filename, fieldnames):
    with open(filename, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()


def append_record(filename, fieldnames, dict_records):
    with open(filename, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow(dict_records)


def append_multiple_records(filename, fieldnames, list_records):
    with open(filename, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        for row in list_records:
            row_dict = {fieldnames[i]: row[i] for i in range(len(fieldnames))}
            writer.writerow(row_dict)


def get_link_pokemon(driver):
    driver.get("https://pokemondb.net/pokedex/national")
    query_links_pokemon = "//*[@id='gen-1']/following-sibling::div//div[@class='infocard ']//span[@class='infocard-lg-data text-muted']/a"
    links_pokemon = driver.find_elements(By.XPATH, query_links_pokemon)
    links_pokemon = [item.get_attribute("href") for item in links_pokemon]
    return links_pokemon


def find_name(driver):
    query_name = "//*[@id='main']/h1"
    name = driver.find_elements(By.XPATH, query_name)
    name = name[0].text
    return name


def find_generation(driver):
    query_generation = "/html/body/main/p/abbr"
    generation = driver.find_elements(By.XPATH, query_generation)
    generation = generation[0].text
    return generation


def find_national_number(driver):
    query_national_number = "/html/body/main/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td/strong"
    national_number = driver.find_elements(By.XPATH, query_national_number)
    national_number = national_number[0].text
    return national_number


def find_type(driver):
    query_type = "/html/body/main/div[2]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td/a"
    pokemon_type = driver.find_elements(By.XPATH, query_type)
    pokemon_type = [item.text for item in pokemon_type]
    if len(pokemon_type) == 1:
        pokemon_type.append("")
    return pokemon_type


def find_species(driver):
    query_species = "/html/body/main/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[3]/td"
    species = driver.find_elements(By.XPATH, query_species)
    species = species[0].text
    return species


def find_height(driver):
    query_height = "/html/body/main/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[4]/td"
    height = driver.find_elements(By.XPATH, query_height)
    height = height[0].text
    return height


def find_weight(driver):
    query_weight = "/html/body/main/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[5]/td"
    weight = driver.find_elements(By.XPATH, query_weight)
    weight = weight[0].text
    return weight


def find_image_url(driver):
    query_image_url = "/html/body/main/div[2]/div[2]/div/div[1]/div[1]/p[1]/a/picture/img"
    image_url = driver.find_elements(By.XPATH, query_image_url)
    image_url = image_url[0].get_attribute("src")
    return image_url


def find_base_stat(driver):
    queries_base_stat = [f"/html/body/main/div[2]/div[2]/div/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[1]" for i in range(1, 7)]
    base_stats = [driver.find_elements(By.XPATH, query)[0].text for query in queries_base_stat]
    return base_stats


def find_min_stat(driver):
    queries_min_stat = [f"/html/body/main/div[2]/div[2]/div/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[3]" for i in range(1, 7)]
    min_stats = [driver.find_elements(By.XPATH, query)[0].text for query in queries_min_stat]
    return min_stats


def find_max_stat(driver):
    queries_max_stat = [f"/html/body/main/div[2]/div[2]/div/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[4]" for i in range(1, 7)]
    max_stats = [driver.find_elements(By.XPATH, query)[0].text for query in queries_max_stat]
    return max_stats


def find_pokedex_entries(driver):
    h2_element = driver.find_element(By.XPATH, "//h2[text()='Pokédex entries']")
    div_element = h2_element.find_element(By.XPATH, "following-sibling::div[@class='resp-scroll']")
    table_element = div_element.find_element(By.XPATH, ".//table[@class='vitals-table']")
    th_elements = table_element.find_elements(By.XPATH, ".//th")
    td_elements = table_element.find_elements(By.XPATH, ".//td")
    version = [item.text for item in th_elements]
    version = [item.replace("\n", " / ") for item in version]
    description = [item.text for item in td_elements]
    output = list(zip(version, description))
    return output


if __name__ == "__main__":
    main()

# https://www.pokemon.com/us/play-pokemon/about/video-game-glossary


