/*
Projeto: Pisca Led
Autor: Luis Fernando
Instituição: Senai Jaguariúna
Data: 14/05/2024  Rev: 0
*/

//Definiu um nome "Led" para o pino "2"
#define Led 2

//Configura pinos e periféricos, e se são entrada ou saida
void setup() {
  // put your setup code here, to run once:
  //Configura o pino como I/O (input ou output)
  pinMode(Led, OUTPUT); //configura o pino Led como saída.
}

//
void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(Led, HIGH); //Sinais digitaos só tem dois estados, ligado ou desligado. Esp mandando o sinal para o pino (Liga o pino Led)
  delay(500); //aguarda 0,5 segundos
  digitalWrite(Led, LOW); //Desligando o pino Led
  delay(300); //aguarda 0,3 segundos (milisegundos)

}
