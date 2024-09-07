# Define custom error type
```rust
#[derive(Error, Clone, Debug, PartialEq)]
4
pub enum CreateUserError {  
    #[error("invalid email address: {0}")]  
    InvalidEmail(String),  
    #[error("invalid password: {reason}")]  
    InvalidPassword {  
        reason: String,  
    },  
    #[error("failed to hash password: {0}")]  
    PasswordHashError(#[from] BcryptError),  
    #[error("user with email address {email} already exists")]  
    UserAlreadyExists {  
        email: String,  
    },  
    // ...  
}
```
# Test cases
```rust
#[cfg(test)]  
mod tests {  
    use super::*;  
  
    #[test]  
    fn test_create_user_invalid_email() {  
        let email = "invalid-email";  
        let password = "password";  
        let result = create_user(email, password);  
        let expected = Err(CreateUserError::InvalidEmail(email.to_string()));  
        assert_eq!(result, expected);  
    }  
  
    #[test]  
    fn test_create_user_invalid_password() { unimplemented!() }  
  
    #[test]  
    fn test_create_user_password_hash_error() { unimplemented!() }  
  
    #[test]  
    fn test_create_user_user_already_exists() { unimplemented!() }  
  
    #[test]  
    fn test_create_user_success() { unimplemented!() }  
}

```

# New type essentials
```rust
#[derive(Debug, Clone, PartialEq)]
pub struct EmailAddress(String);  
 
#[derive(Debug, Clone, PartialEq)]
pub struct Password(String);

 
pub fn create_user(email: EmailAddress, password: Password) -> Result<User, CreateUserError> {

    validate_email(&email)?;  
    validate_password(&password)?;  
    let password_hash = hash_password(&password)?;  
    // ...  
    Ok(User)  
}
```
# Validation in the constructor
```rust
#[derive(Debug, Clone, PartialEq)]
pub struct EmailAddress(String);
  
#[derive(Error, Debug, Clone, PartialEq)]
#[error("{0} is not a valid email address")]
pub struct EmailAddressError(String);
7
 
impl EmailAddress {
    pub fn new(raw_email: &str) -> Result<Self, EmailAddressError> {
        if email_regex().is_match(raw_email) {
8
            Ok(Self(raw_email.into()))
        } else {
            Err(EmailAddressError(raw_email))
        }
    }
}
 
#[derive(Error, Clone, Debug, PartialEq)]
#[error("a user with email address {0} already exists")]
pub struct UserAlreadyExistsError(EmailAddress);
9
  


```
# Tests
```rust
#[cfg(test)]  
mod email_address_tests {  
    use super::*;  
  
    #[test]  
    fn test_new_invalid_email() {  
        let raw_email = "invalid-email";  
        let result = EmailAddress::new(raw_email);  
        let expected = Err(EmailAddressError(raw_email.to_string()));  
        assert_eq!(result, expected);  
    }  
  
    #[test]  
    fn test_new_success() { unimplemented!() }  
}  
  
#[cfg(test)]  
mod create_user_tests {  
    use super::*;  
  
    #[test]  
    fn test_user_already_exists() { unimplemented!() }
  
    #[test]  
    fn test_success() { unimplemented!() }  
}
```

# New Type trait implementation
```rust
#[derive(Debug, Clone, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub struct EmailAddress(String);

```

# New type display
```rust
impl Display for EmailAddress {  
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {  
        write!(f, "{}", self.0)  
    }  
}
```

# From implementation from other type
```rust
struct WrappedI32(i32);
  
impl From<i32> for WrappedI32 {
    fn from(raw: i32) -> Self {
        Self(raw)
    }
}
 
fn demonstrate() {
    let _ = WrappedI32::from(84);
    let _: WrappedI32 = 84.into();
16
}

```

# Getting the value out of new type

## User friendly getter
```rust
impl EmailAddress {
    pub fn into_string(self) -> String {
        self.0
    }
	
18
}

```

## As Ref

```rust 
impl AsRef<str> for EmailAddress {
    fn as_ref(&self) -> &str {
        &self.0
    }
}
```

## Deref



## Borrow

