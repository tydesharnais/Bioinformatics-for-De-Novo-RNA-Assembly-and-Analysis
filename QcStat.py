def main():

    with open("fastqc_data.txt", "r") as file:

        content = file.readlines()
        sequenceTotal = content[6]
        fileName = content[3]
        sum = 0
        total = 0
        
        for i in range(26):

            totalReads = content[8654+i].split("\t")
            removeSuff = totalReads[1].removesuffix('\n')
            floatRemove = float(removeSuff)
            total=floatRemove+total

        for i in range(8):

            qualityReads = content[8672+i].split("\t")
            removeSuff = qualityReads[1].removesuffix('\n')
            floatRemove = float(removeSuff)
            sum+=floatRemove

        goodRead = (sum/total)*100

    file.close()

    with open("PiPypeStat.txt", "w") as writer:

        writer.writelines("""
______           _    _____  _____   ______  _ ______                    
|  ___|         | |  |  _  |/  __ \  | ___ \(_)| ___ \                   
| |_  __ _  ___ | |_ | | | || /  \/  | |_/ / _ | |_/ /_   _  _ __    ___ 
|  _|/ _` |/ __|| __|| | | || |      |  __/ | ||  __/| | | || '_ \  / _ | 
| | | (_| |\__ \| |_ \ \/' /| \__/\  | |    | || |   | |_| || |_) ||  __/
\_|  \__,_||___/ \__| \_/\_\ \____/  \_|    |_|\_|    \__, || .__/  \___|
                                                       __/ || |          
                                                      |___/ |_|   
                                        +-+
         +---+--+----+-+-+-+--+--+--+-+-+-+ | ++++++++++++++++++++++++++++
         |   |  |    +-+ | |  |  |  | | |+| |  @copyright Tyler Desharnais 
         |   |  |    |  ++ |  +--+--+-+ |+| | ++++++++++++++++++++++++++++
         +---+--+----+--++-+--+-------+-+-+ |
                                        +-+
==========================================================================
""")
        writer.write(f'{fileName}')
        writer.write('==========================================================================\n')
        writer.write(sequenceTotal) 
        writer.write(f'Amount of Quality reads (Over 30) {sum}\n')
        writer.write(f'Percentage of Quality reads (Over 30) {goodRead}')

    writer.close()

if __name__ == "__main__":
    main()