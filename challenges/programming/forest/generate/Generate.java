import java.io.*;
import java.util.regex.*;
import java.security.SecureRandom;

class Generate {
    public static void main(String[] args) throws IOException {
        String folderName = ".." + File.separator + "distrib" + File.separator + "forest",
            sampleSpace = "{ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789}ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
            regexPattern = "^GCTF\\{.+\\}$";

        Pattern pattern = Pattern.compile(regexPattern);

        // make directory
        File folder = new File(folderName);
        folder.mkdirs();

        boolean notDone = true;
        // actual seed used was 36
        int seed = 0;

        do {
            SecureRandom random = new SecureRandom(String.valueOf(seed).getBytes());
            for (int i = 1; i <= 1000; i++) {
                String fileName = folderName + File.separator + Integer.toString(i);
                String outString = "GCTF{";

                for (int j = 0; j < 34; j++) {
                    outString += sampleSpace.charAt(random.nextInt(sampleSpace.length()));
                }

                // write to file
                File file = new File(fileName);
                file.delete();
                FileWriter fileWriter = new FileWriter(file);
                fileWriter.write(outString);
                fileWriter.flush();
                fileWriter.close();
            }

            // count number of files, ensure 10
            int count = 0;
            for (File currFile : folder.listFiles()) {
                char[] buffer = new char[1024];
                FileReader fileRd = new FileReader(currFile);
                fileRd.read(buffer);
                fileRd.close();
                String data = new String(buffer);
                data = data.trim();
                Matcher m = pattern.matcher(data);

                if (m.matches()) {
                    count++;
                }
            }

            System.out.println(seed + " : " + count);

            if (count == 10) {
                notDone = false;
            } else {
                seed++;
            }
        } while (notDone);
    }
}
