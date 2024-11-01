package clase3;
import  java.util.Scanner;


public class restaurantExample {
    public static void main(String[] args) {
        int cantidadPlatos = 0;
        String nombrePlato1 = "";
        String nombrePlato2 = "";
        String nombrePlato3 = "";
        String nombrePlato4 = "";
        String nombrePlato5 = "";
        float precioPlato1 = 0;
        float precioPlato2 = 0;
        float precioPlato3 = 0;
        float precioPlato4 = 0;
        float precioPlato5 = 0;
        boolean digitarPlato = true;
        boolean terminar = false;
        float gananciaTotal = 0;
        int cantidadMesasAtendidas = 0;

        System.out.println("""
                           ################################## 
                           Iniciando programa, por favor digite los platos del menu de hoy 
                           ------------------------------------------""");
        while (digitarPlato && cantidadPlatos < 5) {
            System.out.println("Digite el nombre del plato y el precio");
            String nombre = inputText("Escriba el nombre del plato plato: ");
            float precio = inputFloat("Escriba el precion del plato: ");
            boolean isPosibleResponse = false;

            if (cantidadPlatos == 0) {
                nombrePlato1 = nombre;
                precioPlato1 = precio;
            }
            if (cantidadPlatos == 1) {
                nombrePlato2 = nombre;
                precioPlato2 = precio;
            }
            if (cantidadPlatos == 2) {
                nombrePlato3 = nombre;
                precioPlato3 = precio;
            }
            if (cantidadPlatos == 3) {
                nombrePlato4 = nombre;
                precioPlato4 = precio;
            }
            if (cantidadPlatos == 4) {
                nombrePlato5 = nombre;
                precioPlato5 = precio;
            }
            cantidadPlatos++;
            System.out.println("¿Desea escribir otro plato? \n 1) Si \n 2) No");
            if (cantidadPlatos >= 5) {
                isPosibleResponse = true;
            }

            while (!isPosibleResponse) {
                String response = inputText("Respuesta: ");
                if ("1".equals(response) || "Si".equals(response) || "SI".equals(response) || "si".equals(response)) {
                    isPosibleResponse = true;
                } else if ("2".equals(response) || "No".equals(response) || "NO".equals(response) || "no".equals(response)) {
                    isPosibleResponse = true;
                    digitarPlato = false;
                }
            }

        }

        System.out.println("""
                ----------------------------------------------
                        Platos registrados
                        Iniciando programa de facturacion...
                ----------------------------------------------
                """);
        
        while (!terminar) { 
            String factura = "------------------------------------ \n     Factura";
            float montoTotal = 0;
            System.out.println("Mesa numero "+(cantidadMesasAtendidas+1)+" ¿Cuantas ordenes va a pedir?");
            int numeroPersonas = inputInt("Cantidad de ordenes: ");
            System.out.println("¿La orden sera para llevar? \n 1) Si \n 2) No");
            int responseLlevar = inputInt("Respuesta (solo en numero): ");
            boolean paraLlevar = false;
            boolean isPosibleResponse = false;

            if (responseLlevar == 1) {
                paraLlevar = true;
            }

            for (int i = 0; i < numeroPersonas; i++) {
                System.out.println("¿Que va a ordenar?");
                System.out.println("1) "+nombrePlato1+ " ...... "+precioPlato1);
                if (cantidadPlatos > 1) {
                    System.out.println("2) "+nombrePlato2+ " ...... "+precioPlato2);
                }
                if (cantidadPlatos > 2) {
                    System.out.println("3) "+nombrePlato3+ " ...... "+precioPlato3);
                }
                if (cantidadPlatos > 3) {
                    System.out.println("4) "+nombrePlato4+ " ...... "+precioPlato4);
                }
                if (cantidadPlatos > 4) {
                    System.out.println("5) "+nombrePlato5+ " ...... "+precioPlato5);
                }

                int response = inputInt("Eleccion: ");
                if (response == 1) {
                    factura += "\n "+nombrePlato1+" ...... valor: "+precioPlato1;
                    montoTotal += precioPlato1;
                }
                if (response == 2) {
                    factura += "\n "+nombrePlato2+" ...... valor: "+precioPlato2;
                    montoTotal += precioPlato2;
                }
                if (response == 3) {
                    factura += "\n "+nombrePlato3+" ...... valor: "+precioPlato3;
                    montoTotal += precioPlato3;
                }
                if (response == 4) {
                    factura += "\n "+nombrePlato4+" ...... valor: "+precioPlato4;
                    montoTotal += precioPlato4;
                }
                if (response == 5) {
                    factura += "\n "+nombrePlato5+" ...... valor: "+precioPlato5;
                    montoTotal += precioPlato5;
                }
            }

            if (paraLlevar) {
                String direccion = inputText("Escriba su direccion: ");
                String nombre = inputText("Escriba su nombre: ");
                factura += "\n \n Cliente: "+nombre+" \n Direccion: "+direccion;
            }
            factura += "\n Total a pagar: "+montoTotal+" \n------------------------------------";
            System.out.println(factura);
            gananciaTotal += montoTotal;

            System.out.println("¿Cerrar tienda? \n 1) Si \n 2) No");
            cantidadMesasAtendidas++;

            while (!isPosibleResponse) {
                String response = inputText("Respuesta: ");
                if ("1".equals(response) || "Si".equals(response) || "SI".equals(response) || "si".equals(response)) {
                    isPosibleResponse = true;
                    terminar = true;
                } else if ("2".equals(response) || "No".equals(response) || "NO".equals(response) || "no".equals(response)) {
                    isPosibleResponse = true;
                }
            }
        }

        System.out.println("""
          --------------------------------------- 
                Dia terminado 
            Ganancia total: """+gananciaTotal+" \n" +
        " ---------------------------------------");
        input.close();
    }

    public static Scanner input = new Scanner(System.in);

    public static String inputText (String text) {
       System.out.print(text); 
       String result = input.nextLine();

       return result;
    }

    public static float inputFloat (String text) {
        System.out.print(text); 
        float result = input.nextFloat();
        return result;
    }
    public static int inputInt (String text) {
       System.out.print(text); 
       int result = input.nextInt();
       return result;
    }
}
