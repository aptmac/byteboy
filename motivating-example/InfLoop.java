public class InfLoop {

    private void doWork(int i) {
        while(i == 0) {
            work();
        }
    }

    private static void work() {
    }

    public static void main(String[] args) { 
        InfLoop inf  = new InfLoop();
	    inf.doWork(0);
    }

}
