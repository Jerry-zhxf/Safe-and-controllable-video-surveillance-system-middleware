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

	static String ip=null; // ������IP��ַ
	static String userName = null; // ���ڵ�½���������û���
	static String passWord = null; // ��½����
	static String remoteDirectoryPath = null; // Զ���ļ��еľ���·��
	@Test
	public static void uploadFile(String localFilePath) {
		String file = "config.txt";
		try{
            BufferedReader br = new BufferedReader(new FileReader(file));//����һ��BufferedReader������ȡ�ļ�
            String s = null;
            while((s = br.readLine())!=null){//ʹ��readLine������һ�ζ�һ��
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

		String remoteFileName = "time"; // ��ʱ����������ļ��ϴ������������ļ�������

		FTPClient ftpClient = new FTPClient();
		try {
			ftpClient.connect(ip);
			boolean isLogin = ftpClient.login(userName, passWord);
			System.out.println("uploadFile ��½�ɹ� " + isLogin);
			ftpClient.changeWorkingDirectory(remoteDirectoryPath);
			InputStream is = new FileInputStream(new File(localFilePath));
			boolean isStore = ftpClient.storeFile(remoteFileName, is);
			System.out.println("�ϴ��ɹ� " + isStore);
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
		uploadFile("C:\\Users\\zh200\\Desktop\\��ݮ�ɴ���\\generate7z\\generate7z\\1.7z");
	}
	
}