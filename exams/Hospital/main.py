from classes.hospital import Hospital



if __name__ == "__main__":
   hospital = Hospital("Ninguna")   
   
   ruta_csv_1 = "./data/atenciones_farmacia.csv"
   ruta_csv_2 = "./data/pacientes.csv"
   ruta_csv_3 = "./data/atenciones_medicas.csv"
   
   hospital.cargar_atencion_farmacia(ruta_csv_1, ruta_csv_2, ruta_csv_3)
   hospital.mostrar_datos()
   hospital.importe_total_atencion_consulta()
   hospital.importe_promedio_atenciones(5000, 16000)
   hospital.codigo_primera_atencion_habitual()

        
