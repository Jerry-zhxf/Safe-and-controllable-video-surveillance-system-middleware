package mytest;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import org.apache.commons.net.ftp.FTPClient;
import org.apache.commons.net.ftp.FTPFile;
import org.junit.Test;

public class test01 {

	static String ip=null; // 服务器IP地址
	static String userName = null; // 用于登陆服务器的用户名
	static String passWord = null; // 登陆密码
	static String remoteDirectoryPath = null; // 远程文件夹的绝对路径
	@Test
	public static void uploadFile(String localFilePath) {
		String file = "config.txt";
		try{
            BufferedReader br = new BufferedReader(new FileReader(file));//构造一个BufferedReader类来读取文件
            String s = null;
            while((s = br.readLine())!=null){//使用readLine方法，一次读一行
               if(s.substring(0, s.lastIndexOf(":"))=="IP"){
            	   ip = s.substring(s.lastIndexOf(":"));
            	   System.out.println(ip);
               }
               if(s.substring(0, s.lastIndexOf(":"))=="Username"){
            	   userName = s.substring(s.lastIndexOf(":"));
            	   System.out.println(userName);
               }
               if(s.substring(0, s.lastIndexOf(":"))=="Password"){
            	   passWord = s.substring(s.lastIndexOf(":"));
            	   System.out.println(passWord);
               }
               if(s.substring(0, s.lastIndexOf(":"))=="RemoteDir"){
            	   remoteDirectoryPath = s.substring(s.lastIndexOf(":"));
            	   System.out.println(remoteDirectoryPath);
               }
            }
            br.close();    
        }catch(Exception e){
            e.printStackTrace();
        }

		String remoteFileName = "time"; // 用时间戳将本地文件上传到服务器后文件的名字

		FTPClient ftpClient = new FTPClient();
		try {
			ftpClient.connect(ip);
			boolean isLogin = ftpClient.login(userName, passWord);
			System.out.println("uploadFile 登陆成功 " + isLogin);
			ftpClient.changeWorkingDirectory(remoteDirectoryPath);
			InputStream is = new FileInputStream(new File(localFilePath));
			boolean isStore = ftpClient.storeFile(remoteFileName, is);
			System.out.println("上传成功 " + isStore);
			is.close();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				ftpClient.logout();
				ftpClient.disconnect();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
	public static void main(String args[]) {
		uploadFile("C:\\Users\\zh200\\Desktop\\树莓派代码\\generate7z\\generate7z\\1.7z");
	}
	
}
