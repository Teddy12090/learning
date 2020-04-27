package org.lee.teddy;


import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.universal.SuperRobot;

@ComponentScan(basePackageClasses = Robot.class)
@ContextConfiguration(classes = {TypeSafeScanTest.class})
@RunWith(SpringJUnit4ClassRunner.class)
public class TypeSafeScanTest {
    @Autowired(required = false)
    private Robot extreme;

    @Autowired(required = false)
    private SuperRobot teddy;

    @Test
    public void testRobot() {
        Assert.assertNotNull(extreme);
    }

    @Test
    public void testSuperRobot() {
        Assert.assertNull(teddy);
    }
}