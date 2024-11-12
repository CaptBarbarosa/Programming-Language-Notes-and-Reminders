import java.util.HashMap;
import java.util.Map;

// Step 1: Define the Language interface
interface Language {
    String localize(String msg);
}

// Step 2: Implement concrete classes for each language
class FrenchLanguage implements Language {
    private final Map<String, String> translations;

    public FrenchLanguage() {
        translations = new HashMap<>();
        translations.put("books", "livres");
        translations.put("phoneno", "numero de telephone");
        translations.put("cloths", "vetements");
    }

    @Override
    public String localize(String msg) {
        return translations.getOrDefault(msg, msg);
    }
    public void onlyfrench(){
        System.out.println("Hey this is french");
    }
}

class SpanishLanguage implements Language {
    private final Map<String, String> translations;

    public SpanishLanguage() {
        translations = new HashMap<>();
        translations.put("books", "libro");
        translations.put("phoneno", "telefono");
        translations.put("cloths", "pano");
    }

    @Override
    public String localize(String msg) {
        return translations.getOrDefault(msg, msg);
    }

    public void onlyspanish(){
        System.out.println("Hey this is Spanish");
    }
}

class EnglishLanguage implements Language {
    @Override
    public String localize(String msg) {
        return msg; // Simply return the same message
    }

    public void onlyEnglish(){
        System.out.println("Hey this is English");
    }
}

// Step 3: Create the LanguageFactory class
final class LanguageFactory {
    public static Language createLanguage(String language) {
        switch (language.toLowerCase()) {
            case "french":
                return new FrenchLanguage();
            case "spanish":
                return new SpanishLanguage();
            case "english":
                return new EnglishLanguage();
            default:
                throw new IllegalArgumentException("Unknown language: " + language);
        }
    }
}

// Step 4: Client code to use the Factory
public class Second_Example {
    public static void main(String[] args) {
        Language french = LanguageFactory.createLanguage("French");
        System.out.println("french instanceof EnglishLanguage: " + (french instanceof EnglishLanguage) + " french instanceof FrenchLanguage: " + (french instanceof FrenchLanguage)+ " french instanceof Language: " + (french instanceof Language));
        if(french instanceof FrenchLanguage){
            ((FrenchLanguage) french).onlyfrench();
            //FrenchLanguage second_french = (FrenchLanguage) french;
            //second_french.onlyfrench();
        }
        Language english = LanguageFactory.createLanguage("English");
        Language spanish = LanguageFactory.createLanguage("Spanish");

        String[] messages = {"books", "phoneno", "cloths"};
        
        for (String msg : messages) {
            System.out.println(msg + " in French: " + french.localize(msg));
            System.out.println(msg + " in English: " + english.localize(msg));
            System.out.println(msg + " in Spanish: " + spanish.localize(msg));
        }
        EnglishLanguage my_eng = (EnglishLanguage) LanguageFactory.createLanguage("English");
        my_eng.onlyEnglish();
    }
}
