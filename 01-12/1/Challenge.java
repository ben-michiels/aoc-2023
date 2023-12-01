import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.*; 
import java.util.stream.*; 
import java.util.ArrayList;
import java.util.Scanner; // Import the Scanner class to read text files

public class Challenge {

  public static void main(String[] args) {
    ArrayList<String> lines = getLines();
    Optional<Integer> count = lines.stream().map(line -> readLine(line)).reduce((a, b) -> (a + b));

    count.ifPresentOrElse(
      foundCount -> System.out.println(foundCount),
      () -> System.out.println("Failed to count lines.")
    );
  }

  public static ArrayList<String> getLines() {
    ArrayList<String> lines = new ArrayList<String>();
    try {
      File myObj = new File("../input.txt");
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        lines.add(data);
      }
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
    return lines;
  }

  public static Integer readLine(String line) {
    List<String> parsableStrings = Arrays.stream(line.split(""))
      .filter(string -> isParsableInt(string))
      .collect(Collectors.toList());

      String combinedParsableString = parsableStrings.get(0) + parsableStrings.get(parsableStrings.size() - 1);

      return Integer.parseInt(combinedParsableString);
  }

  public static boolean isParsableInt(String string) {
    try {
        Stream.of(Integer.parseInt(string));
        return true;
      } catch (NumberFormatException e) {
        return false;
      }
  }
}