# Write json file to populate dynamoDB
def write_to_file(filetowrite, filetoread, table):
    with open(filetowrite, 'w', encoding="UTF-8") as file1, open(filetoread, "r", encoding="UTF-8") as file2:
        file1.write("{\n")
        file1.write("\t\"{}\": [\n".format(table))
        count = 0
        # write out putrequests
        for line in file2:
            count += 1
            file1.write("\t\t{\n")
            file1.write("\t\t\t\"PutRequest\": {\n")
            file1.write("\t\t\t\t\"Item\": {\n")
            file1.write("\t\t\t\t\t\"id\": {\n")
            file1.write("\t\t\t\t\t\t\"N\": \"{}\"\n".format(count))
            file1.write("\t\t\t\t\t},\n")
            file1.write("\t\t\t\t\t\"Fortune\": {\n")
            file1.write(("\t\t\t\t\t\t\"S\": \"{}\"\n".format(line.strip())))
            file1.write("\t\t\t\t\t}\n")
            file1.write("\t\t\t\t}\n")
            file1.write("\t\t\t}\n")
            file1.write("\t\t},\n")
        # Close the json file and close open files
        file1.write("\t]\n")
        file1.write("}")
        file1.close()
        file2.close()


if __name__ == "__main__":
    write_to_file("fortunedb.json", "fortunelist.txt", "Fortunes")
