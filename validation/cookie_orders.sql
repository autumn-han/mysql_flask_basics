-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema cookie_orders
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `cookie_orders` ;

-- -----------------------------------------------------
-- Schema cookie_orders
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cookie_orders` DEFAULT CHARACTER SET utf8 ;
USE `cookie_orders` ;

-- -----------------------------------------------------
-- Table `cookie_orders`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cookie_orders`.`customers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cookie_orders`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cookie_orders`.`orders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cookie_type` VARCHAR(45) NULL,
  `amount` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
  `customer_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_orders_customers_idx` (`customer_id` ASC) VISIBLE,
  CONSTRAINT `fk_orders_customers`
    FOREIGN KEY (`customer_id`)
    REFERENCES `cookie_orders`.`customers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
