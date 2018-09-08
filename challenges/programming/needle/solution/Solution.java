import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

class Solution {
    public static void main(String[] args) throws IOException {
        // open directory
        String folderName = ".." + File.separator + "distrib" + File.separator + "forest";
        File folder = new File(folderName);

        // prepare regex string
        String regex_pattern = "^GCTF\\{.+\\}$";
        Pattern pattern = Pattern.compile(regex_pattern);

        for (File file : folder.listFiles()) {
            char[] buffer = new char[1024];
            FileReader fileRd = new FileReader(file);
            fileRd.read(buffer);
            fileRd.close();
            String data = new String(buffer);
            data = data.trim();
            Matcher m = pattern.matcher(data);

            if (m.matches()) {
                System.out.println(file.getName() + " " + data);
            }
        }
    }
}
