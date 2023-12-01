import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
// Import the Scanner class to read text files
import java.util.*; 
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Challenge {
  static Map<String, String> numberWordMap  = new HashMap<String, String>() {{
    put("one", "1");
    put("two", "2");
    put("three", "3");
    put("four", "4");
    put("five", "5");
    put("six", "6");
    put("seven", "7");
    put("eight", "8");
    put("nine", "9");
  }};

  static Pattern numberPattern = Pattern.compile("[\\d]|(?:one)|(?:two)|(?:three)|(?:four)|(?:five)|(?:six)|(?:seven)|(?:eight)|(?:nine)", Pattern.MULTILINE);

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
      String firstNumber = "";
      String lastNumber = "";
      int lineLength = line.length();

      for (int i = 1; i <= lineLength; i++) {
        String subString = line.substring(0, i);

        Optional<String> match = matchedInteger(subString);
        if (match.isPresent()) {
          String number = match.get();
          firstNumber = number.length() > 1 ? numberWordMap.get(number) : number;
          break;
        }
      }      

      for (int i = lineLength - 1; i >= 0; i--) {
        String subString = line.substring(i, lineLength);

        Optional<String> match = matchedInteger(subString);
        if (match.isPresent()) {
          String number = match.get();
          lastNumber = number.length() > 1 ? numberWordMap.get(number) : number;
          break;
        }
      }

      String combinedParsableString = firstNumber + lastNumber;

      return Integer.parseInt(combinedParsableString);
  }

  public static Optional<String> matchedInteger(String string) {
    Matcher matcher = numberPattern.matcher(string);

    if(matcher.find()){
      return Optional.of(matcher.group(0));
    }
    return Optional.empty();
  }
}